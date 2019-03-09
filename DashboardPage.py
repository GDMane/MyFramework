from MyUtilities import MyUtilitiesClass
from selenium.webdriver.common.action_chains import ActionChains


class DashboardPageFlows():

    def LogoutFromAccount(self):
        MyUtilitiesClass.driver.find_element_by_id('branding').find_element_by_id('welcome').click()#aboutDisplayLink
        #MyUtilitiesClass.driver.find_element_by_id('branding').find_element_by_id('welcome-menu').find_element_by_tag_name('ul').find_element_by_link_text('About').click()
        MyUtilitiesClass.driver.find_element_by_id('branding').find_element_by_id('welcome-menu').find_element_by_tag_name('ul').find_element_by_link_text('Logout').click()
        #MyUtilitiesClass.driver.find_element_by_xpath('//*[@id="welcome-menu"]/ul/li[2]').click()
        #MyUtilitiesClass.driver.find_element_by_partial_link_text('Logout').click()


    def GotoAddEmp(self):
        #Menu_PIM = MyUtilitiesClass.driver.find_element_by_class_name('menu').find_elements_by_tag_name('li')[2].find_element_by_id('menu_pim_viewPimModule')
        Menu_PIM = MyUtilitiesClass.driver.find_element_by_xpath('// *[ @ id = "menu_pim_viewPimModule"] / b')

        #AddEmpForm = MyUtilitiesClass.driver.find_element_by_class_name('menu').find_elements_by_tag_name('li')[2].find_element_by_id('menu_pim_viewPimModule').find_element_by_id('menu_pim_addEmployee')
        AddEmpForm = MyUtilitiesClass.driver.find_element_by_xpath('// *[ @ id = "menu_pim_addEmployee"]')

        ActionChains(MyUtilitiesClass.driver).move_to_element(Menu_PIM).move_to_element(AddEmpForm).click().perform()