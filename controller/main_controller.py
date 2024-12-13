from model.data_preprocessing import DataPreprocessing
from view.menu_view import MenuView
import pandas as pd
from datetime import datetime


class MainController:

    def __init__(self, file_path):
        self.model = DataPreprocessing(file_path)
        self.view = MenuView()
        # self.model.load_clean_data()

    def start(self):
        df_trs = pd.DataFrame()
        """Start the main menu loop."""
        while True:
            self.view.call_menu()
            num = input("Choose an option (1-11): ")

            if num == '0':  # 0. Import a CSV File
                df_cleaned = self.model.load_clean_data()
                df_trs = df_cleaned
                print(df_trs.info())

            elif num == '1':  # 1. View All Transactions
                print(f"----- All Transactions ----- \n {df_trs}")
            elif num == '2':  # 2. View Transactions by Date Range
                # Date 컬럼을 datetime 형식으로 변환
                df_trs['Date'] = pd.to_datetime(df_trs['Date'])
                start_date = input("Enter the start date (YYYY-MM-DD) : ")
                end_date = input("Enter the end date (YYYY-MM-DD) : ")

                # 날짜 범위 필터링
                print(f"--- Transactions from {start_date} to {end_date} ---")
                filtered_df_trs = df_trs[(df_trs['Date'] >= start_date) & (df_trs['Date'] <= end_date)]
                if filtered_df_trs is None:
                    print("No transactions found in this date range.")
                else:
                    print(filtered_df_trs)

            elif num == '3':  # 3. Add a Transaction
                new_date = input("Enter the date (YYYY-MM-DD) : ")
                new_category = input("Enter the category (e.g., CAFE, MARKET) : ")
                new_merchant = input("Enter the merchant : ")
                new_amount = input("Enter the amount : ")

                # 새로운 행 생성
                new_transaction = {
                    'Date': new_date,
                    'Merchant': new_merchant,
                    'Amount': new_amount,
                    'Category': new_category
                }

                # 기존 데이터프레임에 추가
                df_trs = df_trs._append(new_transaction, ignore_index=True)

                # 날짜 순으로 정렬
                df_trs.sort_values('Date', ascending=False, inplace=True)

                # .csv 파일로 저장
                # timestamp = datetime.now().strftime("%Y%m%d_%H%M")
                # output_file_path = f'data/bank_tracker_{timestamp}.csv'
                output_file_path = f'data/bank_tracker.csv'
                df_trs.to_csv(output_file_path, index=False)

                print("Transaction added successfully!")
            elif num == '4':  #4. Edit a Transaction
                idx = input("Enter the index of the transaction to edit:")
                df_from_idx = df_trs.loc[int(idx)]
                print(f"Current Transaction Details:\n{df_from_idx}")

                edit_date = input("Enter new date (YYYY-MM-DD) or press Enter to keep current:")
                edit_merchant = input("Enter new merchant or press Enter to keep current:")
                edit_amount = input("Enter new amount or press Enter to keep current:")
                edit_category = input("Enter new category or press Enter to keep current:")

                if edit_date is not None:
                    df_trs.loc[int(idx), 'Date'] = edit_date
                if edit_merchant is not None:
                    df_trs.loc[int(idx), 'Merchant'] = edit_merchant
                if edit_amount is not None:
                    df_trs.loc[int(idx), 'Amount'] = float(edit_amount)
                if edit_category is not None:
                    df_trs.loc[int(idx), 'Category'] = edit_category

                print(df_trs)
                # print(df_from_idx)
