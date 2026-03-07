import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys


opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
opts.add_argument("--disable-notifications")


driver = webdriver.Chrome(opts)
ac = ActionChains(driver)
wait = WebDriverWait(driver, 10)

# driver.get("https://demowebshop.tricentis.com/")
# time.sleep(2)

''' 1. '''
# driver.find_element('xpath', "(//a[contains(text(),'Books')])[3]").click()
# time.sleep(2)
#
# driver.find_element('xpath', '(//input[@value="Add to cart"])[1]').click()
# time.sleep(4)
#
# driver.find_element('xpath', '(//span[@class="cart-label"])[1]').click()
# time.sleep(2)
#
# if wait.until(EC.url_contains("cart")):
#     print("Successfully added to cart")
# else:
#     print("Not successfully added to cart")

'''2. '''

# driver.get("https://demowebshop.tricentis.com/")
# time.sleep(2)
#
# driver.find_element('xpath', "(//a[contains(text(),'Electronics')])[3]").click()
# time.sleep(2)
#
# driver.find_element('xpath', '(//a[contains(text(), "Cell phones")])[3]').click()
# time.sleep(2)


'''3. '''

# driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")
# time.sleep(2)
#
# driver.find_element('xpath', '//button[text() = "Start"]').click()
# time.sleep(2)
#
# text_element = wait.until(
#     EC.visibility_of_element_located((By.ID, "finish"))
# )
#
# print(text_element.text)
#
# driver.quit()

'''4. '''
# driver.get("https://the-internet.herokuapp.com/dynamic_controls")
# time.sleep(2)
#
# driver.find_element("xpath", '//button[text()="Remove"]').click()
#
# add_button = wait.until(
#     EC.element_to_be_clickable(("xpath", '//button[text()="Add"]'))
# )
#
# add_button.click()

'''5. '''

# driver.get("https://demoqa.com/select-menu")
# time.sleep(2)
#
# dropdown = driver.find_element("id", "react-select-2-input")
#
# dropdown.send_keys("Group 2, option 1")
# dropdown.send_keys(Keys.ENTER)
#
# selected_value = driver.find_element(
#     "xpath", "//div[contains(text(),'Group 2, option 1')]"
# ).text
#
# print("Selected value:", selected_value)
#
# if selected_value == "Group 2, option 1":
#     print("Verification Passed")
# else:
#     print("Verification Failed")


'''6. '''

# driver.get("https://demoqa.com/select-menu")
# time.sleep(2)
#
#
# ref_ele = driver.find_element('xpath', '//b[text()="Standard multi select"]')
# ac.scroll_to_element(ref_ele).perform()
#
# multi_select = driver.find_element('id', 'cars')
#
# # Create Select object
# select_obj = Select(multi_select)
#
# # Select Volvo, Saab, Opel
# select_obj.select_by_visible_text("Volvo")
# select_obj.select_by_visible_text("Saab")
# select_obj.select_by_visible_text("Opel")
# select_obj.select_by_visible_text("Audi")
#
# time.sleep(2)
#
# all_options = select_obj.all_selected_options
#
# for option in all_options:
#     print(option.text)

'''7. '''

# driver.get("https://demoqa.com/menu/")
# time.sleep(2)
#
# main_item2 = driver.find_element('xpath', '//a[text()="Main Item 2"]')
# ac.move_to_element(main_item2).perform()
# time.sleep(2)
#
# sub_sub_list = driver.find_element('xpath', '//a[text()="SUB SUB LIST »"]')
# ac.move_to_element(sub_sub_list).perform()
# time.sleep(2)
#
# sub_sub_item1 = driver.find_element('xpath', '//a[text()="Sub Sub Item 1"]')
# sub_sub_item1.click()
# time.sleep(2)

'''8. '''

# driver.get("https://demoqa.com/droppable")
# time.sleep(3)
#
# drag = driver.find_element("xpath", "//div[@id='draggable']")
# drop = driver.find_element("xpath", "//div[@id='droppable']")
#
# ac.click_and_hold(drag).move_to_element(drop).release().perform()
#
# time.sleep(2)
#
# result = driver.find_element("xpath", "//div[@id='droppable']").text
# print(result)
#
# if result == "Dropped!":
#     print("Test Passed: Element dropped successfully")
# else:
#     print("Test Failed")

'''9. '''

# driver.get("https://the-internet.herokuapp.com/javascript_alerts")
# time.sleep(2)
#
# driver.find_element('xpath', '//button[text()="Click for JS Confirm"]').click()
# time.sleep(2)
#
# alert = driver.switch_to.alert
# alert.accept()
#
# time.sleep(2)
#
# result = driver.find_element('id', 'result').text
#
# if result == "You clicked: Ok":
#     print("Test Passed")
# else:
#     print("Test Failed")


''' 10. '''

driver.get("https://the-internet.herokuapp.com/upload")
time.sleep(2)

file_path = r"C:\Users\KIIT\Desktop\cg\capgemini_project\files\demo.html"

driver.find_element('id', 'file-upload').send_keys(file_path)
time.sleep(2)

driver.find_element('id', 'file-submit').click()
time.sleep(2)

uploaded_file = driver.find_element('id', 'uploaded-files').text

if uploaded_file == "demo.html":
    print("Test Passed: File uploaded successfully")
else:
    print("Test Failed")

















