import unittest
from LoginPage import LoginPageFlows
from DashboardPage import DashboardPageFlows
from EmpListPage import EmpListFlows


class MyTestCase4(unittest.TestCase):

    def test_DeleteEmp(self):

        LoginPageObj = LoginPageFlows()
        LoginPageObj.LoginInToAccount('Admin','admin123')

        MainDashboardObj = DashboardPageFlows()
        MainDashboardObj.GotoEmpList()

        EmpListPageObj = EmpListFlows()
        EmpListPageObj.SearchEmp('Ganesh')

        EmpListPageObj.DeleteEmp()

if __name__ == '__main__':

    unittest.main()
