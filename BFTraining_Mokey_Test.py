# Import the required libraries.
import sys
import os

from datetime import datetime, date, time
import re
import time
import random
from random import randint

import base64

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

# Define the log file:
try:
    log_file = open('log_file.txt', mode = 'w')
except:
    print ("Unable to open the log file.")

# Print out the error message to the both standard output and log_file.
def print_log(message):
    try:
        log_file.write(str(datetime.now()) + ': ' + message + '\n')
        print (str(datetime.now()) + ': ' + message)
    except:
        print ("Unable to write into the log file.")

# Expand definition of find_element_by_id to return False in case there is no element.
def exists_by_id(parentObj, idText, ignoreNone = False, waitToFind = False, triesNum = 0):
    try:
        return parentObj.find_element_by_id(idText)
    except:
        print_log("Element by id = '" + idText + "' not found.")
        if ignoreNone:
            if waitToFind and triesNum < 10:
                time.sleep(1)
                return exists_by_id(parentObj, idText, ignoreNone, waitToFind, triesNum + 1)
            return None
        if waitToFind and triesNum < 10:
            time.sleep(1)
            return exists_by_id(parentObj, idText, ignoreNone, waitToFind, triesNum + 1)
        sys.exit()

# Expand definition of find_element_by_name to return False in case there is no element.
def exists_by_name(parentObj, name, ignoreNone = False, waitToFind = False, triesNum = 0):
    try:
        return parentObj.find_element_by_name(name)
    except:
        print_log("Element by name = '" + name + "' not found.")
        if (ignoreNone):
            if waitToFind and triesNum < 10:
                time.sleep(1)
                return exists_by_name(parentObj, name, ignoreNone, waitToFind, triesNum + 1)
            return None
        if waitToFind and triesNum < 10:
            time.sleep(1)
            return exists_by_name(parentObj, name, ignoreNone, waitToFind, triesNum + 1)
        sys.exit()

# Expand definition of find_element_by_tag_name to return False in case there is no element.
def exists_by_tag_name(parentObj, tagName, ignoreNone = False, waitToFind = False, triesNum = 0):
    try:
        return parentObj.find_element_by_tag_name(tagName)
    except:
        print_log("Element by tag name = '" + tagName + "' not found.")
        if (ignoreNone):
            if waitToFind and triesNum < 10:
                time.sleep(1)
                return exists_by_tag_name(parentObj, tagName, ignoreNone, waitToFind, triesNum + 1)
            return None
        if waitToFind and triesNum < 10:
            time.sleep(1)
            return exists_by_tag_name(parentObj, tagName, ignoreNone, waitToFind, triesNum + 1)
        sys.exit()

# Expand definition of find_element_by_css_selector to return False in case there is no element.
def exists_by_css_selector(parentObj, css_selector, ignoreNone = False, waitToFind = False, triesNum = 0):
    try:
        return parentObj.find_element_by_css_selector(css_selector)
    except:
        print_log("Element by CSS selector = '" + css_selector + "' not found.")
        if (ignoreNone):
            if waitToFind and triesNum < 10:
                time.sleep(1)
                return exists_by_css_selector(parentObj, css_selector, ignoreNone, waitToFind, triesNum + 1)
            return None
        if waitToFind and triesNum < 10:
            time.sleep(1)
            return exists_by_css_selector(parentObj, css_selector, ignoreNone, waitToFind, triesNum + 1)
        sys.exit()

# Expand definition of find_element_by_xpath to return False in case there is no element.
def exists_by_xpath(parentObj, xpath, ignoreNone = False, waitToFind = False, triesNum = 0):
    try:
        return parentObj.find_element_by_xpath(xpath)
    except:
        print_log("Element by xpath = '" + xpath + "' not found.")
        if (ignoreNone):
            if waitToFind and triesNum < 10:
                time.sleep(1)
                return exists_by_xpath(parentObj, xpath, ignoreNone, waitToFind, triesNum + 1)
            return None
        if waitToFind and triesNum < 10:
            time.sleep(1)
            return exists_by_xpath(parentObj, xpath, ignoreNone, waitToFind, triesNum + 1)
        sys.exit()

