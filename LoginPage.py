from MyUtilities import MyUtilitiesClass

class LoginPageFlows():

    driverInst = None

    def __init__(self):
        LoginPageFlows.driverInst = MyUtilitiesClass.Mydriver()


    def LoginInToAccount(self,Uname,Password):
        LoginPageFlows.driverInst.find_element_by_xpath('//*[@id="txtUsername"]').send_keys(Uname)
        LoginPageFlows.driverInst.find_element_by_xpath('//*[@id="txtPassword"]').send_keys(Password)
        LoginPageFlows.driverInst.find_element_by_xpath('//*[@id="btnLogin"]').click()

    def GetErrorText(self):
        try:
            return LoginPageFlows.driverInst.find_element_by_id('spanMessage').text
        except:
            None

