'''
번역에서 가장 원조
rc1 정식으로 버전을 내기 전에 테스트 버전으로 사용
Google Translate API를 무료로 사용해서 번역 가능
2020년에 개발 중단 == 3.9
Python3.12 에서는 심하게 불안정
최신 파이썬에서는 사용을 잘 하지 않음
구글에서 유로로 만든 버전을이용하면 안정적이고 편안하게 최신 버전에서도 이용 가능하다~^^
pip install googletrans==4.0.0-rc1

튀니지 출신 엔지니어가 googletrans 가 불안정해지자, 더 안정적이고 다양한 번역 서비스를 지원하는 라이브러리 개발
누구나 소스코드를 보고 기여할 수 있도록 코드를 오픈
라이브러리 : 특정 기능에 특화된 도구 모음
pip install deep-translator


구글이 개발을 중단하여 기존에 구글에서 개발하던 googletrans 복사하여 만든 복사본 구글에서 만든 것이 아님
deep-translator 보다 안정적이지는 않음
pip install googletrans-py

Successfully installed 가 뜨면 무사히 설치 완료!
'''

# deep_translator 깊이있는 번역 라이브러리(도구모음)에서 GoogleTranslator 라는 도구를 활용하여 번역을 진행하겠다.
from deep_translator import GoogleTranslator

text = "HELLO world"
결과 = GoogleTranslator(source='en', target='ja').translate(text)
print(결과)

text1 = "안녕하세요."
결과2 = GoogleTranslator(source='auto', target='en').translate(text1)
print(결과2)

'''

GoogleTranslator().translate()
구글번역기능()
  .           내부에 존재하는 기능들 중에서
  translate() 라는 기능을사용하겠다.


  .기능명칭() = 특정 변수나, 특정 기능에서만 사용되는 기능

GoogleTranslator() 기능 내부에서 translate() 기능이 정의되었으며, 
GoogleTranslator().translate() = 구글번역기능 내부에 존재하는 translate() 기능을 사용하겠다.



GoogleTranslator(          source='대소문자 상관없음'    , target='대소문자 상관없음'   ).translate('문장')
구글번역기같은기능이다(원래 문장은 ㅇㅇ 나라 언어로 되어있고, ㅇㅇ 나라 언어로 변경할 것이다.).변환기능('언어 변경할 문장') 을 이용해서 변환하겠다.

source = 'auto' 사용 가능
           auto 문장을 보고 어떤 나라의 언어인지 언어를 알아서 감지하겠다.


                 원본언어      목표언어    번역실행기능("번역할문장" )
GoogleTranslator(source='en', target='ja).translate("번역될문자열")


'''