import os
from dotenv import load_dotenv

# 載入 .env 檔案中的環境變數
load_dotenv()

# 從環境變數中讀取 API 金鑰
api_key = os.getenv("STACKEXCHANGE_KEY")

# 現在你可以安全地使用這個金鑰了
print(f"我的 API 金鑰是：{api_key}")

# 你可以將這個金鑰傳遞給你的 API 呼叫函式
# response = call_stack_overflow_api(api_key)