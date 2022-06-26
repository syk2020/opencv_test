import csv
import asyncio
from playwright.async_api import async_playwright

async def make_screenshots(url, label, num):
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto(url)
        # print(await page.title())
        # 読み込み不十分なまま参照しているため、待ち時間を発生させる
        await page.wait_for_timeout(5000)
        path = f'{label}_{num}.png'
        await page.screenshot(path=f'./playwright_test/ss/{path}')
        await browser.close()

def main():
    with open('./playwright_test/restaurantANDhospital.csv') as f:
        reader = csv.reader(f)

        for i, row in enumerate(reader):
            asyncio.run(make_screenshots(row[0], row[1], i+1))

if __name__ == '__main__':
    main()