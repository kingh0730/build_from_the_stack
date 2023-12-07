from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver


browser = webdriver.Chrome()
browser.get(
    "https://www.dropbox.com/sh/nx3tnilzqz7df8a/AAAYlTq2tiEHl5hsESw6-yfLa?dl=0",
)


sleep(10)


# Find all elements with class "_sl-list-column-hover_1oha5_41"
elements = browser.find_elements(By.CLASS_NAME, "_sl-list-column-hover_1oha5_41")

for element in elements:
    # Move the cursor to the element without clicking it
    webdriver.ActionChains(browser).move_to_element(element).perform()

    sleep(2)

    # Find the download button and click it
    # The download button has the "data-testid" attribute set to "list-item-hover-download-button"
    download_button = element.find_element(
        By.CSS_SELECTOR, '[data-testid="list-item-hover-download-button"]'
    )
    download_button.click()

    sleep(3)


sleep(60)


def first_dig_label_group_content():
    # Find first element with class "dig-LabelGroup-content" and move the cursor to it
    # without clicking it
    first_element = browser.find_element(By.CLASS_NAME, "dig-LabelGroup-content")
    webdriver.ActionChains(browser).move_to_element(first_element).perform()
    sleep(3)
