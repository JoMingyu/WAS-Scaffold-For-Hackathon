# WAS-Scaffold-For-Hackathon
Flask Large Application Example의 조민규 개인화 버전. 해커톤때 구현/문서화/배포 모두 빨리 싹 해치우고 도망가기 위함.

## 뭐 쓰냐
### 인프라는
- Lambda & API Gateway
- MySQL on RDS

### 어플리케이션 레벨
- Flask
- Zappa for package&deploy
- SQLAlchemy

### 의존성 관리
- Pipenv

### CI
- CircleCI - 테스트를 작성할 수 있을런진 모르겠고, push 이벤트 받아서 배포 알아서 해주는 용도

## Flask-Large-Application-Example에서 달라진 건?
1. zappa init을 했음 - zappa_settings.json
2. zappa 배포용 Flask app을 만들기 위해 lambda_app.py를 추가함
3. extension에서 flask-cors가 사라지고, flask-jwt-extended랑 SQLAlchemy에서 쓸 engine들 정의함
4. SQLAlchemy session을 관리하는 데코레이터 추가함
5. config에 DB와 JWT 관련 설정들 집어넣음
6. models/\__init\__.py에 declarative base 넣어둠
