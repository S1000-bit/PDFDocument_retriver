import os
from app import get_vector_store,data_ingestion
from unittest.mock import MagicMock,patch

def test_faiss_vectorstore_created(tmp_path):
    docs = data_ingestion()
    mock_embeddings = MagicMock()
    
    with patch('app.FAISS.from_documents') as mock_faiss:
        mock_faiss_instance = MagicMock()
        mock_faiss.return_value = mock_faiss_instance
        os.chdir(tmp_path)
        get_vector_store(docs,embeddings = mock_embeddings)
        mock_faiss.assert_called_once()
        assert True