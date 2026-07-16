import pandas as pd
hiking = pd.read_json("hiking.json") # Lê o arquivo JSON e cria um DataFrame chamado hiking
print(hiking.head) # Exibe as 5 primeiras linhas do DataFrame

print(wine.describe())  # Exibe estatísticas descritivas das colunas numéricas do DataFrame wine

# removing missing data
print(df)
print(df.dropna()) # drop NaN
print(df.drop([1, 2, 3])) # linha específica
print(df.drop("A", axis=1)) # coluna
print(df.isna().sum()) # quantas linhas NaN em cada coluna
print(df.dropna(subset=["B"])) # especificando qual coluna eu quero saber, e traz as linhas válida de B
print(df.dropna(thresh=2)) # especificando quantos valores Nao Missing que uma linha/coluna precisa ter para ser mantida

### 1
##  como contar quantas linhas NaN tem em uma coluna chamada locality de um arquivo?
#   print(volunteer["locality"].isna().sum())

### 2
## Drop the Latitude and Longitude columns from volunteer
#   volunteer_cols = volunteer.drop("Latitude", axis=1)
#   volunteer_cols = volunteer_cols.drop("Longitude", axis=1)
#
#  Drop rows with missing category_desc values from volunteer_cols
#   volunteer_subset = volunteer_cols.dropna(subset=["category_desc"])
#
#  Print out the shape of the subset
#   print(volunteer_subset.shape)