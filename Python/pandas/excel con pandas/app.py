
import pandas as pd
from datetime import datetime, date


'%Y-%m-%d %H:%M:%S'
parametro = 'temperatura'
dates = ['2018-06-29 08:15:27', '2019-06-29 08:15:27', '2020-06-29 08:15:27', '2021-06-29 08:15:27', '2018-06-29 08:15:27', '2019-06-29 08:15:27', '2020-06-29 08:15:27', '2021-06-29 08:15:27', '2018-06-29 08:15:27', '2019-06-29 08:15:27', '2020-06-29 08:15:27', '2021-06-29 08:15:27', '2018-06-29 08:15:27', '2019-06-29 08:15:27', '2020-06-29 08:15:27', '2021-06-29 08:15:27', '2018-06-29 08:15:27', '2019-06-29 08:15:27', '2020-06-29 08:15:27', '2021-06-29 08:15:27', '2018-06-29 08:15:27', '2019-06-29 08:15:27', '2020-06-29 08:15:27', '2021-06-29 08:15:27', '2018-06-29 08:15:27', '2019-06-29 08:15:27', '2020-06-29 08:15:27', '2021-06-29 08:15:27', '2018-06-29 08:15:27', '2019-06-29 08:15:27', '2020-06-29 08:15:27', '2021-06-29 08:15:27', '2018-06-29 08:15:27', '2019-06-29 08:15:27', '2020-06-29 08:15:27', '2021-06-29 08:15:27', '2018-06-29 08:15:27', '2019-06-29 08:15:27', '2020-06-29 08:15:27', '2021-06-29 08:15:27']
datetimes = [datetime.strptime(date, '%Y-%m-%d %H:%M:%S') for date in dates]

values = [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]


df = pd.DataFrame({'Date and time': datetimes, parametro:values})

writer = pd.ExcelWriter(
    "pandas_datetime.xlsx",
    engine='xlsxwriter',
    datetime_format='dd/mm/yyyy hh:mm:ss',
)

df.to_excel(writer, sheet_name=parametro)
workbook  = writer.book
worksheet = writer.sheets[parametro]
worksheet.set_column('B:C', 20)



writer.save()