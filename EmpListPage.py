from MyUtilities import MyUtilitiesClass
from MyParent import MyParentClass

class EmpListFlows(MyParentClass):

    def SearchEmp(self,Ename,Eid):

        try:
            EnameLoc = MyUtilitiesClass.driver.find_element_by_id('empsearch_employee_name_empName')
            self.MySendKeys(EnameLoc,Ename)

            EidLoc =MyUtilitiesClass.driver.find_element_by_id('empsearch_id')
            self.MySendKeys(EidLoc,Eid)

            ESerBtnLoc = MyUtilitiesClass.driver.find_element_by_id('searchBtn')
            self.MyClick(ESerBtnLoc)

            self.MyScroll('100')
            #EResetBtnLoc = MyUtilitiesClass.driver.find_element_by_id('resetBtn')
            #self.MyClick(EResetBtnLoc)
        except:
            self.SearchEmp("AddNewEmp_Basic")
            return print('Exception : Web element related to method "SearchEmp" not found')

