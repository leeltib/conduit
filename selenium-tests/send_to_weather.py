from time import sleep
from selenium import webdriver
from PIL import Image
from io import BytesIO
from twython import Twython
import requests
import json

try:

    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    options.add_argument("lang=ko_KR")
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument("disable-gpu")
    options.add_argument("--no-sandbox")

    # chrome driver
    driver = webdriver.Chrome('chromedriver', chrome_options=options)
    driver.implicitly_wait(3)

    # 케이웨더 접속
    driver.get('https://www.kweather.co.kr/weather.html')
    driver.maximize_window()

    kweather_map = driver.find_element_by_class_name('kweather_map')

    location = kweather_map.location
    size = kweather_map.size

    left = location['x']
    top = location['y']
    right = location['x'] + size['width']
    bottom = location['y'] + size['height']
    sleep(3)

    png = driver.get_screenshot_as_png()
    img = Image.open(BytesIO(png))
    # 오늘의 날씨 영역만 잘라냅니다.
    area = (left, top, right, bottom)
    kweather = img.crop(area)
    kweather.save('kweather.png')
    photo = open("./kweather.png", 'rb')

    #############################################
    # configure twitter API
    ######################################
    APP_KEY = 'Sj2nUNEWxHFNdkR1234567890'  # 수정1
    APP_SECRET = 'UQ4FUe7tlC3OZKPYrZLWhZFewDeaxzcxvaKysVor1234567890'  # 수정2
    OAUTH_TOKEN = '976599794335416320-ould5HpxCQjgNcIai6rkA1234567890'  # 수정3
    OAUTH_TOKEN_SECRET = 'DbIWTEWZwCQW2u1K3US0TJNVD8D3B1fm96S1234567890'  # 수정4

    ###################
    # upload twitter
    ##################
    twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
    # 트위터에 잘라낸 오늘의 날씨 영역 이미지를 업로드 합니다.
    response = twitter.upload_media(media=photo)
    tweet_message = 'kweather'
    result = twitter.update_status(status=tweet_message, media_ids=[response['media_id']])
    photo_url = result['extended_entities']['media'][0]['media_url_https']

    #######################
    # send to slack
    ############################
    # Slack 인커밍 웹훅
    slack_incoming_url = "https://hooks.slack.com/services/TFN5D0ALR/BKUL3LYGL/6mDjUaSdUgaIal1234567890"  # 수정5
    slack_payload = {
        "attachments": [
            {

                "text": "Ez egy szöveg.",
                "image_url": photo_url,
                "color": "#764FA5"
            }
        ]
    }
    # 슬랙에 쏩니다!
    req = requests.post(url=slack_incoming_url, data=json.dumps(slack_payload))
    print(req)

except Exception as e:
    print(e)
    driver.quit()

finally:
    print("finally...")
    driver.quit()