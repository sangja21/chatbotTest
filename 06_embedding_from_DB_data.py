from langchain_community.llms import Ollama
from dotenv import load_dotenv
from langchain.vectorstores import Chroma
from langchain.embeddings import GPT4AllEmbeddings
from langchain.callbacks.manager import CallbackManager
from langchain import PromptTemplate
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.chains import RetrievalQA
import csv
import sys
import pymysql
import os

## DB에 분류된 데이터를 불러와서 embedding 하는 코드

load_dotenv()
host_name = os.getenv("HOST")
user_name = os.getenv("ACCOUNT")
password_one = os.getenv("PASSWORD")
db_name = os.getenv("DB")

conn = pymysql.connect(host=host_name, port=3306, user=user_name, password=password_one, db=db_name, charset='utf8')

cur = conn.cursor()

# CSV 파일 저장 경로 설정
csv_file_path = '/Users/sangja/dev/langchain-python-simple/source_documents/data.csv'

class SuppressStdout:
    def __enter__(self):
        self._original_stdout = sys.stdout
        self._original_stderr = sys.stderr
        sys.stdout = open(os.devnull, 'w')
        sys.stderr = open(os.devnull, 'w')

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout.close()
        sys.stdout = self._original_stdout
        sys.stderr = self._original_stderr

# 간단한 문서 클래스 정의
class Document:
    def __init__(self, text):
        self.page_content = text

cur.execute("SELECT message, intent, entities, emotion FROM analyzed_text")
result = cur.fetchall()

print("#########################################################",result)

# 'result'에서 각 튜플의 첫 번째 요소를 사용하여 문서 객체 리스트 생성
results2 = [Document(row[0]) for row in result]
print("***********************************************************",results2)

# CSV 파일 작성
with open(csv_file_path, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # CSV 헤더 작성 (선택 사항)
    writer.writerow(['message'])
    # 각 행의 데이터 작성
    writer.writerows(result)


cur.close()
conn.close()

# while True:
    # query = input("\nQuery: ")
    # if query == "exit":
    #     break
    # if query.strip() == "":
    #     continue

    #     # Prompt
    # template = """Use the following pieces of context to answer the question at the end. 
    # If you don't know the answer, just say that you don't know, don't try to make up an answer. 
    # Use three sentences maximum and keep the answer as concise as possible. 
    # {context}
    # Question: {question}
    # Helpful Answer:"""
    # QA_CHAIN_PROMPT = PromptTemplate(
    #     input_variables=["context", "question"],
    #     template=template,
    # )


    # llm = Ollama(model="llama2:13b", callback_manager=CallbackManager([StreamingStdOutCallbackHandler()]))
    # qa_chain = RetrievalQA.from_chain_type(
    #     llm,
    #     retriever=vectorstore.as_retriever(),
    #     chain_type_kwargs={"prompt": QA_CHAIN_PROMPT},
    # )

    # result = qa_chain({"query": query})