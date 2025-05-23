from app import data_ingestion

def test_data_ingestion_returns_documents():
    docs = data_ingestion()
    assert isinstance(docs,list)
    assert len(docs) > 0
    assert hasattr(docs[0], "page_content")
    