'''
tkinter
파이썬에서 그래픽 화면을 만드는 기본 라이브러리
'''
import tkinter as tk #GUI = 그래픽 UI 사용자들이 눈으로보는 프로그램 만들기 위해 필요한 도구
#                  파일/폴더 선택 창    알림창 띄우기
from tkinter import filedialog      , messagebox
#      운영체제 기능 사용(파일, 폴더 다루기)
import os
#      파일 이동, 복사 등의 작업
import shutil
#      날짜, 시간 다루기 (여기에서는 날짜다루기는 아직 안한 상태)
from datetime import datetime
#   파일 정리 함수 만들기 시작
def organize_files():

    # 사용자에게 폴더 선택 창 띄우기, 선택한 경로를 folder 에 저장
    folder = filedialog.askdirectory(title="정리한 폴더 선택")
    # 폴더를 선택 안 했으면(취소 누름)  함수는 종료
    # .askdirectory  = 어떤 폴더 = 디렉토리를 선택할 것인지 물어보는 기능 
    if not folder: return  # 만약에 폴더를 선택하지 않았다면 return 프로그램을 종료하러 돌려보내기 처리

    # 파일 분류 기준 이미지 폴더에는 jpg png  문서 폴더에는 pdf docs txt
    categories = {
        "이미지":['.jpg','.png'], 
        '문서':['.pdf', '.docx', '.txt'], 
        '기타':{}
        }
    # 정리한 파일 개수 세기
    count = 0


    # 선택한 폴더 안의 모든 파일/폴더 이름을 하나씩 가져온다.
    for file in os.listdir(folder):
        # 폴더 경로 + 파일 이름을 합쳐서 진짜 파일인지 확인 (폴더 제외)
        if os.path.isfile(os.path.join(folder, file)):
            # ext = 파일 확장자의 줄임말 파일 확장자를 추출하여 소문자로 변환
            # .splitext(file) 현재 파일의 글자를 자르겠다. .을 기준으로 
            # .splitext(file)[0] = 파일명칭
            # .splitext(file)[1] = .을 기준으로 뒤에 존재하는 확장자 명칭
            # .확장자이름을 lower() 소문자로 변경하겠다.
            ext = os.path.splitext(file)[1].lower()
            # categories 에서 확장자에 맞는 카테고리 찾기, 없으면 기타
            # 예를 들어 .jpg 면 이미지, .pdf 이면 문서
            cat = next((k for k, v in categories.items() if ext in v), '기타')
            # 카테고리에 해당하는 폴더 만들기 
            # exist_ok=True  이미 있으면 에러 안나고 있는거 사용하겠다.
            os.makedirs(os.path.join(folder, cat), exist_ok=True)
            # 파일을 원래 현재 폴더 위치에서 우리가 분류해놓은 카테고리에 해당하는 폴더로 파일 이동시키겠다.
            #    움직이다   현재폴더에 존재하는파일을,  cat고리로 분류해놓은 폴더 위치에
            shutil.move(os.path.join(folder, file), os.path.join(folder, cat, file))
            # 정리한 파일 개수 1 중가
            count += 1
    # 파일을 정리하고 나서 메세지 창으로 몇 개의 파일 정리했는지 확인
    messagebox.showinfo("완료", f"{count}개 파일 정리 완료")


# 1. 윈도우 창 만들기
root = tk.Tk()
root.title("내 프로그램") # 제목
root.geometry("400x300") # 크기(가로x세로)

# 2. 위젯(버튼, 라벨 등) 추가
#                                     폰트 스타일      크기 두께       폰트를 기준으로 y = 위 아래 세로 20씩 여백 설정 padding 세로 위 아래 20 씩 
tk.Label(root, text="파일 자동 정리", font=("맑은 고딕", 16, "bold")).pack(pady=20)
tk.Button(root, text="파일  정리 시작", command=organize_files,
          bg="#4caf50", fg='white', width=20, height=2).pack(pady=10)
# bg = 배경색   fg = 글자색

# 설명 글씨
tk.Label(root, text='폴더를 선택하면 자동으로 파일을 분류합니다.', font=("맑은고딕", 9)).pack(pady=10)
# 3. 프로그램 실행 (창이 닫힐 때 까지 대기)
root.mainloop()


'''
pyinstaller = python 파일(.py)을 실행파일(.exe) 로 바꿔주는 도구

문제 : python 이 없는 컴퓨터는 .py 파일 실행 안됨 -> 파이썬 언어부터 설치
해결 : .exe 파일로 만들면 어디서든 파이썬 언어가 없어도 실행 가능

.spec 파일
exe 파일을 만드는 설계도 or 레시피
.spec 
-> 어떤 파일을 포함할 것이고,
-> 어떤 설정으로 만들 것이고,
-> 아이콘은 뭘 사용할 것이고,
-> 콘솔창을 보일지 말지 작성한 스펙

마지막으로 spec 파일을 읽어서 스펙이 나열된대로 EXE 파일 제작

내 폴더/
   파이썬파일.py
   파이썬파일.spec
   build/           중간 작업 파일  다 만들고 나면 삭제해도 문제 없음
   dist/            최종 결과물이 들어있는 폴더
     파이썬파일.exe

pip install pyinstaller

pyinstaller --onefile 파이썬파일이름.py

현재 폴더에서 파이썬파일이름.spec 파일생성
pyinstaller 파이썬파일이름.spec  실행하면

dist 폴더 내에

파이썬파일이름.exe 실행

프로그램 하나 생성
pyinstaller --onefile  --noconsole  --icon=icon.ico 파이썬파이름.py
pyinstaller     --옵션들
--onefile       하나의 EXE 파일로 만들기
--noconsole     검은 콘솔창 뒤에 안보이고 GUI 파일만 띄우기
--windowed      --noconsole 같은 옵션
--name          EXE 파일 이름 지정 (파이썬 파일 이름과 같게 생성하고 싶지 않을 때, 처음부터 이름 다르게 생성하고 싶을 때)
--icon=icon.ico 아이콘변경
--add-data      추가 파일 포함

icon 을 변경하는 icon.ico 는 pyinstaller 를 실행하는 폴더 위치에 아이콘 파일도 있어야지, 해당 아이콘 모형으로 생성

pyinstaller --onefile  --noconsole  --icon=icon.ico 파일이름.py
'''