# Expand definition of find_elements_by_tag_name to return False in case there is no element.
def exist_all_by_name(parentObj, name, ignoreNone = False, waitToFind = False, triesNum = 0):
    try:
        elements = parentObj.find_elements_by_name(name)
        # If lisList is not found:
        if len(elements) == 0:
            print_log("Elements by name = '" + name + "' not found.")
            if (ignoreNone):
                if waitToFind and triesNum < 10:
                    time.sleep(1)
                    return exist_all_by_name(parentObj, name, ignoreNone, waitToFind, triesNum + 1)
                return None
            if waitToFind and triesNum < 10:
                time.sleep(1)
                return exist_all_by_name(parentObj, name, ignoreNone, waitToFind, triesNum + 1)
            sys.exit()
        return elements
    except:
        print_log("Element by name = '" + name + "' not found.")
        if waitToFind and triesNum < 10:
            time.sleep(1)
            return exist_all_by_name(parentObj, name, ignoreNone, waitToFind, triesNum + 1)
        sys.exit()

# Expand definition of find_elements_by_tag_name to return False in case there is no element.
def exist_all_by_tag_name(parentObj, tagName, ignoreNone = False, waitToFind = False, triesNum = 0):
    try:
        elements = parentObj.find_elements_by_tag_name(tagName)
        # If lisList is not found:
        if len(elements) == 0:
            print_log("Elements by tag name = '" + tagName + "' not found.")
            if (ignoreNone):
                if waitToFind and triesNum < 10:
                    time.sleep(1)
                    return exist_all_by_tag_name(parentObj, tagName, ignoreNone, waitToFind, triesNum + 1)
                return None
            if waitToFind and triesNum < 10:
                time.sleep(1)
                return exist_all_by_tag_name(parentObj, tagName, ignoreNone, waitToFind, triesNum + 1)
            sys.exit()
        return elements
    except:
        print_log("Element by tag name = '" + tagName + "' not found.")
        if waitToFind and triesNum < 10:
            time.sleep(1)
            return exist_all_by_tag_name(parentObj, tagName, ignoreNone, waitToFind, triesNum + 1)
        sys.exit()

# Expand definition of find_elements_by_css_selector to return False in case there is no element.
def exist_all_by_css_selector(parentObj, css_selector, ignoreNone = False, waitToFind = False, triesNum = 0):
    try:
        elements = parentObj.find_elements_by_css_selector(css_selector)
        # If lisList is not found:
        if len(elements) == 0:
            print_log("Elements by CSS selector = '" + css_selector + "' not found.")
            if (ignoreNone):
                if waitToFind and triesNum < 10:
                    time.sleep(1)
                    return exist_all_by_css_selector(parentObj, css_selector, ignoreNone, waitToFind, triesNum + 1)
                return None
            if waitToFind and triesNum < 10:
                time.sleep(1)
                return exist_all_by_css_selector(parentObj, css_selector, ignoreNone, waitToFind, triesNum + 1)
            sys.exit()
        return elements
    except:
        print_log("Element by CSS selector = '" + css_selector + "' not found.")
        if waitToFind and triesNum < 10:
            time.sleep(1)
            return exist_all_by_css_selector(parentObj, css_selector, ignoreNone, waitToFind, triesNum + 1)
        sys.exit()

# Expand definition of find_elements_by_xpath to return False in case there is no element.
def exist_all_by_xpath(parentObj, xpath, ignoreNone = False, waitToFind = False, triesNum = 0):
    try:
        elements = parentObj.find_elements_by_xpath(xpath)
        # If lisList is not found:
        if len(elements) == 0:
            print_log("Elements by xpath = '" + xpath + "' not found.")
            if (ignoreNone):
                if waitToFind and triesNum < 10:
                    time.sleep(1)
                    return exist_all_by_xpath(parentObj, xpath, ignoreNone, waitToFind, triesNum + 1)
                return None
            if waitToFind and triesNum < 10:
                time.sleep(1)
                return exist_all_by_xpath(parentObj, xpath, ignoreNone, waitToFind, triesNum + 1)
            sys.exit()
        return elements
    except:
        print_log("Element by xpath = '" + xpath + "' not found.")
        if waitToFind and triesNum < 10:
            time.sleep(1)
            return exist_all_by_xpath(parentObj, xpath, ignoreNone, waitToFind, triesNum + 1)
        sys.exit()


