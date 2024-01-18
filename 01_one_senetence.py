from langchain_community.llms import Ollama
import pymysql
import os
from dotenv import load_dotenv

## 한 문장씩 DB에서 불러와서 인공지능을 통해 intent, entities, label(positive, negative, neutral)을 출력하는 예제

load_dotenv()
host_name = os.getenv("HOST")
user_name = os.getenv("ACCOUNT")
password_one = os.getenv("PASSWORD")
db_name = os.getenv("DB")

conn = pymysql.connect(host=host_name, port=3306, user=user_name, password=password_one, db=db_name, charset='utf8')

cur = conn.cursor()

cur.execute("SELECT message FROM sendnow_message ORDER BY RAND()")
# result = cur.fetchone()
result = cur.fetchone()
print("sendNow message : ", result[0])

cur.close()
conn.close()

# input = input("What is your question?")
input = result[0] # DB에서 가져온 문장을 input에 넣는다 
llm = Ollama(model="llama2", temperature=0.0)
# prompt = """Classify the below sentence(s) as the followings:
# Intent : 
# Entities : 
# emotions : 
# """

# 추가사항. DB에 업종별로 구분하여 들어간 정보를 주고 이를 통해 인공지능이 구분하도록 함. 
prompt = """Classify this text into the intent of a single word and the entities that appear here,
and Classify Text into one of 3 labels : positive, negative, neutral :
Intent : 
Entities : 
labels : 
"""
res = llm.predict(prompt + input)

print("--------------------------------------------------")
print (res)
print("--------------------------------------------------")
