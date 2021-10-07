#4

import sys
import math

input = sys.stdin.readline

up, down, high = map(int, input().split())

day = (high - up) / (up - down) + 1 # -a 만큼 해준 것이 날짜 기준으로는 하루가 더 해지는 것이기때문

print(math.ceil(day))


#5

import sys

input = sys.stdin.readline

room = int(input())

for i in range(room):
    h, w, n = map(int, input().split()) # 6 12 10 = 402 // 6 12 12
    num = n // h + 1
    floor = n % h
    if n % h == 0: # h의 배수이면,
        num = n // h
        floor = h
    print(f'{floor*100+num}')


#6

import sys

input = sys.stdin.readline

test = int(input())

for _ in range(test):
    floor = int(input()) # 층
    num = int(input()) # 호
    f0 = [x for x in range(1, num+1)] # 0층의 리스트
    for k in range(floor): # 층 수 만큼 반복
        for i in range(1, num): # 1 ~ n-1까지 (인덱스로 사용)
            f0[i] += f0[i-1] # 층별 각 호실의 사람 수를 변경 // 굳이 리스트를 생성할 필요가X
    print(f0[-1]) # 가장 마지막 수를 출력


#7

import sys

input = sys.stdin.readline

sugar = int(input())

bag = 0

while sugar >= 0:
    if sugar % 5 == 0: # 5의 배수이면
        bag += (sugar // 5) # 5로 나눈 몫을 구해야 정수가 됨
        print(bag)
        break
    sugar -= 3
    bag += 1 # 5의 배수가 될 때까지 설탕-3, 봉지+ 1
else:
    print(-1)


#8

import sys

input = sys.stdin.readline

a, b = map(int, input().split())

c = a + b

print(c)


#9

t = int(input())

for _ in range(t):
    x, y = map(int, input().split())
    distance = y - x
    count = 0 # 이동 횟수
    move = 1 # count별 이동 가능한 거리
    move_plus = 0 # 이동한 거리의 합
    while move_plus < distance:
        count += 1
        move_plus += move # count 수에 해당하는 move를 더함
        if count % 2 == 0: # count가 2의 배수일 때,
            move += 1
    print(count)