from moviepy import VideoFileClip, ImageClip, CompositeVideoClip
from PIL import Image
import numpy as np

print("Loading Manim render...")
manim_clip = VideoFileClip("media/videos/ep01_syllogism/720p30/SyllogismScene.mp4")

print("Loading character image...")
# Load and resize Aristotle to fit in corner
char_img = Image.open("studio/assets/characters/test_aristotle.png")
char_img = char_img.resize((200, 200), Image.LANCZOS)
char_img.save("/tmp/aristotle_small.png")

char_clip = (ImageClip("/tmp/aristotle_small.png")
             .with_duration(manim_clip.duration)
             .with_position(("right", "bottom"))
             .with_effects([]))

print("Compositing...")
final = CompositeVideoClip([manim_clip, char_clip])

print("Writing output...")
final.write_videofile(
    "studio/episodes/ep01/scenes/test_composite.mp4",
    fps=30, codec="libx264", audio=False,
    logger=None
)

print(f"Done! Duration: {manim_clip.duration:.1f}s")
