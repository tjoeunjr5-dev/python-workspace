from playwright.sync_api import sync_playwright
from wordcloud import WordCloud
from matplotlib import font_manager, rc
import time
import matplotlib.pyplot as plt
def get_comments_from_community(keyword: str):
    comments = []
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        # 예: 네이버 뉴스 댓글 (실제로는 해당 사이트 구조에 맞게 수정)
        page.goto(f"https://search.naver.com/search.naver?query={keyword}")
        # ... 댓글 영역으로 이동, 스크롤하며 수집 ...
        
        # 또는 DC인사이드 마이너 갤러리 예시
        # page.goto(f"https://gall.dcinside.com/mgallery/board/lists?id={keyword}")
        
        # 댓글 텍스트 수집 로직 (실제 selector는 사이트마다 다름)
        comment_elements = page.query_selector_all(".comment-content")  # 가상 selector
        for el in comment_elements:
            comments.append(el.inner_text().strip())
            
        browser.close()
    return " ".join(comments)

# 2단계: 워드클라우드
text = get_comments_from_community("인공지능")   # ← 여기 원하는 키워드

# 1. 폰트 경로를 절대 경로로 지정 (이게 제일 안전)
font_path = r'C:/Windows/Fonts/malgun.ttf'

# 2. matplotlib에 한글 폰트 적용 (한글 깨짐 방지)
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)
# 현재 웹사이트마다 돌아서 받은 데이터를 텍스트 내부에 넣고, 
# 조회한데이터를 텍스트 기반으로 출력
# 3. 워드클라우드 생성
wc = WordCloud(
    font_path=font_path,
    width=800,
    height=800,
    background_color="white",
    max_font_size=300,
    min_font_size=10,
    colormap="viridis"
).generate(text)

plt.figure(figsize=(12, 12))
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.show()