from selenium import webdriver

class MyUtilitiesClass:

    driver = None

    @staticmethod
    def Mydriver(browser = "Chrome"):

        if browser == "Chrome":
            MyUtilitiesClass.driver = webdriver.Chrome("E://GMtes//MyFramework//Driver//chromedriver.exe")
        else:
            pass

        MyUtilitiesClass.driver.get("https://opensource-demo.orangehrmlive.com/")
        MyUtilitiesClass.driver.maximize_window()

        #MyUtilitiesClass.driver.find_element_by_
        return MyUtilitiesClass.driver


