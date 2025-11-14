import os, argparse, json
from transformers import pipeline
from utils import chunk_list

def caption_images(frames, model="Salesforce/blip-image-captioning-base", out_jsonl="captions.jsonl"):
    cap = pipeline("image-to-text", model=model)
    results = []
    for chunk in chunk_list(frames, 4):
        imgs = [p for p, _ in chunk]
        outs = cap(imgs)
        for (path, t), out in zip(chunk, outs):
            caption = out[0].get("generated_text", "") if isinstance(out, list) else str(out)
            results.append({"frame": path, "time": float(t), "caption": caption})
    with open(out_jsonl, "w") as f:
        for r in results:
            f.write(json.dumps(r) + "\n")
    return results
