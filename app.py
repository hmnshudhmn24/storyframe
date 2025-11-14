import streamlit as st
import tempfile, os, json
from extract_frames import extract_frames
from caption_frames import caption_images
from generate_script import generate_script

st.title("STORYFRAME — Video to Cinematic Script")

video = st.file_uploader("Upload video", type=["mp4","mov","avi"])
if video:
    tmp = tempfile.mkdtemp()
    path = os.path.join(tmp, video.name)
    with open(path, "wb") as f:
        f.write(video.read())
    st.video(video)
    if st.button("Generate Script"):
        frames = extract_frames(path, os.path.join(tmp,"frames"))
        captions = caption_images(frames)
        json_path = os.path.join(tmp,"captions.jsonl")
        generate_script(json_path, out_file=os.path.join(tmp,"script.txt"))
        st.success("Script generated! Check tmp folder.")
