# 参考URL
# https://note.nkmk.me/python-file-io-open-with/
# https://note.nkmk.me/python-pathlib-file-open-read-write-unlink/

# 新しくディレクトリを作成、その中に新たなファイルパスを指定
import pathlib
import os
#exist_okはTrueにすると末端ディレクトリが存在していなければ新規作成するし、存在してイナkレバ何もしない。
#つまり、前もって末端ディレクトリの存在確認をする必要がないので便利
os.makedirs('temp', exist_ok=True)
p_empty = pathlib.Path('temp/empty_file.txt') #この時点でフォルダは作成されたがファイルは作成されていない
print(p_empty) #temp/empty_file.txt
print(type(p_empty)) #<class 'pathlib.PosixPath'>

# ファイルの確認
print(p_empty.exists())
# touchで空ファイルが作成される
p_empty.touch()
print(p_empty.exists())

# 再度touchを実行するとタイムスタンプが更新される
p_empty.touch()
# 引数exist_ok=Falseとすると既存ファイルに対してはエラーになる
## p_empty.touch(exist_ok=False)
# 中間ディレクトリが存在しない場合はエラーになる
## pathlib.Path('temp/new_dir/empty_file.txt').touch()

# 中間ディレクトリが存在しない場合、親ディレクトリのPathオブジェクトをparent属性で取得し得てmkdir()でディレクトリを作成してからttouch()を実行
p_empty_new = pathlib.Path('temp/new_dir/empty_file.txt')
p_empty_new.parent.mkdir(parents=True,exist_ok=True)
p_empty_new.touch()