import os
import sys
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
sys.path.append(os.path.join(os.path.dirname(__file__), '.env'))
from dotenv import load_dotenv
load_dotenv() #環境変数のロード

JSONKEY = os.environ["SPREADSHEET_JSONKEY"]

class SpreadsheetManager():

    def __init__(self):
        self.worksheet = None

    #追加：ワークシート存在チェック
    def exist_worksheet(self, file, sheet_name):
        credentials = ServiceAccountCredentials.from_json_keyfile_name(JSONKEY, gspread.auth.DEFAULT_SCOPES)
        gs = gspread.authorize(credentials)
        worksheets = gs.open_by_key(file).worksheets()
        for sheet in worksheets:
            #print(sheet.title)
            if sheet.title == sheet_name:
                return sheet
        return None

    #追加：ワークシート追加
    def add_worksheet(self, file, sheet_name):
        credentials = ServiceAccountCredentials.from_json_keyfile_name(JSONKEY, gspread.auth.DEFAULT_SCOPES)
        gs = gspread.authorize(credentials)
        worksheet = gs.open_by_key(file).add_worksheet(title=sheet_name, rows=100, cols=20)    
        return worksheet

    def connect_by_sheetname(self, file_id, sheet_name):
        credentials = ServiceAccountCredentials.from_json_keyfile_name(JSONKEY, gspread.auth.DEFAULT_SCOPES)
        gs = gspread.authorize(credentials)
        self.worksheet = gs.open_by_key(file_id).worksheet(sheet_name)
    
    def fetch_all_data(self):
        try:
            data = self.worksheet.get_all_values() # セルに数式が埋め込まれている場合は数式を計算した結果を取得
            return data
        except Exception as e:
            if e.args[0].get('code') == 429:
                raise Exception("スプレッドシート更新回数の上限です")

    def fetch_all_data_to_df(self):
        try:
            data = self.fetch_all_data()
            if not data:
                raise Exception("data is None")
            return pd.DataFrame(data[1:], columns=data[0:1])
        except Exception as e:
            if e.args[0].get('code') == 429:
                raise Exception("スプレッドシート更新回数の上限です")
    
    def list_insert(self, datas:list):
        '''
        listを指定してスプレッドシートを一括更新
        '''
        begin_row = self.get_last_row() + 1 # 最終行の次の行から始める
        header = self.init_fetch_sheet_header()
        cells = self.worksheet.range(begin_row, 1, len(datas) + begin_row -1 , len(header))
        #print(cells)
        for row,data in enumerate(datas):
            #print(row)
            #print(data)
            for d in data:
                try:
                    col = data.index(d)
                    num = row*(len(header)) + col # 複数行にまたがるデータの場合でも１次元配列に格納されているため２次元→１次元に変換する
                    #print(f"{col}:{num}")
                    # print(data)
                    cells[num].value = d
                except Exception as e:
                    print(e)
                    pass

        self.worksheet.update_cells(cells)
        return True

    def init_fetch_sheet_header(self, header_row: int=1):
        df = pd.DataFrame(self.worksheet.get_all_values())
        #print(df)
        #print(header_row)
        #print(df.loc[header_row-1,:])
        return list(df.loc[header_row-1,:]) 


    def get_last_row(self):
        '''
        最終行の取得
        '''
        return len(self.worksheet.get_all_values())