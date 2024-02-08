import datapane as dp
import pandas as pd

fichero_csv = "DI_U05_A02_02.csv"
df = pd.read_csv(fichero_csv)#Array Bidimensional

datos_diciembre = df[df['Mes']=='Diciembre']
unidades_diciembre = datos_diciembre['Unidades'].sum()

datos_noviembre = df[df['Mes']=='Noviembre']
unidades_noviembre = datos_noviembre['Unidades'].sum()

unidades = dp.BigNumber(heading='Unidades totales en diciembre', 
             value=unidades_diciembre, 
             change=unidades_diciembre - unidades_noviembre, 
             is_upward_change=unidades_diciembre > unidades_noviembre)

report = dp.Report(unidades)
report.save(path='DI_U05_A02_0005.html', open=True)