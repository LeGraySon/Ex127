import pandas as pd

file_path = "SampleData2.csv"
df = pd.read_csv(file_path)

def print_all_data():
    print(df)

def sort_by_price():
    sorted_df = df.sort_values(by='Price', ascending=True)
    return sorted_df

def search_symbol_and_reduce(symbol):
    df.loc[df['Symbol'] == symbol, 'Price'] /= 2
    return df[df['Symbol'] == symbol]

def add_usd_column():
    df['USD'] = df['Price'] / 23
    return df

def add_new_row(symbol, price, pe):
    usd = price / 23
    new_row = pd.DataFrame({'Symbol': [symbol], 'Price': [price], 'PE': [pe], 'USD': [usd]})
    global df
    df = pd.concat([df, new_row], ignore_index=True)
    return df

def group_and_statistics():
    grouped = df.groupby('Group').agg({'Price': ['mean', 'sum', 'count']})
    return grouped

def delete_by_symbol(symbol):
    global df
    df = df[df['Symbol'] != symbol]
    return df

if __name__ == "__main__":
    while True:
        print("\nChọn chức năng:")
        print("1. In toàn bộ dữ liệu")
        print("2. Sắp xếp dữ liệu theo Price tăng dần")
        print("3. Nhập Symbol để giảm Price xuống 1/2")
        print("4. Thêm cột USD với giá trị = Price / 23")
        print("5. Thêm dòng dữ liệu mới")
        print("6. Nhóm dữ liệu theo Group và thống kê")
        print("7. Xóa dòng theo Symbol")
        print("8. Thoát")

        choice = input("Nhập lựa chọn (1-8): ")

        if choice == "1":
            print_all_data()
        elif choice == "2":
            result = sort_by_price()
            print(result)
        elif choice == "3":
            symbol = input("Nhập Symbol để tìm: ").strip()
            result = search_symbol_and_reduce(symbol)
            print(result)
        elif choice == "4":
            add_usd_column()
            print(df)
        elif choice == "5":
            symbol = input("Nhập Symbol: ").strip()
            price = float(input("Nhập Price: "))
            pe = float(input("Nhập PE: "))
            result = add_new_row(symbol, price, pe)
            print(result)
        elif choice == "6":
            result = group_and_statistics()
            print(result)
        elif choice == "7":
            symbol = input("Nhập Symbol cần xóa: ").strip()
            result = delete_by_symbol(symbol)
            print(result)
        elif choice == "8":
            print("Thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng nhập lại.")
