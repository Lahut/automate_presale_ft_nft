from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time 



PATH = "/Users/bass/Downloads/chromedriver"
EXTENSION_PATH = "C:\Program Files (x86)\extension_10_7_0_0.crx"


# driver = webdriver.Chrome(PATH)
options = webdriver.ChromeOptions()
# options.add_extension(EXTENSION_PATH)
options.add_argument(r"--user-data-dir=/Users/bass/Library/Application Support/Google/Chrome")
options.add_argument(r'--profile-directory=Default')


driver = webdriver.Chrome(chrome_options=options,executable_path=PATH)
# print(type(driver))




driver.get("https://fishingtown.io/")
buy_rod_target = driver.find_element_by_class_name('play-btn')

# print(type(buy_rod_target))
buy_rod_target.click()
time.sleep(30)
canvas_maingame = driver.find_element_by_id('unity-canvas')

canvas_size = canvas_maingame.size
canvas_center_x = canvas_size['width'] / 2
canvas_center_y = canvas_size['height'] / 2


connect_wallet_btn_x = canvas_center_x
connect_wallet_btn_y = canvas_center_y + (canvas_center_y/3) * 2

ActionChains(driver).move_to_element_with_offset(canvas_maingame,
                                                connect_wallet_btn_x,
                                                connect_wallet_btn_y).click().perform()

print(canvas_center_x,canvas_center_y)
print(connect_wallet_btn_x,connect_wallet_btn_y)

# print(canvas_maingame.size)
time.sleep(5)
# driver.get("https://fishingtown.io/")
# driver.get("https://cryptoplanes.me/")


driver.quit()




