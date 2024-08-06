import os
import dotenv
from langchain_openai import OpenAIEmbeddings
from pinecone import Pinecone
from pinecone import ServerlessSpec

dotenv.load_dotenv()
OPEN_AI_API_KEY = os.getenv("OPEN_AI_API_KEY")
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_PLACE_INDEX_NAME = os.getenv("PINECONE_PLACE_INDEX_NAME")
PINECONE_CLOUD = os.getenv("PINECONE_CLOUD")
PINECONE_REGION = os.getenv("PINECONE_REGION")

embedding_model = OpenAIEmbeddings(model="text-embedding-3-large", dimensions=1024)

pc = Pinecone(api_key=PINECONE_API_KEY)

for index in pc.list_indexes():
    if index["name"] == PINECONE_PLACE_INDEX_NAME:
        is_place_index_present = True
        

if not is_place_index_present:
    pc.create_index(
    name=PINECONE_PLACE_INDEX_NAME,
    dimension=1024,
    metric="cosine",
    spec=ServerlessSpec(
        cloud=PINECONE_CLOUD,
        region=PINECONE_REGION
        )
    )

place_index = pc.Index(PINECONE_PLACE_INDEX_NAME)

def add_place(place_id, description):
    embedding = embedding_model.embed_query(description)
    place_index.upsert(vectors=[(place_id, embedding)])

def remove_place(place_id):
    place_index.delete(ids=[place_id])

def get_all_place_ids():
    vector_list = []
    total_vector_count = place_index.describe_index_stats()["total_vector_count"]
    if (total_vector_count == 0):
        return vector_list
    for place in place_index.query(vector=[0] * 1024, top_k=total_vector_count)["matches"]:
        vector_list.append(place["id"])
    return vector_list

def perform_similarity_search(interests, top_k=10):
    user_embedding = embedding_model.embed_query(" ".join(interests))
    search_results = place_index.query(vector=[user_embedding], top_k=top_k)
    return [match['id'] for match in search_results['matches']]
