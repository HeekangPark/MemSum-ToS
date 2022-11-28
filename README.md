# tos-summary
SNU CS &amp; AI 4190.678: Natural Language Processing

## Building the data
> NOTE: bug now fixed (bug: the website suspects that our scraper is calling abusive requests); needs to fully download data and filter it

### Example data format
Example data is in JSONL format (`.jsonl`), where each line in the file corresponds to a JSON object containing information of a document.
```
# ./examples/tosdr_instagram.jsonl
{
    "service": "Instagram", 
    "url": "https://edit.tosdr.org//services/219/annotate",
    "document_title": "Data Policy", 
    "original_text_length": 222, 
    "summary_length": 75, 
    "original_text": ["Data Policy", "This policy describes the information we process to support Facebook, Instagram, Messenger and other products and features offered by Facebook (Facebook Products or Products).", "You can find additional tools and information in the Facebook Settings and Instagram Settings.", ...],
    "summary": ["This policy describes the information we process to support Facebook, Instagram, Messenger and other products and features offered by Facebook (Facebook Products or Products).", "What kinds of information do we collect?", "To provide the Facebook Products, we must process information about you.", "The types of information we collect depend on how you use our Products.", ...]
}

The final dataset consists of only "text" and "summary", with all words lowercased.

```

### Commands
```
conda create -n tos-scraper python=3.9
```

```
pip install -r requirements.txt
```

```
python tosdr_scraper.py
```

Or run the notebook `test_tosdr.ipynb`.

To run the script in the background, specify the `nohup` and the `&` argument. The logs are written in real-time at the `nohup.out` file.
```
nohup python scrape/tosdr_scraper.py &
```
```
tail -f nohup.out
```

