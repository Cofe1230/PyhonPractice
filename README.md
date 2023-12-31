# 파이썬(빅데이터) 수업

## Day01

Python 기본 문법 연습

## Day02
### Code
* **Code 01 02**  
Python CSV 데이터 읽기  
* **Code 03**  
CSV파일 테이블로 출력  
* **Code 04**  
CSV파일 읽고 쓰기  
* **Code 05**  
특정한 열만 조건으로 쓰기(map)  
* **Code 06**  
CSV라이브러리  
* **Code 07**  
CSV 파일 합치기  
* **Code 08 09**  
CSV 파일 GUI 출력 (tkinter)  
* **Code 10**  
폴더 안에 CSV 합치기 (csv, glob, os)  
폴더 전체 가져오기(glob)  
* **Code11**  
RAW 이미지 -> CSV파일로 전환하여 저장 -> CSV파일 수정 -> RAW로 저장  
### 파이썬에서 액셀 파일 처리
#### 외부 라이브러리 설치  
__액셀 97~03 xls파일 처리__  
**cmd**
```  
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
* **Code12 Code13 Code14**  
python으로 액셀파일 처리(xlrd)  
* **Code15**  
액셀 파일 저장 
* **Code16 Code17**  
16 : 평균 키가 165 이상인 행만 추출하여 액셀 저장  
17 : 인원수가 6명 이상인 그루만 추출하여 액셀 저장  
* **Code 18**  
엑셀 파일을 CSV파일로 저장  
* **Code 19**  
특정 열만 CSV파일로 저장  
* **Code 20**  
xlsx 액셀 파일 처리 (openxyxl 라이브러리)  
* **Code 21**  
액셀 파일 서식 복사  
* **Code 22**  
이미지 데이터 배열 변수에 저장  
* **Code 23**
이미지 데이터 배열을 저장하여 액셀로 나타내기
## Day03
### SQLite 설치
sqlite-tools-win32-x86 다운로드  
[https://www.sqlite.org/download.html](https://www.sqlite.org/download.html)  
DB Browser SQLite GUI  
[https://sqlitebrowser.org/dl/](https://sqlitebrowser.org/dl/)  
DBeaver 여러가지 DB GUI  
[https://dbeaver.io/download/](https://dbeaver.io/download/)

### SQLite 사용

**SQLite cmd**  
```
.open 데이터베이스이름
```  
없으면 생성하고 있으면 연다  


```
.header on
.mode column
```  
테이블을 좀 예쁘게 보기 위해 사용한다  

### 크롤링 라이브러리
urllib.request로 가져온 html에 필요한 내용을 추출하기 위한 라이브러리
**cmd**  
```
pip3 install bs4
```

### Code
* **code01**  
python SQLite DB연결(DB파일에 직접 연결)  
input에 입력하면 DB테이블에 insert 된다  
* **code02**  
python MySQL DB연결(MySql 접속해서 연결)  
insert, select GUI 화면으로 표현  
* **code03**  
지정된 문자열에 해당 문자가 몇번 썼는지 DB에 저장하는 코드  
* **code04 -웹 크롤링-**  
urillib.request 라이브러리 사용  
nate 메인 페이지 html코드를 읽어 출력하는 코드  
* **code05**  
bs4 사용  
불러온 html에서 \<div>태그만 뽑아 출력하는 코드
\<div>태그를 빼고싶다면 결과에 .text를 붙여주면 된다.
* **code06**  
bs4 사용  
\<ul>태그와 관련된 전체 추출  
\<li>태그중 첫번째만 추출  
findAll('태그명')으로 전체 추출  
세가지 순서대로 나온다  
* **code07**  
\<ul>의 클래스 myClass2를 찾아서 추출  
\<li>의 클래스 myClass3가 들어있는 모든 태그를 추출해서 리스트로 생성  
* **code08**  
\<a>태그를 리스트로 추출
모든 리스트에서 \<a>태그의 href 속성을 출력
* **code09**
CSV 파일을 쓰기모드로 열어 현재 시간을 추출한 후 3초마다 날짜 시간을 기록
* **code10**
nate news사이트에서 news정보 크롤링해서 출력
* **code11**
yes24사이트에서 파이썬 관련된 책을 순위대로 csv에 저장

## Day04
### 외부 라이브러리
#### Numpy
파이썬에서 배열을 처리할때 사용되는 라이브러리 수식 계산을 위한 용도로 많이 사용된다  
장점 빠른 처리 속도  
```
pip install numpy
```
#### pandas
엑셀이 없어도 엑셀의 기능을 파이썬에서 사용할 수 있도록 도와주는 라이브러리  
```
pip install pandas
```
#### matplotlib
파이썬 리스트, 넘파이 배열, 판다스 데이터프레임 또는 시리즈를 그래프로 시각화  
```
pip install matplotlib
```
### Code
**code01, cod02**  
랜덤한 수가 출력되는 5X5배열을 만들어 출력하고 모든 숫자에 100씩 더해서 다시 출력  
Code01은 리스트로 02는numpy를 사용한것  
**code03**  
리스트와 numpy 처리 속도를 계산하는 코드  
**code04 code05**  
2차원 배열을 슬라이싱 하는 코드  
04는 파이썬 리스트로  05는 numpy를 사용하여 슬라이싱 한다 기능은 같지만 numpy방식을 익히면 훨씬 간단하고 빠르게 동작한다.  
**code06**  
numpy를 사용한 GIF파일 영상 처리  
1. 원본 추출
2. 반전 처리
3. 회색 영성 처리
4. 흑백 처리 
 
**code07**  
yes24 홈페이지 [국내도서]->[IT 모바일] 에서 주간 베스트 도서를 크롤링 하여 엑셀 파일로 저장  


















