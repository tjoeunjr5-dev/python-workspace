'''
자동화 + 폴더 용량 분석 하는 기능을

하나의 exe 파일로 생성하기

'''

'''
파일 관리 종합 프로그램
1. 파일 자동 정리
2. 폴더 용량 분석
'''
import tkinter as tk
from tkinter import filedialog, messagebox
import os
import shutil

# ========== 파일 자동 정리 기능 ==========
def organize_files():
    """파일을 확장자별로 자동 분류하는 함수"""
    # 사용자에게 폴더 선택 창 띄우기
    folder = filedialog.askdirectory(title="정리할 폴더 선택")
    
    # 폴더를 선택 안 했으면 함수 종료
    if not folder:
        return
    
    # 파일 분류 기준
    categories = {
        "이미지": ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg'],
        "문서": ['.pdf', '.docx', '.txt', '.xlsx', '.pptx', '.doc'],
        "비디오": ['.mp4', '.avi', '.mkv', '.mov'],
        "음악": ['.mp3', '.wav', '.flac'],
        "압축파일": ['.zip', '.rar', '.7z'],
        "기타": []
    }
    
    # 정리한 파일 개수 세기
    count = 0
    
    try:
        # 선택한 폴더 안의 모든 파일/폴더 이름을 하나씩 가져온다
        for file in os.listdir(folder):
            file_path = os.path.join(folder, file)
            
            # 폴더는 제외하고 파일만 처리
            if os.path.isfile(file_path):
                # 파일 확장자 추출 (소문자로 변환)
                ext = os.path.splitext(file)[1].lower()
                
                # 확장자에 맞는 카테고리 찾기
                cat = next((k for k, v in categories.items() if ext in v), '기타')
                
                # 카테고리 폴더 생성
                cat_folder = os.path.join(folder, cat)
                os.makedirs(cat_folder, exist_ok=True)
                
                # 파일 이동
                dest_path = os.path.join(cat_folder, file)
                
                # 같은 이름의 파일이 있으면 이름 변경
                if os.path.exists(dest_path):
                    base, extension = os.path.splitext(file)
                    counter = 1
                    while os.path.exists(dest_path):
                        new_name = f"{base}_{counter}{extension}"
                        dest_path = os.path.join(cat_folder, new_name)
                        counter += 1
                
                shutil.move(file_path, dest_path)
                count += 1
        
        # 완료 메시지
        messagebox.showinfo("완료", f"✅ {count}개 파일 정리 완료!")
        
    except Exception as e:
        messagebox.showerror("오류", f"파일 정리 중 오류 발생:\n{str(e)}")


# ========== 폴더 용량 분석 기능 ==========
def analyze_folder():
    """폴더의 전체 용량과 파일 개수를 분석하는 함수"""
    # 사용자에게 폴더 선택 창 띄우기
    folder = filedialog.askdirectory(title='분석할 폴더 선택')
    
    # 폴더를 선택 안 했으면 함수 종료
    if not folder:
        return
    
    # 전체 파일 용량 합계
    total_size = 0
    # 파일 개수
    file_count = 0
    
    try:
        # 선택한 폴더의 모든 하위 폴더까지 탐색
        for dirpath, dirnames, filenames in os.walk(folder):
            for f in filenames:
                # 파일 전체 경로
                fp = os.path.join(dirpath, f)
                
                # 파일이 실제로 존재하는지 확인 (심볼릭 링크 등 예외 처리)
                if os.path.exists(fp):
                    # 파일 크기 누적
                    total_size += os.path.getsize(fp)
                    # 파일 개수 증가
                    file_count += 1
        
        # 바이트를 MB로 변환
        size_mb = total_size / (1024 * 1024)
        
        # GB 단위도 표시 (1GB 이상일 경우)
        if size_mb >= 1024:
            size_gb = size_mb / 1024
            size_text = f"{size_gb:.2f} GB ({size_mb:.2f} MB)"
        else:
            size_text = f"{size_mb:.2f} MB"
        
        # 결과 알림창
        messagebox.showinfo(
            "분석 결과",
            f"📊 폴더 용량 분석 완료\n\n"
            f"📁 폴더: {os.path.basename(folder)}\n"
            f"📄 파일 개수: {file_count:,}개\n"
            f"💾 총 용량: {size_text}"
        )
        
    except Exception as e:
        messagebox.showerror("오류", f"폴더 분석 중 오류 발생:\n{str(e)}")


# ========== GUI 메인 윈도우 생성 ==========
def create_main_window():
    """메인 윈도우를 생성하고 설정하는 함수"""
    root = tk.Tk()
    root.title("파일 관리 종합 프로그램")
    root.geometry("450x400")
    root.resizable(False, False)
    
    # 배경색 설정
    root.configure(bg="#f0f0f0")
    
    # ===== 제목 =====
    title_frame = tk.Frame(root, bg="#2196F3", height=80)
    title_frame.pack(fill=tk.X)
    title_frame.pack_propagate(False)
    
    tk.Label(
        title_frame,
        text="🗂️ 파일 관리 종합 프로그램",
        font=("맑은 고딕", 18, "bold"),
        bg="#2196F3",
        fg="white"
    ).pack(expand=True)
    
    # ===== 설명 =====
    tk.Label(
        root,
        text="원하는 기능을 선택하세요",
        font=("맑은 고딕", 11),
        bg="#f0f0f0",
        fg="#555"
    ).pack(pady=20)
    
    # ===== 버튼 프레임 =====
    button_frame = tk.Frame(root, bg="#f0f0f0")
    button_frame.pack(pady=10)
    
    # 버튼 1: 파일 자동 정리
    btn1 = tk.Button(
        button_frame,
        text="📁 파일 자동 정리",
        command=organize_files,
        font=("맑은 고딕", 12, "bold"),
        bg="#4CAF50",
        fg="white",
        width=25,
        height=3,
        relief=tk.RAISED,
        bd=3,
        cursor="hand2"
    )
    btn1.pack(pady=10)
    
    # 버튼 설명 1
    tk.Label(
        button_frame,
        text="폴더 안의 파일을 확장자별로 자동 분류합니다",
        font=("맑은 고딕", 9),
        bg="#f0f0f0",
        fg="#666"
    ).pack()
    
    # 구분선
    separator = tk.Frame(button_frame, height=2, bg="#ddd")
    separator.pack(fill=tk.X, pady=15, padx=30)
    
    # 버튼 2: 폴더 용량 분석
    btn2 = tk.Button(
        button_frame,
        text="📊 폴더 용량 분석",
        command=analyze_folder,
        font=("맑은 고딕", 12, "bold"),
        bg="#673AB7",
        fg="white",
        width=25,
        height=3,
        relief=tk.RAISED,
        bd=3,
        cursor="hand2"
    )
    btn2.pack(pady=10)
    
    # 버튼 설명 2
    tk.Label(
        button_frame,
        text="폴더의 전체 용량과 파일 개수를 분석합니다",
        font=("맑은 고딕", 9),
        bg="#f0f0f0",
        fg="#666"
    ).pack()
    
    # ===== 하단 정보 =====
    footer_frame = tk.Frame(root, bg="#f0f0f0")
    footer_frame.pack(side=tk.BOTTOM, pady=10)
    
    tk.Label(
        footer_frame,
        text="v1.0 | 파일 관리 도우미",
        font=("맑은 고딕", 8),
        bg="#f0f0f0",
        fg="#999"
    ).pack()
    
    # 윈도우 실행
    root.mainloop()


# ========== 프로그램 실행 ==========
if __name__ == "__main__":
    create_main_window()