<h1>Scraping Zillow Rentals</h1>
<p>This is a python script that scrapes rental information from Zillow's website. The data that is scraped includes rental prices, addresses and url links for each property. The data is then stored in 3 separate lists named url_links, prices_list and addresses_list.</p>

<h2>Prerequisites</h2>
To run this script, you need to have the following python packages installed:
<ul>
    <li>BeautifulSoup</li>
    <li>Requests</li>
    <li>Lxml</li>
    <li>Selenium</li>
    <li>Webdriver Manager</li>
</ul>
<h4>You can install these packages using pip:</h4>
<ol>
    <li>pip install beautifulsoup4</li>
    <li>pip install requests</li>
    <li>pip install lxml</li>
    <li>pip install selenium</li>
    <li>pip install webdriver-manager</li>
</ol>
<h3>Script Walk-through</h3>
<p>
    The first step in the script is to make a GET request to the Zillow website using the Requests library. The headers are added to the request to mimic the request being made by a web browser. The response from the website is stored in a variable named response.
    The next step is to parse the raw html content of the response into a BeautifulSoup object. This object can then be used to extract specific information from the html. In this script, the information that is of interest is the rental prices, addresses, and url links of each property.
    A function named extract_number is defined to extract only the decimal part from a string. This function will be used to extract the rental prices.
    The script then loops through each rental property on the Zillow website and extracts the necessary information. The rental price, address, and url link are stored in the prices_list, addresses_list and url_links lists respectively.
    Finally, the script opens a new instance of the Chrome web browser using the Selenium library. The Chrome driver is managed by the Webdriver Manager library. The script then visits each of the rental properties by navigating to the url stored in the url_links list and extracts further information from the property's webpage.
</p>
<h6><em>Conclusion</em></h6>
<hr noshade>
<p>This script is a great starting point for anyone who wants to scrape rental information from the Zillow website. With a few modifications, the script can be used to scrape other types of information from the Zillow website or from other websites altogether. The script serves as a demonstration of the power of web scraping and how it can be used to gather valuable data for various purposes.</p>
