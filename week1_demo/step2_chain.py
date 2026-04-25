import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config import OPENAI_API_KEY
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# 初始化模型
llm = ChatOpenAI(
    model="Qwen/Qwen2.5-72B-Instruct",
    api_key=OPENAI_API_KEY,
    base_url="https://api.siliconflow.cn/v1",
    temperature=0
)

# 第一步提示词：提取市场信息
prompt_extract = ChatPromptTemplate.from_template(
    """你是一名市场分析师。请从以下新闻文本中提取关键市场信息。

新闻文本：
{news_text}

请提取以下信息：
- 涉及的行业或市场
- 主要公司或品牌
- 关键数据或数字（市场规模、增长率、份额等）
- 重要事件或趋势

请用简洁的要点格式输出。"""
)

# 第二步提示词：转为JSON格式
prompt_to_json = ChatPromptTemplate.from_template(
    """请将以下市场信息整理成JSON格式。

市场信息：
{extracted_info}

输出格式要求（严格按照这个JSON结构）：
{{
  "industry": "行业名称",
  "companies": ["公司1", "公司2"],
  "key_data": {{
    "market_size": "市场规模（如有）",
    "growth_rate": "增长率（如有）",
    "market_share": "市场份额（如有）"
  }},
  "trends": ["趋势1", "趋势2"]
}}

只输出JSON，不要其他文字。"""
)

# 用 | 把两步串起来
extract_chain = prompt_extract | llm | StrOutputParser()

full_chain = (
    {"extracted_info": extract_chain}
    | prompt_to_json
    | llm
    | StrOutputParser()
)

def run_chain(news_text: str):
    print("\n---- 第一步：提取市场信息 ----")
    step1_result = extract_chain.invoke({"news_text": news_text})
    print(step1_result)

    print("\n---- 第二步：转为JSON格式 ----")
    step2_result = full_chain.invoke({"news_text": news_text})
    step2_result = step2_result.replace("```json", "").replace("```", "").strip()
    print(step2_result)

    return step2_result

if __name__ == "__main__":
    test_news = """
    2025年第一季度，中国新能源汽车市场持续高速增长。
    比亚迪以35%的市场份额继续领跑，销量达到120万辆，
    同比增长42%。特斯拉中国区销量为28万辆，市场份额约8%。
    整体市场规模达到3400亿元，分析师预测全年将突破1.5万亿元。
    造车新势力中，理想汽车表现亮眼，季度销量首次突破10万辆大关。
    """

    print("输入文本：", test_news)
    run_chain(test_news)