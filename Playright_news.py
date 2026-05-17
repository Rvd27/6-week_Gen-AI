#  write a playwright python script for open a webbrowser and search pak vs bangladesh test match, get the latest news
from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:

    # Launch browser
    browser = p.chromium.launch(
        headless=False
    )

    # Create new page
    page = browser.new_page()

    # Open Google
    page.goto("https://www.google.com")

    # Wait for page load
    page.wait_for_timeout(2000)

    # Type search query
    page.fill('textarea[name="q"]',
              "Pak vs Bangladesh test match latest news")

    # Press Enter
    page.keyboard.press("Enter")

    # Wait for results
    page.wait_for_timeout(3000)

    # Click first search result
    first_result = page.locator("h3").first
    first_result.click()

    # Wait for article page
    page.wait_for_timeout(5000)

    # Print details
    print("Page Title:")
    print(page.title())

    print("\nCurrent URL:")
    print(page.url)

    # Keep browser open for few seconds
    time.sleep(10)

    # Close browser
    browser.close()