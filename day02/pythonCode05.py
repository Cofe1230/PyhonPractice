#singer1 읽어서 new_singer3로 저장
#이름 , 국번, 전화번호 전화번호가 없을경우 저장안한다
with open("C:/pythonwork/CSV/singer1.csv", "r") as inFp :
    with open("C:/pythonwork/CSV/new_singer3.csv", "w") as outFp:
        header = inFp.readline()
        header = header.strip()
        header_list= header.split(',')
        idx1 = header_list.index('이름')
        idx2 = header_list.index('국번')
        idx3 = header_list.index('전화 번호')
        header_list = [header_list[idx1], header_list[idx2], header_list[idx3]]
        header_str = ','.join(map(str, header_list))
        outFp.write(header_str + '\n')
        for inStr in inFp:
            inStr = inStr.strip()
            row_list = inStr.split(',')
            if row_list[idx3] != "" :
                row_list = [row_list[idx1], row_list[idx2], row_list[idx3]]
                row_str = ','.join(map(str, row_list))
                outFp.write(row_str + '\n')

print('Save. OK~')
