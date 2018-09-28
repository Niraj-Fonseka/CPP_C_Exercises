import os
import numpy as np 
import pandas as pd 
import tensorflow as tf
from sklearn.preprocessing import LabelEncoder

#from tutorial : https://medium.com/tensorflow/predicting-the-price-of-wine-with-the-keras-functional-api-and-tensorflow-a95d1c2c1b03

from tensorflow import keras 
layers = keras.layers

print("Tensorflow Version : " , tf.__version__)

#read data into a variable 
data = pd.read_csv("wine_data.csv")

train_size = int(len(data) * .8) # ? 

#train features 
description_train = data['description'][:train_size]
variety_train = data['variety'][:train_size]

#test features
description_test = data['description'][train_size:]
variety_test = data['variety'][train_size:]

#Test Lables
label_test = data['price'][train_size:]

#creating a bag of words 
vocab_size = 12000
tokenize = keras.preprocessing.text.Tokenizer(num_words=vocab_size, char_level=False)
tokenize.fit_on_texts(description_train) # only fit on train


#converting each matrix to bag of words
description_bow_train = tokenize.texts_to_matrix(description_train)
description_bow_test = tokenize.texts_to_matrix(description_test)


print(description_bow_test)
print(description_bow_train)
encoder = LabelEncoder()
encoder.fit(variety_train)
variety_train = encoder.transform(variety_train)
variety_test = encoder.transform(variety_test)
num_classes = np.max(variety_train) + 1

# Convert labels to one hot
variety_train = keras.utils.to_categorical(variety_train, num_classes)
variety_test = keras.utils.to_categorical(variety_test, num_classes)

bow_inputs = layers.Input(shape=(vocab_size,))
variety_inputs = layers.Input(shape=(num_classes,))
merged_layer = layers.concatenate([bow_inputs, veriety_inputs])
merged_layer = layers.Dense(256 , activation='relu')(merged_layer)
predictions = layers.Dense(1)(merged_layer)
wide_model = Model(inputs=[bow_inputs , variety_inputs], outputs=predictions)

#compiling the model
wide_model.compile(loss='mse' , optimizer='adam' , metrics=['accuracy'])

train_embed = tokenize.texts_to_sequences(description_train)
test_embed = tokenize.texts_to_sequences(description_test)


#pad sequences adds zeros to each description vector to make thhem the same length
max_seq_length = 170
train_embed = keras.preprocessing.sequence.pad_sequences(train_embed, maxlen=max_seq_length)
test_embed = keras.preprocessing.sequence.pad_sequences(test_embed, maxlen=max_seq_length)

deep_inputs = layers.Input(shape=(max_seq_length,)) #defining the shape of the inputs to the deep model

#creating an emedding layer with 8 dimensions ( can tweak this )
embedding = layers.Embedding(vocab_size, 8,   input_length=max_seq_length)(deep_inputs)
embedding = layers.Flatten()(embedding) #flatenning the embedding layer 


#Feed into the model and compile

embed_out = layers.Dense(1, activation='linear')(embedding)
deep_model = Model(inputs=deep_inputs, outputs=embed_out)
deep_model.compile(loss='mse', optimizer='adam', metrics=['accuracy'])
