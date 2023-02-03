# total
전체적 통합용 및 통합적인 환경에 대한 안내


# Rule
1. 같은 OS(Window 11) 안에서 실행
2. 경로는 아래 path를 따른다.
3. 기본적인 설치 사항들 역시 아래 requirement를 따른다. 
4. 기본적으로 각자 역할과 맡은 일에 따라 개인의 repository(보관소)에서 작업 후 팀 회의 및 팀 작업 때 통합된 내용은 현 total 보관소에서 처리한다.

## Infrastructure 구성 환경

### requriement 설치요소
1. 파이썬 공식 홈페이지 주소: [https://www.python.org](https://www.python.org) 
```python --version``` 
위 명령어로 버전 확인 시 최소 3.9 이상 아닐 경우
```python -m pip install --upgrade pip``` 으로 업그레이드 먼저

2. cmd에서 장고 개발환경 참조 : [https://wikidocs.net/70588](점프투장고)

3. requirements는 ```pip install Django==4.1.5``` 을 기본으로 한다<br>
현 장고 버전 : pip install Django==4.1.5

### path
- 기본 경로 : C:\silverScore
- projects(실제 프로젝트 경로) 경로 : C:\silverScore\projects\silverScore
- venvs 경로(`python -m venv silverScore`로 만든) : C:\silverScore\venvs\silverScore

### batch file
- 배치파일명 : silverScore.cmd

```
@echo off
cd C:\silverScore\projects\silverScore
C:\silverScore\venvs\silverScore\Scripts\activate

```

위와 같은 배치파일 만들고 각자의 시스템 환경 변수의 path 에 C:\silverScore\venvs\silverScore 를 등록 후 진행할 것

---



