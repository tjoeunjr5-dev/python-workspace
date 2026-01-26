import os
import json
import requests
from playwright.sync_api import sync_playwright
import time

SEARCH_KEYWORD = "강아지"
IMAGE_DIR = f"google_images_{SEARCH_KEYWORD}"
JSON_FILE = f"google_{SEARCH_KEYWORD}_images.json"

os.makedirs(IMAGE_DIR, exist_ok=True)

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
    "Referer": "https://www.google.com/"
}

def download_image(url, path):
    try:
        r = requests.get(url, headers=HEADERS, timeout=15)
        if r.status_code == 200 and len(r.content) > 1000:  # 최소 1KB 이상
            with open(path, "wb") as f:
                f.write(r.content)
            return True
    except Exception as e:
        print(f"  ⚠️ 다운로드 실패: {str(e)[:50]}")
    return False

images_data = []

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context(
        locale="ko-KR",
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    )
    page = context.new_page()

    # 구글 이미지 검색 URL
    search_url = f"https://www.google.com/search?q={SEARCH_KEYWORD}&tbm=isch"
    
    print(f"'{SEARCH_KEYWORD}' 이미지 검색 중...")
    page.goto(search_url, timeout=60000)
    page.wait_for_timeout(3000)

    max_images = 30  # 다운로드할 이미지 개수
    count = 0
    clicked_count = 0

    print(f"\n이미지 수집 시작 (목표: {max_images}개)\n")

    while count < max_images:
        try:
            # 현재 페이지의 모든 이미지 썸네일 찾기
            thumbnails = page.locator('img[jsname]').all()
            
            if clicked_count >= len(thumbnails):
                print("\n모든 이미지를 확인했습니다. 다음 페이지로 이동...")
                
                # "결과 더보기" 또는 다음 페이지 버튼 찾기
                try:
                    more_button = page.locator('input[value="결과 더보기"], input[type="button"]').first
                    if more_button.is_visible():
                        more_button.click()
                        page.wait_for_timeout(3000)
                        clicked_count = 0
                        continue
                except:
                    pass
                
                # 스크롤을 시도
                page.evaluate("window.scrollBy(0, 1000)")
                page.wait_for_timeout(2000)
                
                new_thumbnails = page.locator('img[jsname]').all()
                if len(new_thumbnails) == len(thumbnails):
                    print("더 이상 이미지가 없습니다.")
                    break
                
                continue

            # 현재 썸네일 클릭
            thumbnail = thumbnails[clicked_count]
            clicked_count += 1

            try:
                # 썸네일 클릭
                thumbnail.click()
                page.wait_for_timeout(1500)

                # 큰 이미지 찾기 (여러 선택자 시도)
                large_img = None
                
                # 시도 1: img[jsname="kn3ccd"]
                try:
                    large_img = page.locator('img[jsname="kn3ccd"]').first
                    if large_img.is_visible():
                        img_url = large_img.get_attribute("src")
                except:
                    pass

                # 시도 2: .sFlh5c.pT0Scc.iPVvYb
                if not img_url or img_url.startswith("data:"):
                    try:
                        large_img = page.locator('.sFlh5c.pT0Scc.iPVvYb').first
                        if large_img.is_visible():
                            img_url = large_img.get_attribute("src")
                    except:
                        pass

                # 시도 3: 일반 큰 이미지
                if not img_url or img_url.startswith("data:"):
                    try:
                        large_img = page.locator('img.iPVvYb, img.n3VNCb').first
                        if large_img.is_visible():
                            img_url = large_img.get_attribute("src")
                    except:
                        pass

                # URL 검증
                if not img_url or img_url.startswith("data:") or "base64" in img_url:
                    print(f"[{clicked_count}] 유효하지 않은 이미지 - 건너뜀")
                    continue

                # 파일 확장자 결정
                ext = "jpg"
                if "." in img_url.split("?")[0]:
                    url_ext = img_url.split("?")[0].split(".")[-1].lower()
                    if url_ext in ["jpg", "jpeg", "png", "gif", "webp"]:
                        ext = url_ext

                img_name = f"{SEARCH_KEYWORD}_{str(count+1).zfill(3)}.{ext}"
                img_path = os.path.join(IMAGE_DIR, img_name)

                print(f"[{count+1}/{max_images}] 다운로드: {img_name}")
                
                if download_image(img_url, img_path):
                    images_data.append({
                        "index": count + 1,
                        "filename": img_name,
                        "url": img_url
                    })
                    count += 1
                    print(f"             ✅ 성공\n")
                else:
                    print(f"             ❌ 실패\n")

            except Exception as e:
                print(f"이미지 {clicked_count} 처리 실패: {str(e)[:80]}\n")
                continue

        except Exception as e:
            print(f"오류 발생: {e}")
            break

    browser.close()

# JSON 파일로 저장
with open(JSON_FILE, "w", encoding="utf-8") as f:
    json.dump(images_data, f, ensure_ascii=False, indent=2)

print(f"{'='*60}")
print(f"✅ 크롤링 완료!")
print(f"📊 다운로드된 이미지: {len(images_data)}개")
print(f"📁 이미지 폴더: {IMAGE_DIR}/")
print(f"📄 이미지 정보: {JSON_FILE}")
print(f"{'='*60}")