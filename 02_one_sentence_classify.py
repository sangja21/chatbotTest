from langchain_community.llms import Ollama
import pymysql
import os
from dotenv import load_dotenv

## 한 문장씩 DB에서 불러와서 인공지능을 통해 intent, entities, label(positive, negative, neutral)을 정확히 한 단어로 출력하는 예제 : prompt 수정

load_dotenv()
host_name = os.getenv("HOST")
user_name = os.getenv("ACCOUNT")
password_one = os.getenv("PASSWORD")
db_name = os.getenv("DB")

conn = pymysql.connect(host=host_name, port=3306, user=user_name, password=password_one, db=db_name, charset='utf8')

cur = conn.cursor()

cur.execute("SELECT category, message FROM sendnow_message ORDER BY RAND()")
# result = cur.fetchone()
result = cur.fetchone()
print("sendNow category : ", result[0])
print("sendNow message : ", result[1])

category = result[0]
message = result[1]

cur.close()
conn.close()

input = result[0]
llm = Ollama(model="llama2", temperature=0.0)
# temperature가 낮을 수록 일관성 있는 답변이 생성됨 

# 추가사항. DB에 업종별로 구분하여 들어간 정보를 주고 이를 통해 인공지능이 구분하도록 함. 
prompt1 =  "This industry is " + category + ", consider this when answering the following question."  
prompt2 = """
"Please enter the text for analysis.

1. Intent: [Describe the primary purpose of the text in one word]
2. Entities: [List key entities mentioned in the text, one word each]
3. Emotion: [Classify the text's emotion as Positive, Negative, or Neutral in one word]

Note: Please provide responses in single words only for each category.

Enter text:"
"""
print("")
print("**************************************************")
print("")
print(prompt1, prompt2)
print(message)


res = llm.invoke(prompt1 + prompt2 + input)
#res = "res"
print("")
print("--------------------------------------------------")
print (res)
print("--------------------------------------------------")


