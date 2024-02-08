import datapane as dp
import pandas as pd

fichero_csv = "DI_U05_A02_02.csv"
df = pd.read_csv(fichero_csv)

table = dp.Table(df)
data_table = dp.DataTable(df)
report = dp.Report(table, data_table)
report.save(path='DI_U05_A02_03.html', open=True)