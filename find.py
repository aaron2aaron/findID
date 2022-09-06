import re
from playwright.sync_api import Page, expect


def test_homepage_has_Playwright_in_title_and_get_started_link_linking_to_the_intro_page(page: Page):
    page.goto("https://iforgot.apple.com/appleid")

    page.locator('[class="generic-input-field  form-textbox-input    iforgot-firstname   "]').fill("Esther")
    page.locator('[class="generic-input-field  form-textbox-input    iforgot-lastname   "]').fill("Lombogia")
    page.locator('[class="generic-input-field  form-textbox-input    email-field    form-textbox form-textbox-text "]').fill("e.lombogia@icloud.com")
    page.locator('[class="generic-input-field  form-textbox-input    captcha-input   "]').fill("e.lombogia@icloud.com")
    page.locator('[alt="Image challenge"]').screenshot(path="captcha.png")
    # create a locator
    #get_started = page.locator("text=Continue")

    # Click the get started link.
    #get_started.click()