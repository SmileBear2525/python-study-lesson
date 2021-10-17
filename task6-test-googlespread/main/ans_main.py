import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '.env'))
from dotenv import load_dotenv
load_dotenv() #環境変数のロード
import request as req

from spread_sheet_manager import SpreadsheetManager
#from spread_sheet_manager import SpreadsheetManager
#from engine.yahoo import YahooAPI

SPREADSHEET_ID = os.environ["SPREADSHEET_ID"]
print(SPREADSHEET_ID)

def main():
    # jan一覧の取得
    # 「jan_test」のワークシートがあることが条件、ワークシートが存在しない場合エラーになる
    ss = SpreadsheetManager()
    ss.connect_by_sheetname(SPREADSHEET_ID, "jan_list")
    jan_df = ss.fetch_all_data_to_df()
    jan_list = jan_df["jan"].values.tolist()
    print(jan_list)
    
    #YahooAPI
    # items = []
    # for jan in jan_list:
    #     print(jan)
    #     item = YahooAPI.fetch_item(jan[0])
    #     if item:
    #         items.append(item.__dict__)

    #RakutenAPI------------------
    worksheetname = 'item_list'
    #ワークシート存在チェック
    exist_worksheet = ss.exist_worksheet(SPREADSHEET_ID, worksheetname)
    #ワークシートが存在していなければワークシートの追加
    if exist_worksheet == None:
        worksheet = ss.add_worksheet(SPREADSHEET_ID, worksheetname)
    else:
        worksheet = exist_worksheet
    
    #楽天APIリクエストURL
    url = "https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706?format=json&applicationId=1017111620275786286&keyword={}"
    keyword = "Pythonプログラミング入門"

    #リクエスト実行
    response = req.get_api(url.format(keyword))

    #商品情報要素取得
    dic_element_name = 'Item'
    dict_item_sub = {'itemName':'商品名','itemPrice':'価格'}

    #ワークシートヘッダの追加
    for i,(key,value) in enumerate(dict_item_sub.items()):
        worksheet.update_cell(1, i+1, value)
    #ws.update_cell(1,1,"test1")
    
    #関数を使ってレスポンス情報のサブ階層取得
    items = req.get_response_api_sub(response['Items'], dic_element_name, dict_item_sub)
    #RakutenAPI------------------

    # 書き込み
    ss.connect_by_sheetname(SPREADSHEET_ID, worksheetname)
    ss.list_insert(items)
    #ss.bulk_insert(items)


main()
