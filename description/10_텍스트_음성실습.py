from gtts import gTTS
from playsound3 import playsound

# tts 제거하여 한 번에 hello 라는 파일로 저장하기
gTTS(text="안녕하세요. 어서오세요. 반갑습니다. ", lang='ko')
tts.save("hi.mp3")
playsound("hi.mp3")