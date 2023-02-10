from _ast import Assert

import self as self
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

#Task_1
driver = webdriver.Chrome(r'H:\New folder\chromedriver.exe')

#Task_2
driver.get("http://automationexercise.com")

#Task_4
Add_To_Cart_CSS_Selector = ".btn.btn-default.add-to-cart"
Action_Add_To_Cart = driver.find_element(By.CSS_SELECTOR, Add_To_Cart_CSS_Selector)

Action_Add_To_Cart.click()
print(Action_Add_To_Cart)

#Task_5

Close_Continue_Shopping =".btn.btn-success.close-modal.btn-block"
Action_Close_Continue_Shopping=driver.find_element(By.CSS_SELECTOR, Close_Continue_Shopping)
Action_Close_Continue_Shopping.click()
print(Action_Close_Continue_Shopping)

Click_Cart =".fa.fa-shopping-cart"
Action_Click_Cart = driver.find_element(By.CSS_SELECTOR, Click_Cart)
Action_Click_Cart.click()
print(Action_Click_Cart)

#Task_6
Shopping_Cart_Button = "//li[text()='Shopping Cart']"
Shopping_Cart_find_elem=driver.find_element(By.XPATH, Shopping_Cart_Button)
Shopping_Cart_text_store = (Shopping_Cart_find_elem.text)

if Shopping_Cart_text_store == "Shopping Cart":
    print("Cart Page is Displayed")

#Task_7
Proceed_To_Checkout = ".btn.btn-default.check_out"
Action_Proceed_To_Checkout = driver.find_element(By.CSS_SELECTOR, Proceed_To_Checkout)
Action_Proceed_To_Checkout.click()
print(Action_Proceed_To_Checkout)

#Task_8
Register_Login_Button = "//u[text()='Register / Login']"
Register_Find_Element = driver.find_element(By.XPATH, Register_Login_Button)
Register_Find_Element.click()
print("Register_Find_Element")

#Task_9
Name_button = "name"
#Email_button_loc = "//button[data-qa()='signup-email']"
Action_Name = driver.find_element(By.NAME, Name_button).send_keys("Faizul")
Action_Email = driver.find_element(By.CSS_SELECTOR,"[data-qa='signup-email']").send_keys("zagalfayeezullah@gmail.com")
#Signup_button = ".btn.btn-default"
Action_SignUP = driver.find_element(By.CSS_SELECTOR,"[data-qa='signup-button']").click()
#Action_SignUP.click()
print(Action_SignUP)

#Task-10 and 11

radio_button = driver.find_element(By.ID, "id_gender1").click()
Action_SignUP = driver.find_element(By.CSS_SELECTOR,"[data-qa='password']").send_keys("faizul")
#print("xx")
drop_down_date = driver.find_element(By.ID, "days")
select = Select(drop_down_date)
select.select_by_value("1")
#print("jor")
drop_down_months = driver.find_element(By.ID, "months")
select = Select(drop_down_months)
select.select_by_value("3")
#print("jor")
drop_down_years = driver.find_element(By.ID, "years")
select = Select(drop_down_years)
select.select_by_value("2015")

first_name = driver.find_element(By.CSS_SELECTOR,"[data-qa='first_name']").send_keys("Faizul")
last_name = driver.find_element(By.CSS_SELECTOR,"[data-qa='last_name']").send_keys("Zagal")
company_name = driver.find_element(By.CSS_SELECTOR,"[data-qa='company']").send_keys("Google")
address_name = driver.find_element(By.CSS_SELECTOR,"[data-qa='address']").send_keys("Banani")
address_2_name = driver.find_element(By.CSS_SELECTOR,"[data-qa='address2']").send_keys("Road-12")
state_name = driver.find_element(By.CSS_SELECTOR,"[data-qa='state']").send_keys("Dhaka")
city_name = driver.find_element(By.CSS_SELECTOR,"[data-qa='city']").send_keys("Barisal")
zip_name = driver.find_element(By.CSS_SELECTOR,"[data-qa='zipcode']").send_keys("1213")
mobile_number = driver.find_element(By.CSS_SELECTOR,"[data-qa='mobile_number']").send_keys("01323572537")

submit_s = driver.find_element(By.CSS_SELECTOR,"[data-qa='create-account']")
submit_s.click()
print("Submitted")

account_created_continue = driver.find_element(By.CSS_SELECTOR,"[data-qa='continue-button']")
account_created_continue.click()
#print("ajsdjkas")


logged_in_admin = "//b[text()='Faizul']"
login_find_elem=driver.find_element(By.XPATH, logged_in_admin)
as_text_store = (login_find_elem.text)

if Shopping_Cart_text_store == "Shopping Cart":
    print("True")

#Task-12 and 13
Click_Cart_13 =".fa.fa-shopping-cart"
Action_Click_Cart_13 = driver.find_element(By.CSS_SELECTOR, Click_Cart_13)
Action_Click_Cart_13.click()
print(Action_Click_Cart_13)

Proceed_to_checkout_14 =".btn.btn-default.check_out"
Action_to_checkout_14 = driver.find_element(By.CSS_SELECTOR, Proceed_to_checkout_14)
Action_to_checkout_14.click()
print(Action_to_checkout_14)
print("hs")

#Task_15
des_cc='message'
Description_button = driver.find_element(By.NAME, des_cc).send_keys("This is a comment")
place_cc = '.btn.btn-default.check_out'
Place_Order_Button = driver.find_element(By.CSS_SELECTOR,place_cc).click()
print("xs")

#Task_16 and 17
Name_On_card = driver.find_element(By.CSS_SELECTOR,"[data-qa='name-on-card']").send_keys("Fayeezullah")
Card_Number = driver.find_element(By.CSS_SELECTOR,"[data-qa='card-number']").send_keys("1234 5678 9102 1234")
CVC = driver.find_element(By.CSS_SELECTOR,"[data-qa='cvc']").send_keys("123")
Expiry_Month = driver.find_element(By.CSS_SELECTOR,"[data-qa='expiry-month']").send_keys("6")
Expiry_Year = driver.find_element(By.CSS_SELECTOR,"[data-qa='expiry-year']").send_keys("2015")

Pay_Confirm_Order_css = '.form-control.btn.btn-primary.submit-button'
Action_Pay_confirm_order = driver.find_element(By.CSS_SELECTOR,Pay_Confirm_Order_css).click()

print("Hello")
















