from pages.adminpage import Adminpage


class TestDeleteAdminUser:

    def test_delete_admin_user(self, setup):
        driver = setup
        ap = Adminpage(driver)
        ap.admin_page()
        ap.search_user()
        ap.delete_user()


