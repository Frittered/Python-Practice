from selenium import webdriver
driver = webdriver.Firefox(executable_path=r'C:\Users\fritz\PycharmProjects\selenium_test\geckodriver.exe')
print(driver)
driver.maximize_window()
# I used a extensive tea export site yunnan sourcing as my test subject
site = driver.get('https://yunnansourcing.com/')
search_field = driver.find_element_by_name('q')

# the following argument will be the search keywords

search_field.send_keys('jinggu raw puerh')
search_button = driver.find_element_by_class_name('coolbutton')
search_button.click()
search_results = driver.find_element_by_xpath('(//div[@class=\'row\'])[1]').text

# It will print the number of results for a given search

print(f'There are this many results:{search_results}')

driver.close()
