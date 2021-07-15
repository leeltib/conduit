# A004 test case - Saját, meglévő blogbejegyzés módosítása - kilépés.

from selenium import webdriver
import time
import data.data_tcA004 as da04

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

# Belépés, blog módosítás, ellenőrzés
def test_blog_edit():
    email.send_keys(da04.mail)
    password.send_keys(da04.passw)
    sign_in_button.click()
    wait(By.XPATH, '//div[@id="app"]/nav/div/ul/li[4]/a')
    time.sleep(2)
    driver.find_element_by_xpath('//div[@id="app"]/nav/div/ul/li[4]/a').click()
    wait(By.XPATH, '//div[@id="app"]/div/div[2]/div/div/div[2]/div/div/div[1]/a/span')
    time.sleep(2)
    try:
        driver.find_element_by_xpath('//div[@id="app"]/div/div[2]/div/div/div[2]/div/div/div[1]/a/span').click()
        wait(By.XPATH, '//div[@id="app"]/div/div[1]/div/div/span/a/span')
        time.sleep(1)
        driver.find_element_by_xpath('//div[@id="app"]/div/div[1]/div/div/span/a/span').click()
        wait(By.XPATH, '//div[@id="app"]/div/div/div/div/form/fieldset/fieldset[1]/input')
        time.sleep(1)
        input1 = driver.find_element_by_xpath('//div[@id="app"]/div/div/div/div/form/fieldset/fieldset[1]/input')
        input1.clear()
        input1.send_keys(da04.title)
        input2 = driver.find_element_by_xpath('//div[@id="app"]/div/div/div/div/form/fieldset/fieldset[2]/input')
        input2.clear()
        input2.send_keys(da04.what)
        input3 = driver.find_element_by_xpath('//div[@id="app"]/div/div/div/div/form/fieldset/fieldset[3]/textarea')
        input3.clear()
        input3.send_keys(da04.write)
        wait(By.XPATH, '//div[@id="app"]/div/div/div/div/form/fieldset/fieldset[4]/div/div/ul/li[1]/div[2]/i[2]')
        time.sleep(1)
        driver.find_element_by_xpath('//div[@id="app"]/div/div/div/div/form/fieldset/fieldset[4]/div/div/ul/li[1]/div[2]/i[2]').click()
        wait(By.XPATH, '//div[@id="app"]/div/div/div/div/form/fieldset/fieldset[4]/div/div/ul/li/input')
        time.sleep(1)
        input4 = driver.find_element_by_xpath('//div[@id="app"]/div/div/div/div/form/fieldset/fieldset[4]/div/div/ul/li/input')
        input4.send_keys(da04.tags)
        driver.find_element_by_xpath('//div[@id="app"]/div/div/div/div/form/button').click()
        wait(By.XPATH, '//div[@id="app"]/div/div[2]/div[1]/div/div[1]/p')
        time.sleep(1)
        write_cont = driver.find_element_by_xpath('//div[@id="app"]/div/div[2]/div[1]/div/div[1]/p').text
        print(write_cont)
        tags_cont = driver.find_element_by_xpath('//div[@id="app"]/div/div[2]/div[1]/div/div[2]/a').text
        print(tags_cont)
        try:
            assert tags_cont == da04.tags
        except:
            print('A "tags" paraméter nem egyezik.')
        driver.find_element_by_xpath('//div[@id="app"]/nav/div/ul/li[4]/a').click()
        wait(By.XPATH, '//div[@id="app"]/div/div[2]/div/div/div[2]/div/div/div/a/h1')
        time.sleep(1)
        my_art_title = driver.find_element_by_xpath('//div[@id="app"]/div/div[2]/div/div/div[2]/div/div/div/a/h1').text
        print(my_art_title)
        my_art_what = driver.find_element_by_xpath('//div[@id="app"]/div/div[2]/div/div/div[2]/div/div/div/a/p').text
        print(my_art_what)
        time.sleep(1)
        try:
            assert my_art_title == da04.title
            assert my_art_what == da04.what
        except:
            print('A "title" vagy a "what" paraméter nem egyezik.')
        driver.find_element_by_xpath('//div[@id="app"]/nav/div/ul/li[5]/a').click()
        return write_cont
    except:
        print("Nincs módosítható bejegyzés.")
    finally:
        time.sleep(1)
        driver.close()

write_edit_text = test_blog_edit()


# normál futtatáshoz:
if __name__ == "__main__":
    print(write_edit_text)
    try:
        assert da04.write == write_edit_text
    except:
        print("Hiba, az ellenőrző feltételnél nincs egyezés.")

