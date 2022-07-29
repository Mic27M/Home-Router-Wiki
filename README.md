# Home-Router-Wiki
The Home Router Wiki is a Tool for scraping firmware from multiple vendor webpages using [FirmwareScraper](https://github.com/fkie-cad/FirmwareScraper) , collect information and visualize them on a webpage-wiki using [hugo](https://gohugo.io/) and [geekdocs](https://geekdocs.de/) 

## Installation
### FirmwareScraper
#### Dependencies
Ubuntu 14.04 and above

Some packages need to be installed using apt-get/apt before installing scrapy

sudo apt-get install python-dev python-pip libxml2-dev libxslt1-dev zlib1g-dev libffi-dev libssl-dev

As python 2 is almost at EOL, python3 additionally needs python3-dev

sudo apt-get install python3 python3-dev

Scrapy can then be installed using the following command:

pip install scrapy

pip install -U selenium

download geckodriver or chromedriver https://www.selenium.dev/selenium/docs/api/py/

For more information about the installation process of scrapy, see here.
Use

To use the existing scrapy project, just clone it into a repository of your choice

git clone https://github.com/mellowCS/FirmwareScraper.git

To run a spider, just go into the project's folder and type the following command into the terminal:

scrapy crawl *name of spider e.g. avm* -o *name of file to output metadata e.g. spidername.json*

Selenium

pip install selenium


For selenium to be able to render the desired page you need a driver executable (geckodriver, chromedriver etc.) to be in the correct path in the settings.py.

SELENIUM_DRIVER_EXECUTABLE_PATH = '/home/username/driver/geckodriver'

For more information about the installation process of selenium, see here.

To get the supported drivers for selenium see here.
Beautiful Soup

Some spiders use Beautiful Soup to search for attributes in a webpage.

pip install beautifulsoup4

For more information about the installation process of Beautiful Soup, see here.
