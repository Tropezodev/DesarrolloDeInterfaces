import datapane as dp
import pandas as pd

fichero_csv = "DI_U05_A02_PP_E_01_Modificado.csv"
df = pd.read_csv(fichero_csv)

table = dp.Table(df)
data_table = dp.DataTable(df)

datos_2022 = df[df['Anio']==2022]
asistencia_2022 = datos_2022['Asistencia'].sum()

datos_2021 = df[df['Anio']==2021]
asistencia_2021 = datos_2021['Asistencia'].sum()

asistencia = \
dp.BigNumber(heading='Asistencia en 2022', 
             value=asistencia_2022, 
             change=asistencia_2022 - asistencia_2021, 
             is_upward_change=asistencia_2022 > asistencia_2021)

titulo = dp.HTML('''
<p style="font-size:30px;text-align:center;color:#ffffff;background-color:#4d4d4d;">
    Informe de Asistencia a Eventos
</p>''')
fichero = dp.Attachment(file='DI_U05_A02_PP_E_01_Modificado.csv')
texto = dp.Text('**Puedes descargar el fichero con los datos del informe.**')
imagen = dp.Media(file='pepehonk.png')

report = dp.Report(imagen, titulo, asistencia,data_table, texto, fichero)
report.save(path='ExamenT2.html', open=True)