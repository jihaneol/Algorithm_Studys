def solution(bin1, bin2):
    answer = bin(int(bin1,2) + int(bin2,2))[2:] #앞에 문자 생략
    return answer

# bin1	bin2	result
# "10"	"11"	"101"
# "1001"	"1111"	"11000"