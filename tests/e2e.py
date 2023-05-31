from selenium import webdriver
from selenium.webdriver.common.by import By


def test_scores_service(app_url):
    driver = webdriver.Chrome()
    driver.get(app_url)
    score_element = driver.find_element(By.ID, "score")
    score_text = score_element.text
    driver.quit()
    try:
        score = int(score_text)
        if 1 <= score <= 1000:
            return True
        else:
            return False
    except ValueError:
        return False


def main_function():
    app_url = "http://127.0.0.1:5001"
    result = test_scores_service(app_url)
    if result:
        print("Tests passed.")
        return 0
    else:
        print("Tests failed.")
        return -1

