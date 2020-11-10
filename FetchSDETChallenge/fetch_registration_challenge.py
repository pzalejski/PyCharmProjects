from appium import webdriver
import unittest
from email_form import first_name, last_name, email as em
from pass_gen import pw_gen


class TestFetchCases(unittest.TestCase):
    desired_caps = dict(
        platformName="android",
        deviceName="Galaxy Note10+",
        appPackage="com.fetchrewards.fetchrewards.hop",
        appActivity="com.fetchrewards.fetchrewards.activities.SplashActivity"
    )

    DRIVER = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

    def test_sign_up_with_email(self, driver=DRIVER):
        driver.implicitly_wait(10)
        try:
            driver.find_element_by_id("com.fetchrewards.fetchrewards.hop:id/email_signup_button").click()
        except:
            print("cannot find element")

    def test_sign_up_fields(self, driver=DRIVER):
        email = em()
        try:
            driver.find_element_by_id("com.fetchrewards.fetchrewards.hop:id/tiet_signup_name").send_keys(first_name)
            driver.find_element_by_id("com.fetchrewards.fetchrewards.hop:id/tiet_signup_last_name").send_keys(last_name)
            driver.find_element_by_id("com.fetchrewards.fetchrewards.hop:id/tiet_signup_email").send_keys(email)
            driver.find_element_by_id("com.fetchrewards.fetchrewards.hop:id/tiet_signup_email_confirm").send_keys(
                email)
            driver.find_element_by_id("com.fetchrewards.fetchrewards.hop:id/tiet_signup_password").send_keys(pw_gen())
        except:
            self.fail("Failed")

    def test_sign_up_button(self, driver=DRIVER):
        driver.implicitly_wait(5)
        try:
            driver.find_element_by_id("com.fetchrewards.fetchrewards.hop:id/sign_up_button").click()
        except:
            self.fail("Failed")

    # def tearDown(self):
    #     self.driver.quit()


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestFetchCases("test_sign_up_with_email"))
    suite.addTest(TestFetchCases("test_sign_up_fields"))
    suite.addTest(TestFetchCases("test_sign_up_button"))
    unittest.TestLoader().loadTestsFromTestCase(TestFetchCases)
    unittest.TextTestRunner(verbosity=2).run(suite)
