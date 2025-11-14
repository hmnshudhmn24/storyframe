import os, argparse
from moviepy.editor import VideoFileClip
from utils import ensure_dir

def extract_frames(video_path, out_dir, fps=1, max_frames=60):
    ensure_dir(out_dir)
    clip = VideoFileClip(video_path)
    duration = clip.duration
    t = 0
    step = 1.0 / fps
    frames = []
    while t < duration and len(frames) < max_frames:
        frame = clip.get_frame(t)
        frame_path = os.path.join(out_dir, f"frame_{len(frames):04d}.jpg")
        from PIL import Image
        Image.fromarray(frame).save(frame_path, quality=80)
        frames.append((frame_path, t))
        t += step
    return frames

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--video", required=True)
    parser.add_argument("--out_dir", default="frames")
    parser.add_argument("--fps", type=float, default=1.0)
    parser.add_argument("--max_frames", type=int, default=60)
    args = parser.parse_args()
    lst = extract_frames(args.video, args.out_dir, fps=args.fps, max_frames=args.max_frames)
    print(f"Extracted {len(lst)} frames.")
