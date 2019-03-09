from MyUtilities import MyUtilitiesClass

class AddEmpPageFlows:

    def AddNewEmp_Basic(self,Fname,Mname,Lname,Id):

        MyUtilitiesClass.driver.find_element_by_id('firstName').send_keys(Fname)
        MyUtilitiesClass.driver.find_element_by_id('middleName').send_keys(Mname)
        MyUtilitiesClass.driver.find_element_by_id('lastName').send_keys(Lname)
        MyUtilitiesClass.driver.find_element_by_name('employeeId').send_keys(Id)

        MyUtilitiesClass.driver.find_element_by_id('btnSave').click()
