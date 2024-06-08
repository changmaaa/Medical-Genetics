#!/usr/bin/env python 

number_dictionary = { #숫자를 key로 단어를 value로 하는 dictionary 선언
    '1' : 'one',
    '2' : 'two',
    '3' : 'three',
    '4' : 'four',
    '5' : 'five',
    '6' : 'six',
    '7' : 'seven',
    '8' : 'eight',
    '9' : 'nine',
    '0' : 'zero'
}

sentence = input("Type the sentence : ") # input으로 입력 받아서 sentence에 저장

print("Previous Sentence :", sentence) # 이전 Sentence 출력
for i in sentence : #단어를 한글자씩 확인
    if i in number_dictionary.keys() : # i가 숫자, 즉 dictionary에 key로 존재한다면
        sentence = sentence.replace(i, number_dictionary[i]) #i를 key의 value로 replace 함수 써서 변환
print("Fixed Sentence :", sentence) # 수정된 sentence 출력