# convert_excel_csv.py

import pandas as pd

# file_path='japanese_whisky.xlsx'
file_name='final_data4'

file_path=f'{file_name}.xlsx'

df = pd.read_excel(file_path)

df.to_csv(f'{file_name}.csv', index=False)
print("Excel file converted to CSV successfully.")