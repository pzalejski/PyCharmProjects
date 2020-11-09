from appium import webdriver
import unittest


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

    def test_first_and_last(self, driver=DRIVER):
        try:
            driver.find_element_by_id("com.fetchrewards.fetchrewards.hop:id/tiet_signup_name").send_keys("Jane")
            driver.find_element_by_id("com.fetchrewards.fetchrewards.hop:id/tiet_signup_last_name").send_keys(
                "Jane")
        except:
            print("cannot find element")

    # def tearDown(self):
    #     self.driver.quit()


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestFetchCases("test_sign_up_with_email"))
    suite.addTest(TestFetchCases("test_first_and_last"))
    unittest.TestLoader().loadTestsFromTestCase(TestFetchCases)
    unittest.TextTestRunner(verbosity=2).run(suite)
