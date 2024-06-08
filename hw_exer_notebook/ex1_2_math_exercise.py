#!/usr/bin/env python 

import math # math library import

area = int(input("Type Area of Square : ")) # 사각형 면적 입력 받음

square_length = math.sqrt(area) #루트를 사용해서 사각형 한변의 길이 계산
inner_circle_radius = (1/2) * square_length #안에 있는 원의 반지름 계산
outer_circle_radius = (1/2) * square_length * math.sqrt(2) # 바깥에 있는 원의 반지름 계산
inner_circle_area = math.pi * inner_circle_radius * inner_circle_radius # math.pi를 사용하여 원의 넓이 계산
outer_circle_area = math.pi * outer_circle_radius * outer_circle_radius

print("Area of Inner Circle :", inner_circle_area) #원의 넓이 출력
print("Area of Outer Circle :", outer_circle_area)