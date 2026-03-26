"""
Lip-sync compositor v3 — base image + transparent mouth overlays on top.
"""
import json, sys
import numpy as np
from pathlib import Path
from PIL import Image
from moviepy import ImageClip, AudioFileClip, CompositeVideoClip

SHAPE_MAP = {
    'A': 'closed', 'B': 'small', 'C': 'small', 'D': 'wide',
    'E': 'small', 'F': 'closed', 'G': 'wide', 'H': 'small', 'X': 'closed',
}

def composite_lipsync(character_dir, lipsync_json, audio_file, output_file,
                      bg_color=(30, 30, 60), size=(1920, 1080), char_scale=0.6):
    char = Path(character_dir)
    
    base = Image.open(char / 'base.png').convert('RGBA')
    
    mouths = {}
    for v in ['closed', 'small', 'wide', 'smile']:
        p = char / f'mouth_{v}.png'
        if p.exists():
            mouths[v] = Image.open(p).convert('RGBA')
            print(f'  Loaded mouth_{v}.png')
    
    if not mouths:
        print('ERROR: No mouth variants found')
        sys.exit(1)
    
    # Scale
    aspect = base.width / base.height
    char_h = int(size[1] * char_scale)
    char_w = int(char_h * aspect)
    base_scaled = base.resize((char_w, char_h), Image.LANCZOS)
    
    scaled_mouths = {}
    for v, m in mouths.items():
        scaled_mouths[v] = m.resize((char_w, char_h), Image.LANCZOS)
    
    # Pre-compose each frame: background + base + mouth overlay
    frames = {}
    bg = Image.new('RGBA', size, (*bg_color, 255))
    char_x = (size[0] - char_w) // 2
    char_y = (size[1] - char_h) // 2
    
    for v in mouths:
        frame = bg.copy()
        # Base + mouth overlay on top
        combined = Image.alpha_composite(base_scaled, scaled_mouths[v])
        frame.paste(combined, (char_x, char_y), combined)
        frames[v] = np.array(frame.convert('RGB'))
        print(f'  Pre-composed: {v}')
    
    # Also make a base-only frame (no mouth) for silence
    frame_base = bg.copy()
    frame_base.paste(base_scaled, (char_x, char_y), base_scaled)
    frames['_base'] = np.array(frame_base.convert('RGB'))
    
    with open(lipsync_json) as f:
        cues = json.load(f)['mouthCues']
    print(f'  {len(cues)} mouth cues')
    
    audio = AudioFileClip(audio_file)
    print(f'  Audio: {audio.duration:.2f}s')
    
    clips = []
    for cue in cues:
        variant = SHAPE_MAP.get(cue['value'], 'closed')
        frame = frames.get(variant, frames['closed'])
        clip = ImageClip(frame).with_duration(cue['end'] - cue['start']).with_start(cue['start'])
        clips.append(clip)
    
    bg_clip = ImageClip(frames['_base']).with_duration(audio.duration)
    video = CompositeVideoClip([bg_clip] + clips, size=size)
    video = video.with_audio(audio)
    
    print(f'  Rendering...')
    video.write_videofile(output_file, fps=24, codec='libx264', audio_codec='aac', logger=None)
    print(f'  Done! {output_file}')


if __name__ == '__main__':
    composite_lipsync(
        character_dir='/workspace/studio/assets/characters/aristotle',
        lipsync_json='/workspace/studio/episodes/ep01/voiceover/cold_open_host_lipsync.json',
        audio_file='/workspace/studio/episodes/ep01/voiceover/cold_open_host.wav',
        output_file='/workspace/studio/episodes/ep01/scenes/cold_open_test.mp4',
    )
