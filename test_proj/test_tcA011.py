# A011 test case -  cookie funkció tesztelése
# A teszthez random generálással készülnek a tesztadatok (data_tcA011.py)

import data.data_tcA011 as da11
import func.func_01 as fu01

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


# *** TC-A011 **************************************

user_dec = [da11.users[0][0], da11.users[0][1], da11.users[0][2]]
user_acc = [da11.users[1][0], da11.users[1][1], da11.users[1][2]]

# Teszt az "I decline!" gombra kattintás esetére:
def test_A011_cookie_decline(users):
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
    driver.get("http://localhost:1667")
    fu01.wait(driver, By.ID, "app", 1)
    cookie_valid_data = []
    time.sleep(1)
    cookie_valid_sign_up = fu01.cookie_valid_decline(driver)
    fu01.sign_up(driver, users[0], users[1], users[2])
    fu01.registr_check(driver)
    time.sleep(1)
    driver.refresh()
    time.sleep(1)
    cookie_valid_data.append(cookie_valid_sign_up)
    cookie_valid_sign_in = fu01.cookie_valid_decline(driver)
    fu01.sign_in(driver, users[1], users[2])
    fu01.login_check(driver)
    cookie_valid_data.append(cookie_valid_sign_in)
    fu01.close_driver(driver)
    return cookie_valid_data


expect_valid_dec = ['"I decline!" click', 'No cookies']

cookie_valid_dec = test_A011_cookie_decline(user_dec)


# Teszt az "I accept!" gombra kattintás esetére:
def test_A011_cookie_accept(users):
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
    driver.get("http://localhost:1667")
    fu01.wait(driver, By.ID, "app", 1)
    cookie_valid_data2 = []
    time.sleep(1)
    cookie_valid_sign_up = fu01.cookie_valid_accept(driver)
    fu01.sign_up(driver, users[0], users[1], users[2])
    fu01.registr_check(driver)
    time.sleep(1)
    driver.refresh()
    time.sleep(1)
    cookie_valid_data2.append(cookie_valid_sign_up)
    cookie_valid_sign_in = fu01.cookie_valid_decline(driver)
    fu01.sign_in(driver, users[1], users[2])
    fu01.login_check(driver)
    cookie_valid_data2.append(cookie_valid_sign_in)
    fu01.close_driver(driver)
    return cookie_valid_data2


expect_valid_acc = ['"I accept!" click', 'No cookies']

cookie_valid_acc = test_A011_cookie_accept(user_acc)


# ***************************************************
# normál futtatáshoz:
if __name__ == "__main__":
    print(user_dec)
    print(user_acc)
    print(cookie_valid_dec)
    print(expect_valid_dec)
    print(cookie_valid_acc)
    print(expect_valid_acc)
    try:
        assert cookie_valid_dec == expect_valid_dec
        assert cookie_valid_acc == expect_valid_acc
    except:
        print("A cookies funkció validálása közben nem kaptuk mindenhol az elvárt eredményt.")

