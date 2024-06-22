# Chat with PDF using AWS Bedrock

This project enables users to interact with PDF documents through a chatbot interface using AWS Bedrock. The application leverages natural language processing (NLP) and machine learning models to provide accurate and detailed answers to user queries based on the content of the PDFs.

## Features

- Load and process PDF documents.
- Create vector embeddings from document content using AWS Bedrock.
- Use FAISS for vector storage and retrieval.
- Generate responses using Llama3 LLM.
- Streamlit interface for user interaction.

## Prerequisites

- Docker
- AWS Account with appropriate permissions
- AWS CLI configured with your credentials

## Installation

### Using Docker

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/your-repo-name.git
    cd your-repo-name
    ```

2. **Build the Docker image**:
    ```bash
    docker build -t chat-pdf-app .
    ```

3. **Run the Docker container**:
    ```bash
    docker run -p 8501:8501 -v ~/.aws:/root/.aws chat-pdf-app
    ```

### Local Setup (Without Docker)

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/your-repo-name.git
    cd your-repo-name
    ```

2. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the application**:
    ```bash
    streamlit run your_script_name.py
    ```

## Usage

1. **Access the application**:
   Open your web browser and go to `http://localhost:8501`.

2. **Upload PDF Files**:
   Use the sidebar to upload PDF files and update the vector store.

3. **Ask Questions**:
   Enter your question in the text input field and get responses based on the content of the uploaded PDFs.

## Project Structure


## Environment Variables

Ensure that the following environment variables are set in your environment:

- `AWS_ACCESS_KEY_ID`: Your AWS access key ID.
- `AWS_SECRET_ACCESS_KEY`: Your AWS secret access key.
- `AWS_REGION`: The AWS region where your Bedrock resources are located.

## Security

Make sure to handle AWS credentials securely. Do not hardcode your credentials in the source code. Use environment variables or AWS IAM roles for better security practices.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Langchain](https://github.com/hwchase17/langchain)
- [Streamlit](https://www.streamlit.io/)
- [AWS Bedrock](https://aws.amazon.com/bedrock/)
- [FAISS](https://github.com/facebookresearch/faiss)

