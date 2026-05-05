"""
Test Case: Product Search Functionality

===========================================
Test Steps
===========================================

1. Open the application in the browser.
2. Locate the search box on the Home page.
3. Enter a valid product name (for example, "iPhone") in the search box.
4. Click on the "Search" button.
5. Verify that the Search Results page is displayed.
6. Check if the searched product name appears in the list of search results.

Expected Result:
----------------
The Search Results page should appear, and the searched product should be
visible in the search results list.
"""
import time
import pytest
from pages.home_page import HomePage
from pages.product_search_page import ProductSearchPage
from config import Config
from playwright.sync_api import expect

# these custom markers are needed for grouping and are present in the pytest.ini file
@pytest.mark.regression
def test_search_product(page):
    home_page = HomePage(page)
    prod_search = ProductSearchPage(page)
    #step3:
    home_page.enter_product_name(Config.product_name)
    #step4:
    home_page.click_search()
    time.sleep(2)
    #step5:
    expect(prod_search.search_button_visible()).to_be_visible(timeout=2000)
    #step6:
    expect(prod_search.is_product_present(Config.product_name)).to_be_visible(timeout=2000)
    time.sleep(1)
    prod_search.select_product(Config.product_name)
    time.sleep(2)
