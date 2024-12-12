import pandas as pd
from datetime import datetime
import os

# todo data loading and cleaning

class DataPreprocessing:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_clean_data(self):

        # 1. load
        data = pd.read_csv(self.file_path)
        df = pd.DataFrame(data)

        # cleaning
        # 2-1. drop : This is only for analyzing my expenses so I will remove the 'Payback' column.
        df = df.drop('Payback', axis=1)

        # 2-2 NULL 값 체크 후 값이 없는 행 전체를 delete 할꺼.
        missing_values = df.isnull().sum()
        print(missing_values)

        null_col = df.columns[df.isnull().sum() > 0]
        # print(null_col.values)
        # df_cleaned = df.dropna(subset=['Amount'])
        df_cleaned = df.dropna(subset=null_col.values)

        #todo 데이터 클리닝 더 해야되는데 일단 다음 스텝으로 고



        # todo When 'data cleaning' is done, I'm going to save it as a csv file

        output_file_path = 'data/bank_tracker.csv'
        # df_cleaned.to_csv(output_file_path, index=False)

        # 파일 존재 여부 확인
        if os.path.exists(output_file_path):
            print(f"File already exists: {output_file_path}. No new file created.")
        else:
            # 파일이 존재하지 않으면 저장
            df_cleaned.to_csv(output_file_path, index=False)
            print(f"Excel file saved as: {output_file_path}")

        if df_cleaned is not None:
            print("Data loaded successfully")
        else:
            print("Failed to load data")

        return df_cleaned




