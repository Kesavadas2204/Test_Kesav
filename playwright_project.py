from playwright.sync_api import sync_playwright

def scrape_amazon():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)  # set False if you want to see browser
        page = browser.new_page()

        try:
            # Open Amazon India
            page.goto("https://www.amazon.in", timeout=60000)

            # Wait for page to load
            page.wait_for_load_state("domcontentloaded")

            # Optional: wait for main content
            page.wait_for_selector("body", timeout=15000)

            # Get full visible text content
            content = page.inner_text("body")

            # Save to file
            with open("amazon_content.txt", "w", encoding="utf-8") as f:
                f.write(content)

            print("✅ Content saved to amazon_content.txt")

        except Exception as e:
            print("❌ Error:", e)
            page.screenshot(path="amazon_error.png")
            print("📸 Screenshot saved as amazon_error.png")

        finally:
            browser.close()


if __name__ == "__main__":
    scrape_amazon()
    