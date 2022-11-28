import pickle
import os
import pandas as pd
from tqdm import tqdm

def dump_pickle(file_path, object):
    with open(file_path, 'wb') as handle:
        pickle.dump(object, handle)

def load_pickle(file_path):
    with open(file_path, 'rb') as handle:
        object = pickle.load(handle)
    return object

def gather_stats():
    PICKLE_PATH = "./pickles"
    stats = []
    # df = pd.DataFrame(columns=["block_num", "idx_in_block", "text_length", "summary_length", "ratio"])
    
    for _, _, files in os.walk(PICKLE_PATH):
        for file in sorted(files):
            if file.startswith("tosdr_block"):
                print("Processing", file)
                block_num = file.split('.')[0].split('_')[2]
                block_dicts = load_pickle(PICKLE_PATH + '/' + file)
                for i, block_dict in enumerate(tqdm(block_dicts)):
                    text_len = len(block_dict["text"])
                    summary_len = len(block_dict["summary"])
                    stats.append({"block_num": block_num, 
                                  "idx_in_block": i, 
                                  "text_length": text_len, 
                                  "summary_length": summary_len, 
                                  "ratio": summary_len / text_len})
    df =pd.DataFrame.from_records(stats)
    dump_pickle(PICKLE_PATH + '/tosdr_stats_df.pickle', df)
    

if __name__ == "__main__":
    gather_stats()