from unittest.mock import MagicMock,patch
from app import get_response_llm


def test_llm_response_mocked():
    mock_llm = MagicMock()
    mock_vectorstores = MagicMock()
    mock_vectorstores.as_retriever.return_value = MagicMock()
    
    mock_chain = MagicMock()
    mock_chain.return_value = {"result":"this is a mock drill"}
    
    with patch("app.RetrievalQA.from_chain_type", return_value=mock_chain):
        result = get_response_llm(mock_llm, mock_vectorstores, "what is LLM")
        assert isinstance(result, str)