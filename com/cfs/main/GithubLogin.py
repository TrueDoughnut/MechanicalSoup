import mechanicalsoup
import sys

def run():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    browser = mechanicalsoup.StatefulBrowser(
        soup_config={'features': 'lxml'},
        raise_on_404=True,
        user_agent='MyBot/0.1: mysite.example.com/bot_info'
    )
    #browser.set_verbose(2)

    browser.open("https://github.com")
    browser.follow_link("login")
    browser.select_form("#login form")
    browser["login"] = username
    browser["password"] = password

    response = browser.submit_selected()

    browser.select_form("form[action='/sessions/two-factor']")
    browser["otp"] = input("Enter the authentication token: ")

    #verify logged in
    page = browser.get_current_page()
    messages = page.find("div", class_="flash-messages")
    if messages:
        print(messages.text)
    assert page.select(".logout-form")

    print(page.title.text)

    page3 = browser.open("https://github.com/MechanicalSoup/MechanicalSoup")
    assert page3.soup.select(".logout-form")

if __name__ == '__main__':
    run()