# Find the element and extract its text.
def find_and_extract(parentObj, objName, xpath):
    # Find the element.
    ObjTag = exists_by_xpath(parentObj, xpath, True)

    # Find the text of the element.
    if ObjTag != None:
        objText = ObjTag.text
    else:
        objText = ""

    print_log(objName + ": " + objText)

    return objText

def hover_and_click(htmlObj, browser):

    actionChains = ActionChains(browser)
    actionChains.move_to_element(htmlObj).perform()

    browser.execute_script("arguments[0].setAttribute('style', 'visibility:visible;');", htmlObj)

    htmlObj.click()

    # bodyObj = exists_by_tag_name(browser, 'body', ignoreNone = False, waitToFind = True)
    # location = htmlObj.location

    # browser.execute_script("var e = new jQuery.Event('click'); e.pageX = " + str(location['x']) + "; e.pageY = " + str(location['y']) + "; $('body').trigger(e);")

    # actionChains.move_to_element_with_offset(bodyObj, location['x'], location['y'])
    # actionChains.click()
    # actionChains.perform()

# Click the element and wait for a random number between 1 and 10 seconds.
def click_and_wait(htmlObj, browser):

    hover_and_click(htmlObj, browser)

    # Random float x, 1.0 <= x < 10.0
    randomTimePeriod = random.uniform(1, 4)

    print_log("Wait time: " + str(randomTimePeriod) + " seconds")

    time.sleep(randomTimePeriod)

# Go back to the previous page and wait for a random number between 1 and 10 seconds.
def back_and_wait(browser):

    browser.back()

    # Random float x, 1.0 <= x < 10.0
    randomTimePeriod = random.uniform(1, 4)

    print_log("Wait time: " + str(randomTimePeriod) + " seconds")

    time.sleep(randomTimePeriod)



# Main program:

# Define the browser to be used as Mozilla Firefox, because it if the most flexible one among well-known browsers.
firefox_profile = webdriver.FirefoxProfile()
# firefox_profile.set_preference('permissions.default.stylesheet', 2)
# firefox_profile.set_preference('permissions.default.image', 2)

browser = webdriver.Firefox(firefox_profile)

# Define the url to start crawling with.
url = 'https://bftrain.miserver.it.umich.edu'

# Retrieve the content of the start page.
browser.get(url)
browser.maximize_window()


html = exists_by_tag_name(browser, 'html', ignoreNone = False, waitToFind = True)

#Check for operating system and zoom out using correct keys.
from sys import platform as _platform
if _platform == "linux" or _platform == "linux2":
    # linux
    print_log("linux")
elif _platform == "darwin":
    # OS X
    print_log("Mac OSX")
    html.send_keys(Keys.COMMAND + Keys.SUBTRACT)
    html.send_keys(Keys.COMMAND + Keys.SUBTRACT)
    html.send_keys(Keys.COMMAND + Keys.SUBTRACT)		
elif _platform == "win32":
    # Windows...
    print_log("windows")
    html.send_keys(Keys.CONTROL + Keys.SUBTRACT)
    html.send_keys(Keys.CONTROL + Keys.SUBTRACT)
    html.send_keys(Keys.CONTROL + Keys.SUBTRACT)

inputEmailObj = exists_by_id(browser, "inputEmail", ignoreNone = False, waitToFind = True)

accountRandomString =str(randint(0, 99999999))
domainRandomString =  str(randint(0, 99999999))

inputEmailObj.send_keys(accountRandomString + "@" + domainRandomString + ".com")

submitMethod = randint(0, 1)

if submitMethod == 0:
    submitBtn = exists_by_xpath(browser, "/html/body/div/div[1]/div[2]/form/button", ignoreNone = False, waitToFind = True)
    hover_and_click(submitBtn, browser)
else:
    inputEmailObj.send_keys(Keys.ENTER)

startPretestBtn = exists_by_id(browser, 'StartBtn', ignoreNone = False, waitToFind = True)
hover_and_click(startPretestBtn, browser)

for index in range(7):
    linkAnchor = exists_by_css_selector(browser, '.LinkAnchor', ignoreNone = False, waitToFind = True)

    actionChains = ActionChains(browser)
    if randint(0, 1) == 1:
        actionChains.move_to_element(linkAnchor).perform()

    # if randint(0, 1) == 1:
    #     hover_and_click(linkAnchor, browser)

    if randint(0, 1) == 1:
        actionChains.context_click(linkAnchor).perform()

    browser.execute_script("window.scrollTo(0, 1000);")

    YesOrNo = randint(0, 1)

    if YesOrNo == 0:
        NoBtn = exists_by_id(browser, "NoButton", ignoreNone = False, waitToFind = True)
        hover_and_click(NoBtn, browser)
    else:
        YesBtn = exists_by_id(browser, "YesButton", ignoreNone = False, waitToFind = True)
        hover_and_click(YesBtn, browser)

