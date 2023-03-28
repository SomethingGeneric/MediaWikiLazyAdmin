import asyncio
from playwright.async_api import async_playwright

import getpass

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()

        # Login to the website
        await page.goto('https://winni.wiki/index.php?title=Special:UserLogin&returnto=Special%3ANukeDPL')
        await page.fill('#wpName1', 'matt')
        await page.fill('#wpPassword1', getpass.getpass())
        await page.click('#wpLoginAttempt')

        while True:
            # Navigate to the desired URL and interact with the elements
            await page.goto('https://winni.wiki/index.php/Special:NukeDPL')
            await page.fill('textarea[name="query"]', 'notmodifiedby = matt')
            await page.click('input[type="submit"]')
            await asyncio.sleep(0.5)

asyncio.run(main())
