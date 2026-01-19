# app.py
from flask import Flask, render_template

app = Flask(__name__)

# 메인 페이지
@app.route("/")
def home():
    return render_template("index.html")

# 연구 분야
#   <li><a href="/research">연구분야</a></li>
# templates 내부 폴더에 존재하는 research.html 파일 명칭 동일
@app.route("/research")
def research():
    researches = [
        {"title": "인공지능", "desc": "딥러닝 및 머신러닝 연구", "icon": "🤖"},
        {"title": "데이터 분석", "desc": "빅데이터 처리 및 분석", "icon": "📊"},
        {"title": "컴퓨터 비전", "desc": "이미지 인식 및 처리", "icon": "👁️"}
    ]
    return render_template("research.html", researches=researches)

# 연구원
@app.route("/members")
def members():
    professor = {"name": "홍길동", "position": "교수", "email": "hong@university.ac.kr"}
    
    students = [
        {"name": "김철수", "position": "박사과정", "research": "AI"},
        {"name": "이영희", "position": "석사과정", "research": "데이터분석"},
        {"name": "박민수", "position": "학부연구생", "research": "컴퓨터비전"}
    ]
    return render_template("members.html", professor=professor, students=students)

# 논문/성과
@app.route("/publications")
def publications():
    papers = [
        {"title": "딥러닝을 활용한 이미지 분류", "year": "2024", "journal": "AI Journal"},
        {"title": "빅데이터 분석 프레임워크", "year": "2023", "journal": "Data Science"},
        {"title": "컴퓨터 비전 알고리즘 개선", "year": "2023", "journal": "CV Conference"}
    ]
    return render_template("publications.html", papers=papers)

# 연락처
@app.route("/contact")
def contact():
    info = {
        "lab": "AI 연구실",
        "address": "서울시 강남구 대학로 123",
        "phone": "02-1234-5678",
        "email": "lab@university.ac.kr"
    }
    return render_template("contact.html", info=info)

if __name__ == "__main__":
    app.run(debug=True)