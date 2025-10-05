import undetected_chromedriver as uc
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from bs4 import BeautifulSoup
import time

chrome_options = uc.ChromeOptions()
chrome_options.add_argument("--incognito")  #open tab in incognito window
# chrome_options.add_experimental_option('detach',True)   #to hold the window on screen
chrome_options.add_argument('--disable-notifications')
chrome_options.add_argument('--disable-infobars')

driver = uc.Chrome(options=chrome_options)

driver.get('https://www.99acres.com/search/property/buy/residential-apartments/gurgaon?city=8&property_type=1&preference=S&area_unit=1&res_com=R')
time.sleep(4)

## select only resale flats
try:
    purchase_type = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//span[text()="Purchase type"]'))
    )

    # Scroll to the element
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", purchase_type)
    time.sleep(1)

    # Click it using JavaScript (safe for non-clickable spans)
    driver.execute_script("arguments[0].click();", purchase_type)
    print("✅ Clicked on 'Purchase type' span.")
    time.sleep(1)

    resale_btn = driver.find_element(By.XPATH , '//span[text() = "Resale"]')
    driver.execute_script("arguments[0].click();", resale_btn)
    time.sleep(2)

except Exception as e:
    print("Could not click purchase type':", e)


#extract links of resale flats
links = []
old_height = driver.execute_script('return document.body.scrollHeight')
count = 0

while True:
    time.sleep(2)

    ##scroll to bottom of page
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
    time.sleep(2)

    new_height = driver.execute_script('return document.body.scrollHeight')

    print("old height" , old_height)
    print('new height' , new_height)

    if new_height == old_height:

        count+=1
        print('count : ',count)
        print("new height = old height")

        soup = BeautifulSoup(driver.page_source, 'html.parser')
        page_links = soup.find_all('a', class_ = "tupleNew__propertyHeading ellipsis")
        for tag in page_links:
            href = tag.get('href')
            if href:
                links.append(href)
        print('total links = ', len(links))
        try:

            driver.execute_script("""const banner = document.getElementById('cs_PopUp');
                                  if (banner) banner.remove();""")  #remove any banner blocking click on next_button

            next_button = driver.find_element(By.XPATH, '//a[contains(text(), "Next")]') 
            # Scroll to make sure it’s visible
            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", next_button)
            time.sleep(1)
            next_button.click()
            print("✅ Clicked on the next page.")

        except Exception as e:
            print("Could not click the next button:", e)
            break

    else:
        old_height = new_height
    
    if len(links)>=6000:
      break

with open('webscrape_links.txt', 'w') as f:
    f.write("\n".join(links))

# Pause the script to keep the browser open
input("Press ENTER to exit...")


#<a href="https://www.99acres.com/flats-in-gurgaon-ffid-page-7" class="list_header_bold">Next Page &gt;</a>

#<a class="list_header_bold">Next Page &gt;</a>
#<a class="list_header_bold">Next Page &gt;</a>

#/html/body/div[1]/div/div/div[4]/div[3]/div[3]/div[4]/a
#//*[@id="app"]/div/div/div[4]/div[3]/div[3]/div[4]/a

#