GotoTrainingBtn = exists_by_id(browser, 'GotoTraining', ignoreNone = False, waitToFind = True)
hover_and_click(GotoTrainingBtn, browser)

# time.sleep(10);

browser.switch_to.frame(exists_by_tag_name(browser, 'iframe', ignoreNone = False, waitToFind = True))

StartTrainingBtn = exists_by_id(browser, 'Button_54', ignoreNone = False, waitToFind = True)
# hover_and_click(StartTrainingBtn, browser)
while not StartTrainingBtn.is_displayed():
    time.sleep(1)
actionChains = ActionChains(browser)
actionChains.send_keys(Keys.TAB).perform()
actionChains.send_keys(Keys.ENTER).perform()

ContinueTrainingBtn = exists_by_id(browser, 'Button_57', ignoreNone = True, waitToFind = True)

while ContinueTrainingBtn == None:
    actionChains = ActionChains(browser)
    actionChains.send_keys(Keys.TAB).perform()
    actionChains.send_keys(Keys.ENTER).perform()

    ContinueTrainingBtn = exists_by_id(browser, 'Button_57', ignoreNone = True, waitToFind = True)

# hover_and_click(ContinueTrainingBtn, browser)
actionChains.send_keys(Keys.TAB).perform()
actionChains.send_keys(Keys.ENTER).perform()

Continue_to_Practice_EmailBtn = exists_by_id(browser, 'Continue_to_Practice_Email', ignoreNone = False, waitToFind = True)
hover_and_click(Continue_to_Practice_EmailBtn, browser)

Practice_Email_Answer = randint(0, 1)

if Practice_Email_Answer == 0:
    Practice_Email_NoBtn = exists_by_id(browser, 'Practice_Email_No', ignoreNone = False, waitToFind = True)
    hover_and_click(Practice_Email_NoBtn, browser)

    Button_28Btn = exists_by_id(browser, 'Button_28', ignoreNone = False, waitToFind = True)
    hover_and_click(Button_28Btn, browser)
else:
    Practice_Email_YesBtn = exists_by_id(browser, 'Practice_Email_Yes', ignoreNone = False, waitToFind = True)
    hover_and_click(Practice_Email_YesBtn, browser)

    Button_27Btn = exists_by_id(browser, 'Button_27', ignoreNone = False, waitToFind = True)
    hover_and_click(Button_27Btn, browser)

Button_29Btn = exists_by_id(browser, 'Button_29', ignoreNone = False, waitToFind = True)
hover_and_click(Button_29Btn, browser)

Practice_Email2_Answer = randint(0, 1)

if Practice_Email2_Answer == 0:
    Button_22Btn = exists_by_id(browser, 'Button_22', ignoreNone = False, waitToFind = True)
    hover_and_click(Button_22Btn, browser)

    Practice_Email2_No = randint(0, 1)

    if Practice_Email2_No == 0:
        Button_34Btn = exists_by_id(browser, 'Button_34', ignoreNone = False, waitToFind = True)
        hover_and_click(Button_34Btn, browser)
        Button_35Btn = exists_by_id(browser, 'Button_35', ignoreNone = False, waitToFind = True)
        hover_and_click(Button_35Btn, browser)
    else:
        Button_33Btn = exists_by_id(browser, 'Button_33', ignoreNone = False, waitToFind = True)
        hover_and_click(Button_33Btn, browser)
else:
    Button_21Btn = exists_by_id(browser, 'Button_21', ignoreNone = False, waitToFind = True)
    hover_and_click(Button_21Btn, browser)

    Practice_Email2_Yes = randint(0, 1)

    if Practice_Email2_Yes == 0:
        Button_32Btn = exists_by_id(browser, 'Button_32', ignoreNone = False, waitToFind = True)
        hover_and_click(Button_32Btn, browser)
    else:
        Button_31Btn = exists_by_id(browser, 'Button_31', ignoreNone = False, waitToFind = True)
        hover_and_click(Button_31Btn, browser)

