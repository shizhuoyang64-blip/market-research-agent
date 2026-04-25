# -Repository-name-
市场调研智能体
# 市场调研智能体

基于LangChain的多智能体市场调研系统。

## 环境要求
- Python 3.10 或以上
- Git

## 快速开始

### 1. 克隆仓库
git clone https://github.com/shizhuoyang64-blip/market-research-agent.git
cd market-research-agent

### 2. 安装依赖
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

### 3. 配置API Key
新建 .env 文件，填入：
OPENAI_API_KEY=你的硅基流动key
OPENAI_BASE_URL=https://api.siliconflow.cn/v1

申请地址：siliconflow.cn

### 4. 验证环境
python week1_demo/step1_api_test.py
看到"测试通过"说明环境OK。

### 5. 运行提示链Demo
python week1_demo/step2_chain.py

## 目录结构
week1_demo/   第一周Demo代码
docs/         文档和笔记

## 技术栈
- LangChain 0.3.7
- 模型：Qwen2.5-72B（硅基流动API）