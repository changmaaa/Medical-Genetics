#!/usr/bin/env python 

#디렉토리 설정 후 열어주기
directory = "/home/share/medicalgenetics/drug_target.txt" 
f = open(directory, 'r')

drug_target_dic = {} #빈 딕셔너리 선언

while True : 
    line = f.readline().strip() # 한줄씩 읽어옴
    if not line : break
    # 약물은 | 로 나눴을때 첫번째이므로 [0]으로 설정후 drug에 저장
    drug = line.split('|')[0] 
    # 타겟은 | 로 나눴을때 두번째이므로 [1]로 설정 후, 여러개인 경우 , 로 나눠서 list 형태로 저장
    target = line.split('|')[1].split(',')
    drug_target_dic[drug] = target # drug를 key, target을 벨류로 딕셔너리에 저장

f.close()
# 찾고자 하는 약물 입력
drug = input("Type drugbank code of drug : ")
if drug in drug_target_dic.keys() : # 약물이 key값에 존재시
    target_list = drug_target_dic[drug] # 출력하고자 하는 리스트를 저장
    print("Target of", drug) # 약물 입력 출력
    for target in target_list : # 리스트를 하나씩 출력
        print(target)
else : 
    print("Incorrect Drug name") # 약물이 없을경우, 없다는 내용 출력