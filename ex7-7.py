def 民國_to_西元(民國_year):
    return 民國_year + 1911

def 西元_to_民國(西元_year):
    return 西元_year - 1911

民國 = int(input("請輸入民國年:"))
print ("對應的西元年是：", 民國_to_西元(民國))

西元 = int(input("請輸入西元年:"))
print ("對應的民國年是：", 西元_to_民國(西元))
