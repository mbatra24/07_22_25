from pages.PIMPage import pim_add_employee, pim_search_employee


def test_pim_page(setup):
    driver = setup
    pim_add_employee(driver)
    pim_search_employee(driver)
