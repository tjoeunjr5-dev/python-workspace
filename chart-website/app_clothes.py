from flask import Flask, render_template
from currency_converter import CurrencyConverter
import requests

app = Flask(__name__)

# 환율 변환기 (전역으로 1번만 생성)
cc = CurrencyConverter() # 실습으로 진행했었던 환율 변환 기능

@app.route("/")
def home():
    # Fake Store API에서 상품 가져오기
    # 가짜 데이터를 제공하는 주소
    # https://fakestoreapi.com/products
    # 개발자들이 쇼핑몰 전반적인 형태나 코드 연습을 할 때
    # 가짜 데이터를 호출해 쓸 수 있도록 만든 무료 서비스
    # keikaavousi 제작-> 코드 공개
    # 코드를 공개할테니 함께 재능기부하여 데이터를 사용할 수 있는
    # 이 웹사이트를 발전시킵시다! 취지로 오픈 소스로 운영되고 있다.
    # 제공 데이터 상품 / 장바구니 / 사용자 / 로그인 인증 등 제공

    #      우리가요청한것을.가져올 것이다.("어디서 = 어느사이트에서 = API에서") 
    response = requests.get("https://fakestoreapi.com/products")
    # 문자열 형태가 아니라
    # .json() 키명칭 = 데이터 형식으로 변환하여 사용하겠다.
    키_데이터_형식으로변환된것들 = response.json()

    변환된제품들 = []

    for 하나씩꺼내서 in 키_데이터_형식으로변환된것들:
        # 미국돈이라는 변수공간에 잠시 저장하고
        미국돈 = 하나씩꺼내서["price"] # 내부에 키이름으로 price로 되어있는 것의 데이터를
        # 미국돈을 한국돈으로 환율계산해서 변환해주는 convert변환기능을 사용해서
        # 한국돈이라는 변수공간에 저장하겠다.
        한국돈 = cc.convert(미국돈, "USD", "KRW")

        # 기존 상품 + 변환된 가격 추가
        # 하나씩꺼낸것들  price_krw 라는 키 이름에 한국돈을 round = 반올림해서 저장
        하나씩꺼내서["price_krw"] = round(한국돈)

        # 하나씩 꺼내서 변환된제품들 리스트에 저장하겠다.
        변환된제품들.append(하나씩꺼내서)

    return render_template(
        "index.html",
        #index.html에서는 변환된제품들에 담겨있는 가격들을 
        # 전부다 products 변수이름에 담아서 사용하겠다.
        products=변환된제품들
    )

@app.route("/product/<int:product_id>")
def product_detail(product_id):
    response = requests.get(f"https://fakestoreapi.com/products/{product_id}")
    product = response.json()

    product["price_krw"] = round(
        cc.convert(product["price"], "USD", "KRW")
    )

    return render_template(
        "detail.html",
        product=product
    )

@app.route("/cart")
def cart():
    return render_template("cart.html")

if __name__ == "__main__":
    app.run(debug=True)
