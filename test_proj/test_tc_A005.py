# A005 test case - Saját, meglévő blogbejegyzés törlése - kilépés.

from selenium import webdriver
import time
import data.data_tcA005 as da05

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager               # webdriver-manager / Chrome

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')

driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)       # Headless mód
#driver = webdriver.Chrome(ChromeDriverManager().install())                              # normál mód

driver.get("http://localhost:1667")

# Függvény várakozások beállítására:
def wait(by, attr):
    try:
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((by, attr)))
    except TimeoutException:
        print("Loading took too much time!-Try again")

# Várakozás a betöltésre
wait(By.ID, "app")
time.sleep(2)

# Cookie elutasítása
try:
    driver.find_element_by_xpath('//div[@id="cookie-policy-panel"]/div/div[2]/button[1]/div').click()
except:
    print("Nincs cookie.")

# Sign in gomb kiválasztása, klikk -> bejelentkezés űrlap megnyitása
driver.find_element_by_xpath('//div[@id="app"]/nav/div/ul/li[2]/a').click()
wait(By.XPATH, '//div[@id="app"]/div/div/div/div/form/fieldset[1]/input')
email = driver.find_element_by_xpath('//div[@id="app"]/div/div/div/div/form/fieldset[1]/input')
password = driver.find_element_by_xpath('//div[@id="app"]/div/div/div/div/form/fieldset[2]/input')
sign_in_button = driver.find_element_by_xpath('//div[@id="app"]/div/div/div/div/form/button')

# Belépés, meglévő blog törlése
def test_blog_del():
    del_list = []
    email.send_keys(da05.mail)
    password.send_keys(da05.passw)
    sign_in_button.click()
    wait(By.XPATH, '//div[@id="app"]/nav/div/ul/li[4]/a')
    time.sleep(1)
    driver.find_element_by_xpath('//div[@id="app"]/nav/div/ul/li[4]/a').click()
    wait(By.XPATH, '//div[@id="app"]/div/div[2]/div/div/div[2]/div/div/div/a/p')
    time.sleep(1)
    try:
        blog_del_what = driver.find_element_by_xpath('//div[@id="app"]/div/div[2]/div/div/div[2]/div/div/div/a/p').text
        print(blog_del_what)
        del_list.append(blog_del_what)
        driver.find_element_by_xpath('//div[@id="app"]/div/div[2]/div/div/div[2]/div/div/div[1]/a/span').click()
        wait(By.XPATH, '//div[@id="app"]/div/div[1]/div/div/span/button/span')
        time.sleep(1)
        driver.find_element_by_xpath('//div[@id="app"]/div/div[1]/div/div/span/button/span').click()
        wait(By.XPATH, '//div[@id="app"]/nav/div/ul/li[4]/a')
        time.sleep(1)
        driver.find_element_by_xpath('//div[@id="app"]/nav/div/ul/li[4]/a').click()
        wait(By.XPATH, '//div[@id="app"]/div/div[2]/div/div/div[2]/div/div/div[1]/a/p')
        time.sleep(1)
        try:
            blog_stay_what = driver.find_element_by_xpath('//div[@id="app"]/div/div[2]/div/div/div[2]/div/div/div[1]/a/p').text
            print(blog_stay_what)
            del_list.append(blog_stay_what)
            try:
                assert blog_del_what != blog_stay_what
            except:
                print("Hiba a törlésnél, a bejegyzés megmaradt.")
        except:
            del_list.append('None')
            print("Nincs több bejegyzés a My Articles mappában.")
        driver.find_element_by_xpath('//div[@id="app"]/nav/div/ul/li[5]/a').click()
        return del_list
    except:
        print("Nincs módosítható bejegyzés.")
    finally:
        time.sleep(1)
        driver.close()

what_text = test_blog_del()


# normál futtatáshoz:
if __name__ == "__main__":
    print(what_text[0], what_text[1],)
    try:
        assert what_text[0] != what_text[1]
    except:
        print("Hiba, az ellenőrző feltételnél nincs eltérés.")
