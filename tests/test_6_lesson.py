from datetime import time


def test_dark_theme_by_time():
    current_time = time(hour=23)

    if 6 <= current_time.hour < 22:
        is_dark_theme = None
    else:
        is_dark_theme = True
    assert is_dark_theme is True


def test_dark_theme_by_time_and_user_choise():

    current_time=time(hour=16)
    dark_theme_enabled_by_user = True

    if (6 <= current_time.hour < 22) and dark_theme_enabled_by_user is True:
        is_dark_theme = True
    elif dark_theme_enabled_by_user:
        is_dark_theme = True
    else:
        is_dark_theme = None
    assert is_dark_theme is True


def test_find_suitable_user():
    users = [
        {"name": "Oleg", "age": 32},
        {"name": "Sergey", "age": 24},
        {"name": "Stanislav", "age": 15},
        {"name": "Olga", "age": 45},
        {"name": "Maria", "age": 18}
    ]

    suitable_users = None

    for i in users:
        if i['name'] == 'Olga':
            suitable_users = i
    assert suitable_users == {"name": "Olga", "age": 45}

    suitable_users = []

    for i in users:
        if i['age'] < 20:
            suitable_users.append(i)
    assert suitable_users == [
        {"name": "Stanislav", "age": 15},
        {"name": "Maria", "age": 18}
    ]

def print_function(func, *args):
    result = func.__name__.replace("_", " ").title() + f" [{', '.join(args)}]"
    print(result)
    return result

def test_readable_function():
    open_browser(browser_name="Chrome")
    go_to_companyname_homepage(page_url="https://companyname.com")
    find_registration_button_on_login_page(page_url="https://companyname.com/login", button_text="Register")

def open_browser(browser_name):
    actual_result = print_function(open_browser, browser_name)
    assert actual_result == "Open Browser [Chrome]"

def go_to_companyname_homepage(page_url):
    actual_result = print_function(go_to_companyname_homepage, page_url)
    assert actual_result == "Go To Companyname Homepage [https://companyname.com]"

def find_registration_button_on_login_page(page_url, button_text):
    actual_result = print_function(find_registration_button_on_login_page, page_url, button_text)
    assert actual_result == "Find Registration Button On Login Page [https://companyname.com/login, Register]"