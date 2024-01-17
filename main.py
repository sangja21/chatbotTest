from langchain.llms import Ollama
import pymysql
import os
from dotenv import load_dotenv

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
