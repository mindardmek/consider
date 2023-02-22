import scrapy
from scrapy.crawler import CrawlerProcess


class LsvpSpider(scrapy.Spider):
    name = 'lsvp_spider'
    allowed_domains = ['lsvp.com']
    start_urls = ['http://lsvp.com/portfolio/']

    def parse(self, response):
        # Initializes an empty dictionary to store the company domain
        company_domain = {}

        # Extracts the list of companies from the page using XPath selector
        company_list = response.xpath('//div[@class="portfolio-item"]')
        for company in company_list:
            # Extracts the type of ownership of the company using XPath
            ownership_type = company.xpath('.//div[@class="txt"]/strong/text()').get()
            
            # If the `ownership_type` is "Private Company", extract the domain of the company using XPath selector
            if ownership_type == 'Private Company':
                domain = company.xpath(
                    './/div[@class="txt"]/span/text()').get()

                # Creates a new key-value pair where the key is `lsvp.com` and the value is an empty list
                if 'lsvp.com' not in company_domain:
                    company_domain['lsvp.com'] = []
                # Appends the domain to the list in the `company_domain` dictionary
                company_domain['lsvp.com'].append(domain)

        # Yields a dictionary containing the company domain
        yield{
            'lsvp.com': company_domain['lsvp.com']
        }
        
process = CrawlerProcess(settings = {
    'FEED_URI': 'item.jl',
    'FEED_FORMAT': 'jl'
    })
process.crawl(LsvpSpider)
process.start()