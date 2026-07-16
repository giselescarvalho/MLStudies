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


# Working With DataTypes

print(df.info())
df["C"] = df["C"].astype("float") #astype converte o tipo de dado de uma coluna para um tipo específico
print(df.dtypes) # dtype: object

### 3 
##  quais tipo contem em volunteer?
#   print(volunteer.info())


### 4
## Print the head of the hits column
#   print(volunteer["hits"].head())
#
#  Convert the hits column to type int
#   volunteer["hits"] = volunteer["hits"].astype("int")
#
#  Look at the dtypes of the dataset
#   print(volunteer.dtypes)


# Training and testsets

from sklearn.model_selection import train_test_split # Importa a função para dividir os dados em conjuntos de treinamento e teste

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42) # Divide os dados em treino (80%) e teste (20%)

X_train,X_test,y_train,y_test = train_test_split(X, y, stratify=y, random_state=42) # stratified sampling # Divide os dados preservando a proporção das classes (amostragem estratificada)
y["labels"].value_counts()       # Exibe a quantidade de registros em cada classe da variável alvo
y_train["labels"].value_counts() # Exibe a quantidade de amostras de cada classe no conjunto de treinamento
y_test["labels"].value_counts()   # Exibe a quantidade de amostras de cada classe no conjunto de teste

### 5
##  Quais descrições ocorrem menos de 50 vezes no conjunto de dados volunteer?
#    volunteer["category_desc"].value_counts()

### 6
## from sklearn.model_selection import train_test_split
# Create a DataFrame with all columns except category_desc
# X = volunteer.drop("category_desc", axis=1)
#
# Create a category_desc labels dataset
# Em aprendizado de máquina, normalmente:
#  X = atributos (features)
#  y = rótulo/variável-alvo (target)
# y = volunteer[["category_desc"]]
#
# Use stratified sampling to split up the dataset according to the y dataset
# X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=42)
#
# Print the category_desc counts from y_train
# print(y_train["category_desc"].value_counts())
