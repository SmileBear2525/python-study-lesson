import os
import sys
import time

sys.path.append(os.path.join(os.path.dirname(__file__), '.env'))
from dotenv import load_dotenv
load_dotenv() #環境変数のロード
import request as req
from spread_sheet_manager import SpreadsheetManager
import ast

# GOOGLEスプレッドシート
SPREADSHEET_ID = os.environ["SPREADSHEET_ID"]
SHEET_NAME = os.environ["SPREADSHEET_SHEET_NAME"]

# 楽天API
RAKUTEN_API_URL = os.environ["RAKUTEN_API_URL"]
RAKUTEN_API_APPID = os.environ["RAKUTEN_API_APPID"]
RAKUTEN_API_KEYWORD = os.environ["RAKUTEN_API_KEYWORD"]
RES_TOP_ELEMENT_NAME = os.environ["RAKUTEN_API_GET_TOP_ELEMENT_NAME"]
RES_SUB_ELEMENT_NAME = os.environ["RAKUTEN_API_GET_SUB_ELEMENT_NAME"]

#ワークシート存在チェック(存在していなければ作成)
def check_worksheet(spreadmanager, file_id, sheetname):
  exist_worksheet = spreadmanager.exist_worksheet(file_id, sheetname)
  #ワークシートが存在していなければワークシートの追加
  if exist_worksheet == None:
    worksheet = spreadmanager.add_worksheet(file_id, sheetname)
  else:
    worksheet = exist_worksheet
  return worksheet

#ワークシートヘッダの追加
def add_worksheet_header(wksheet, dict_item):
  for i,(key,value) in enumerate(dict_item.items()):
    wksheet.update_cell(1, i+1, value)

#楽天APIリクエスト
def request_API():
  #楽天APIリクエスト
  params = {
    "format": "jason",
		"applicationId": RAKUTEN_API_APPID,
		"keyword" : RAKUTEN_API_KEYWORD	
  }
  #リクエスト実行
  response = req.get_api_param(RAKUTEN_API_URL, params)
  return response

#ワークシートへ書き込み
def write_worksheet(spreadmanager, file_id, sheet_name, itemlist):
  spreadmanager.connect_by_sheetname(file_id, sheet_name)
  spreadmanager.list_insert(itemlist)


def main():
  #処理前の時刻
  t1 = time.time()

  #クラス呼び出し
  ss = SpreadsheetManager()
  
  #楽天APIリクエスト実行
  res = request_API()
  
  #レスポンス情報のサブ階層取得
  items = req.get_response_api_sub(res['Items'], RES_TOP_ELEMENT_NAME, ast.literal_eval(RES_SUB_ELEMENT_NAME))

  print("スレッド使用なし")
  t2 = time.time()
  middle_time = t2-t1
  print(f"スレッド使用なし---途中経過時間：{middle_time}")  

  #ワークシート存在チェック
  ws = check_worksheet(ss, SPREADSHEET_ID, SHEET_NAME)

  #ワークシートヘッダー追加
  add_worksheet_header(ws, ast.literal_eval(RES_SUB_ELEMENT_NAME))

  # ワークシートへ書き込み
  write_worksheet(ss, SPREADSHEET_ID, SHEET_NAME, items)

  # 処理後の時刻
  t3 = time.time()
 
  # 経過時間を表示
  elapsed_time = t3-t1
  print(f"スレッド使用なし---経過時間：{elapsed_time}")  


if __name__ == "__main__":
  main()

