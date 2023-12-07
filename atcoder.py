from time import sleep
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver


browser = webdriver.Chrome()
browser.get(
    "https://www.dropbox.com/sh/nx3tnilzqz7df8a/AAAYlTq2tiEHl5hsESw6-yfLa?dl=0",
)


sleep(10)


# Find all elements with class "dig-LabelGroup-content"
# Or we can also find all elements with class "_sl-list-column-hover_1oha5_41"
elements = browser.find_elements(By.CLASS_NAME, "dig-LabelGroup-content")

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

    sleep(2)

    # Delete the div element with class "ReactModalPortal"
    # The div element with class "ReactModalPortal" is the modal that appears
    # after clicking the download button

    # modal = browser.find_element(By.CLASS_NAME, "ReactModalPortal")
    browser.execute_script(
        "document.querySelectorAll('.ReactModalPortal').forEach(e => e.remove())",
    )

    sleep(2)


sleep(60)


def first_dig_label_group_content():
    # Find first element with class "dig-LabelGroup-content" and move the cursor to it
    # without clicking it
    first_element = browser.find_element(By.CLASS_NAME, "dig-LabelGroup-content")
    webdriver.ActionChains(browser).move_to_element(first_element).perform()
    sleep(3)
