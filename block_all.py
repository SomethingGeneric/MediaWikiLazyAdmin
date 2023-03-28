import asyncio
from playwright.async_api import async_playwright
import getpass


async def run() -> None:
    # Launching the browser
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=True)
        page = await browser.new_page()

        # Navigating to the login page
        await page.goto("https://winni.wiki/index.php?title=Special:UserLogin&returnto=Special%3ABlock")

        # Entering the username and password
        await page.click("#wpName1")
        await page.fill("#wpName1", "matt")
        await page.click("#wpPassword1")
        await page.fill("#wpPassword1", getpass.getpass())

        # Clicking the login button
        await page.click("#wpLoginAttempt")

        # Navigating to the Special:Block page
        await page.goto("https://winni.wiki/index.php/Special:Block")

        # Loading the list of users from a file
        with open("user_names.txt", "r") as f:
            all_users = f.read().splitlines()

        # Entering each user into the input box
        for user in all_users:
            await page.click('//*[@id="ooui-php-1"]')
            await page.fill('//*[@id="ooui-php-1"]', user)

            await page.click('//*[@id="mw-input-wpExpiry"]/div[3]/div[2]/input')
            await page.fill('//*[@id="mw-input-wpExpiry"]/div[3]/div[2]/input', "indefinite")

            await page.keyboard.press("Enter")
            print("Blocked " + user)
            await asyncio.sleep(0.2)
            await page.goto("https://winni.wiki/index.php/Special:Block")

        # Closing the browser
        await browser.close()


asyncio.run(run())
