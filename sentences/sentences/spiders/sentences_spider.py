import scrapy
from kanjisite.manageset.models import Sentence
from kanjisite.manageset.models import Words
from sentence.items import SentanceItem

class TatoebaSpider(scrapy.Spider):
    name = "tatoeba_sentences"
    allowed_domains = ["tatoeba.org"]
    start_urls = ["www.tatoeba.org"]
    words = Words.objects.filter(id = 3000)
    print words
    
    

    def parse(self, response):
        for row in response.css("body"):
            item = SentenceItem()
            item['sentence'] = row.css("td:nth-child(1)::text").extract()
            yield item