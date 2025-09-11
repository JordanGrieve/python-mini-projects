# rightmove_quick_scrape_fixed.py
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def human_sleep():
    time.sleep(3)   # fixed 3 seconds each time

def driver_new():
    opts = webdriver.ChromeOptions()
    opts.add_argument("--start-maximized")
    return webdriver.Chrome(options=opts)

def accept_cookies(d):
    try:
        WebDriverWait(d, 8).until(
            EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler"))
        ).click()
        print("✅ Accepted cookies")
    except TimeoutException:
        pass
    human_sleep()

def choose_location(d, q="Glasgow"):
    box = WebDriverWait(d, 15).until(
        EC.presence_of_element_located((By.ID, "ta_searchInput"))
    )
    box.clear(); human_sleep()
    for ch in q:
        box.send_keys(ch)
        time.sleep(0.15)  # still a little typing delay
    print(f"✅ Typed '{q}'")

    # Select suggestion
    try:
        WebDriverWait(d, 8).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid^="typeahead-option"]'))
        ).click()
        print("✅ Selected first suggestion")
    except TimeoutException:
        box.send_keys(Keys.ARROW_DOWN); human_sleep()
        box.send_keys(Keys.ENTER)
        print("↩️ Selected suggestion via keyboard")
    human_sleep()

def start_search(d):
    WebDriverWait(d, 12).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="forSaleCta"]'))
    ).click()
    print("✅ Clicked 'For sale'")
    human_sleep()

    try:
        WebDriverWait(d, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button#submit[data-testid="submit"]'))
        ).click()
        print("✅ Clicked 'Search properties'")
    except TimeoutException:
        try:
            WebDriverWait(d, 2).until(EC.alert_is_present())
            d.switch_to.alert.accept()
        except TimeoutException:
            pass
        d.find_element(By.ID, "ta_searchInput").send_keys(Keys.ENTER)
        print("↩️ Submitted search with Enter")
    human_sleep()

def find_cards(d, want=10):
    cards = []
    for _ in range(12):  # scroll a few times
        cards = d.find_elements(By.XPATH, "//div[starts-with(@data-testid,'propertyCard-')]")
        if len(cards) >= want: break
        d.execute_script("window.scrollBy(0, 600);")
        human_sleep()
    return cards[:want]

def txt(root, *sels):
    for how, sel in sels:
        try: return root.find_element(how, sel).text.strip()
        except: pass
    return ""

def href(root, *sels):
    for how, sel in sels:
        try:
            h = root.find_element(how, sel).get_attribute("href") or ""
            if h.startswith("/"): h = "https://www.rightmove.co.uk" + h
            if h: return h
        except: pass
    return ""

def extract_card(card):
    title = txt(card, (By.CSS_SELECTOR, '[data-testid="property-address"]'),
                       (By.CSS_SELECTOR, "address"))
    price = txt(card, (By.CSS_SELECTOR, '[data-test="property-card-price"]'),
                      (By.CSS_SELECTOR, "[class*='PropertyPrice']"))
    url = href(card, (By.CSS_SELECTOR, 'a[data-test="property-details"]'),
                      (By.CSS_SELECTOR, 'a[href*="/properties/"]'))
    return {"title": title, "price": price, "url": url}

def main(query="Glasgow", take=10):
    d = driver_new()
    try:
        d.get("https://www.rightmove.co.uk/")
        accept_cookies(d)
        choose_location(d, query)
        start_search(d)
        WebDriverWait(d, 25).until(EC.url_contains("/find.html"))
        cards = find_cards(d, take)
        results = [extract_card(c) for c in cards]

        print(f"\nFound {len(results)} results for '{query}':\n")
        for i, r in enumerate(results, 1):
            print(f"{i}. {r['title']}\n   {r['price']}\n   {r['url']}\n")

        return results
    finally:
        d.quit()

if __name__ == "__main__":
    main("Glasgow", take=10)
