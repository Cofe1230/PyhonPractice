import random

#전역 변수
imageList = []
value = 0
ROW = COL = 5

#메인 코드
if __name__=="__main__" :
    for i in range(0,ROW) :
        tmpList = []
        for k in range(0, COL):
            value = random.randrange(0,255)
            tmpList.append(value)
        imageList.append(tmpList)

    print('## 원본 2차원 배열 ##')
    for i in range(0, ROW) :
        for k in range(0, COL) :
            print("%03d" % imageList[i][k], end = " ")
        print("")
    print("")

    for i in range(0, ROW) :
        for k in range(0, COL) :
            imageList[i][k] = 255 - imageList[i][k]

    print('## 반전된  배열 ##')
    for i in range(0, ROW) :
        for k in range(0, COL) :
            print("%03d" % imageList[i][k], end = " ")
        print("")
    print("")
