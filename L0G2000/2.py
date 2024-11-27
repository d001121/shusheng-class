#./internlm_test.py
from openai import OpenAI
import os


def internlm_gen(prompt,client):
    '''
    LLM生成函数
    Param prompt: prompt string
    Param client: OpenAI client 
    '''
    response = client.chat.completions.create(
        model="internlm2.5-latest",
        messages=[
            {"role": "user", "content": prompt},
      ],
        stream=False
    )
    return response.choices[0].message.content

api_key = os.getenv('api_key')
#api_key = "" #也可以明文写在代码内，不推荐
client = OpenAI(base_url="https://internlm-chat.intern-ai.org.cn/puyu/api/v1/",api_key=api_key)
prompt = '''你好！你是谁？'''
response = internlm_gen(prompt,client)
print(response)