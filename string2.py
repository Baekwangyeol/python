python = "Python is Amazing"
print(python.lower())#소문자
print(python.upper())#대문자
print(python[0].isupper())#괄호안 숫자자리가 대문자인지 체크
print(len(python))#문자 길이 반환
print(python.replace("Python", "JAVA"))#원하는글자 바꿔서 출력

index = python.index("n")#문자의 위치 알려줌

print(index)

index = python.index("n", index+1)#뒷자리 n의 위치찾기

print(index)

print(python.find("n"))#똑같이 찾는것 
print(python.find("java"))# index와 다른점 find는 찾는글자가 없으면 -1을반환
# print(python.index("java")) index는 없으면 에러발생 다음줄들이 실행x

print(python.count("n"))#n이 몇번 나왔는지 카운트

