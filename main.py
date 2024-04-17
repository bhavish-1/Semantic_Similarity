import sys
import pandas as pd
import tensorflow as tf
import numpy as np
from numpy import dot
from numpy.linalg import norm
import tensorflow_hub as hub

def embed(input):
     module_url = "https://tfhub.dev/google/universal-sentence-encoder/4"
     model = hub.load(module_url)
     return model(input)

def Embedding(Data):
        message = [Data['text1'][0], Data['text2'][0]]
        message_embeddings = embed(message)
        return message_embeddings

def main(text1, text2):
    
    Data = pd.DataFrame({'text1':[text1], 'text2':[text2]})
    
    message_embeddings = Embedding(Data)

    a_np = tf.make_ndarray(tf.make_tensor_proto(message_embeddings))

    ans = []
    messages = [Data['text1'][0], Data['text2'][0]]               #storing each sentence pair in messages
    message_embeddings = embed(messages)                          #converting the sentence pair to vector pair using the embed() function
    a = tf.make_ndarray(tf.make_tensor_proto(message_embeddings)) #storing the vector in the form of numpy array
    cos_sim = dot(a[0], a[1])/(norm(a[0])*norm(a[1]))             #Finding the cosine between the two vectors
    ans.append(cos_sim) 


    # Ans = pd.DataFrame(ans, columns=['Similarity_Score'])
    
    # Data = Data.join(Ans)
    # Data['Similarity_Score'] = Data['Similarity_Score'] + 1
    avg_similarity = (np.array(ans) + 1) / 2
    return avg_similarity



