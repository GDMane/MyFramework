from MyUtilities import MyUtilitiesClass
from MyParent import MyParentClass

class EmpListFlows(MyParentClass):

    def SearchEmp(self,Ename):

        try:
            EnameLoc = MyUtilitiesClass.driver.find_element_by_id('empsearch_employee_name_empName')
            self.MySendKeys(EnameLoc,Ename)

            ESerBtnLoc = MyUtilitiesClass.driver.find_element_by_id('searchBtn')
            self.MyClick(ESerBtnLoc)

            self.MyScroll('100')
            #EResetBtnLoc = MyUtilitiesClass.driver.find_element_by_id('resetBtn')
            #self.MyClick(EResetBtnLoc)
        except:
            self.SearchEmp("SearchEmp")
            return print('Exception : Web element related to method "SearchEmp" not found')

    def DeleteEmp(self):

        #try:
            ECheckBoxLoc = MyUtilitiesClass.driver.find_element_by_id('tableWrapper').find_element_by_tag_name('tr').find_elements_by_tag_name('td')

            for index, col in enumerate(ECheckBoxLoc):
                if index == 1:
                 print('colnText', col.text, type(col.text), print(len(col.text)))

            #for item in ECheckBoxLoc:
             #   print(ECheckBoxLoc[item].text)
            #len(colns[4].text) == 0:




            #self.MyClick(ECheckBoxLoc)

        #except:
         #   self.SearchEmp("DeleteEmp")
          #  return print('Exception : Web element related to method "DeleteEmp" not found')
