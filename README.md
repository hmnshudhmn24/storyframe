# STORYFRAME

**STORYFRAME** — Video-to-Story Generation (scene, emotion, dialogue).

STORYFRAME extracts frames from video clips, captions them, and generates a cinematic-style script.

### Steps
1. Extract frames: `python extract_frames.py --video input.mp4`
2. Caption frames: `python caption_frames.py --frames_dir frames`
3. Generate script: `python generate_script.py --captions captions.jsonl`

Run Streamlit app:  
`streamlit run app.py`
