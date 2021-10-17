#参考URL
#https://note.com/npaka/n/nd522e980d995

import gspread
from oauth2client.service_account import ServiceAccountCredentials

#####ここが重要#####
JSON_PATH = '../../python-study-329306-496b88f91109.json'	#サービスアカウントキーのパス
SHEET_NAME = 'python-study-task6'	#スプレッドシートのファイル名

# スプレッドシートとの接続
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name(JSON_PATH, scope)
gc = gspread.authorize(credentials)
worksheet = gc.open(SHEET_NAME).sheet1

# スプレッドシートの読み書き
worksheet.update_acell('A1', 'Hello World!')
print(worksheet.acell('A1'))