# A007 select user - Szűrés blogszerző szerint, a kiválasztott blogszerző bejegyzéseinek kiírása text fájlba

import data.data_tcA007 as da07
import func.func_02 as fu02

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager               # webdriver-manager / Chrome

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')

driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)       # Headless mód
#driver = webdriver.Chrome(ChromeDriverManager().install())                              # normál mód

driver.get("http://localhost:1667")

# Várakozás a betöltésre
fu02.wait(driver, By.ID, "app")
time.sleep(2)

# *** TC-A007 **************************************


def test_A007_select():
    fu02.sign_in(driver, da07.mail, da07.passw)
    return fu02.select_user(driver, da07.username)


user_blog_num1 = test_A007_select()


def test_A007_read():
    blog_read = fu02.user_read(driver, user_blog_num1)
    fu02.out_close_driver(driver)
    return blog_read


blog_read_full = test_A007_read()


def test_A007_write():
    filename = f"data_out/a007_{da07.username}_blogs"
    with open(filename, "w", encoding='utf-8') as f:
        f.write(f"{da07.username} bejegyzései:\n")
        r_num = len(blog_read_full)
        for i in range(r_num):
            b_tit = str(blog_read_full[i][0])
            b_tit_upper = b_tit.upper()
            f.write(f"\n{b_tit_upper}\n")
            b_tex = str(blog_read_full[i][1]).replace('. ', '.\n')
            f.write(f"{b_tex}\n")
    return r_num


user_blog_num2 = test_A007_write()


# ***************************************************

# normál, önálló futtatáshoz:
if __name__ == "__main__":
    print(f"{da07.username} bejegyzései:")
    r_n = len(blog_read_full)
    for i in range(r_n):
        b_title = str(blog_read_full[i][0])
        b_title_upper = b_title.upper()
        print(f"\n{b_title_upper}")
        b_text = str(blog_read_full[i][1]).replace('. ', '.\n')
        print(b_text)
    try:
        assert user_blog_num1 == user_blog_num2
    except:
        print("Hiba, az ellenőrző feltételek nem a várt eredményt mutatják.")

