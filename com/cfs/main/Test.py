import mechanicalsoup

def run():
    # create the browser object
    browser = mechanicalsoup.StatefulBrowser()
    # set url
    print(browser.open("http://httpbin.org/"))
    print(browser.get_url())
    # follow a link with the given text
    browser.follow_link("forms")
    print(browser.get_url())

    # get the html of the current page
    print(browser.get_current_page())

    print()
    # find all html with the given tag
    print(browser.get_current_page().find_all('legend'))

    # select a form
    browser.select_form("form[action='/post']")

    print()
    # get fields of selected form
    print(browser.get_current_form().print_summary())

    # set a text field
    browser["custname"] = "me"
    browser["custtel"] = "000 000 0001"
    browser["custemail"] = "nobody@example.com"

    # set a radio button
    browser["size"] = "small"
    # same to set check boxes
    browser["topping"] = "bacon"  # single checkbox
    browser["topping"] = ("bacon", "cheese") # multiple checkboxes

    print()
    print(browser.get_current_form().print_summary())

    response = browser.submit_selected()
    print(response.text)



if __name__ == '__main__':
    run()
