# A008 - comment function
# Kiválasztható a blogszerző, és a konkrét blog
# A komment szövegét külső fájlból olvassuk be

import data.data_tcA008 as da08
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

# *** TC-A008 **************************************


def test_comment_text():
    with open('data/a008.txt', 'r', encoding='utf-8') as file:
        comm_full = file.readlines()
        comm_full_list = []
        for i in range(da08.com_row_num):
            com_start = da08.com_row[i][0]
            com_stop = da08.com_row[i][1]
            comm_str = ""
            for element in comm_full[com_start:com_stop]:
                if element == comm_full[com_stop-1]:
                    el = element.replace("\n", "")
                else:
                    el = element.replace("\n", " ")
                comm_str += el
            comm_full_list.append(comm_str)
        return comm_full_list


comments_text = test_comment_text()


def test_A008_comment():
    fu02.sign_in(driver, da08.mail, da08.passw)
    co_da_li = fu02.user_comment(driver, da08.com_list_num, da08.com_list, comments_text)
    fu02.out_user(driver)
    return co_da_li


comments_user_title_list = test_A008_comment()


def test_A008_control():
    fu02.sign_in(driver, da08.mail_cont, da08.passw_cont)
    cont_da_li = fu02.user_comment_control(driver, da08.com_list_num, da08.com_list, comments_text)
    fu02.out_user(driver)
    return cont_da_li


control_user_title_text_list = test_A008_control()
control_text_list = []
for comment_text in control_user_title_text_list:
    control_text_list.append(comment_text[2])


def test_A008_del():
    fu02.sign_in(driver, da08.mail, da08.passw)
    del_da_li = fu02.user_comment_del(driver, da08.com_list_num, da08.com_list, comments_text)
    fu02.out_close_driver(driver)
    return del_da_li


del_user_title_list = test_A008_del()


# ***************************************************

# normál, önálló futtatáshoz:
if __name__ == "__main__":
    print(comments_text)
    print(comments_user_title_list)
    print(control_user_title_text_list)
    print(control_text_list)
    print(del_user_title_list)
    try:
        assert comments_text == control_text_list
        assert comments_user_title_list == del_user_title_list
    except:
        print("Hiba, az ellenőrző feltételek nem a várt eredményt mutatják.")

