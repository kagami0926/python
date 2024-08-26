from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import csv
import re

class SearchBook:
    def __init__(self, search_words):
        self.lib_url = "https://jimkilisuf1.admin.tus.ac.jp/"
        self.search_words = search_words

        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")

        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get(self.lib_url)

    def search_book_lists(self):
        search_box = self.driver.find_element(By.ID, 'opac_tab_keywd0')
        search_box.send_keys(self.search_words)
        button = self.driver.find_element(By.XPATH, '/html/body/table/tbody/tr[2]/td/table/tbody/tr/td[2]/div/table/tbody/tr/td/div[1]/table/tbody/tr/td/div/div/div/div[1]/div[1]/div[1]/div[1]/tab_body/div[1]/form/table/tbody/tr[2]/td/button')
        button.click()
        time.sleep(2)

        titles = self.driver.find_elements(By.CLASS_NAME, "opac_book_title")
        book_title_lists = [title.text for title in titles]

        book_url_lists = []
        for i in range(11):
            try:
                url_element = self.driver.find_element(By.ID, f'link{i}_2960')
                book_url_lists.append(url_element.get_attribute('href'))
            except:
                book_url_lists.append('')

        combined_lists = [[title, url] for title, url in zip(book_title_lists, book_url_lists)]
        return combined_lists

    def save_to_csv(self, file_name):
        combined_lists = self.search_book_lists()
        with open(file_name, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["Title", "URL"])
            writer.writerows(combined_lists)

    def __del__(self):
        self.driver.quit()

def sanitize_filename(filename):
    return re.sub(r'[<>:"/\\|?*\x00-\x1F]', '_', filename)

search_words = ["量子物理学", "宇宙物理学", "電磁気学", "相対論", "熱力学"]

for word in search_words:
    sanitized_word = sanitize_filename(word)
    file_name = f'LibrarySearch/csv/{sanitized_word}.csv'
    search_book = SearchBook(word)
    search_book.save_to_csv(file_name)
    print(f'Saved search results for "{word}" to {file_name}')
