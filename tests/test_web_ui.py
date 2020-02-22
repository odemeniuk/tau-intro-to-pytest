"""
This module contains basic Web UI tests using selenium.
Their purpose is to show how to use the pytest framework by example.
To run these tests, make sure both Chrome and ChromeDriver are installed.

To learn more about Web UI testing, take a full tutorial:
https://github.com/AndyLPK247/tau-intro-selenium-py
"""

# --------------------------------------------------------------------------------
# Imports
# --------------------------------------------------------------------------------

import pytest
import selenium.webdriver

from pages.result import DuckDuckGoResultPage
from pages.search import DuckDuckGoSearchPage


# --------------------------------------------------------------------------------
# Fixtures
# --------------------------------------------------------------------------------

@pytest.fixture
def browser():

  # Initialize the WebDriver instance
  b = selenium.webdriver.Chrome()

  # Make its calls wait for elements to appear
  b.implicitly_wait(10)

  # Return the WebDriver instance for the setup
  yield b

  # Quit the WebDriver instance for the cleanup
  b.quit()


# --------------------------------------------------------------------------------
# Tests
# --------------------------------------------------------------------------------

@pytest.mark.parametrize('phrase', ['panda', 'python', 'polar bear'])
def test_basic_duckduckgo_search(browser, phrase):
  search_page = DuckDuckGoSearchPage(browser)
  result_page = DuckDuckGoResultPage(browser)
  
  # Given the DuckDuckGo home page is displayed
  search_page.load()

  # When the user searches for the phrase
  search_page.search(phrase)

  # Then the search result query is the phrase
  assert phrase == result_page.search_input_value()
  
  # And the search result links pertain to the phrase
  titles = result_page.result_link_titles()
  matches = [t for t in titles if phrase.lower() in t.lower()]
  assert len(matches) > 0

  # And the search result title contains the phrase
  assert phrase in result_page.title()
