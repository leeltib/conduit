# test case A003 - New blog post  - exit

import data.data_tcA003 as da03
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

# *** TC-A003 **************************************


def test_A003():
    fu01.cookie_ok(driver)
    fu01.sign_in(driver, da03.mail, da03.passw)
    wr_cont = fu01.blog_write(driver, da03)
    fu01.out_close_driver(driver)
    return wr_cont


write_add_text = test_A003()


# ***************************************************

# Normal run
if __name__ == "__main__":
    print(write_add_text)
    try:
        assert da03.write == write_add_text
    except:
        print("Hiba, az ellenőrző feltételnél nincs egyezés.")


