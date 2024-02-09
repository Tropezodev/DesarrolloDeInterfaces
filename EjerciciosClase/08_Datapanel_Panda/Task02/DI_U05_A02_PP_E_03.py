import datapane as dp
import pandas as pd

fichero_csv="DI_U05_A02_PP_E_01.csv"
df=pd.read_csv(fichero_csv)

data_table=dp.DataTable(df)
datos_2021 = df[df['Año']==2021]
unidades_2021 = datos_2021['Ventas'].sum()

datos_2017 = df[df['Año']==2017]
unidades_2017 = datos_2017['Ventas'].sum()

unidades = \
dp.BigNumber(heading='Ventas totales en 2021', 
             value=unidades_2021, 
             change=unidades_2021 - unidades_2017, 
             is_upward_change=unidades_2021 > unidades_2017)

titulo = dp.HTML('''
<p style="font-size:30px;text-align:center;color:#ffffff;background-color:#4d4d4d;">
    Informe de ventas
</p>''')
fichero = dp.Attachment(file='DI_U05_A02_PP_E_01.csv')
texto = dp.Text('**Puedes descargar el fichero con los datos del informe.**')
imagen = dp.Media(file='DI_U05_A02_PP_E_02.jpg')

report = dp.Report(imagen, titulo, unidades,data_table, texto, fichero)
report.save(path='DI_U05_A02_PP_E_06.html', open=True)





