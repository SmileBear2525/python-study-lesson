#Pythonクラス

class TestClass:
	x = "変数１"

	def test_method(self):
		print(self.x)

	def test_method2(self, arg1):
		print("引数１：" + arg1)

testclass = TestClass()
testclass.test_method()
testclass.test_method2("あいうえお")

#オーバーロードはできない
#最後に定義したメソッドが有効になる

#コンストラクタ
class TestClass2:
	val = []
	def __init__(self):
		print("init:" + str(self.val))
		#初期化
		self.val.append(1)
		self.val.append(2)
		self.val.append(3)

	def test_method(self):
		print("test_method" + str(self.val))

testclass2 = TestClass2()
testclass2.test_method()

#コンストラクタに引数を渡すことも可能
class TestClass3():
	val = []
	def __init__(self, arg1, arg2):
		self.val.append(arg1)
		self.val.append(arg2)
		print("init:" + str(self.val))

testclass3 = TestClass3(3,5)

#デストラクタ
#デストラクタの定義はdel
class TestClass4:
	val = []
	def __del__(self):
		print("del:クラス削除（デストラクタ）")

testclass4 = TestClass4()
del testclass4

#引数：クラス変数とインスタンス変数
class TestClass5:
	val = "クラス変数"
	def __init__(self, arg):
		self.x = arg

testclass5_1 = TestClass5("インスタンス変数１")
testclass5_2 = TestClass5("インスタンス変数２")
print(TestClass5.val)
print(testclass5_1.x)
print(testclass5_2.x)
print(testclass5_1.val)

#引数：クラス変数とインスタンス変数（どちらも変数名が同じ場合）
class TestClass6:
	val = "クラス変数"
	def __init__(self, arg):
		self.val = arg

testclass6 = TestClass6("インスタンス変数")
print(TestClass6.val)
print(testclass6.val) #インスタンス変数が優先
del testclass6.val
print(testclass6.val)

#継承
class Parent:
	parent_val = "Parent"
	def parent_function(self):
		print("ParentMethod:" + self.parent_val)

class Child(Parent): #Parentを継承したクラスChild
	child_val = "Child"
	def child_function(self):
		print("ChildMethod:" + self.child_val)

child = Child()
print(child.parent_val)
print(child.child_val)
child.parent_function()
child.child_function()

#継承（継承先と継承元が同じ名前の変数の場合）
class Parent1:
	val = "Parent1"
	def all_function(self):
		print("Parent1Method:" + self.val)

class Child1(Parent1): #Parent1を継承したクラスChild1
	val = "Child1"
	def all_function(self):
		print("Child1Method:" + self.val)

parent1 = Parent1()
print(parent1.val)	#Parent1
parent1.all_function() #Parent1Method:Parent1
child1 = Child1() #作成したインスタンスの内容が優先される
print(child1.val)	#Child1
child1.all_function() #Child1Method:Child1

#継承：super()で継承元の変数を呼び出し
class Parent2:
    val = "Parent2"
    def all_function(self):
        print("Parent2Method:" + self.val)

class Child2(Parent2):
    val = "Child2"
    def all_function(self):
        print("Child2Method:" + self.val)
        super().all_function()

child2 = Child2()
child2.all_function() #superで呼び出しても作成したインスタンスの内容が優先される

#継承：コンストラクタ
class Parent_Construct:
    def __init__(self):
        print("Parentコンストラクタ")

class Child_Construct(Parent_Construct):
    def __init__(self):
        print("Childコンストラクタ")

child_c = Child_Construct() #作成したインスタンスのコンストラクタが呼び出される

#継承：コンストラクタ＋super()
class Parent_Construct1:
    def __init__(self):
        print("Parent1コンストラクタ")

class Child_Construct1(Parent_Construct1):
    def __init__(self):
        super().__init__()
        print("Child1コンストラクタ")

child_c1 = Child_Construct1() #継承元のコンストラクタを呼び出したい場合、継承先コンストラクタ内で継承元のコンストラクタを呼び出し

#staticメソッド
#staticメソッドとはインスタンスを生成しなくてもクラスから直接呼び出すことができるメソッド
#定義は@staticmethod
class TestStaticMethod:
	@staticmethod
	def function():
		print("staticメソッド")

TestStaticMethod.function() #インスタンスを生成しなくてもクラスから直接呼び出し可能
testStaticMethod = TestStaticMethod()
testStaticMethod.function()

#classメソッド
#定義は@classmethod
class TestClassMethod:
	@classmethod
	def function(cls):
		print("classメソッド:{}".format(cls))

TestClassMethod.function()
testClassMethod = TestClassMethod()
testClassMethod.function()

#staticメソッドとclassメソッドの違い、使い分け
#staticメソッドはクラスを引数に受け取らないので、クラスに依存しないメソッドの定義に利用
#classメソッドはクラウを引数に受け取るので他のクラスメソッドを呼び出すことが可能なため、クラスに依存したメソッドの定義に利用
