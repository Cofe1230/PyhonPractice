# 파이썬 수업

## Day01

Python 기본 문법 연습

## Day02
* Code 01 02  
Python CSV 데이터 읽기  
* Code 03  
CSV파일 테이블로 출력  
* Code 04  
CSV파일 읽고 쓰기  
* Code 05  
특정한 열만 조건으로 쓰기(map)  
* Code 06  
CSV라이브러리  
* Code 07  
CSV 파일 합치기  
* Code 08 09  
CSV 파일 GUI 출력 (tkinter)  
* Code 10  
폴더 안에 CSV 합치기 (csv, glob, os)  
폴더 전체 가져오기(glob)  
* Code11  
RAW 이미지 -> CSV파일로 전환하여 저장 -> CSV파일 수정 -> RAW로 저장  
#### 파이썬에서 액셀 파일 처리
* 외부 라이브러리 설치  
__액셀 97~03 xls파일 처리__
```
cmd  
pip install xlrd xlwt  
```
xlrd와 xlwt는 액셀 97~03 버전의 xls 파일만 처리한다  
__액셀 07 이후에서 사용하는 xlsx파일을 처리하기 위한 외부 라이브러리 설치__
```
pip install openpyxl
```
__xlsx파일의 쓰기를 지원하는 외부 라이브러리__
```
pip install xlsxwriter
```
* Code12 Code13 Code14  
python으로 액셀파일 처리(xlrd)  
* Code15  
액셀 파일 저장 
* Code16 Code17  
16 : 평균 키가 165 이상인 행만 추출하여 액셀 저장  
17 : 인원수가 6명 이상인 그루만 추출하여 액셀 저장  
* Code 18  
엑셀 파일을 CSV파일로 저장  
* Code 19  
특정 열만 CSV파일로 저장  
* Code 20  
xlsx 액셀 파일 처리 (openxyxl 라이브러리)  
* Code 21  
액셀 파일 서식 복사  
* Code 22  
이미지 데이터 배열 변수에 저장  
* Code 23
이미지 데이터 배열을 저장하여 액셀로 나타내기
## Day03
#### SQLite 설치
sqlite-tools-win32-x86 다운로드  
[https://www.sqlite.org/download.html](https://www.sqlite.org/download.html)  
DB Browser SQLite GUI  
[https://sqlitebrowser.org/dl/](https://sqlitebrowser.org/dl/)  
DBeaver 여러가지 DB GUI
[https://dbeaver.io/download/](https://dbeaver.io/download/)

#### SQLite 사용

* **cmd**  
```
.open 데이터베이스이름
```  
없으면 생성하고 있으면 연다  


```
.header on
.mode column
```  
테이블을 좀 예쁘게 보기 위해 사용한다  

### Code
* **code01**  
python DB연결(DB파일에 직접 연결)  
input에 입력하면 DB테이블에 insert 된다  
* **code02**  
python DB연결(SQLite 접속해서 연결)  
insert, select GUI 화면으로 표현





















