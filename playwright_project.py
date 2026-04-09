from playwright.sync_api import sync_playwright

def get_news():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=200)
        page = browser.new_page()

        try:
            # Open Bing News directly
            page.goto("https://www.bing.com/news/search?q=SA+vs+AUS+update", timeout=60000)

            # Wait for news titles
            page.wait_for_selector("a.title", timeout=20000)

            print("\n🔍 Latest SA vs AUS News:\n")

            results = page.locator("a.title")
            count = results.count()

            for i in range(min(count, 10)):
                title = results.nth(i).inner_text()
                link = results.nth(i).get_attribute("href")

                print(f"{i+1}. {title}")
                print(f"   {link}\n")

        except Exception as e:
            print("❌ Error occurred:", e)
            page.screenshot(path="error_debug.png")
            print("📸 Screenshot saved as error_debug.png")

        finally:
            browser.close()


if __name__ == "__main__":
    get_news()