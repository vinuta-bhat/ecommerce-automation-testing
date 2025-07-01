from pages.dropdown_page import DropdownPage

import pytest

def test_select_day(driver):
    dropdown_page = DropdownPage(driver)
    dropdown_page.load()
    dropdown_page.select_day("Friday")
    assert "Day selected :- Friday" in dropdown_page.get_result_text()


@pytest.mark.parametrize("day", ["Monday", "Wednesday", "Friday"])
def test_select_multiple_days(driver, day):
    dropdown_page = DropdownPage(driver)
    dropdown_page.load()
    dropdown_page.select_day(day)
    assert f"Day selected :- {day}" in dropdown_page.get_result_text()
