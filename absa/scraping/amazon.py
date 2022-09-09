from scrapy import Spider
from bs4 import BeautifulSoup


class AmazonSpider(Spider):
    name = "amazon"

    allowed_domains = ["amazon.com"]

    custom_settings = {
        "LOG_LEVEL": "INFO",
        "DOWNLOAD_DELAY": 2,  # delay between requests (in seconds),
        "CLOSESPIDER_ITEMCOUNT": 25,  # number of items to scrape
        "COOKIES_ENABLED": True,
        "USER_AGENT": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36",
    }

    def __init__(self, *args, **kwargs):
        super(AmazonSpider, self).__init__(*args, **kwargs)

        self.start_urls = [kwargs.get("start_url")]

    def get_text(self, el):
        return BeautifulSoup(el.extract(), "html.parser").get_text(
            strip=True,
            separator=" ",
        )

    def parse_rating_string(self, text):
        return int(float(text[:3]))

    def parse(self, response):
        data = response.css("#cm_cr-review_list")

        title = data.css(".review-title")
        star_ratings = data.css(".review-rating")
        feedback_text = data.css(".review-text > span")

        for i, _ in enumerate(star_ratings):
            yield {
                "title": self.get_text(title[i]),
                "rating": self.parse_rating_string(self.get_text(star_ratings[i])),
                "text": self.get_text(feedback_text[i]),
            }

        for next_page in response.css("li.a-last > a"):
            yield response.follow(next_page, self.parse)
