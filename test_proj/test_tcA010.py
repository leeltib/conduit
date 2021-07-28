# A010 test case -  regisztrációs űrlap mezőinek validálása
# A teszthez random generálással készülnek a tesztadatok (data_tcA010.py)

import data.data_tcA010 as da10
import func.func_01 as fu01

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.headless = True
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)

driver.get("http://localhost:1667")

# Várakozás a betöltésre
fu01.wait(driver, By.ID, "app", 1)


# *** TC-A010 **************************************


def test_A010_sign_up_valid(users):
    valid_data = []
    for user in users:
        time.sleep(1)
        fu01.cookie_ok(driver)
        fu01.sign_up(driver, user[0], user[1], user[2])
        result_test = fu01.registr_check_a010(driver)
        valid_data.append(result_test)
    fu01.close_driver(driver)
    return valid_data


expect_valid = ['OK', 'FAIL', 'FAIL', 'FAIL', 'FAIL', 'FAIL', 'FAIL', 'FAIL', 'FAIL', 'FAIL', 'FAIL', 'FAIL', 'FAIL']

sign_up_valid_list = test_A010_sign_up_valid(da10.users)


for i in range(13):
    if i == 0:
        if expect_valid[i] == sign_up_valid_list[i]:
            print('A további tesztekhez szükséges "meglévő" user adatok feltöltése OK.')
        else:
            print('Hiba történt a további tesztekhez szükséges "meglévő" user adatok feltöltése közben!')
    elif i == 1:
        if expect_valid[i] == sign_up_valid_list[i]:
            print("Username. Üres mezős teszt OK!")
        else:
            print("Username. ERROR! Nincs hibaüzenet az üres mezős tesztnél!")
    elif i == 2:
        if expect_valid[i] == sign_up_valid_list[i]:
            print("Username. Meglévő felhasználónév teszt OK!")
        else:
            print("Username. ERROR! Nincs hibaüzenet a meglévő felhasználóneves tesztnél!")
    elif i == 3:
        if expect_valid[i] == sign_up_valid_list[i]:
            print("Email. Üres mezős teszt OK!")
        else:
            print("Email. ERROR! Nincs hibaüzenet az üres mezős tesztnél!")
    elif i == 4:
        if expect_valid[i] == sign_up_valid_list[i]:
            print("Email. Meglévő email cím teszt OK!")
        else:
            print("Email. ERROR! Nincs hibaüzenet a meglévő email cím tesztnél!")
    elif i == 5:
        if expect_valid[i] == sign_up_valid_list[i]:
            print("Email. Hiányzó '@' karakter teszt OK!")
        else:
            print("Email. ERROR! Nincs hibaüzenet a hiányzó '@' karakter tesztnél!")
    elif i == 6:
        if expect_valid[i] == sign_up_valid_list[i]:
            print("Email. Hiányzó '.' karakter teszt OK!")
        else:
            print("Email. ERROR! Nincs hibaüzenet a hiányzó '.' karakter tesztnél!")
    elif i == 7:
        if expect_valid[i] == sign_up_valid_list[i]:
            print("Password. Üres mezős teszt OK!")
        else:
            print("Password. ERROR! Nincs hibaüzenet az üres mezős tesztnél!")
    elif i == 8:
        if expect_valid[i] == sign_up_valid_list[i]:
            print("Password. Meglévő jelszó teszt OK!")
        else:
            print("Password. ERROR! Nincs hibaüzenet a meglévő jelszó tesztnél!")
    elif i == 9:
        if expect_valid[i] == sign_up_valid_list[i]:
            print("Password. 8 karakternél kevesebb teszt OK!")
        else:
            print("Password. ERROR! Nincs hibaüzenet a 8 karakternél kevesebb tesztnél!")
    elif i == 10:
        if expect_valid[i] == sign_up_valid_list[i]:
            print("Password. A nincs benne szám teszt OK!")
        else:
            print("Password. ERROR! Nincs hibaüzenet a nincs benne szám tesztnél!")
    elif i == 11:
        if expect_valid[i] == sign_up_valid_list[i]:
            print("Password. A nincs benne kisbetű teszt OK!")
        else:
            print("Password. ERROR! Nincs hibaüzenet a nincs benne kisbetű tesztnél!")
    elif i == 12:
        if expect_valid[i] == sign_up_valid_list[i]:
            print("Password. A nincs benne nagybetű teszt OK!")
        else:
            print("Password. ERROR! Nincs hibaüzenet a nincs benne nagybetű tesztnél!")
    else:
        print("A range füfggvény értéke nem jó! ")


# ***************************************************
# normál futtatáshoz:
if __name__ == "__main__":
    print(expect_valid)
    print(sign_up_valid_list)
    try:
        assert expect_valid == sign_up_valid_list
    except:
        print("A beviteli mezők validálása közben nem kaptuk mindenhol az elvárt eredményt.")

