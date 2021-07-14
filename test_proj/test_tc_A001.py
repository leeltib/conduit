# A001 test case -  Új felhasználó regisztrációja felhasználó név, email cím és jelszó megadásával.

from selenium import webdriver
import time
import data.data_tcA001 as da01

from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager               # webdriver-manager / Chrome

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')

driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)       # Headless mód
#driver = webdriver.Chrome(ChromeDriverManager().install())                              # normál mód

driver.get("http://localhost:1667")

# Cookie elutasítása
try:
    driver.find_element_by_xpath('//div[@id="cookie-policy-panel"]/div/div[2]/button[1]/div').click()
except:
    print("Nincs cookie.")

# Sign up gomb kiválasztása, klikk -> regisztrációs űrlap megnyitása
driver.find_element_by_xpath('//div[@id="app"]/nav/div/ul/li[3]/a').click()

username = driver.find_element_by_xpath('//div[@id="app"]/div/div/div/div/form/fieldset[1]/input')
email = driver.find_element_by_xpath('//div[@id="app"]/div/div/div/div/form/fieldset[2]/input')
password = driver.find_element_by_xpath('//div[@id="app"]/div/div/div/div/form/fieldset[3]/input')
sign_up_button = driver.find_element_by_xpath('//div[@id="app"]/div/div/div/div/form/button')

# Adatok bevitele, welcome OK, username megjelenésének ellenőrzése
def test_registr():
    username.send_keys(da01.name)
    email.send_keys(da01.mail)
    password.send_keys(da01.passw)
    sign_up_button.click()
    time.sleep(1)
    try:
        welcome_button = driver.find_element_by_xpath('/html/body/div[2]/div/div[4]/div/button')
        welcome_button.click()
        time.sleep(1)
        usern_text = driver.find_element_by_xpath('//div[@id="app"]/nav/div/ul/li[4]/a').text
        time.sleep(1)
        driver.find_element_by_xpath('//div[@id="app"]/nav/div/ul/li[5]/a').click()
        print(usern_text)
        return usern_text
    except:
        print("Ez a felhasználó már létezik.")
    finally:
        time.sleep(1)
        driver.close()

user_menu_text = test_registr()

# normál futtatáshoz:
if __name__ == "__main__":
    print(user_menu_text)
    try:
        assert da01.name == user_menu_text
    except:
        print("Hiba, az ellenőrző feltételnél nincs egyezés.")


