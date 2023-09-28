# 📖 프로젝트명 

### ✔️ 데스크 워커를 위한 자세 교정 서비스 '척추의 요정' (메타버스 아카데미 2기 9월 월말평가 기획/서버/AI 융합 팀 프로젝트)

# 📃 프로젝트 소개

### ✔️ MediaPipe (자세 감지), ChatGPT API (챗봇), Recommendation System (자세 교정 제품 추천), LDA (댓글 분석), Animated Drawings(대표 캐릭터)를 활용한 자세 교정 서비스 '척추의 요정' 프로젝트입니다.

이번 기획 / 서버 / AI 융합 프로젝트 목표는 '우리 재미있게 쓰고 사용해보고 싶은 서비스를 만들어 보자'입니다. 

이번 프로젝트를 기획하게된 계기는 다음과 같습니다. 국민건강보험공단의 조사 내용에 따르면 2014년 기준 허리통증 및 척추질환으로 진료받은 환자 수는 1200만명으로 전국민 4명 중 1명꼴 이라고 합니다. 또한 건강보험심사평가원의 조사에 따르면 2022년 척추질환자는 1131만명으로 전체 인구의 22%를 차지하는 것으로 나타났습니다. 이렇게 대다수 국민, 특히 많은 데스크 워커들이 앓고 있는 척추 질환을 예방하고 올바른 자세로 교정하는데 도움을 주고자 자세 교정 서비스를 기획하고 개발하게 되었습니다.<br>

[2014년 우리나라 국민 4명중 1명 척추질환으로 진료받아, 국민건강보험공단, 2015.11.26](https://www.hira.or.kr/bbsDummy.do?pgmid=HIRAA020041000100&brdScnBltNo=4&brdBltNo=9054)<br>
[척추질환 환자 증가, 건강보험심사평가원, 2022.12.01](https://www.xn--989a170ahhpsgb.com/15/?q=YToyOntzOjEyOiJrZXl3b3JkX3R5cGUiO3M6MzoiYWxsIjtzOjQ6InBhZ2UiO2k6MTMzO30%3D&bmode=view&idx=13580562&t=board)

# 👩‍🔧 팀원 소개 및 역할

### ✔️ 팀원 및 분장
- 메타버스 아카데미 2기 기획/서버/AI 총 8명
- 팀명 : 척추적 60분
  
🔹기획<br>
황해솔 : 기획 / PM<br>
이시온 : 기획 / 디자인

🔹서버<br>
정지원 : 챗봇 통신 / 알림 / 추천<br>
남효정 : 로그인 / 커뮤니티<br>
안희찬 : 프론트 엔드

🔹AI<br>
김우정 : 대표 캐릭터 디자인 / 애니메이션 적용<br>
임정민 : 챗봇 구축 / LDA 댓글 분석<br>
오수종 : 자세 감지 / 추천 시스템 

### ✔️ AI 세부 역할 분담

- 김우정
1) VideoTo3dPoseAndBvh 라이브러리, Animated Drawings 오픈 소스 활용 캐릭터 모션 적용
2) 대표 캐릭터 '레톤이' 디자인 협업 및 검수

- 임정민
1) LangChain / ChatGPT API 활용 챗봇 구축
2) 유사 서비스 'Forest' 리뷰 LDA 분석   

- 오수종
1) MediaPipe 활용 거북목 / 비대칭 / 기대앉기 / 졸음 감지
2) ML PipeLine 활용 개인화 추천 시스템 구현 

# 📅프로젝트 진행 기록

### ✔️ 수행 기간
- 2023.09.04 ~ 2023.09.27

### ✔️ AI 세부 진행 기록

