from model.data_preprocessing import DataPreprocessing
from view.menu_view import MenuView
import pandas as pd
import matplotlib.pyplot as plt
from config.constants import FILE_NAME


class MainController:

    def __init__(self, file_path):
        self.model = DataPreprocessing(file_path)
        self.view = MenuView()

    def start(self):
        df_trs = pd.DataFrame()
        while True:
            self.view.call_menu()
            num = input("Choose an option (1-11): ")

            if num == '0':  # 0. Import a CSV File
                df_cleaned = self.model.load_clean_data()
                df_trs = df_cleaned
                print(df_trs.info())

            elif num == '1':  # 1. View All Transactions
                if df_trs.empty is True:
                    print("Please load your bank data first! Press '0' ")
                else:
                    print(f"----- All Transactions ----- \n {df_trs}")
            elif num == '2':  # 2. View Transactions by Date Range

                if df_trs.empty is True:
                    print("Please load your bank data first! Press '0' ")
                else:
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
                if df_trs.empty is True:
                    print("Please load your bank data first! Press '0' ")
                else:
                    new_date = input("Enter the date (YYYY-MM-DD) : ")
                    new_category = input("Enter the category (e.g., CAFE, MARKET) : ")
                    new_merchant = input("Enter the merchant : ")
                    new_amount = input("Enter the amount : ")

                    new_date = pd.to_datetime(new_date)
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
                    df_trs = df_trs.sort_values(by='Date', ascending=False)

                    # .csv 파일로 저장
                    df_trs.to_csv(FILE_NAME, index=False)

                    print(f"{df_trs} \nTransaction added successfully!")
            elif num == '4':  #4. Edit a Transaction
                if df_trs.empty is True:
                    print("Please load your bank data first! Press '0' ")
                else:
                    print(df_trs)
                    idx = input("Enter the index of the transaction to edit:")
                    index = int(idx)
                    if index in df_trs.index:
                        df_from_idx = df_trs.loc[index]
                        print(f"Current Transaction Details:\n{df_from_idx}")

                        edit_date = input("Enter new date (YYYY-MM-DD) or press Enter to keep current:")
                        edit_merchant = input("Enter new merchant or press Enter to keep current:")
                        edit_amount = input("Enter new amount or press Enter to keep current:")
                        edit_category = input("Enter new category or press Enter to keep current:")

                        if edit_date:
                            df_trs.loc[index, 'Date'] = edit_date
                        if edit_merchant:
                            df_trs.loc[index, 'Merchant'] = edit_merchant
                        if edit_amount:
                            df_trs.loc[index, 'Amount'] = float(edit_amount)
                        if edit_category:
                            df_trs.loc[index, 'Category'] = edit_category

                        # 날짜 순으로 정렬
                        df_trs = df_trs.sort_values(by='Date', ascending=False)

                        # .csv 파일로 저장
                        df_trs.to_csv(FILE_NAME, index=False)

                        print(f"{df_trs} \nTransaction updated successfully!")
                    else:
                        print("Invalid index.")
            elif num == '5':  #5. Delete a Transaction
                if df_trs.empty is True:
                    print("Please load your bank data first! Press '0' ")
                else:
                    print(df_trs)
                    idx = input("Enter the index of the transaction to delete:")
                    index = int(idx)
                    if index in df_trs.index:
                        df_trs = df_trs.drop(index)
                        # .csv 파일로 저장
                        df_trs.to_csv(FILE_NAME, index=False)
                        print(f"{df_trs} \nTransaction deleted successfully!")
                    else:
                        print("Invalid index.")
            elif num == '6':  # 6. Analyze Spending by Category
                if df_trs.empty is True:
                    print("Please load your bank data first! Press '0' ")
                else:
                    print("--- Total Spending by Category ---")
                    category_sums = df_trs.groupby('Category')['Amount'].sum()
                    print(category_sums)
            elif num == '7':  # 7. Calculate Average Monthly Spending
                if df_trs.empty is True:
                    print("Please load your bank data first! Press '0' ")
                else:
                    df_trs['Date'] = pd.to_datetime(df_trs['Date'])
                    df_trs['Month'] = df_trs['Date'].dt.to_period('M')

                    # 월별 지출 총액
                    monthly_sums = df_trs.groupby('Month')['Amount'].sum()
                    print(monthly_sums)
            elif num == '8':  # 8. Show Top Spending Category
                if df_trs.empty is True:
                    print("Please load your bank data first! Press '0' ")
                else:
                    print("--- Top Spending Category ---")
                    category_sums = df_trs.groupby('Category')['Amount'].sum()
                    sorted_category_sums = category_sums.sort_values(ascending=False)

                    print(sorted_category_sums)
            elif num == '9':  # 9. Visualize Monthly Spending Trend
                if df_trs.empty is True:
                    print("Please load your bank data first! Press '0' ")
                else:
                    print("Visualize Monthly Spending Trend")
                    df_trs['Date'] = pd.to_datetime(df_trs['Date'])
                    df_trs['Month'] = df_trs['Date'].dt.to_period('M')

                    # 월별 지출 총액
                    monthly_sums = df_trs.groupby('Month')['Amount'].sum()
                    print(monthly_sums)

                    plt.figure(figsize=(10, 6))
                    monthly_sums.plot(kind='bar', color='skyblue')
                    plt.title('Monthly amount')
                    plt.xlabel('Month')
                    plt.ylabel('Total')
                    plt.show()

                    # 카테고리별 지출금액
                    category_expenses = df_trs.groupby('Category')['Amount'].sum()

                    plt.figure(figsize=(7, 7))
                    category_expenses.plot(
                        kind='pie',
                        autopct='%1.1f%%',  # 퍼센트 표시
                        colors=plt.cm.Pastel1.colors,
                        legend=False  # 범례 제거
                    )
                    plt.title('Expenditure Amount by Category')
                    plt.ylabel('')
                    plt.show()

            elif num == '10':  # 10. Save Transactions to CSV
                if df_trs.empty is True:
                    print("Please load your bank data first! Press '0' ")
                else:
                    file_name = input("Enter file name to save (e.g., 'transactions.csv'):")
                    df_trs.to_csv(f"data/{file_name}", index=False)
                    print(f"Transactions saved to {file_name} successfully!")
            elif num == '11':
                print("Exiting the Personal Finance Tracker. Goodbye!")
                break
            elif num not in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11'):
                print("WRONG NUMBER!! Please enter from 0 to 11")
