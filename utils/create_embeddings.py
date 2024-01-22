#!/usr/bin/env python3
import os
import glob
from typing import List
from multiprocessing import Pool


from langchain.document_loaders import (
    CSVLoader,
)

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.docstore.document import Document
from constants import CHROMA_SETTINGS

# Load environment variables
persist_directory = os.environ.get('PERSIST_DIRECTORY', 'db')
source_directory = os.environ.get('SOURCE_DIRECTORY', 'source_documents')
embeddings_model_name = os.environ.get('EMBEDDINGS_MODEL_NAME', 'all-MiniLM-L6-v2')
chunk_size = 500
chunk_overlap = 50




def load_documents_from_csv(csv_file_path: str, ignored_files: List[str] = []) -> List[Document]:
    documents = []
    # CSVLoader 객체 생성
    csv_loader = CSVLoader(file_path=csv_file_path)
    csv_data = csv_loader.load()

    for row in csv_data:
         # row는 CSV 파일의 각 행을 나타내며, 여기서는 문자열입니다.
        if row and row not in ignored_files:
            # 문자열 데이터를 그대로 리스트에 추가
            documents.append(row)

    return documents

def process_documents(ignored_files: List[str] = [],csv_file_path: str = None) -> List[Document]:
    """
    Load documents and split in chunks
    """
    print(f"Loading documents from {source_directory}")
    if csv_file_path:
        documents = load_documents_from_csv(csv_file_path, ignored_files)
    else:
        documents = load_documents_from_csv(source_directory, ignored_files)

    if not documents:
        print("No new documents to load")
        exit(0)
    print(f"Loaded {len(documents)} new documents from {source_directory}")
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    texts = text_splitter.split_documents(documents)
    print(f"Split into {len(texts)} chunks of text (max. {chunk_size} tokens each)")
    return texts

def does_vectorstore_exist(persist_directory: str) -> bool:
    """
    Checks if vectorstore exists
    """
    if os.path.exists(os.path.join(persist_directory, 'index')):
        if os.path.exists(os.path.join(persist_directory, 'chroma-collections.parquet')) and os.path.exists(os.path.join(persist_directory, 'chroma-embeddings.parquet')):
            list_index_files = glob.glob(os.path.join(persist_directory, 'index/*.bin'))
            list_index_files += glob.glob(os.path.join(persist_directory, 'index/*.pkl'))
            # At least 3 documents are needed in a working vectorstore
            if len(list_index_files) > 3:
                return True
    return False


