import pandas as pd
import time
from numpy import var

url = "data.csv"
data = pd.read_csv(url)


variables = []
for i in data:
  variables.append(i)


variables.pop(8)
variables.pop(1)
variables.pop(8)

#print(variables)

start = time.time()

for v in variables:
  categorias = []
  cont = []

  for i in data.index:
    if data[v][i] not in categorias:
      categorias.append(data[v][i])
      cont.insert(categorias.index(data[v][i]), 1)
    else:
      cont[categorias.index(data[v][i])] += 1
  print(v)
  print("")
  for i in categorias:
    print(i + ":")
    print(cont[categorias.index(i)])
end = time.time()
print("Done, time taken", end - start)
