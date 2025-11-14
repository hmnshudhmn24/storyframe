from pathlib import Path

def ensure_dir(path):
    Path(path).mkdir(parents=True, exist_ok=True)

def chunk_list(seq, size):
    for i in range(0, len(seq), size):
        yield seq[i:i+size]
