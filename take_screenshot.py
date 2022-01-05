import ast
import time
import random
import sqlite3
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# def take_screenshot(cursor, driver, row):
    # links = ast.literal_eval(row)
    # links_screenshots = []

    # for link in links:
    #     driver.get(link)
    #     time.sleep(2)
    #     # height = driver.execute_script("return Math.max( document.body.scrollHeight, document.body.offsetHeight, document.documentElement.clientHeight, document.documentElement.scrollHeight, document.documentElement.offsetHeight);")
    #     driver.set_window_size(1920, 3000)

    #     file_name = "-".join([str(random.randint(1000, 9999)) for i in range(4)])

    #     driver.save_screenshot(f'screenshots/{file_name}.png')

    #     links_screenshots.append([link, file_name])

    # return links_screenshots


def main():
    conn = sqlite3.connect("alfa_bee.db", check_same_thread=False)
    cursor = conn.cursor()

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(chrome_options=chrome_options)

    # df = pd.read_csv("kw_links_1.csv")

    # df["sites"] = df["sites"].agg(lambda row: take_screenshot(cursor, driver, row))

    cursor.execute("SELECT * FROM t;")
    results = cursor.fetchall()

    count = 0

    for row in results:
        try:
            driver.get(row[1])
            time.sleep(2)
            driver.execute_script("window.ResizeObserver = undefined;")
            height = driver.execute_script("return Math.max( document.body.scrollHeight, document.body.offsetHeight, document.documentElement.clientHeight, document.documentElement.scrollHeight, document.documentElement.offsetHeight);")
            if height > 3000:
                driver.set_window_size(1920, 3000)
            elif height > 0:
                driver.set_window_size(1920, height)

            driver.save_screenshot(f'screenshots/{row[2]}.png')

            count += 1
            print(count)
        except:
            pass

    driver.quit()

    # df.to_csv("kw_links_screenshots.csv")
    

if __name__ == "__main__":
    main()