'''
.set~~  생성기능

.get~~ 생성되어진 무언가의 데이터를 가져오는 기능

'''
# 가져오기 zipfile.py  os.py  random.py  string.py
import zipfile, os, random, string
def 비밀번호압축고전():
    문자들 = string.digits
    비밀번호 = "".join(random.choice(문자들) for _ in range(4))
    print(f"생성된 비밀번호 : {비밀번호}")

    with zipfile.ZipFile('password1.zip', 'w') as my_zip:
        # my_zip.setpassword(비밀번호.encode())
        for file in os.listdir():
            if file.endswith('.txt'): #.text 라는 확장자는 존재하지 않는다.
                my_zip.write(file, compress_type=zipfile.ZIP_DEFLATED)
                my_zip.setpassword(비밀번호.encode())
                print(f"{file} 압축완료")

# zipfile -> 압축 하기 할 때 굉장히 예전 사용 많이하던 파이썬 인기 모듈이었지만
# 시대가 변하며... 성장했으나 이에 zipfile 모듈이 따라오지 못하여 현재는 주로 압축 풀기용 많이 사용됨
# 업그레이드 버전으로 pyminizip 이라는 모듈이 흥행

'''
현재 우리의 컴퓨터에는 C++ 언어가 없음
pyminizip -> C++  + python 조합으로 이루어진 모듈
컴퓨터에 C관련 언어를 설치 후 사용 가능
pip install pyminizip

pip install pyzipper

    # 비밀번호 생성
    # 현재 폴더에서 png 확장자를 찾은 후 
    # zip 파일에 넣고 비밀번호를 강력히 설정
'''
import pyzipper
'''
AES = 비밀번호로 자물쇠 거는 잠금 방식
현재 표준으로 사용되는 암호화 방식
일반 zipfile 허술한 다이얼 자물쇠
  AESzipfile 은행 금고급 자물쇠
비밀번호는 같아 보여도 자물쇠 내부 구조 다름
AES = 은행 앱, 카카오톡 , Wifi 정부 기업 보안 믿고 사용하는 표준 암호
AES-128 -192 -256 중에서 AES-256 거의 철벽


pyzipper.AESZipFile = pyzipper.py 내부에 .AESZipFile() 메서드 기능이 작성되어 있다.
.AESZipFile() = AES-256암호화해서 압축한 파일

compression=pyzipper.ZIP_DEFLATED,
compression = 파일을 ZIP에 넣을 때 압축 방식 지정
.ZIP_DEFLATED = 가장 널리 쓰이는 표준 압축 알고리즘 압축률 / 속도 균형 좋음
7zip. WinRAR, windows 기본 압축 모두 지원

encryption = ZIP파일의 암호화 방식 지정(암호화 영어단어)
.WZ_AES    = WinZip AES 암호화 규격
현재 ZIP에서 가장 안전한 방식
대부분의 압축 프로그램 지원

안쓰면 어떻게 되는가.. -> 현대 암호 기준에서 구식으로 암호화가 안되거나 (=암호하는 값어치가 없기 때문 ..)

encryption=pyzipper.WZ_AES
'''
def 비밀번호압축_최신() : 
    with pyzipper.AESZipFile(
        'pyZipperPassword.zip',            # 압축 상자 이름.종류                           압축_파일_이름.압축파일형식
        'w',                               # 압축 상자에 물건을 담겠다                     압축파일 만들겠다. = write
        compression=pyzipper.ZIP_DEFLATED, # 압축할 때 압축잘되는가? 속도는? -> 정도껏 ^^    파일을 ZIP에 넣을 때 압축 방식 지정 압축률 / 속도 무난한 방법을 사용
        encryption=pyzipper.WZ_AES         # 단단한 자물쇠로 잠글 것                        ZIP 파일의 암호화 방식을 지정 
    ) as zf:                               # 위 세팅을 대신 축소에서 사용할 변수이름          이렇게 설정한 형식을 zf 라는 변수이름으로 사용하겠다.
        zf.setpassword(b'hiPassword')      # 자물쇠 비밀번호 세팅                           비밀번호 설정 반드시 b = byte 타입으로 비밀번호 생성
        #zf.write('test.txt')
        zf.write('내정보.png')              # 담을 파일 넣기                                 txt라는 파일을만드는 것이 아니라 현재 폴더에서 존재하는 파일을 zip 추가

