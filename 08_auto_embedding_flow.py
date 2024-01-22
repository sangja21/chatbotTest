import os

from utils.db_to_csv import extract_and_save_to_csv
from utils.create_embeddings import  process_documents, does_vectorstore_exist
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma
from constants import CHROMA_SETTINGS

embeddings_model_name = os.environ.get('EMBEDDINGS_MODEL_NAME', 'all-MiniLM-L6-v2')

def main():
    # 데이터베이스에서 데이터 추출 및 CSV 저장
    csv_file_path = extract_and_save_to_csv()

    # 임베딩 생성 및 벡터스토어에 저장
    embeddings = HuggingFaceEmbeddings(model_name=embeddings_model_name)
    persist_directory = os.environ.get('PERSIST_DIRECTORY', 'db')

    if does_vectorstore_exist(persist_directory):
        print(f"Appending to existing vectorstore at {persist_directory}")
        db = Chroma(persist_directory=persist_directory, embedding_function=embeddings, client_settings=CHROMA_SETTINGS)
        collection = db.get()
        texts = process_documents([metadata['source'] for metadata in collection['metadatas']], csv_file_path)
        db.add_documents(texts)
    else:
        print("Creating new vectorstore")
        texts = process_documents([], csv_file_path)
        db = Chroma.from_documents(texts, embeddings, persist_directory=persist_directory)

    db.persist()
    print("Data extraction, embedding, and storage complete.")

if __name__ == "__main__":
    main()
