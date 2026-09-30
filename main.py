from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import json
import pandas as pd


def get_developer_banks(driver: webdriver.Chrome, dev_id: int):
    driver.get(f"https://xn--80az8a.xn--d1aqf.xn--p1ai/%D1%81%D0%B5%D1%80%D0%B2%D0%B8%D1%81%D1%8B/%D0%B5%D0%B4%D0%B8%D0%BD%D1%8B%D0%B9-%D1%80%D0%B5%D0%B5%D1%81%D1%82%D1%80-%D0%B7%D0%B0%D1%81%D1%82%D1%80%D0%BE%D0%B9%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/%D0%B7%D0%B0%D1%81%D1%82%D1%80%D0%BE%D0%B9%D1%89%D0%B8%D0%BA/{dev_id}")
    links = driver.find_elements(By.CLASS_NAME, 'Tabs__NewTabsItem-sc-jsq7op-3')
    for link in links:
        if link.text == "Уполномоченные банки":
            link.click()
            break

    time.sleep(3)

    table = driver.find_element(By.CLASS_NAME, "Table-sc-17it3za-0")

    try:
        link = table.find_element(By.CLASS_NAME, "AccNumberCell__CellButton-sc-117ovkm-1")
        link.click()
        time.sleep(3)
    except Exception:
        pass

    column_elements = table.find_elements(By.CLASS_NAME, "BaseCell__Cell-sc-7809tj-0")


    return {
        "dev_id": dev_id,
        "Название банка": column_elements[0].text,
        "Расчетный счет": column_elements[1].text,
        "РнС, для которого открыт счет": column_elements[2].text,
        "ИНН банка": column_elements[3].text,
        "ОГРН банка": column_elements[4].text,
        "БИК банка": column_elements[5].text,
    }


def main():
    with open('developers.json') as f:
        developers = json.load(f)

    driver = webdriver.Chrome()
    driver.get("https://google.com")
    df = pd.DataFrame()
    for developer in developers:
        try:
            dev_id = developer['devId']
            bank_data = get_developer_banks(driver, dev_id)
            df = pd.concat([df, pd.DataFrame([bank_data], index=[0])], ignore_index=True)
            df.to_excel('developers_bank.xlsx', index=False)
        except Exception:
            pass

    driver.quit()


if __name__ == "__main__":
    main()
