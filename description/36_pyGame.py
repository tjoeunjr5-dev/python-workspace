'''
pip install pygame
파이썬으로 2D 게임 만들기위해 설계된 라이브러리
소리 출력, 키보드/마우스 입력 처리/충돌 감지 등 게임 제작에 필요한 도구보유

무한 루프 : 게임은 멈춰있는 프로그램이 아니라, 초당 수십 번씩 화면을 그리는 무한 루프
게임의 경우 - 메모리, 트래픽 관리 신경써야함

Event(이벤트)    : 유저가 키보를 누르거나, 움직이거나, 마우스를 클릭하는 것과 같이 가만히 있는 화면에서 행동을 하는 것을 이벤트
                   사람이 하는 모든 행동을 이벤트(= 예상치 못한 행위)
Update(업데이트) : 캐릭터의 위치를 계산하고, 적과 부딪혔는지 확인
Draw(그리기)     : 계산된 위치에 맞게 캐릭터와 배경을 화면에 새로 그림
Tick(속도조절)   : 게임이 너무 빠르거나 느리지 않게 초당 프레임 고정

Surface : 그림을 그리는 도화지
Rect    : 위치와 크기를 다루는 사각형 / 충돌 체크의 핵심
Event   : 사용자의 입력 감지
Mixer   : 효과음이나 배경 재생
Font    : 화면에 글자 표시
'''
import pygame, random, sys

# 1. 초기화
pygame.init()

# 2. 화면 설정
screen_width = 480
screen_height = 640
#        게임    화면   크기세팅     가로크기       세로크기  
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("유성 피하기 게임")

# 색상 정의
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED   = (255, 0, 0)
YELLOW = (255, 255, 0)
# 언어에서 대문자로 변수이름을 사용한다는 것은 개발자간의 표기
# 한 번 선언이후 아래에서 변수 명칭 내부에 존재하는 데이터를 변경하지 않고 이대로 쭉~ 사용하겠다.


# 초당 보여줄 화면 프레임 설정
# FPS 설정
clock = pygame.time.Clock()

# 2. 게임 설정
# 플레이어 (사각형으로 대체)
player_size = 40
player_x = screen_width / 2 - player_size / 2
player_y = screen_height - player_size - 10
player_speed = 7

# 적 (유성)
enemy_size = 30
enemy_x = random.randint(0, screen_width - enemy_size)
enemy_y = 0
enemy_speed = 5

# 점수
score = 0
font = pygame.font.SysFont("malgungothic", 30)

# 게임 루프

running = True
while running : # while 은 True 에서 False 가 될 때 까지 횟수 제한 없이 평생 반복 
    dt = clock.tick(60) # FPS를 60으로 고정

    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # 이벤트 타입이 .QUIT 종료와 같다면
            running = False # 게임플레이를 멈추겠다.

    # 키 입력 처리
    keys = pygame.key.get_pressed() # 클라이언트가 입력하는 키보드 데이터 모두 가져오기
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < screen_width - player_size:
        player_x += player_speed

    # 위치 업데이트
    enemy_y += enemy_speed

    # 유성이 떨어지면 다시 생성
    if enemy_y > screen_height :
        enemy_y = 0
        enemy_x = random.randint(0, screen_width - enemy_size)
        score += 1
        enemy_speed += 0.2 # 피하고 점수가 높을 수록 난이도 상승
    # 4. 충돌 처리
    player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
    enemy_rect = pygame.Rect(enemy_x, enemy_y, enemy_size, enemy_size)

    if player_rect.colliderect(enemy_rect):
        print(f"충돌 최종점수 : {score}")
        running = False
    # 5. 화면 그리기
    screen.fill(BLACK) # 배경 색상 채우기

    # 플레이어와 적 그리기
    pygame.draw.rect(screen, YELLOW, player_rect)
    pygame.draw.circle(screen, RED, (enemy_x + enemy_size//2, enemy_y + enemy_size//2), enemy_size//2)

    # 점수 표기
    score_text = font.render(f"Score : {score}", True, WHITE)
    screen.blit(score_text, (10, 10))
    pygame.display.update() #화면 업데이트

pygame.quit() # 게임 종료하고
sys.exit()    # 화면 나가기