import csv
from html.parser import HTMLParser
from urllib.request import urlopen


class QuotesParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.quotes = []
        self.current = None
        self.tag_mode = False
        self.text_mode = False
        self.author_mode = False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        class_name = attrs.get("class", "")

        if tag == "div" and "quote" in class_name.split():
            self.current = {"text": "", "author": "", "tags": []}
        elif self.current is not None and tag == "span" and "text" in class_name.split():
            self.text_mode = True
        elif self.current is not None and tag == "small" and "author" in class_name.split():
            self.author_mode = True
        elif self.current is not None and tag == "a" and "tag" in class_name.split():
            self.tag_mode = True

    def handle_data(self, data):
        if self.current is None:
            return

        data = data.strip()
        if not data:
            return

        if self.text_mode:
            self.current["text"] += data
        elif self.author_mode:
            self.current["author"] += data
        elif self.tag_mode:
            self.current["tags"].append(data)

    def handle_endtag(self, tag):
        if tag == "span":
            self.text_mode = False
        elif tag == "small":
            self.author_mode = False
        elif tag == "a":
            self.tag_mode = False
        elif tag == "div" and self.current is not None:
            if self.current["text"] and self.current["author"]:
                self.quotes.append(self.current)
            self.current = None


def load_page(url):
    with urlopen(url) as response:
        return response.read().decode("utf-8")


def save_to_csv(quotes, filename):
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["quote", "author", "tags"])
        for quote in quotes:
            writer.writerow([
                quote["text"],
                quote["author"],
                ", ".join(quote["tags"])
            ])


url = "https://quotes.toscrape.com/"
html = load_page(url)
parser = QuotesParser()
parser.feed(html)
save_to_csv(parser.quotes, "quotes.csv")

print("Сохранено записей:", len(parser.quotes))
print("Файл: quotes.csv")
