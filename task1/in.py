# 参考URL
# https://note.nkmk.me/python-in-basic/


# inによる演算はbool値(True, Flase)を返す

# 0,1,2の中に1が含まれるか？
print(1 in [0, 1, 2])

# 0,1,2の中に100が含まれるか？
print(100 in [0, 1, 2])

# タプルは()で括る
print(1 in (0, 1, 2))

# 集合setは{}で括る
print(1 in {0, 1, 2})

# range
print(1 in range(3))


l = [0, 1, 2]
i = 100

if i in l:
	print('{} is a member of {}.'.format(i, l))
else:
	print('{} is not a member of {}'.format(i, l))

# リストやタプル、文字列などは空だとFalse
# 空でなければ、Trueと判定される

l = []
if l:
	print('not empty')
else:
	print('empty')

l = [0, 1, 2, 3, 4]
print(sum(i > 2 for i in l))
# 3, 4がTrueになり、True(=1)の合計値が2となる

# 辞書dictに対するin
# 辞書dictをそのままin演算で使うと、キーに対する判定となる
d = {'key1' : 'value1', 'key2' : 'value2', 'key3' : 'value3'}
print('key1' in d) #True
print('value1' in d) #False
#値あるいはキーと値の組み合わせに対して処理したい場合はvalues(), items()を使う
print('value1' in d.values())  #True
print(('key1','value1') in d.items()) #True
print(('key1','value2') in d.items()) #False

#文字列strに対するin
print('a' in 'abc')
print('x' in 'abc')
print('ab' in 'abc')
print('ac' in 'abc')

# not in
print(10 not in [0, 1, 2])
print(not 10 in [0, 1, 2])

# 複数の要素に対するin
print([0, 1] in [0, 1, 2]) #Flase
print([0, 1] in [[0, 1], [1, 0]]) #True

# and orを使う
l = [0, 1, 2]
v1 = 0
v2 = 100
print(v1 in l and v2 in l) #False
print(v1 in l or v2 in l) #True
print((v1 in l) or (v2 in l)) #True

# 集合setを使う
# set()で集合に変換
l1 = [0, 1, 2, 3, 4]
l2 = [0, 1, 2]
l3 = [0, 1, 5]
l4 = [5, 6, 7]
print(set(l2) <= set(l1)) #True
print(set(l3) <= set(l1)) #False

# l1とl4が互いに素
print(set(l1).isdisjoint(l4)) #True
# l1とl3の要素に少なくとも一つは含まれている
print(not set(l1).isdisjoint(l3)) #True

# inの計測速度
# listは遅い、探す値の位置によって処理時間が変わる
# 集合setは早い、探す値によって処理時間が大きく変わることもない


