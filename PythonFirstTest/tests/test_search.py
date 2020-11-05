from pages.search import DuckDuckGoSearchPage
from pages.result import DuckDuckGoResultPage


def test_basic_duckduckgo_search(browser):
    """
    Scenario: Basic DuckDuckGo Search

        Given the DuckDuckGo home page is displayed
        When the user searches ofr "panda"
        Then the search result title contains "panda"
        And the search result query is "panda"
        And the search result links pertain to "panda"
    """
    search_page = DuckDuckGoSearchPage(browser)
    result_page = DuckDuckGoResultPage(browser)

    search_page.load()

    search_page.search("panda")

    assert "panda" in result_page.title()

    assert "panda" == result_page.search_input_value()

    assert result_page.result_count_for_phrase("panda") > 0
