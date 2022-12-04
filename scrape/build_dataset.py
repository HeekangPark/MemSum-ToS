import pickle
import os
from tqdm import tqdm
import ujson
import random
from pathlib import Path

def load_pickle(file_path):
    with open(file_path, 'rb') as handle:
        object = pickle.load(handle)
    return object

PICKLE_PATH = "./pickles"
OUT_PATH = "./dataset"

def pickle_to_dataset(out_label="v1_minimum_preprocess", file_name=None):
    pickle_path = Path(PICKLE_PATH)
    out_path = Path(OUT_PATH)
    write_f = open(out_path / f"full_{out_label}.jsonl", 'w')
    
    if file_name:
        print("Loading", file_name)
        block_dicts = load_pickle(pickle_path / file_name)
        for block_dict in tqdm(block_dicts):
            new_dict = {"text": [text.lower() for text in block_dict["text"]],
                        "summary": [summary.lower() for summary in block_dict["summary"]]}
            write_f.write(ujson.dumps(new_dict) + '\n')
    
    else:
        for _, _, files in os.walk(pickle_path):
            for file in sorted(files):
                if file.startswith("tosdr_block"):
                    print("Loading", file)
                    block_dicts = load_pickle(pickle_path / file)
                    for block_dict in tqdm(block_dicts):
                        new_dict = {"text": [text.lower() for text in block_dict["text"]],
                                    "summary": [summary.lower() for summary in block_dict["summary"]]}
                        write_f.write(ujson.dumps(new_dict) + '\n')
    
    with open(out_path / f"full_{out_label}.jsonl", 'r') as f:
        data = f.readlines()
    
    random.seed(77)
    random.shuffle(data)
    
    n = len(data)
    train_size = int(n * 0.8)
    val_size = (n - train_size) // 2 + 1
    # test_size = n - train_size - val_size
    
    out_path = out_path / out_label
    out_path.mkdir(exist_ok=True)
    
    with open(out_path / "train.jsonl", 'w') as f:
        f.writelines(data[:train_size])
    with open(out_path / "validation.jsonl", 'w') as f:
        f.writelines(data[train_size:train_size+val_size])
    with open(out_path / "test.jsonl", 'w') as f:
        f.writelines(data[train_size+val_size:])
    

if __name__ == "__main__":
    pickle_to_dataset(out_label="v2_remove_1word", file_name="tosdr_v2_removed_1word.pickle")
                    
    