jumin = "981231-1234567"
#내가 생년만 꺼내오는것들을 슬라이싱

print("성별 : " +jumin[7])
print("연 : " + jumin[0:2])
print("월 : "+jumin[2:4])
print("일  : " +jumin[4:6])
print("생년월일 : "+jumin[:6])#처음부터 6직전까지
print("뒤 7자리 :" + jumin[7:])# 7번째부터 끝까지
print("뒤 7자리(뒤에서부터) : "+jumin[-7:])