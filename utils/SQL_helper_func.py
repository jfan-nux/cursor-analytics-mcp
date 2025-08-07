import numpy as np
import json
import re
from openai import OpenAI
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics.pairwise import norm


#helper functions
def create_embeddings(raw_embeds):
  #this function is used to transform sql array embeddings into numpy arrays
  embs = {}
  for i, j in raw_embeds.items():
    if i.isdigit():
      key = int(i)
    else:
      key = i
    embs[key] = np.array(json.loads(j))
  return embs

def preprocess_bm25(text):
  #makes text ready for bm25 usage by splitting out special characters, white spaces, and new lines
  text = text.lower()
  text = re.sub(r'[_]', ' ', text)
  text = re.sub(r'::\w+', '', text)
  text = re.sub(r'[^a-z0-9\s]', ' ', text)
  text = re.sub(r'\s+', ' ', text).strip()
  return text.split()

def create_emb_matrix(embedding_series):
  #used for efficient computation of cosine similarity, ie. euclidean distance on normed vectors = cos similarity
  keys = list(embedding_series.keys())
  emb_matrix = np.array(list(embedding_series.values()), dtype=np.float32)
  emb_matrix_norm = emb_matrix / norm(emb_matrix, axis=1, keepdims=True)
  return keys, emb_matrix_norm

def embed_texts(texts, ids, model="text-embedding-3-small"):
  #batch embedding texts if a user inputs in a list of texts and associated text ids. will return list of ids and embedding
    try:
        response = client.embeddings.create(model=model, input=texts)
        embs = [r.embedding for r in response.data]
        return list(zip(ids, embs))
    except Exception as e:
        print(f"Issue happened embedding: {e}")
        raise  # Will be caught and retried by @retry

def load_intent_context(data):
  #transform dataframe into text table format for openAI prompt
    context = []
    for i, j in data.iterrows():
        context.append({
            "team": j["team"],
            "subteam": j["subteam"],
            "mission": j["mission"],
            "okr": j["metric"],
            "details": j["context_def"]
        })

    return json.dumps(context)