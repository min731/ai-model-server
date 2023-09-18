import csv
import random

# 가능한 값들 정의
sex = ['남', '녀']
age = ['10대', '20대', '30대', '40대', '50대', '60대이상']
job = ['관리자', '전문가 및 관련 종사자', '사무 종사자', '서비스 종사자', '판매 종사자', '농림어업 숙련 종사자', '기능원 및 관련 기능 종사자', '장치·기계 조작 및 조립 종사자',
      '단순노무 종사자', '군인']
product = ['A','B','C','D','E','F','G','H','I','J']

# 랜덤 데이터 생성 및 CSV 파일 작성
with open('데이터.csv', 'w', newline='',encoding='ANSI') as csvfile:
    fieldnames = ['성별', '나이', '직업', '거북목', '졸음', '비대칭', '척추후만','제품']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()

    for _ in range(1000):
        row = {
            '성별': random.choice(sex),
            '나이': random.choice(age),
            '직업': random.choice(job),
            '거북목': random.randint(1, 10),
            '졸음': random.randint(1, 10),
            '비대칭': random.randint(1, 10),
            '척추후만': random.randint(1, 10),
            '제품' : random.choice(product)
        }
        writer.writerow(row)

print("CSV 파일이 생성되었습니다.")
