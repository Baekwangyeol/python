address = "http://daum.com"

address = address.replace("http://","")#규칙1
a= address.find(".")
address = address[:a] #규칙2
password = address[0:3] + str(len(address))+str(address.count("e"))+"!"

print(password)
