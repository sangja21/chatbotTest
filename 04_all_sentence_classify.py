from langchain_community.llms import Ollama
import pymysql
import os
from dotenv import load_dotenv
import asyncio

## 모든 문장들을 DB에서 불러와서 인공지능을 통해 intent, entities, label(positive, negative, neutral)을 정확히 한 단어로 출력하는 예제

async def classify_text(idx, category, message):
    # 여기에 비동기적으로 외부 서비스를 호출하는 코드 작성
    # 예: response = await some_async_http_call(text)

    llm = Ollama(model="llama2", temperature=0.0) # temperature가 낮을 수록 일관성 있는 답변이 생성됨 

    # # 추가사항. DB에 업종별로 구분하여 들어간 정보를 주고 이를 통해 인공지능이 구분하도록 함. 
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
    print("************************ " + idx + " **************************")
    print("")
    print(prompt1, prompt2)
    print(message)

    res = llm.invoke(prompt1 + prompt2 + message)
    print(idx)
    print("--------------------------------------------------")
    print (res)
    print("--------------------------------------------------")

    return res


async def main():

    # 데이터베이스에 연결
    load_dotenv()
    host_name = os.getenv("HOST")
    user_name = os.getenv("ACCOUNT")
    password_one = os.getenv("PASSWORD")
    db_name = os.getenv("DB")

    conn = pymysql.connect(host=host_name, port=3306, user=user_name, password=password_one, db=db_name, charset='utf8')
    cur = conn.cursor()

    # 데이터베이스에서 문장을 가져오는 코드
    cur.execute("SELECT id, category, message FROM sendnow_message")
    results = cur.fetchall()

    # 모든 행을 순회하며 category와 message 출력
    print("------------------------------------ - DB에서 가져온 값 - -------------------------------------")
    for result in results:
        id = result[0]
        category = result[1]  # 각 행의 첫 번째 요소 (category)
        message = result[2]  # 각 행의 두 번째 요소 (message)
        print(f"id: ", id)
        print(f"Category: ", category)
        print(f"Message: ", message)
    print("------------------------------------ - DB에서 가져온 값 - -------------------------------------")

    # 모든 문장에 대해 비동기적으로 classify_text 호출
    tasks = [classify_text(str(result[0]), result[1], result[2]) for result in results]
    results = await asyncio.gather(*tasks)

    cur.close()
    conn.close()

    # 결과 처리
    #for result in results:
    #    print(result)  # 또는 결과를 데이터베이스에 저장 등의 처리


# 이벤트 루프 실행
asyncio.run(main())