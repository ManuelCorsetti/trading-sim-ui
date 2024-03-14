import pandas as pd
import os

script_path = os.path.abspath(__file__)

script_dir = os.path.dirname(script_path)
parent_dir = os.path.dirname(script_dir)
data_dir = os.path.join(parent_dir, "data/ticker_names")
sp500_path = os.path.join(data_dir, "sp500.csv")

sp500 = pd.read_csv(sp500_path)

print(sp500.head())
print(sp500.columns)

# def download_sp500_list():
#     url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
#     tables = pd.read_html(url, header=0)  # Read all tables from the webpage
#     sp500_table = tables[0]  # The first table is usually what we need
#     return sp500_table

# # Usage
# sp500_df = download_sp500_list()
# sp500_df.to_csv('../data/sp500_2.csv', index=False)


# import pandas as pd

# headers = [header.text.strip() for header in table.find_all('th')]

# table_data = []

# for row in table.find_all('tr'):
#     table_data.append([cell.text.strip() for cell in row.find_all('td')])

# df = pd.DataFrame(table_data, columns=headers)
# df.dropna(how='all', inplace=True)
# df.set_index("No.", inplace=True)
