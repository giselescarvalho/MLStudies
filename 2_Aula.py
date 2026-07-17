# Standadization

### 1
##  Modelando sem normalizar
# Split the dataset into training and test sets
# X_train, X_test, y_train, y_test =  train_test_split(X, y, stratify=y, random_state=42)
#
# knn = KNeighborsClassifier()
#
# Fit the knn model to the training data
# knn.fit(X_train, y_train)
# 
# Score the model on the test data
# print(knn.score(X_test, y_test))


# --------------------------- #
# Log normalization in Python
print(df.var()) #variancia de cada coluna
import numpy as np
df["log_2"] = np.log(df["col2"]) # diminuiu
print(df)
print(df[["col1", "log_2"]].var()) # variancia agora é bem menor
    
### 2
##  Candidato a ser normalizado
#   wine.var   ->  qual tem maior valor

### 3
##  Normalizar Proline
#   Print out the variance of the Proline column
#    print(wine.Proline.var())
#
#   Apply the log normalization function to the Proline column
#    wine["Proline_log"] = np.log(wine["Proline"])
#
#   Check the variance of the normalized Proline column
#    print(wine[["Proline_log"]].var())


# ------- #
# Scaling
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
df_scaled = pd.DataFrame(scaler.fit_transform(df),columns=df.columns) #fit transform
print(df_scaled.var()) #agora a variancia é a mesma para todas as colunas

### 4
##
#df1 = wine['Alcohol'].std()
#df2 = wine['Malic acid'].std()
#
# df3 = wine['Ash'].std()
# df4 = wine['Alcalinity of ash'].std()
#
# df['nome_da_coluna'].max()
# max1 = wine['Ash'].max()
# max2 = wine['Alcalinity of ash'].max()
# max3 = wine ['Magnesium'].max()
# print(max1,max2,max3)
#
# media = df['NomeDaColuna'].mean()
# print(media)
# media1 = df['Malic acid'].mean()
# media2 = df['Ash'].mean()
# print(media1,media2)


### 5
##
# Import StandardScaler
# from sklearn.preprocessing import StandardScaler
#
# Create the scaler
# scaler = StandardScaler()
#
# Subset the DataFrame you want to scale 
# wine_subset = wine[['Ash','Alcalinity of ash','Magnesium']]
#
# Apply the scaler to wine_subset
# wine_subset_scaled = pd.DataFrame(
#    scaler.fit_transform(wine_subset),
#    columns=wine_subset.columns
#)