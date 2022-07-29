# Home-Router-Wiki
The Home Router Wiki is a Tool for scraping firmware from multiple vendor webpages using [FirmwareScraper](https://github.com/fkie-cad/FirmwareScraper) , collect information and visualize them on a webpage-wiki using [hugo](https://gohugo.io/) and [geekdocs](https://geekdocs.de/) 

## Installation
### FirmwareScraper
Ubuntu 14.04 and above

Some packages need to be installed using apt-get/apt before installing scrapy

```bash
sudo apt-get install python-dev python-pip libxml2-dev libxslt1-dev zlib1g-dev libffi-dev libssl-dev
```

As python 2 is almost at EOL, python3 additionally needs python3-dev

```bash
sudo apt-get install python3 python3-dev
```



#### Scrapy

Scrapy can then be installed using the following command:

```bash
pip install scrapy
```

For more information about the installation process of scrapy, see [here](https://docs.scrapy.org/en/latest/intro/install.html#intro-install) .



#### FirmwareScraper 

To use the existing scrapy project, just clone it into a repository of your choice

```bash
git clone https://github.com/fkie-cad/FirmwareScraper.git
```

To run a spider, just go into the project's folder and type the following command into the terminal:

```bash
scrapy crawl *name of spider e.g. avm* -o *name of file to output metadata e.g. spidername.json*
```



#### Selenium

Selenium can then be installed using the following command:

```bash
pip install -U selenium
```

download [geckodriver](https://github.com/mozilla/geckodriver/releases) or [chromedriver](https://chromedriver.chromium.org/downloads)

For selenium to be able to render the desired page you need a driver executable (geckodriver, chromedriver etc.) to be in the correct path in the settings.py.

```bash
SELENIUM_DRIVER_EXECUTABLE_PATH = '/home/username/driver/geckodriver'
```

For more information about the installation process of selenium, [see here](https://selenium-python.readthedocs.io/installation.html).

To get the supported drivers for selenium [see here](https://selenium-python.readthedocs.io/installation.html).



#### Beautiful Soup

Some spiders use Beautiful Soup to search for attributes in a webpage.

```bash
pip install beautifulsoup4
```

For more information about the installation process of Beautiful Soup, [see here](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-beautiful-soup).



### Hugo: Geekdoc

Hugo can then be installed using the following command:

```bash
sudo apt install hugo
```



Install Requirements

```bash
sudo apt install npm
```



