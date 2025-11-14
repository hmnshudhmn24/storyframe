# 🎬 STORYFRAME — Video-to-Story Generation

Transform any video clip into a **cinematic-style script** using STORYFRAME! This project extracts frames, captions them with AI, and weaves them into an expressive screenplay-like narrative.



## ✨ Features

* 🎞️ **Frame Extraction** — Break videos into key frames.
* 🧠 **AI Captioning** — Generate meaningful descriptions for each frame.
* 🎭 **Script Generation** — Convert captions into a movie-style scene script.
* 🌐 **Streamlit Web App** — Simple UI to upload videos and generate scripts instantly.



## 📂 Project Structure

```
STORYFRAME/
├── extract_frames.py
├── caption_frames.py
├── generate_script.py
├── app.py
└── README.md
```



## 🚀 Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/STORYFRAME.git
cd STORYFRAME
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```



## 🛠️ How It Works

### Step 1: Extract Frames

```bash
python extract_frames.py --video input.mp4
```

This will create a folder named `frames/` containing extracted images.

### Step 2: Caption Frames

```bash
python caption_frames.py --frames_dir frames
```

This generates `captions.jsonl` containing descriptions for each frame.

### Step 3: Generate Cinematic Script

```bash
python generate_script.py --captions captions.jsonl
```

The final movie-style script is saved as `script.txt`.

---

## 🌐 Streamlit App

Launch the full UI-based application:

```bash
streamlit run app.py
```

### 🎛️ App Features:

* Upload any video (`.mp4`, `.mov`, `.avi`)
* Preview video instantly
* Auto-extract frames ➜ caption ➜ generate script
* Download or view results



## 📸 Example Workflow

1. Upload a video clip 🎥
2. Click **Generate Script** ✨
3. STORYFRAME produces:

   * Extracted frames folder
   * `captions.jsonl`
   * `script.txt` cinematic story 🎬



## 💡 Use Cases

* Film scene breakdowns
* Creative writing inspiration
* Storyboarding
* AI content creation
