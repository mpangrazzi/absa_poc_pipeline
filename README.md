## A GPT-3-based proof-of-concept Aspect-Based Sentiment Analysis pipeline

This is the code related to the article <link>.

Note that this is a **proof-of-concept** and not a production-ready pipeline. It is not meant to be used in production by any means, but rather to demonstrate the potential of the approach.

## Setup

### Setup virtual environment

```bash
$ python3 -m venv .venv
$ source .venv/bin/activate
```

### Install dependencies

```bash
$ pip install -r requirements.txt
```

## Scraping

### Using CLI

To run the [Scrapy](https://scrapy.org) spider on a specific Amazon url, you can do:

```bash
$ scrapy runspider \
  absa/scraping/amazon.py \
  -O reviews.csv \
  -a start_url='https://www.amazon.com/FIODIO-Comfortable-Anti-Ghosting-Resistant-Multimedia/product-reviews/B086168Y25/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews'
```

It will automatically follow the next pages until the required number of items have been scraped.

### Using the notebook

You can also play with the notebook `notebooks/scraping.ipynb` to see how the scraping works.

## Analysis

The documented analysis pipeline is in `notebooks/analysis.ipynb`.
