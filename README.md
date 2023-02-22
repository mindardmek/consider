## Amplify Partners

#### Assumptions
The Web Scraper is designed to function with “https://www.amplifypartners.com/portfolio/”, and assumes the website's structure and content to be stable. The Web Scraper also assumes that the website has no access controls or restrictions that would hinder content accessibility. However, the website's content is dynamically loaded by JavaScript, which requires the implementation of a third-party Python library to overcome this limitation. The Web Scraper further assumes that the website's terms of service permit web scraping, and that it exclusively extracts data from companies with active investment status.

#### Architecture
The Web Scraper is built using Python3 and the Scrapy web scraping framework. It incorporates the Playwright browser automation library to render the JavaScript website and extract the desired content. The project also includes a custom setting for the Playwright package to enable headless mode. The project employs a modular design approach, where each module is responsible for a specific task such as fetching web pages, parsing HTML content, and data extraction.

#### Data Structures
The Web Scraper stores extracted data in jl format. The output data is a .jl file with "amplifypartners.com" as its key and the domain of the companies with active investment status as its list of values.

#### Testing Methodology
The Web Scraper and its Xpath selectors were rigorously tested in Scrapy shell. In addition, the extracted data underwent manual review for accuracy and completeness.

## Lightspeed Venture Partners

#### Assumptions
The Web Scraper is designed to function with “https://lsvp.com/portfolio/”, and assumes the website's structure and content to be stable. The Web Scraper also assumes that the website has no access controls or restrictions that would hinder content accessibility. The Web Scraper further assumes that the website's terms of service permit web scraping, and that it exclusively extracts data from private companies.

#### Architecture
The Web Scraper is built using Python3 and the Scrapy web scraping framework to extract the desired content. The project employs a modular design approach, where each module is responsible for a specific task such as fetching web pages, parsing HTML content, and data extraction.

#### Data Structures
The Web Scraper stores extracted data in jl format. The output data is a .jl file with "lsvp.com" as its key and the domain of the private companies as its list of values.

#### Testing Methodology
The Web Scraper and its Xpath selectors were rigorously tested in Scrapy shell. In addition, the extracted data underwent manual review for accuracy and completeness.
