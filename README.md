# LangChain

This example is a basic "hello world" of using LangChain with Ollama.

## Running the Example

1. Ensure you have the `llama2` model installed:

   ```bash
   ollama pull llama2
   ```

2. Install the Python Requirements.

   ```bash
   pip install -r requirements.txt
   ```

3. Run the example:

   ```bash
   python main.py
   ```

## Ollama 예제로부터 Test Code 작성

1. pymySQL을 설치하여 python과 DB 연결

```python
import pymysql
import os
from dotenv import load_dotenv

load_dotenv()
host_name = os.getenv("HOST")
user_name = os.getenv("ACCOUNT")
password_one = os.getenv("PASSWORD")
db_name = os.getenv("DB")

conn = pymysql.connect(host=host_name, port=3306, user=user_name, password=password_one, db=db_name, charset='utf8')
```
