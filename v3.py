from splinter import Browser
from bs4 import BeautifulSoup
from time import sleep
def getRoutes(start,end):
    browser = Browser(
        driver_name="firefox"
)
    browser.visit('https://www.hopstop.com/search?xfr=cityscape')
    print(browser.url)
    browser.fill('address1',str(start))
    browser.fill('address2',str(end))
    browser.find_by_name('get_dirs').click()
    print(browser.url)
    if browser.is_text_present('Did you mean?'):
        browser.click_link_by_href("#")
        if browser.is_text_present('Did you mean?'):
            browser.click_link_by_href("#")
    browser.click_link_by_href("#")
    links = browser.find_link_by_partial_href("/station?stid")
    results = []
    for link in links:
        results.append(link.value)
    return results
print(getRoutes("Kew Gardens", "Stuyvesant High School"))
