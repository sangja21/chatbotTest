import csv
import pymysql
import os
from dotenv import load_dotenv



def extract_and_save_to_csv():
    load_dotenv()
    host_name = os.getenv("HOST")
    user_name = os.getenv("ACCOUNT")
    password_one = os.getenv("PASSWORD")
    db_name = os.getenv("DB")

    conn = pymysql.connect(host=host_name, port=3306, user=user_name, password=password_one, db=db_name, charset='utf8')
    cur = conn.cursor()
    cur.execute("SELECT message, intent, entities, emotion FROM analyzed_text")
    result = cur.fetchall()

    # 스크립트 파일의 절대 경로를 기준으로 CSV 파일 경로 생성
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    csv_file_path = os.path.join(base_dir, 'source_documents', 'data.csv')



    with open(csv_file_path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['message', 'intent', 'entities', 'emotion'])  # 헤더 추가
        writer.writerows(result)

    cur.close()
    conn.close()

    return csv_file_path


