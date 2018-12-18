# WAS-Scaffold-For-Hackathon
Flask Large Application Example의 조민규 개인화 버전. 해커톤때 구현/문서화/배포 모두 빨리 싹 해치우고 도망가기 위함.

## 인프라 가정
- Lambda & API Gateway
- Aurora on RDS

## 어플리케이션 레벨
- Flask
- Zappa for package&deploy
- SQLAlchemy

## 의존성 관리
- Pipenv

## CI
- CircleCI - 테스트를 작성할 수 있을런진 모르겠고, push 이벤트 받아서 배포 알아서 해주는 용도