Practice_Email3_Answer = randint(0, 1)

if Practice_Email3_Answer == 0:
    Button_23Btn = exists_by_id(browser, 'Button_23', ignoreNone = False, waitToFind = True)
    hover_and_click(Button_23Btn, browser)

    Practice_Email3_Yes = randint(0, 1)

    if Practice_Email3_Yes == 0:
        Button_37Btn = exists_by_id(browser, 'Button_37', ignoreNone = False, waitToFind = True)
        hover_and_click(Button_37Btn, browser)
    else:
        Button_38Btn = exists_by_id(browser, 'Button_38', ignoreNone = False, waitToFind = True)
        hover_and_click(Button_38Btn, browser)
        Button_41Btn = exists_by_id(browser, 'Button_41', ignoreNone = False, waitToFind = True)
        hover_and_click(Button_41Btn, browser)
else:
    Button_24Btn = exists_by_id(browser, 'Button_24', ignoreNone = False, waitToFind = True)
    hover_and_click(Button_24Btn, browser)

    Practice_Email3_No = randint(0, 1)

    if Practice_Email3_No == 0:
        Button_39Btn = exists_by_id(browser, 'Button_39', ignoreNone = False, waitToFind = True)
        hover_and_click(Button_39Btn, browser)
    else:
        Button_40Btn = exists_by_id(browser, 'Button_40', ignoreNone = False, waitToFind = True)
        hover_and_click(Button_40Btn, browser)
        Button_41Btn = exists_by_id(browser, 'Button_41', ignoreNone = False, waitToFind = True)
        hover_and_click(Button_41Btn, browser)

Practice_Email4_Answer = randint(0, 1)

if Practice_Email4_Answer == 0:
    Button_25Btn = exists_by_id(browser, 'Button_25', ignoreNone = False, waitToFind = True)
    hover_and_click(Button_25Btn, browser)

    Practice_Email4_Yes = randint(0, 1)

    if Practice_Email4_Yes == 0:
        Button_43Btn = exists_by_id(browser, 'Button_43', ignoreNone = False, waitToFind = True)
        hover_and_click(Button_43Btn, browser)
    else:
        Button_44Btn = exists_by_id(browser, 'Button_44', ignoreNone = False, waitToFind = True)
        hover_and_click(Button_44Btn, browser)
        Continue_to_EndBtn = exists_by_id(browser, 'Continue_to_End', ignoreNone = False, waitToFind = True)
        hover_and_click(Continue_to_EndBtn, browser)
else:
    Button_26Btn = exists_by_id(browser, 'Button_26', ignoreNone = False, waitToFind = True)
    hover_and_click(Button_26Btn, browser)

    Practice_Email4_No = randint(0, 1)

    if Practice_Email4_No == 0:
        Button_45Btn = exists_by_id(browser, 'Button_45', ignoreNone = False, waitToFind = True)
        hover_and_click(Button_45Btn, browser)
    else:
        Review_the_CluesBtn = exists_by_id(browser, 'Review_the_Clues', ignoreNone = False, waitToFind = True)
        hover_and_click(Review_the_CluesBtn, browser)
        Continue_to_EndBtn = exists_by_id(browser, 'Continue_to_End', ignoreNone = False, waitToFind = True)
        hover_and_click(Continue_to_EndBtn, browser)

QuitBtn = exists_by_id(browser, 'Quit', ignoreNone = False, waitToFind = True)
hover_and_click(QuitBtn, browser)

Decision1OptionABtn = exists_by_id(browser, 'Decision1OptionA', ignoreNone = True, waitToFind = False)

if Decision1OptionABtn != None:
    for index in range(1, 11):
        option = randint(0, 1)

        if option == 0:
            Decision1OptionABtn = exists_by_id(browser, 'Decision' + index + 'OptionA', ignoreNone = False, waitToFind = True)
            hover_and_click(Decision1OptionABtn, browser)
        else:
            Decision1OptionBBtn = exists_by_id(browser, 'Decision' + index + 'OptionB', ignoreNone = False, waitToFind = True)
            hover_and_click(Decision1OptionBBtn, browser)

SubmitBtnBtn = exists_by_id(browser, 'SubmitBtn', ignoreNone = False, waitToFind = True)
hover_and_click(SubmitBtnBtn, browser)



