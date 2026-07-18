# Feature engineering

print(users["subscribed"]) # encoding binary variables - pandas
users["sub_enc"] = users["subscribed"].apply(lambda val: 1 if val == "y" else 0)
print(users["subscribed", "sub_enc"]) #now encoded


from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
users["sub_enc_le"] = le.fit_transform(users["subscribed"]) #fit pode ser usado tanto para ajustar o codificador aos dados quanto para transformar a coluna
print(users["subscribed", "sub_enc_le"]) 

# One-hot encoding
print(users["fav_color"])
print(pd.get_dummies(users["fav_color"])) #para codificar diretamente valores categóricos

### 1
## Encoding Y and N to 0s and 1s
# # Set up the LabelEncoder object
# enc = LabelEncoder()
# #
# ## Apply the encoding to the "Accessible" column
# hiking["Accessible_enc"] = enc.fit_transform(hiking["Accessible"])
# #
# ## Compare the two columns
# print(hiking[["Accessible_enc", "Accessible"]].head())


### 2
##  Codificando variáveis categóricas - one-hot com pandas
#   Transform the category_desc column
#     category_enc = pd.get_dummies(volunteer["category_desc"])
#   Take a look at the encoded columns
#     print(category_enc.head())

# ----------------------------- #
# Engineering numerical features
print(temps)
temps["mean"] = temps.loc[:,"day1":"day3"].mean(axis=1)
print(temps)

# dates - para granularidade
print(purchases) 
purchases["date_converted"] = pd.to_datetime(purchases["date"]) # pandas convertendo p/ date time
purchases['month'] = purchases["date_converted"].dt.month #extrair o mês


### 3
##  Agregando recursos numéricos
# # Use .loc to create a mean column
#running_times_5k["mean"] = running_times_5k.loc[:, "run1":"run5"].mean(axis=1)
# Take a look at the results
#print(running_times_5k.head())

### 4
## Extraindo componentes de datetime
# # First, convert string column to date column
#volunteer["start_date_converted"] = pd.to_datetime(volunteer["start_date_date"])
#
## Extract just the month from the converted column
#volunteer['start_date_month'] = volunteer["start_date_converted"].dt.month
#
## Take a look at the converted and new month columns
#print(volunteer[["start_date_converted", "start_date_month"]].head())


# --------- #
# Extraction
import re
my_string = "temperature:75.6 F"
temp = re.search("\d+\.\d+", my_string) # d -> digitos, + -> o maximo possível
print(float(temp.group(0)))

# Vectorizing text
from sklearn.feature_extraction.text import TfidfVectorizer
print(documents.head())

tfidf_vec = TfidfVectorizer()
text_tfidf = tfidf_vec.fit_transform(documents)

### 5
## Extraindo Padrões de string
# Write a pattern to extract numbers and decimals 
# def return_mileage(length):
#     
#     # Search the text for matches
#     mile = re.search(r"\d+\.?\d*", length) #nao é o nome da coluna, é o parametro da função
#                                            # 0.8 miles  ->   0.80
#     # If a value is returned, use group(0) to return the found value
#     if mile is not None:
#         return float(mile.group(0))
#         
# # Apply the function to the Length column and take a look at both columns
# hiking["Length_num"] = hiking["Length"].apply(return_mileage)
# print(hiking[["Length", "Length_num"]].head())

### 6 
## Vetorizando texto
# # Take the title text
#title_text = volunteer["title"]
#
## Create the vectorizer method
#tfidf_vec = TfidfVectorizer()
#
## Transform the text into tf-idf vectors
#text_tfidf = tfidf_vec.fit_transform(title_text)