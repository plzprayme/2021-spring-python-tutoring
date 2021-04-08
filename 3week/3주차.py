# -*- coding: utf-8 -*-
"""3주차.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hHodhKX6hxBAtPN5PEumSnfy1ywJhKPZ
"""

# 조건문
# if {조건}:  조건이 True(참)일 때만 실행코드를 실행한다.
# 실행 코드

if True:
  print("참입니다.")

if False:
  print("참입니다.")

a = 5
if a > 7:
  print("참입니다.")
elif a > 6:
  print("참입니다2.")
else:
  print("a는 7보다 크지도 않고 6보다 크지도 않습니다.")

# for 변수 in range(횟수):
#   반복할 코드


arr = [1,2,3,4,5]
for seonghcan in arr:
  print(seonghcan)

string = "일이삼사오"
for i in string:
  print(i)

for i in range(5): # 0 ~ 5-1
  print(i)
  print(string[i])

tup = (1,2,3,4,5)
for i in tup:
  print(i)

while '':
  print("거짓입니다")

# while " ":
#   print("참입니다")

while []:
  print("거짓입니다")

# while [1]:
#   print("참입니다")

for i in range(3):
  print(f"====== i: {i}")
  for j in range(10):
    print("처읍입니다")
    if j == 5:
      continue
    print(j)

# 반복문 연습 
# 별찍기

for i in range(5):

  for j in range(i+1):
    print('*', end="")

  print()

print("=" * 10)

for i in range(1, 6):
  for j in range(i):
    print('*', end="")

  print()

x, y = 0, 0
while y < 5:

  while x < 5:
    print('*', end="")

    if x == y:
      x = 0
      break

    x += 1

  print()
  y += 1

# i = 0
# while True:
#   i += 1
#   if i > 5:
#     break
#   print("*" *i)

i = 1
while i < 6:
  print("*" * i)  
  i += 1

print('문자열' * 3)

# 프로그래머스 콜라츠 추측
# 1. while문 활용한 풀이

num = 6      # 정답: 8
# num = 16     # 정답: 4
# num = 626331 # -1

answer = 0 
while True: 
    if num == 1: 
        return answer
    elif answer == 500: #500회 일때 -1 리턴
        return -1

    if num % 2 == 0:  
        num = num / 2
    elif num % 2 == 1: 
        num = num * 3 + 1

    answer += 1
return answer

#2. for문 활용한 풀이
for i in range(500):
  if num == 1:
      return i

  if num % 2 == 0: # 1-1. 입력된 수가 짝수라면 2로 나눕니다.
      num //= 2
  else:       # 1-2. 입력된 수가 홀수라면 3을 곱하고 1을 더합니다.
      num = num * 3 + 1
  return -1

# 백준 온라인저지지 10871번 문제
# 1. list comprehension을 이용한 풀이
N, X = map(int, input().split())
result = [i for i in map(int, input().split()) if i < X]
[print(i, end=' ') for i in result]
print(result[-1], end=' ')

# 2. filter를 활용한 풀이
N, X = map(int, input().split())
A = map(int, input().split())
[print(i, end=' ') for i in filter(lambda i: i < X, A)]