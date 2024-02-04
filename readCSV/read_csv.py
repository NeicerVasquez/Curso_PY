import csv

def read_csv(ruta):
  with open(ruta, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    main_row = next(reader)
    world_population = []
    for rows in reader:
      data = dict(zip(main_row, rows))
      world_population.append(data)
    return world_population

# def delimitar_pais_rango(data):
#   rango_pais = list(filter(lambda key: int(key['Rank']) >= 234, data))
#   print(rango_pais)
#   print(len(rango_pais))

if __name__ == '__main__':
  world_data = read_csv('data.csv')
  # delimitar_pais_rango(world_data)