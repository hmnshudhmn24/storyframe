import json, argparse
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

def generate_script(captions_file, model="google/flan-t5-small", out_file="script.txt"):
    items = [json.loads(x) for x in open(captions_file)]
    text = " ".join([i["caption"] for i in items])
    prompt = "Generate a cinematic script for these scene captions: " + text
    tokenizer = AutoTokenizer.from_pretrained(model)
    model = AutoModelForSeq2SeqLM.from_pretrained(model)
    inputs = tokenizer(prompt, return_tensors="pt", truncation=True)
    outputs = model.generate(**inputs, max_new_tokens=300)
    result = tokenizer.decode(outputs[0], skip_special_tokens=True)
    open(out_file, "w").write(result)
    print("Script saved to", out_file)

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--captions", default="captions.jsonl")
    p.add_argument("--model", default="google/flan-t5-small")
    p.add_argument("--out", default="script.txt")
    args = p.parse_args()
    generate_script(args.captions, model=args.model, out_file=args.out)
