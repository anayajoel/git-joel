# 3. Análisis de visitas semanales (30%)
# Archivos: semana1.csv y semana2.csv con columnas:
# Día, Visitas, Tiempo_Promedio Desarrolla una función que:

# Cargue ambos archivos, combine sus datos en un solo DataFrame
# y guarde el resultado en visitas_combinadas.csv.
# Agregue una columna Popular si Visitas > 140.
# Retorna el porcentaje de días populares y no populares.

import pandas as pd


def cargar_datos():
    semana1 = pd.read_csv('dataset/semana1.csv')
    semana2 = pd.read_csv('dataset/semana2.csv')

    ambos = pd.concat([semana1, semana2], ignore_index=True)
    df = pd.DataFrame(ambos)
    df.to_csv('dataset/visitas_combinadas.csv', index=False)
    print('Carga correcta')
    return df


def agregar(df):
    df['Popular'] = df['Visitas'] > 140
    print(df)


def calculo(df):
    dias_totales=len(df)
    print(f'Total de dias = {dias_totales}')
    populares=df['Popular'].sum()
    print(f'Dias populares = {populares}')
    porc_pop=(populares/dias_totales)*100
    print(f'Porcentaje de los dias populares = {porc_pop}%')
    no_populares=dias_totales-populares
    print(f'Dias no populares = {no_populares}')
    porc_nopop=(no_populares/dias_totales)*100
    print(f'Porcentaje de los dias no populares = {porc_nopop}%')

    return porc_pop, porc_nopop





if __name__ == "__main__":
    df = cargar_datos()
    print('============')
    agregar(df)
    print('=============')
    calculo(df)
