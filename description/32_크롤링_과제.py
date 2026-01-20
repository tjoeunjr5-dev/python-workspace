import os
import json
import requests
from playwright.sync_api import sync_playwright

URL = "도메인주소"
IMAGE_DIR = "product_images"
JSON_FILE = "products.json"

os.makedirs(IMAGE_DIR, exist_ok=True)

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

def download_image(url, path):
    r = requests.get(url, headers=HEADERS, timeout=15)
    with open(path, "wb") as f:
        f.write(r.content)

products = []

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    context = browser.new_context(locale="ko-KR")
    page = context.new_page()

    page.goto(URL, timeout=60000)
    page.wait_for_timeout(4000)

    # 스크롤 (필수)
    for _ in range(5):
        page.mouse.wheel(0, 3000)
        page.wait_for_timeout(2000)

    # 🔥 최신 Amazon 상품 카드
    cards = page.locator("div.puis-card-container")
    count = cards.count()

    print("상품 수:", count)

    for i in range(count):
        card = cards.nth(i)

        # ======================
        # 상품명
        # ======================
        title = None
        title_el = card.locator("h2 > span")
        if title_el.count() > 0:
            title = title_el.first.text_content().strip()

        # ======================
        # 가격
        # ======================
        price = None
        price_el = card.locator("span.a-price-whole")
        if price_el.count() > 0:
            price = price_el.first.text_content().replace(",", "").strip()

        # ======================
        # 이미지
        # ======================
        img_url = None
        img_el = card.locator("img.s-image")
        if img_el.count() > 0:
            img_url = img_el.first.get_attribute("src")

        if not title or not price or not img_url:
            continue

        ext = img_url.split("?")[0].split(".")[-1]
        img_name = f"img_{len(products)+1}.{ext}"
        img_path = os.path.join(IMAGE_DIR, img_name)

        download_image(img_url, img_path)

        products.append({
            "product_name": title,
            "price": price,
            "image_file": img_name
        })

    browser.close()

with open(JSON_FILE, "w", encoding="utf-8") as f:
    json.dump(products, f, ensure_ascii=False, indent=2)

print("완료 ✅", len(products), "개 저장")
