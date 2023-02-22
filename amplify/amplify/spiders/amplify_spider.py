import scrapy
from scrapy.crawler import CrawlerProcess


class AmplifySpider(scrapy.Spider):
    name = 'amplify_spider'

    def start_requests(self):
        # Sends a request to the URL using Playwright
        yield scrapy.Request('https://www.amplifypartners.com/portfolio/', meta={'playwright': True})

    def parse(self, response):

        # Initializes an empty dictionary to store the company domain
        company_domain = {}

        # Extracts the list of companies from the page using XPath selector
        company_list = response.xpath('//div[@role="listitem"]')

        for company in company_list:
            # Extracts the status of the company using XPath
            company_status = company.xpath(
                './/div[@class="status-div"]//text()').get()

            # If the `company_status` is "Active", extract the domain of the company using XPath selector
            if company_status == 'Active':
                domain = company.xpath(
                    './/div[@class="website__link-wr"]/a/text()').get()

                # Creates a new key-value pair where the key is `amplifypartners.com` and the value is an empty list
                if 'amplifypartners.com' not in company_domain:
                    company_domain['amplifypartners.com'] = []

                # Appends the domain to the list in the `company_domain` dictionary
                company_domain['amplifypartners.com'].append(domain)

        # Yields a dictionary containing the company domain
        yield{
            'amplifypartners.com': company_domain['amplifypartners.com']
        }


process = CrawlerProcess(settings={
    'FEED_URI': 'item.jl',
    'FEED_FORMAT': 'jl'
})
process.crawl(AmplifySpider)
process.start()
