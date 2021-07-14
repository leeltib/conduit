# TC002 test case - Belépés a regisztráció során megadott adatokkal - kilépés.

from selenium import webdriver
import time
import data.data_tcA002 as da02

from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager               # webdriver-manager / Chrome

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')

driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)       # Headless mód
#driver = webdriver.Chrome(ChromeDriverManager().install())                              # normál mód

driver.get("http://localhost:1667")
time.sleep(10)

# Cookie elutasítása
try:
    driver.find_element_by_xpath('//div[@id="cookie-policy-panel"]/div/div[2]/button[1]/div').click()
except:
    print("Nincs cookie.")

# Sign in gomb kiválasztása, klikk -> bejelentkezés űrlap megnyitása
driver.find_element_by_xpath('//div[@id="app"]/nav/div/ul/li[2]/a').click()
time.sleep(3)
email = driver.find_element_by_xpath('//div[@id="app"]/div/div/div/div/form/fieldset[1]/input')
password = driver.find_element_by_xpath('//div[@id="app"]/div/div/div/div/form/fieldset[2]/input')
sign_in_button = driver.find_element_by_xpath('//div[@id="app"]/div/div/div/div/form/button')

# Belépés, username megjelenésének ellenőrzése
def test_login():
    email.send_keys(da02.mail)
    password.send_keys(da02.passw)
    time.sleep(0.2)
    sign_in_button.click()
    time.sleep(1)
    try:
        usern_text = driver.find_element_by_xpath('//div[@id="app"]/nav/div/ul/li[4]/a').text
        time.sleep(1)
        print(usern_text)
        driver.find_element_by_xpath('//div[@id="app"]/nav/div/ul/li[5]/a').click()
        return usern_text
    except:
        print("Hibás belépési adatok, nincs ilyen felhasználó.")
    finally:
        time.sleep(1)
        driver.close()

user_menu_text2 = test_login()


# normál futtatáshoz:
if __name__ == "__main__":
    print(user_menu_text2)
    try:
        assert da02.name == user_menu_text2
    except:
        print("Hiba, az ellenőrző feltételnél nincs egyezés.")

