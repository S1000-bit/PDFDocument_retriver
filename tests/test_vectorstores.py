import os
from app import get_vector_store,data_ingestion

def test_faiss_vectorstore_created(tmp_path):
    docs = data_ingestion()
    os.chdir(tmp_path)
    get_vector_store(docs)
    assert os.path.exists("faiss_index/index.faiss")