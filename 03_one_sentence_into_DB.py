from langchain_community.llms import Ollama
import pymysql
import os
from dotenv import load_dotenv

## 한 문장씩 DB에서 불러와서 인공지능을 통해 intent, entities, label(positive, negative, neutral)을 출력하여 DB에 다시 집어 넣는 예제

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

input = result[0]
llm = Ollama(model="llama2", temperature=0.0)
# temperature가 낮을 수록 일관성 있는 답변이 생성됨 

# 추가사항. DB에 업종별로 구분하여 들어간 정보를 주고 이를 통해 인공지능이 구분하도록 함. 
prompt1 =  "This industry is " + category + ", consider this when answering the following question."  
prompt2 = """
"Please enter the text for analysis.

1. Intent: [Describe the primary purpose of the text in one word]
2. Entities: [List key entities mentioned in the text, one word each]
3. Emotion: [Classify the text's emotion as Positive as p, Negative as n, or Neutral as m in one word]

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

# 결과값을 parsing하여 각각의 값을 가져오기

# 문자열 파싱
lines = res.split('\n')
intent = lines[0].split(': ')[1]
entities = lines[1].split(': ')[1]
emotion = lines[2].split(': ')[1]

print("*******************************************************")
print("intent* : ", intent)
print("entities* : ", entities)
print("emotion* : ", emotion)
print("*******************************************************")

# SQL 쿼리 구성 및 실행
sql = "INSERT INTO analyzed_text (message, intent, entities, emotion) VALUES (%s, %s, %s, %s)"
cur.execute(sql, (message, intent, entities, emotion))
conn.commit()

cur.close()
conn.close()