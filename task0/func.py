# print("関数の外")

def test(num):
	for i in range(num):
		print(f"関数の中:{i}")


# def sum(a, b):
# 	return a + b

# c = sum(1, 5)
# print(c)

def sigma(num):
	total = 0
	for i in range(1,num+1):
		total += i
	return total

print(sigma(5))

#関数名：動詞+名詞