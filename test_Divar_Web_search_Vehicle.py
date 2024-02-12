from selenium import webdriver
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import pytest
import logging
import os

service = Service()
divar_driver = webdriver.Chrome(service=service)
action = ActionChains(driver=divar_driver)
divar_driver.get("https://divar.ir/s/tehran")
sleep(4)


def Wait_For_Appearance(driver,by_find_element, context_of_by):
    try:
        element = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((by_find_element,context_of_by)))
        return element
    except: return None

def Wait_For_Appearance_whole_of_something(driver,by_find_element, context_of_by):
    try:
        elements = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((by_find_element,context_of_by)))
        return elements
    except: return None

def Select_Vehicle_Of_Divar_Website(driver):
    vehicle = Wait_For_Appearance(driver,'xpath',"//div[@class='filter-box p-lr-gutter']//a[contains(text(),'وسایل نقلیه')]")
    vehicle.click()
    car = Wait_For_Appearance(driver,'xpath',"//ul[@class='kt-accordion']//a[@class='kt-accordion-item__header'][contains(.,'خودرو')]")  
    car.click()
    savari = Wait_For_Appearance(driver,'xpath',"//ul[@class='kt-accordion']//a[@class='kt-accordion-item__header'][contains(.,'سواری و وانت')]")
    savari.click()

    color = Wait_For_Appearance(driver,'xpath',"//div[@role='button'][contains(.,'رنگ')]")
    driver.execute_script("arguments[0].scrollIntoView();",color)
    color.click()
    colors = Wait_For_Appearance_whole_of_something(driver,'xpath',"//div[@class='select-field__items-cdd65']//div[@class='kt-control-row kt-control-row--small kt-control-row--clickable']")
    assert len(colors) == 6
    special_color = Wait_For_Appearance(driver,'xpath',"//div[@class='select-field__items-cdd65']//div[@class='kt-control-row kt-control-row--small kt-control-row--clickable'][2]")
    special_color.click()
    sleep(3)

    price = driver.find_element('xpath', "//div[@role='button'][contains(.,'قیمت')]")
    driver.execute_script("arguments[0].scrollIntoView();",price)
    price.click()
    almost_price = Wait_For_Appearance(driver,'xpath',"(//div[@class='kt-ftr'][contains(.,'حداقلحداکثرمثلا ۷۰،۰۰۰،۰۰۰تومانمثلا ۷۰،۰۰۰،۰۰۰تومان')]//button[@type='button'][contains(.,'مثلا ۷۰،۰۰۰،۰۰۰تومان')])[2]")
    almost_price.click()
    price_menu = Wait_For_Appearance_whole_of_something(driver,'xpath',"//ul[@class='kt-select-option-list kt-select-option-list--small kt-select-option-list--bottom-faded'][contains(.,'وارد کردن مقدار دلخواه۱۰۰ میلیون ۱۵۰ میلیون ۲۵۰ میلیون ۳۰۰ میلیون ۴۰۰ میلیون ۵۰۰ میلیون ۶۰۰ میلیون ۸۰۰ میلیون ۱ میلیارد ۱ میلیارد و ۲۵۰ میلیون۱ میلیارد و ۵۰۰ میلیون۱ میلیارد و ۷۵۰ میلیون۲ میلیارد ۲ میلیارد و ۵۰۰ میلیون۳ میلیارد ۳ میلیارد و ۵۰۰ میلیون۴ میلیارد ۵ میلیارد ۸ میلیارد')]")
    special_price = driver.find_element('xpath',"//ul[@class='kt-select-option-list kt-select-option-list--small kt-select-option-list--bottom-faded'][contains(.,'وارد کردن مقدار دلخواه۱۰۰ میلیون ۱۵۰ میلیون ۲۵۰ میلیون ۳۰۰ میلیون ۴۰۰ میلیون ۵۰۰ میلیون ۶۰۰ میلیون ۸۰۰ میلیون ۱ میلیارد ۱ میلیارد و ۲۵۰ میلیون۱ میلیارد و ۵۰۰ میلیون۱ میلیارد و ۷۵۰ میلیون۲ میلیارد ۲ میلیارد و ۵۰۰ میلیون۳ میلیارد ۳ میلیارد و ۵۰۰ میلیون۴ میلیارد ۵ میلیارد ۸ میلیارد')]//li[2]")
    assert special_price.text.find("۱۰۰") != -1
    special_price.click()
    sleep(4)

    kilometrage = driver.find_element('xpath', "//div[@role='button'][contains(.,'کارکرد')]")
    driver.execute_script("arguments[0].scrollIntoView();",kilometrage)
    kilometrage.click()
    least_kilometrage = Wait_For_Appearance(driver,'xpath',"//div[@class='kt-ftr'][contains(.,'ازتامثلا ۱۰۰۰۰کیلومترمثلا ۲۰۰۰۰کیلومتر')]//button[@type='button'][contains(.,'مثلا ۱۰۰۰۰کیلومتر')]")
    least_kilometrage.click()
    kilometrage_menu = Wait_For_Appearance_whole_of_something(driver,'xpath',"//ul[@class='kt-select-option-list kt-select-option-list--small kt-select-option-list--bottom-faded'][contains(.,'وارد کردن مقدار دلخواهصفرهزار ۱۰ هزار ۲۰ هزار ۳۰ هزار ۴۰ هزار ۵۰ هزار ۶۰ هزار ۷۰ هزار ۸۰ هزار ۹۰ هزار ۱۰۰ هزار ۱۱۰ هزار ۱۲۰ هزار ۱۳۰ هزار ۱۴۰ هزار ۱۵۰ هزار ۱۶۰ هزار ۱۷۰ هزار ۱۸۰ هزار ۱۹۰ هزار ۲۰۰ هزار بالای ۲۰۰ هزار')]//li")
    special_kilometrage = driver.find_element('xpath',"//ul[@class='kt-select-option-list kt-select-option-list--small kt-select-option-list--bottom-faded'][contains(.,'وارد کردن مقدار دلخواهصفرهزار ۱۰ هزار ۲۰ هزار ۳۰ هزار ۴۰ هزار ۵۰ هزار ۶۰ هزار ۷۰ هزار ۸۰ هزار ۹۰ هزار ۱۰۰ هزار ۱۱۰ هزار ۱۲۰ هزار ۱۳۰ هزار ۱۴۰ هزار ۱۵۰ هزار ۱۶۰ هزار ۱۷۰ هزار ۱۸۰ هزار ۱۹۰ هزار ۲۰۰ هزار بالای ۲۰۰ هزار')]//li[4]")
    assert special_kilometrage.text.find("۱۰") != -1
    special_kilometrage.click()
    sleep(4)

    filter_icon = Wait_For_Appearance(driver,'xpath',"//i[contains(@class,'kt-icon kt-icon-keyboard-arrow-down-o kt-icon--xs kt-dropdown-button__arrow-icon')]")
    filter_icon.click()

    cheapest_filter = Wait_For_Appearance(driver,'xpath',"//div[@role='menu' and @tabindex='-1']//div[@role='button'][contains(.,'ارزان‌ترین')]")
    cheapest_filter.click()
    sleep(4)

    select_random_data = Wait_For_Appearance(driver,'xpath',"//div[@data-test-id='virtuoso-item-list']//div[4]//div[@class='post-list__widget-col-c1444'][1]")
    driver.execute_script("arguments[0].scrollIntoView();",select_random_data)
    sleep(3)
    select_random_data.click()
    sleep(4)
    directory = os.getcwd()
    driver.save_screenshot(directory+"/result.png")

def test_Select_Vehicle_Of_Divar_Website(driver = divar_driver):
    Select_Vehicle_Of_Divar_Website(driver=driver)





