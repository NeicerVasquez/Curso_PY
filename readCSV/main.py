import utils
import read_csv as rc
import charts as gc
import pandas as pd

def run():
  # Esta parte de código ya la puede hacer pandas
  '''
  data = rc.read_csv('./data.csv')
  data = list(filter(lambda item: item['Continent'] == 'South America', data))

  countries = list(map(lambda x: x['Country/Territory'], data))
  percentages = list(map(lambda x: x['World Population Percentage'], data))
  gc.generate_pie_chart(countries, percentages)
  '''

# Para graficar en barras el país y su población
  # Usando Pandas para leer un csv
  # df == dataFrame
  df = pd.read_csv('data.csv')
  df = df[df['Continent'] == 'Asia']
  
  countries = df['Country/Territory'].values
  percentages = df['World Population Percentage']

  gc.generate_pie_chart(countries, percentages)

  data = rc.read_csv('./data.csv')
  country = input('Type Country => ')
  result = utils.population_by_country(data, country)
  if len(result) > 0:
    country = result[0]
    labels, values = utils.get_population(country)
    gc.generate_bar_chart(country['Country/Territory'], labels, values)


if __name__ == '__main__':
  run()