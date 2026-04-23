import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config import OPENAI_API_KEY
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

def test_api():
    print("正在初始化模型...")

    llm = ChatOpenAI(
    model="Qwen/Qwen2.5-7B-Instruct",
    api_key=OPENAI_API_KEY,
    base_url="https://api.siliconflow.cn/v1",
    temperature=0
)

    print("正在发送测试请求...")

    message = HumanMessage(content="你好，请用一句话介绍你自己。")
    response = llm.invoke([message])

    print("\n---- API调用成功 ----")
    print(f"模型回复：{response.content}")
    print("--------------------\n")

    return True

if __name__ == "__main__":
    try:
        test_api()
        print("测试通过，API连接正常。")
    except Exception as e:
        print(f"测试失败：{e}")