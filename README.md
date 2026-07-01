# HELLO_FLASK

## 📅 2026-07-01

### 1. 오늘 만든 기능

- SQLite 설치
- Flask 프로젝트에 SQLite 연결
- skills.db 생성
- skills 테이블 생성
- SELECT 기능 구현
- INSERT 기능 구현
- UPDATE 기능 구현
- DELETE 기능 구현
- 기존 리스트 CRUD를 SQLite CRUD로 변경
- 서버를 종료해도 데이터가 유지되는 구조 완성

### 2. 사용한 문법

- sqlite3
- import
- sqlite3.connect()
- cursor()
- execute()
- commit()
- close()
- CREATE TABLE
- SELECT
- INSERT
- UPDATE
- DELETE
- WHERE
- fetchall()
- fetchone()
- AUTOINCREMENT
- PRIMARY KEY
- conn.row_factory
- sqlite3.Row

### 3. 실행 결과

- skills.db 파일이 생성됨
- Flask에서 입력한 데이터가 SQLite에 저장됨
- 서버를 종료해도 데이터가 유지됨
- 수정 기능이 정상 동작함
- 삭제 기능이 정상 동작함
- id가 자동으로 생성됨
- HTML 화면은 거의 수정하지 않고 SQLite로 변경함

### 4. 어려웠던 점

-

### 5. 추가로 해본 것

-

## 📅 2026-05-20

### 1. 오늘 만든 기능
- index 기반 CRUD 구조를 id 기반 CRUD 구조로 변경
- 데이터마다 고유 번호인 id 추가
- `next_id`를 사용하여 새 데이터에 id 자동 부여
- 목록 화면에 id 표시 (`#1 Python` 형태)
- id 기준 개별 삭제 기능 구현
- id 기준 선택 삭제 기능 구현
- id 기준 수정 페이지 이동 구현
- id 기준 데이터 수정 기능 구현
- SQLite 전환을 위한 id 구조 준비

### 2. 사용한 문법
- id
- global
- dictionary
- for
- if
- break
- None
- request.form.get
- request.form.getlist
- redirect
- render_template
- route parameter (`<int:item_id>`)
- item["id"]
- messages.remove()
- messages.clear()

### 3. 실행 결과
- 데이터를 추가하면 각 데이터에 id가 자동으로 붙음
- 화면에서 `#1 Python`처럼 id와 기술명이 함께 표시됨
- 삭제 버튼을 누르면 id가 같은 데이터만 삭제됨
- 삭제 후에도 남은 데이터의 id가 바뀌지 않음
- 선택 삭제를 하면 선택한 id의 데이터만 삭제됨
- 수정 후에도 id는 그대로 유지되고 내용만 변경됨

### 4. 어려웠던 점
-

### 5. 추가로 해본 것
-

## 📅 2026-05-12

### 1. 오늘 만든 기능
- 딕셔너리 안에 여러 값을 저장하도록 확장
- `skill`, `level`, `status` 입력값 받기
- 입력한 값을 하나의 딕셔너리로 묶어서 `messages` 리스트에 저장
- 딕셔너리에서 `skill`, `level`, `status` 값을 꺼내 화면에 출력
- 삭제 버튼으로 리스트 안의 딕셔너리 한 덩어리 삭제
- 삭제 확인 메시지 추가
- 전체 삭제 버튼 추가
- 선택 삭제 버튼 추가
- 체크박스로 삭제할 항목 선택
- 삭제 후 메인 화면으로 redirect

### 2. 사용한 문법
- dictionary(dict)
- key
- value
- list
- append
- pop
- clear
- len
- if
- or
- for
- enumerate
- loop.index0
- request.form.get
- request.form.getlist
- strip
- render_template
- redirect
- route parameter
- form
- checkbox
- hidden input

### 3. 실행 결과
- 기술명, 수준, 학습 상태를 입력할 수 있음
- 입력한 데이터가 딕셔너리 형태로 저장됨
- 저장된 딕셔너리에서 각각의 값을 꺼내 화면에 출력함
- 삭제 버튼을 누르면 해당 데이터 한 줄이 삭제됨
- 전체 삭제 버튼을 누르면 모든 데이터가 삭제됨
- 체크박스를 선택한 뒤 선택 삭제 버튼을 누르면 선택한 데이터만 삭제됨
- 삭제 전 확인 메시지가 출력됨
- 삭제 후 메인 화면으로 돌아옴

### 4. 어려웠던 점
-

### 5. 추가로 해본 것
-

## 📅 2026-04-22

### 1. 오늘 만든 기능
- 저장된 데이터 수정 기능
- 수정 버튼 클릭 시 edit 페이지 이동
- 새 값을 입력해서 기존 데이터 변경
- 빈 값 입력 시 수정 차단
- 동일한 값 입력 시 수정 생략

### 2. 사용한 문법
- index
- loop.index0
- form
- hidden input
- request.form
- render_template
- redirect

### 3. 실행 결과
- 목록에서 원하는 데이터를 골라 수정할 수 있게 됨
- 수정 후 메인 화면에서 바뀐 결과를 바로 확인할 수 있음

### 4. 어려웠던 점
-

### 5. 추가로 해본 것
-

## 📅 2026-04-14

### 1. 오늘 만든 기능
- form으로 데이터 전송 구조 만들기
- input 3개로 값 전달하기

### 2. 사용한 문법
- form
- input
- request.form.get

### 3. 실행 결과
- 입력한 값이 화면에 출력됨

### 4. 어려웠던 점
-

### 5. 추가로 해본 것
-

## 프로젝트 소개
Flask와 Jinja2를 사용해서
파이썬 데이터를 HTML 화면에 출력하는 연습을 하는 프로젝트입니다.

## 지난 시간에 배운 내용
- Flask 기본 실행
- templates 폴더 사용
- index.html 만들기
- render_template()로 HTML 연결하기
- 파이썬 딕셔너리 데이터를 HTML에 출력하기

## 이번 시간에 배울 내용
- 리스트 데이터 만들기
- for 문으로 화면 자동 생성하기
- if 문으로 화면 다르게 출력하기

## 프로젝트 파일 설명
- `app.py` : Flask 서버를 실행하는 파일
- `templates/index.html` : 화면을 만드는 HTML 파일
- `README.md` : 프로젝트 설명 문서
