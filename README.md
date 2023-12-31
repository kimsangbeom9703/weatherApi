# weatherApi
```text
    공공데이터 포털 API 활용하여 날씨 , 환경정보 수집하기.
```
## 사용할 언어 및 프레임워크
```text
    python  :   날씨데이터 수집기  
    fastapi :   날씨데이터 API 제공
    react   :   프론트엔드 
```
## 목표? 서비스 결과?
```text
    초기라 두루뭉실 하지만 내가 생각하고 있는 개발 목적은 전국 행정구역 level1~3 까지의 데이터를 수집하고 
    지도에 날씨를 표현한다 지도 클릭시 더 자세한 결과를 보여주고 기상청 날씨누리 같은 모습을 생각한다.
    추가로 회원가입 기능도 개발하여 로그인시 자신이 설정한 지역의( GPS 연동도 고려 ) 날씨 정보를 제공
    챗봇 기능을 추가해 동을 입력하면 날씨 정보 제공     
```

## 공공데이터 포털 API 활용하여 날씨 서비스 개발

### 사용할 API
```text
   1.  기상청_단기예보 ((구)_동네예보) 조회서비스
        -   https://www.data.go.kr/data/15084084/openapi.do
        -   초단기실황, 초단기예보, 단기((구)동네)예보, 예보버전 정보를 조회하는 서비스입니다. 초단기실황정보는 예보 구역에 대한 대표 AWS 관측값을, 초단기예보는 예보시점부터 6시간까지의 예보를, 단기예보는 예보기간을 글피까지 확장 및 예보단위를 상세화(3시간→1시간)하여 시공간적으로 세분화한 예보를 제공합니다.
    
    2.  한국환경공단_에어코리아_사용자
        -   https://www.data.go.kr/data/15075624/openapi.do
        -   한국환경공단에서 제공하는 에어코리아 Open API 사용자들의 활용지원을 위한 서비스
    
    3.  한국환경공단_에어코리아_측정소정보
        -   https://www.data.go.kr/data/15073877/openapi.do
        -   대기질 측정소 정보를 조회하기 위한 서비스로 TM 좌표기반의 가까운 측정소 및 측정소 목록과 측정소의 정보를 조회할 수 있다.
        -   ※ 운영계정으로 사용하고자 할 경우 "한국환경공단 에어코리아 OpenAPI 기술문서" 내 신청 가이드 참고

    4.  한국환경공단_에어코리아_대기오염정보
        -   https://www.data.go.kr/data/15073861/openapi.do
        -   각 측정소별 대기오염정보를 조회하기 위한 서비스로 기간별, 시도별 대기오염 정보와 통합대기환경지수 나쁨 이상 측정소 내역, 대기질(미세먼지/오존) 예보 통보 내역 등을 조회할 수 있다.
        -   ※ 운영계정으로 사용하고자 할 경우 "한국환경공단 에어코리아 OpenAPI 기술문서" 내 신청 가이드 참고
    
    5.  인천국제공항공사_실내대기질 정보
        -   https://www.data.go.kr/data/15095049/openapi.do
        -   인천국제공항 여객터미널 T1,T2,탑승동 실내대기질 실시간 측정 결과 정보(일산화탄소,이산화탄소,이산화질소,미세먼지,초미세먼지,터미널 위치,기준시간)를 제공    
    
    6.  인천국제공항공사_실외대기질 정보
        -   https://www.data.go.kr/data/15117020/openapi.do
        -   인천국제공항 근방 자유무역지역,남북동,을왕동 실외 대기질 실시간 측정 결과 정보(아황산가스,일산화탄소,오존,이산화질소,미세먼지,초미세먼지,위치,기준시간)을 제공
```

[//]: # (### 기상청 단기예보)

[//]: # (```text)

[//]: # (    기상청_단기예보 &#40;&#40;구&#41;_동네예보&#41; 조회서비스)

[//]: # (    1. 예보버전 조회 )

[//]: # (        -   버전 조회 하여 새로 업데이트 된 버전인지 확인)

[//]: # (        -   app/collectrion/getWeatherVersion.py 확인)

[//]: # (            -   단기예보 / 초단기예보 버전정보 조회 하여 정보데이터가 db에 없으면 삽입하고 있으면 저장x)

[//]: # (                나중에 단기예보 , 초단기예보를 조회후 used 값을 업데이트 하여 이미 수집했는지 체크할 예정.)

[//]: # (    2. 단기예보 조회)

[//]: # (    3. 초단기예보 조회)

[//]: # (```)
