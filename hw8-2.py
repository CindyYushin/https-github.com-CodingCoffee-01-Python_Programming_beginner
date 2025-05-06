numbers = [] 

print("Please input 10 numbers，按 Enter check：")

for i in range(10):
    input = input(f"第 {i+1} 個數字是？")
    number = int(input)  
    numbers.append(number) 

sum = sum(numbers)  
average = average / 10  

print(f"These numbers average is：{average}")
