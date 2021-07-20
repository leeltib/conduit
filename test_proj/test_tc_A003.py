# A003 test case - Új blogbejegyzés készítése - kilépés.

import data.data_tcA003 as da03
import func.func_01 as fu01

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager               # webdriver-manager / Chrome

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')

#driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)       # Headless mód
driver = webdriver.Chrome(ChromeDriverManager().install())                              # normál mód

driver.get("http://localhost:1667")

# Várakozás a betöltésre
fu01.wait(driver, By.ID, "app")
time.sleep(2)

# *** TC-A003 **************************************


def test_A003():
    fu01.sign_in(driver, da03.mail, da03.passw)
    wr_cont = fu01.blog_write(driver, da03)
    fu01.out_close_driver(driver)
    return wr_cont


write_add_text = test_A003()


# ***************************************************

# normál futtatáshoz:
if __name__ == "__main__":
    print(write_add_text)
    try:
        assert da03.write == write_add_text
    except:
        print("Hiba, az ellenőrző feltételnél nincs egyezés.")


