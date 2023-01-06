from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://github.com/konscodes')
driver.implicitly_wait(5)
output_file_path = './foo.png'
image = driver.find_element('class name', 'js-yearly-contributions').screenshot(output_file_path)
driver.quit()