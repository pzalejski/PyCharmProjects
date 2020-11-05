import pytest
import selenium.webdriver


@pytest.fixture
def browser():
    # This browser will be local
    # Chrome driver must be on the system Path
    b = selenium.webdriver.Chrome()
    b.implicitly_wait(10)
    yield b
    b.quit()
