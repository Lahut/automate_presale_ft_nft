from selenium import webdriver

EXTENSION_PATH = 'C:/Users/lahut/Desktop/metamask_crx'
opt = webdriver.ChromeOptions()
opt.add_extension(EXTENSION_PATH)

driver = webdriver.Chrome(options=opt)

driver.find_element_by_xpath('//button[text()="Get Started"]').click()
driver.find_element_by_xpath('//button[text()="Import wallet"]').click()
driver.find_element_by_xpath('//button[text()="No Thanks"]').click()

# After this you will need to enter you wallet details

inputs = driver.find_elements_by_xpath('//input')
inputs[0].send_keys(SECRET_RECOVERY_PHRASE)
inputs[1].send_keys('2c1503e7')
inputs[2].send_keys('2c1503e7')
driver.find_element_by_css_selector('.first-time-flow__terms').click()
driver.find_element_by_xpath('//button[text()="Import"]').click()
driver.find_element_by_xpath('//button[text()="All Done"]').click()



EXTENSION_ID = 'nkbihfbeogaeaoehlefnkodbefgpgknn'

driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[1])
driver.get('chrome-extension://{}/popup.html'.format(EXTENSION_ID))