[세부 일정 GitHub Projects](https://github.com/orgs/SpineTracker60/projects/8/views/2)

- 23-09-04 ~ 23-09-06 : 기획/서버/AI 전공별 자기소개 및 팀빌딩
- 23-09-07 ~ 23-09-08 : 아이디어 기획 및 주제 브레인스토밍/토의
- 23-09-11 : 자세 교정 서비스 '척추의 요정' 필수 기술 요구 사항 분석 (자세 감지: 1.거북목 2.비대칭 3.기대앉기 4.졸음 , 챗봇: 1.시스템 안내 2.스트레칭 방법 3.제품 추천)
- 23-09-12 : MediaPipe 활용 자세 감지 모듈 개발(1) , LangChain 활용법 학습 및 서치 
- 23-09-13 : GPT 3.5 Turbo + LangChain 활용 챗봇 구축(1), MediaPipe 활용 자세 감지 모듈 개발(2), Animated Drawings(캐릭터 애니메이션) 오픈 소스 코드 리뷰(1)
- 23-09-14 : GPT 3.5 Turbo + LangChain 활용 챗봇 구축(2), Animated Drawings(캐릭터 애니메이션) 오픈 소스 코드 리뷰(2), 챗봇 프로토 타입 테스트
- 23-09-15 : Flask 활용 챗봇 서빙 모듈 개발 및 통신 테스트(Flask - Node.js), 1주차 기획/서버/AI 전공별 진행상황 보고 및 회의
- 23-09-16 : 중간발표 플로우 설계, Figma 활용 PPT/대본 작성
- 23-09-18 : 팀별 중간발표 및 강사/멘토 피드백, 피드백 기반 팀 회의
- 23-09-19 : Gradio 기반 챗봇 테스트 모듈 개발, 제품 추천 Mock-UP 데이터 구축, VideoTo3dPoseAndBvh 활용 모션 BVH 좌표 추출 모듈 개발(1)
- 23-09-20 : ML PipeLine (LR/RF/SVD/KNC/GBM) 기반 추천 시스템 모듈 개발, 챗봇 프롬프트 수정 및 성능 고도화(1), , VideoTo3dPoseAndBvh 활용 모션 BVH 좌표 추출 모듈 개발(2)
- 23-09-21 : 제품 추천 시스템 챗봇 연동, 대표 캐릭터 초안 디자인
- 23-09-22 : 2주차 기획/서버/AI 전공별 진행상황 보고 및 회의, 대표 캐릭터 애니메이션 적용 모듈 개발(1)
- 23-09-25 : 유사 서비스 'Forest' 서비스 댓글 LDA 분석, 챗봇 프롬프트 수정 및 성능 고도화(2), 대표 캐릭터 애니메이션 적용 모듈 개발(2)
- 23-09-26 : 최종 발표 플로우 설계(서비스 중심), 서비스 시연 GIF 편집, AI 전공 PPT/대본 작성, 10분 발표 리허설 
- 23-09-27 : 최종 발표 및 팀 회식, 깃허브 리드미 작성

# 💡 주요 내용

### ✔️ 유사 서비스 'Forest' 어플 구글 플레이스토어 리뷰 LDA 분석

##### 1) 'Forest' 서비스란?

![image](https://github.com/SpineTracker60/ai-model-server/assets/115389344/f42a30d9-27ef-4169-9513-9a1312eb6449)

- 집중 시간을 측정하고 종료 알림해주는 시간 관리 타이머 서비스
- 집중에 성공하면 유저 자신만의 숲을 가꿀 수 있는 재미요소 가미
- 본 자세 교정 서비스와 유사한 맥락의 서비스로 벤치마킹 시도

##### 2) Forest 구글 플레이 스토어 리뷰 크롤링

- 총 1240개 리뷰 내용/평점 데이터 수집
  
![image](https://github.com/SpineTracker60/ai-model-server/assets/115389344/57b3f01d-a771-408a-bad9-e929375a2125)

##### 3) LDA 활용 토픽 모델링 / 시각화

![image](https://github.com/SpineTracker60/ai-model-server/assets/115389344/893662d3-7afd-43c4-8d00-88fbfafc89e1)

- 토픽 갯수 3종류 (n_component=3) 기준 토픽 분류
1) Topic #1 : 집중력 향상 / 성취감 / 나무,숲 재미요소
2) Topic #2 : 결제 문의 / 프리미엄 유저    
3) Topic #3 : 기능 오류 / 개선점

##### 4) LDA 인사이트 도출

- 긍정적인 반응을 보인 Topic #1 토픽 분석

  ![image](https://github.com/SpineTracker60/ai-model-server/assets/115389344/8905bc78-24ba-4558-8265-f146427b3805)

- 긍정적으로 평가한 리뷰들 중 대부분 집중력 향상과 더불어 나무를 심고 숲을 가꾸는 재미요소에 몰입 / 시너지 효과
- 이러한 실제 유저 반응들을 토대로 시각적 재미(캐릭터 애니메이션)을 적용한 자세 교정 서비스를 기획/개발에 근거

### ✔️ MediaPipe 활용 자세 감지

##### 1) 요구사항 

- '척추의 요정' 서비스의 기본이 되는 거북목 / 비대칭 자세 / 기대 앉기 / 졸음 감지 모듈 개발
  
##### 2) 자세 구분

🔹서비스 사용 시 촬영한 정자세 사진 기준을 통해 비교/구분

![KakaoTalk_20230917_123027747](https://github.com/SpineTracker60/ai-model-server/assets/115389344/206337c1-75bd-440d-a80d-d04ff302321d) ![KakaoTalk_20230917_123027747_01](https://github.com/SpineTracker60/ai-model-server/assets/115389344/f05a305f-af6f-4d1c-a36a-9fb3af762166)

- 거북목 : 정자세 기준 일정 비율 이상 얼굴 크기 확장 시 탐지
- 비대칭 자세 : 어깨 좌표 기울기 이상치 탐지
- 기대 앉기 : 정자세 기준 얼굴 크기 일정 비율 이상 감소 시 탐지
- 졸음 : 눈커플 좌표 y축(위아래 길이) 기준 축소 시 탐지


### ✔️ Object Detection

##### 1) 데이터 전처리 및 증강(RoboFlow)

- 전처리 : Roboflow 활용 box annotations, 클래스 : banner(현수막), frame(지정게시대틀)
- 증강 : rotate ± 10° / brightness ± 25% / saturation ± 25%
- 총 학습 데이터 갯수 : 3226개 (train:2826개, valid:268개, test:132개)

##### 2) yolov8(n) 모델 학습/평가 및 추론

- 학습 파라미터 : epochs=2000, patience=50, batch=32, dropout=0.3, imgz=640 x 640, iou=0.7, optimizer='Adam', lr=0.01
- 평가 지표 : mAP50=0.963 , mAP50-95=0.797 , cls_loss=0.6101 , dfl_loss=1.193 , box_precision=0.948 , box_recall= 0.925

![image](https://github.com/MTVS-AI/META_Yolo_OCR_ChatGPT_PJT/assets/115389344/9fdf52ae-ac29-458a-8e9c-841cc5871528) 

- 학습 Validation 예시

![image](https://github.com/MTVS-AI/META_Yolo_OCR_ChatGPT_PJT/assets/115389344/be2473b8-ab41-47ff-937a-f198db8de386)

- 모델 Predict 예시
  
![image](https://github.com/MTVS-AI/META_Yolo_OCR_ChatGPT_PJT/assets/115389344/c07b3085-0aa8-4e04-acd4-badfa018bec5)
### ✔️ 현수막 Type 분류

##### 1) 현수막 분류 알고리즘
![image](https://github.com/MTVS-AI/META_Yolo_OCR_ChatGPT_PJT/assets/115389344/5deceae0-5fee-4849-b5f9-4ebb3f60664a)

##### 2) 객체 탐지 활용 지정게시대 현수막(합법 현수막) 구분
- 입력된 이미지에 frame (지정게시대 틀) 존재 시, frame/banner의 xyxy 좌표 파악
- banner/frame의 겹치는 비율 계산
- 임계값 70% 이상 시 합법 현수막으로 분류

![image](https://github.com/MTVS-AI/META_Yolo_OCR_ChatGPT_PJT/assets/115389344/1fd7e707-9c90-4631-a732-ba3c7f5c79c0)


### ✔️ OCR
##### 1) PaddleOCR

- 경계가 뚜렷한 텍스트와 숫자 추출에 괜찮은 성능
- 희미한 텍스트에 대해 색상 반전 등의 기법 시도
- 그러나 다음단계로 넘어갔을 때 PaddleOCR로 추출한 텍스트만으로는 현수막 분류가 불가능하여 다른 OCR 활용

![image](https://github.com/MTVS-AI/META_Yolo_OCR_ChatGPT_PJT/assets/115389344/ee6c41a3-e594-4fb1-99ab-462e0474b28b)


##### 2) Naver Clova OCR

- Naver Clova에서 API를 발급받아 요금을 내고 사용하는 고성능 OCR 모듈
- PaddleOCR보다 기울어진 구도의 현수막과, Noise가 들어가있는 텍스트들을 더 효과적으로 추출 가능

![image](https://github.com/MTVS-AI/META_Yolo_OCR_ChatGPT_PJT/assets/115389344/a4901a40-da1e-43dd-95a6-a033c3bf4e70)


### ✔️ 텍스트 분류 (ChatGPT)

- OCR을 통해 추출된 현수막의 텍스트 카테고리 분류 (프레임/합법/정치/기타 총 4개 클래스)
- 프롬프트 엔지니어링 : 역할 부여 - 문제 정의 - 분류 클래스 묘사 - 전달 방식 정의 - 내용 전달 - 반환 방식 정의
![image](https://github.com/MTVS-AI/META_Yolo_OCR_ChatGPT_PJT/assets/115389344/14d7daa7-9b1e-43ae-8f29-005dd65ea3cc)

- Text Classification 예시 ( 프레임=0 , 합법=1 , 정치=2 , 기타=3 )
![image](https://github.com/MTVS-AI/META_Yolo_OCR_ChatGPT_PJT/assets/115389344/6b36a710-95f0-4d29-9c3a-dbe093e42fb2)

### ✔️ 데이터 정제 (DataFrame)

- 데이터프레임 활용 데이터 정제 및 저장
![image](https://github.com/MTVS-AI/META_Yolo_OCR_ChatGPT_PJT/assets/115389344/a30b63eb-bbfe-424f-81ec-d4efb596cb94)


### ✔️ 웹서비스 기반 지도 시각화

- 단속 업무에 활용할 수 있는 현수막 현황 자료

![image](https://github.com/MTVS-AI/META_Yolo_OCR_ChatGPT_PJT/assets/115389344/a2c000f9-c6d9-4374-8332-98b706cf755e)

![image](https://github.com/MTVS-AI/META_Yolo_OCR_ChatGPT_PJT/assets/115389344/0470d1c7-7fab-4aed-9499-ae8a7bd992f0)



##### 1) 입력 정보
- 정제된 DataFrame 바탕
- 이미지 / 이미지의 종류
- 내용 : crop된 이미지의 범례, 현수막의 내용, 해당 범례로 분류한 근거를 표의 형태로 포함

##### 2) folium 모듈
- leaflet.js를 기반으로 만들어진 Python 지도 시각화 라이브러리
- 좌표값을 기반으로 popup 마커 생성, 해당 마커들은 범례에 따라 하나의 그룹으로 통합
- popup에는 html 기반의 표 입력, base64 활용 인코딩 및 디코딩 후 표에 이미지 삽입
- 최종적으로 지도에 popup 마커들이 표시되는 형태
- 우측 상단의 박스 체크를 통해 합법 / 정치 / 불법 현수막들 중 원하는 종류의 현수막 현황을 볼 수 있는 조절 기능 구현

### ✔️ 로그 수집/재학습

##### 서비스 로그 기록/저장
- 촬영 날짜/시간 , 원본 이미지, 예측 이미지, 클래스별 Crop 이미지 저장
- 1) 수집 데이터 기반 재학습 용이
- 2) 특정 기간 단위 데이터 분석 활용 가능 ex) 선거철
  
![image](https://github.com/MTVS-AI/META_Yolo_OCR_ChatGPT_PJT/assets/115389344/41d35ca5-7d10-459b-aaca-2fe5a72cda51)

### ✔️ 한계점 및 개선사항
##### 1) 기울어진 형태의 현수막 OCR
![image](https://github.com/MTVS-AI/META_Yolo_OCR_ChatGPT_PJT/assets/115389344/f630e24a-b7f6-4257-bee9-851fd412f452)
- 한계점 : 탐지된 현수막 외의 근처 현수막의 텍스트까지 포함되는 경우 발생
- 개선점 : Opencv 도형 검출 및 Segmentation 모델 활용을 통한 객체 추출 고도화

##### 2) Naver Clova OCR의 한계
![image](https://github.com/MTVS-AI/META_Yolo_OCR_ChatGPT_PJT/assets/115389344/c0f8f03b-b126-410b-bd16-ee8b6c815b9e)
- 한계점 : Clova OCR 활용에도 불구, 희미한 현수막 문구 일부 추출 혹은 추출 불가능
- 개선점 : 이미지 선명화 (기본/GrayScale) / Blur, Sharpen 조절 등 이미지 자체에 대한 전처리 기법 시도  

# 🛠 기술 스택

### 🔹 언어
<img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white"> <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=python&logoColor=white">

### 🔹 주요 라이브러리
<img src="https://img.shields.io/badge/ultralystics-0099E5?style=for-the-badge&logo=ultralystics&logoColor=white"> <img src="https://img.shields.io/badge/pytorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white"> <img src="https://img.shields.io/badge/torchvision-29A7DF?style=for-the-badge&logo=torchvision&logoColor=white"> <img src="https://img.shields.io/badge/paddleocr-0062B0?style=for-the-badge&logo=paddleocr&logoColor=white"> <img src="https://img.shields.io/badge/openai-412991?style=for-the-badge&logo=openai&logoColor=white"> <img src="https://img.shields.io/badge/folium-77B829?style=for-the-badge&logo=folium&logoColor=white"> <img src="https://img.shields.io/badge/react-61DAFB?style=for-the-badge&logo=react&logoColor=white"> <img src="https://img.shields.io/badge/jquery-FF4154?style=for-the-badge&logo=jquery&logoColor=white"> <img src="https://img.shields.io/badge/flask-000000?style=for-the-badge&logo=flask&logoColor=white"> <img src="https://img.shields.io/badge/jinja2-B41717?style=for-the-badge&logo=jinja&logoColor=white"> <img src="https://img.shields.io/badge/opencv-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white"> <img src="https://img.shields.io/badge/pandas-150458?style=for-the-badge&logo=pandas&logoColor=white"> <img src="https://img.shields.io/badge/matplotlib-0058CC?style=for-the-badge&logo=matplotlib&logoColor=white">

### 🔹 개발 툴
<img src="https://img.shields.io/badge/VS code-2F80ED?style=for-the-badge&logo=VS code&logoColor=white"> <img src="https://img.shields.io/badge/Google Colab-F9AB00?style=for-the-badge&logo=Google Colab&logoColor=white"> <img src="https://img.shields.io/badge/pycharm-000000?style=for-the-badge&logo=pycharm&logoColor=white">

### 🔹 협업 툴
<img src="https://img.shields.io/badge/Github-181717?style=for-the-badge&logo=Github&logoColor=white"> <img src="https://img.shields.io/badge/Notion-000000?style=for-the-badge&logo=Notion&logoColor=white"> <img src="https://img.shields.io/badge/roboflow-A100FF?style=for-the-badge&logo=roboflow&logoColor=white">

# 🔍 참고 자료

### ✔️ 시연 영상 / 블로그
- Youtube : https://www.youtube.com/watch?v=UXZTP0jx1WQ&list=PLml1GH62sPF-tPUg7xatqjC3xG2bXmjgv&ab_channel=%EC%9E%84%EC%A0%95%EB%AF%BC
- Velog : https://velog.io/@min0731/%EB%B6%88%EB%B2%95-%ED%98%84%EC%88%98%EB%A7%89-%ED%83%90%EC%A7%80-%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B81
### ✔️ 기사

- https://www.youtube.com/watch?v=QtI7la0i_7A&ab_channel=%EC%B6%98%EC%B2%9CMBC%EB%89%B4%EC%8A%A4
- https://www.munhwa.com/news/view.html?no=2022092001031039342001
- https://www.joongang.co.kr/article/25170006#home
- https://www.busan.com/view/busan/view.php?code=2023061418340018356
- https://www.ohmynews.com/NWS_Web/View/at_pg.aspx?CNTN_CD=A0002429221
- https://www.greenkorea.org/activity/living-environment/zerowaste/91981/

### ✔️ 오픈소스 (GitHub)

- https://github.com/ultralytics/ultralytics
- https://www.ncloud.com/product/aiService/ocr

### ✔️ 라이브러리 공식 문서

- https://docs.ultralytics.com/modes/predict/
- https://pypi.org/project/paddleocr/
