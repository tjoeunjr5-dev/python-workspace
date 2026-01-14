'''
28_이미지글자읽기의 Docstring

https://github.com/UB-Mannheim/tesseract/wiki
다운로드 받기
tesseract-ocr-w64-setup-5.5.0.20241111.exe (64 bit)
Tesseract 
'''
import pytesseract
from PIL import Image
# C:/Program Files/Tesseract-OCR/tesseract.exe -> 사용

def 에러코드():
    text = pytesseract.image_to_string(Image.open("wrt.jpg"), lang='kor+eng')
    print(text)
def tess활용코드():
    # 1. 설치한 tesseract 파일 활용방법
    # 직접적으로 tesseract.exe 파일이 설치된 모든 경로를 작성한다.

    # 2. 시스템 환경 변수에 C:/Program Files/Tesseract-OCR/ 파일 폴더 위치까지 추가하여
    # 다음부터는 C:/Program Files/Tesseract-OCR/ 경로는 생략한다.
    pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'
    '''
    image_to_string(오픈할 이미지 이름.확장자이름,언어설정="add 에서 추가한 모든 언어")
    image_to_string(오픈할 이미지 이름.확장자이름,언어설정="kor+eng+dnk")
                         이미지에서 추측하여 추출할 수 있는 언어  한국어+영어+덴마크
                         와 같이 +로 이어 작성
    이미지 글자를 추출할 경우 이미지를 직접적으로 넣으면 이미지 글자가 제대로 나오지 않음
    이미지 전처리(결과를 보기위해 전부처리한다.) 작업을 통하여 정확도 올림
    -> 이미지 전처리할 시간이나 지식이 존재하지 않을경우
    시간을 투자하거나, GPT와 같은 AI에 대가를 지불하여 연결한 후, 
    이미지에 존재하는 글자 데이터를 추출할 수 있다.
    '''
    text = pytesseract.image_to_string(Image.open("wrt.jpg"), lang='kor')
    print(text)

tess활용코드()