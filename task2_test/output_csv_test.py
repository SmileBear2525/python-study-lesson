import pandas

def output_csv():

	nums = []
	for num in range(5):
		print(num)
		nums.append(num)

	members = []
	memberlist = ['久保','南野','山田','成岡','スズキ']
	for mem in memberlist:
		print(mem)
		members.append(mem)

	df = pandas.DataFrame({"NO":nums,"メンバー":members})
	df.to_csv(f'csv_test.csv')

if __name__ == '__main__':
	output_csv()