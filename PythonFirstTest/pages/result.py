from selenium.webdriver.common.by import By


class DuckDuckGoResultPage:
    # Locators
    SEARCH_INPUT = (By.ID, "search_form_input")

    @classmethod
    def phrase_results(cls, phrase):
        xpath = f"//div[@id='links'//*[contains(text(),'{phrase}']"
        return By.XPATH, xpath

    # initializer

    def __init__(self, browser):
        self.browser = browser

    # interaction methods

    def result_count_for_phrase(self, phrase):
        results = self.browser.find_element(*self.phrase_results(phrase))
        return len(results)

    def search_input_value(self):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        return search_input.get_attribute('value')

    def title(self):
        return self.browser.title