'''
AES 잠금이 가능한 상자               상자에 쓰이는 자물쇠 종류
pyzipper.AESZipFile()        vs        pyzipper.WZ_AES
ZIP 파일을 만들고                이 ZIP 상자를 AES 방식으로 잠그자
열고                            이 가방에 은행 금고 자물쇠 달아라
파일을 넣고 빼는 그릇 상자          만약에 이 속성을 설정하지 않으면?! -> 비밀번호 없는 ZIP 이되거나 약한 옛날 암호화가 됨


b = byte  사람이 작성한 비밀번호를 컴퓨터가 이해하는 글자 조각으로 변환하여 비밀번호를 설정

사람이 작성한 비밀번호 : myPassword
컴퓨터가 입력하는 비밀번호 : 109 121 112 97 115 115 119 111 이런식으로 숫자처리되어 비밀번호 생성

AES 암호화가 숫자만 계산
'''
# 비밀번호압축_최신()


# 랜덤 비밀번호를 생성해서 압축
# 압축 비밀번호 풀기
# 보통 import는 맨 위에 모두 작성
import random, string

def 비밀번호압축_최신_랜덤():
    문자열 = string.ascii_letters + string.digits
    비밀번호 = "".join(random.choice(문자열) for _ in range(7))
    print(f"생성된 비밀번호 : {비밀번호}")

    with pyzipper.AESZipFile(
        '랜덤비밀번호파일.zip',
        'w',
        compression=pyzipper.ZIP_DEFLATED,
        encryption=pyzipper.WZ_AES
    ) as zf:
        zf.setpassword(비밀번호.encode())
        # zf.setpassword(b'hiPassword')
        zf.write('내정보.png')
# 비밀번호압축_최신_랜덤()

# 특수문자를 포함하여 압축 파일 비밀번호 랜덤 생성
# 비밀번호압축_최신_랜덤_특수문자포함


import glob
def png파일모두압축하기():
    문자열 = string.ascii_letters + string.digits
    비밀번호 = "".join(random.choice(문자열) for _ in range(7))
    print(f"생성된 비밀번호 : {비밀번호}")

    with pyzipper.AESZipFile(
        '랜덤비밀번호파일.zip',
        'w',
        compression=pyzipper.ZIP_DEFLATED,
        encryption=pyzipper.WZ_AES
    ) as zf:
        zf.setpassword(비밀번호.encode())
        # zf.setpassword(b'hiPassword')

        for 파일 in glob.glob("*.png"):
            zf.write(파일)
        
png파일모두압축하기()


'''
목적은 같으나.. 방식이 다른 두 가지 방법

      비밀번호.encode()               vs      b'hiPassword'
         encode()                          비밀번호가 고정일 때 사용
         비밀번호가                       
    변수(랜덤/입력값)일 때
           사용 

    소비자가 입력하거나 랜덤으로 출력되는       고정적인 비밀번호니까
    비밀번호를 모두 확보한 다음에              이미 비밀번호 완성 끝난거잖습니까?
    .encode() 컴퓨터가 이해할 수 있는         바로 비밀번호 컴퓨터가 이해할 수 있는
    글자 방식으로 변환할거야                   글자 방식으로 변환하시죠 ^^
    둘 다 결과는 byte 형태로 변환

    컴퓨터에게 소비자가 입력하거나 랜덤으로 입력되어 컴퓨터가 예측할 수 없는 데이터를 가져온다.
    컴퓨터에게 코드를 실행하며 미리 확보한 문자 비밀번호를 사용하겠다.

glob.glob("*.png")            vs           if file.endswith(".png")
오직 파일 찾기 전용                          파일 이외 폴더까지 모두 찾기
if 보다 빠르고 깔끔                          모두 섬세하게 찾는만큼 glob 보다 느림
'''