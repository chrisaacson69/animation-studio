# Animation Studio
> Tools and utilities for YouTube animation production on RunPod.

**Repo:** Tools & utilities
**Content:** [youtube-migration](https://github.com/chrisaacson69/youtube-migration)
**Infrastructure:** [animation-studio-pod](https://github.com/chrisaacson69/animation-studio-pod)

## Tools

| Tool | Purpose |
|---|---|
| `tools/media-server.py` | HTTP media browser for rendered videos, images, and assets |
| `tools/mouth_marker.html` | Web UI to mark mouth bounding boxes on character art |
| `tools/make_mouth_overlays.py` | Generate transparent mouth variant PNGs from a base character + bounding box |
| `tools/composite_lipsync.py` | Composite character + mouth overlays synced to rhubarb lip-sync timecodes |

## Usage

These tools run on the RunPod pod. The Docker image (`animation-studio-pod`) has all dependencies pre-installed.

```bash
# Media server (auto-starts on boot via post_start.sh)
python3 tools/media-server.py --port 8080

# Mark mouth positions on a character
# Serve tools/ and open mouth_marker.html in browser

# Generate mouth overlays from bounding box
python3 tools/make_mouth_overlays.py <base.png> <output_dir> <x,y,w,h>

# Composite lip-synced video
python3 tools/composite_lipsync.py
```
