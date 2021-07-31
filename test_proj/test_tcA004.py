# test case A004 - Saját, meglévő blogbejegyzés módosítása - kilépés.

import data.data_tcA004 as da04
import func.func_01 as fu01

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.headless = True
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)

driver.get("http://localhost:1667")

# Wait for loading
fu01.wait(driver, By.ID, "app", 2)

# *** TC-A004 **************************************


def test_A004():
    fu01.cookie_ok(driver)
    fu01.sign_in(driver, da04.mail, da04.passw)
    wri_cont = fu01.blog_edit(driver, da04)
    fu01.out_close_driver(driver)
    return wri_cont


write_edit_text = test_A004()


# ***************************************************

# Normal run
if __name__ == "__main__":
    print(write_edit_text)
    try:
        assert da04.write == write_edit_text
    except:
        print("Hiba, az ellenőrző feltételnél nincs egyezés.")


