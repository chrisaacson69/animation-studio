"""
Mouth overlay generator v4.
No hole in base. Mouth overlays are ONLY the inner mouth shapes
(dark opening, teeth, lip line) on transparent background.
Composited ON TOP of the unchanged base image.
"""
import sys, math
from PIL import Image, ImageDraw
from pathlib import Path

def create_mouth_set(base_path, output_dir, box):
    x, y, w, h = box
    cx, cy = x + w // 2, y + h // 2
    rx, ry = w // 2, h // 2
    
    base = Image.open(base_path).convert('RGBA')
    bw, bh = base.size
    out = Path(output_dir)
    out.mkdir(parents=True, exist_ok=True)
    
    print(f'Base: {bw}x{bh}')
    print(f'Mouth box: x={x} y={y} w={w} h={h}')
    print(f'Center: ({cx}, {cy}), radii: ({rx}, {ry})')
    
    lip_color = (160, 70, 70, 255)
    mouth_dark = (60, 20, 20, 255)
    teeth = (235, 235, 225, 255)
    
    def make_mouth(variant):
        # Fully transparent canvas
        img = Image.new('RGBA', base.size, (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)
        
        if variant == 'closed':
            draw.line(
                [(cx - rx + 4, cy), (cx + rx - 4, cy)],
                fill=lip_color, width=max(2, ry // 4)
            )
        
        elif variant == 'small':
            ow, oh = max(4, rx // 2), max(3, ry // 3)
            draw.ellipse(
                [cx - ow, cy - oh, cx + ow, cy + oh],
                fill=mouth_dark, outline=lip_color, width=2
            )
        
        elif variant == 'wide':
            ow, oh = max(6, int(rx * 0.7)), max(5, int(ry * 0.7))
            draw.ellipse(
                [cx - ow, cy - oh, cx + ow, cy + oh],
                fill=mouth_dark, outline=lip_color, width=2
            )
            tw = int(ow * 0.8)
            th = max(2, oh // 4)
            teeth_y = cy - oh // 3
            draw.rectangle(
                [cx - tw, teeth_y - th, cx + tw, teeth_y + th],
                fill=teeth
            )
        
        elif variant == 'smile':
            points = []
            for i in range(30):
                t = i / 29
                px = cx - rx + 4 + t * (rx * 2 - 8)
                py = cy - int(ry * 0.3 * math.sin(t * math.pi))
                points.append((int(px), int(py)))
            draw.line(points, fill=lip_color, width=max(2, ry // 4))
        
        return img
    
    for variant in ['closed', 'small', 'wide', 'smile']:
        img = make_mouth(variant)
        img.save(out / f'mouth_{variant}.png')
        print(f'  Saved mouth_{variant}.png')
    
    # No more base_hole needed - base stays unchanged
    # Remove old base_hole if it exists
    hole = out / 'base_hole.png'
    if hole.exists():
        hole.unlink()
        print('  Removed old base_hole.png (no longer needed)')
    
    # Debug composites
    debug = out / 'debug'
    debug.mkdir(exist_ok=True)
    for variant in ['closed', 'small', 'wide']:
        mouth = Image.open(out / f'mouth_{variant}.png').convert('RGBA')
        comp = base.copy()
        comp = Image.alpha_composite(comp, mouth)
        comp.save(debug / f'freeze_{variant}.png')
    print(f'  Debug frames in {debug}/')
    print('Done!')


if __name__ == '__main__':
    base = sys.argv[1] if len(sys.argv) > 1 else '/workspace/studio/assets/characters/aristotle/base.png'
    outdir = sys.argv[2] if len(sys.argv) > 2 else str(Path(base).parent)
    box_str = sys.argv[3] if len(sys.argv) > 3 else '0,0,100,50'
    box = tuple(int(c) for c in box_str.split(','))
    create_mouth_set(base, outdir, box)
