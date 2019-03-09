from MyUtilities import MyUtilitiesClass
from MyParent import MyParentClass

class LoginPageFlows(MyParentClass):

    driverInst = None

    def __init__(self):
        LoginPageFlows.driverInst = MyUtilitiesClass.Mydriver()


    def LoginInToAccount(self,Uname,Password):

        NameLoc = LoginPageFlows.driverInst.find_element_by_xpath('//*[@id="txtUsername"]')
        self.MySendKeys(MyElement = NameLoc,MyValue = Uname)

        PassLoc = LoginPageFlows.driverInst.find_element_by_xpath('//*[@id="txtPassword"]')
        self.MySendKeys(MyElement=PassLoc, MyValue=Password)

        Button = LoginPageFlows.driverInst.find_element_by_xpath('//*[@id="btnLogin"]')
        self.MyClick(Button)

    def GetErrorText(self):
        try:
            return LoginPageFlows.driverInst.find_element_by_id('spanMessage').text
        except:
            None


