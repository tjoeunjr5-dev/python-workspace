'''
환율 계산할 수 있는 외부 기능을 활용해서
환율 계산 프로그램
currencyconverter

pip install currencyconverter
'''
# currency_converter 라는 외부 라이브러리에서
# CurrencyConverter  라는 도구(클래스)를 가져온다.
# 환율 계산해주는 계산기를 빌려온다.
from currency_converter import CurrencyConverter

# CurrencyConverter() : 환율을 계산해주는 기능 가져와서 사용
cc = CurrencyConverter()
# 환율 계산해주는 기능을 cc 라는 변수 공간 이름 내부에 잠시 저장

# 1달러를 한국 원화로 변환
# 환율 계산해주는 기능에는 다양한 기능이 존재
# 그 중에서 숫자 기존화폐코드 변환하여 확인할 화폐코드를 작성하여
# 환율로 변경하고자 하는 화폐의 단위를 확인
# convert와 비슷하거나 다양한 방법으로 소문자 형태의 화폐 코드도 가능하지만
# 화폐 코드의 경우 전세계 국제 표준으로 지정된 문자가 대문자이기 때문에
# 대문자를 작성하는 것이 기본 규칙
# convert() 기능 내부에서는 반드시 대문자를 사용해야 함

# 가장 표준적이고 원칙적으로 많이 사용되는 외부 기능
# 견제하는 외부 개발자나 다른 회사에서 비슷하지만 성능이 더 좋은 기능을 낼 경우에는
# 최신 환율과 대소문자 구분없이 작성 가능한 기능 제공할 것
print(f"현재 1달러는 {cc.convert(1, 'USD', 'KRW'):.2f}원 입니다.")

'''
굳이 cc 라는 명칭에 CurrencyConverter() 기능을 담아 사용하지 않고
cc.convert(1, 'USD', 'KRW'):.2f
아래와 같이 한 번에 변환하여 사용해도 좋지만
보통은 변수 공간 내부에 기능을 담아 저장된 기능에서 추가적인 기능을 추가하기 때문에
변수이름으로 많이 사용
CurrencyConverter().convert(1, 'USD', 'KRW'):.2f


CurrencyConverter()
 - 주요 기능들
 --- .convert(amount     , from_currency      , to_currency)
              변환할금액    원본 통화 코드        목표 통화 코드
 --- .currencies = 사용 가능한 통화 목록 조회 기능
 --- .bounds     = 환율 데이터의 날짜 범위를 확인 기능

 
:.2f 
 - 파이썬의 문자열 포멧팅 문법
 --- .2 소수점 이하 2자리까지 표시
 --- f(float = 소수점 = 컴퓨터의 모든 언어) 형식으로 표시

 특정 숫자나 계산한 결과에서 소수점 어디까지 보여질 것인지 개발자가 선택할 때 사용

 .upper()
  - 모든 영문을 대문자로 변경

.lower()
 - 모든 영문을 소문자로 변경

.capitalize()
 - 첫 글자만 대문자

.strip()
 - 앞 뒤 공백 제거
'''





