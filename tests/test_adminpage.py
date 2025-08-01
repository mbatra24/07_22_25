from pages.PIMPage import pim_add_employee
from pages.adminpage import Adminpage


class TestAdminPage:
    def test_admin_page(self, setup):
        driver = setup
        pim_add_employee(driver)
        ap = Adminpage(driver)
        ap.admin_page()
        ap.add_user()
        ap.search_user()
        ap.delete_user()







