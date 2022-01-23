# Import libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def startDriver(searchTerm):
    # Connect to chrome driver -- google images search bar
    driver = webdriver.Chrome('C:\webdrivers/chromedriver.exe')
    driver.get("https://www.google.ca/imghp?hl=en")
    box = driver.find_element_by_xpath('//*[@id="sbtc"]/div/div[2]/input')

    box.send_keys(searchTerm)
    box.send_keys(Keys.ENTER)
    scrollToBottom(driver)
    downloadImages(driver, searchTerm)

    driver.quit()

def scrollToBottom(driver):
    #Will keep scrolling down the webpage until it cannot scroll no more
    last_height = driver.execute_script('return document.body.scrollHeight')
    while True:
        driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        time.sleep(2)
        new_height = driver.execute_script('return document.body.scrollHeight')
        try:
            driver.find_element_by_xpath('//*[@id="islmp"]/div/div/div/div/div[5]/input').click()
            time.sleep(2)
        except:
            pass
        if new_height == last_height:
            break
        last_height = new_height

def downloadImages(driver, searchTerm):
    # Edit search term
    searchTerm = searchTerm.split()
    del searchTerm[2]
    searchTerm = "_".join(searchTerm)

    # Download 1000 images
    for i in range(1000):
        try:
            # Skip first three images (blocked by google UI)
            image = driver.find_element_by_xpath('//*[@id="islrg"]/div[1]/div[' + str(i+4) + ']/a[1]/div[1]/img')
            image.screenshot('./' + searchTerm + 's/' + searchTerm + '_' + str(i+1) + '.png')
        except:
            pass

searchTerms = ["one dollar us bill", "five dollar us bill", "ten dollar us bill", "twenty dollar us bill", "fifty dollar us bill", "hundred dollar us bill"]
for searchTerm in searchTerms:
    startDriver(searchTerm)