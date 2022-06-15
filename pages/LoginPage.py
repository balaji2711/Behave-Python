from actions.selenium_actions import SeleniumActions


class LoginPage(SeleniumActions):
    txtUsername = "user-name"
    txtPassword = "password"
    btnLogin = "login-button"
    title = "//span[@class='title']"

    def __init__(self, driver):
        super().__init__(driver)

    def enter_username(self, username):
        self.type("ID", LoginPage.txtUsername, username)

    def enter_password(self, password):
        self.type("ID", LoginPage.txtPassword, password)

    def click_login(self):
        self.click("ID", LoginPage.btnLogin)

    def is_login_successful(self):
        assert self.get("XPATH", LoginPage.title) == "PRODUCTS", "Login is not successful"
