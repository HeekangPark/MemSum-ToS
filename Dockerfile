FROM python:3.9

WORKDIR /app
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt
COPY ./scrape/test_tosdr.ipynb /app/test_tosdr.ipynb
COPY ./scrape/tosdr_scraper.py /app/tosdr_scraper.py
ENTRYPOINT [ "python",  "/app/tosdr_scraper.py"]