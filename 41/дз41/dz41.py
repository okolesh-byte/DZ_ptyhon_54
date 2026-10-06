import csv
from html.parser import HTMLParser
from urllib.request import urlopen


class QuoteParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.quotes = []
        self.item = None
        self.read_text = False
        self.read_author = False
        self.read_tag = False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        css = attrs.get("class", "")

        if tag == "div" and "quote" in css:
            self.item = {"text": "", "author": "", "tags": []}
        elif self.item is not None and tag == "span" and "text" in css:
            self.read_text = True
        elif self.item is not None and tag == "small" and "author" in css:
            self.read_author = True
        elif self.item is not None and tag == "a" and "tag" in css:
            self.read_tag = True

    def handle_data(self, data):
        if self.item is None:
            return

        data = data.strip()
        if data == "":
            return

        if self.read_text:
            self.item["text"] = data
        elif self.read_author:
            self.item["author"] = data
        elif self.read_tag:
            self.item["tags"].append(data)

    def handle_endtag(self, tag):
        if tag == "span":
            self.read_text = False
        elif tag == "small":
            self.read_author = False
        elif tag == "a":
            self.read_tag = False
        elif tag == "div" and self.item is not None:
            if self.item["text"] != "":
                self.quotes.append(self.item)
            self.item = None


class Scraper:
    def __init__(self, url):
        self.url = url
        self.data = []

    def get_html(self, page):
        address = self.url + "/page/" + str(page) + "/"
        with urlopen(address) as response:
            return response.read().decode("utf-8")

    def parse(self, pages):
        for page in range(1, pages + 1):
            parser = QuoteParser()
            parser.feed(self.get_html(page))
            self.data.extend(parser.quotes)

    def save(self, filename):
        with open(filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["quote", "author", "tags"])
            for item in self.data:
                writer.writerow([item["text"], item["author"], ", ".join(item["tags"])])


site = Scraper("https://quotes.toscrape.com")
site.parse(3)
site.save("quotes_pages.csv")
print("Сохранено:", len(site.data))
print("Файл: quotes_pages.csv")
