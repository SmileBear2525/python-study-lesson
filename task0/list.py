# リスト
num_list = [1,2,3,4,5,6,7,8,9,10]

print(num_list)

# forとif
# for num in num_list:
# 	print(num)

# for num in range(1,100):
# 	if num % 2 == 0:
# 		print(f"{num}は偶数です")
# 	else:
# 		print(f"{num}は奇数です")

for number in range(1,101):
	if number % 3 == 0:
		print(f"{number}は３で割り切れます")
	if number % 5 == 0:
		print(f"{number}は５で割り切れます")
	if number % 3 == 0 and number % 5 == 0:
		print(f"{number}は３と５で割り切れます")