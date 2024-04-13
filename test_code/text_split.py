import requests

url = 'https://api.openai.com/v1/chat/completions'

headers = {
    'Authorization': 'Bearer Your_API_Key',
    'Content-Type': 'application/json'
}

# 从外部txt文件中读取消息内容，并指定编码格式为utf-8
system_content = """
## Rules
### Paragraph Splitting
1. Split the text into groups of 2-4 sentences based on their semantic connection；
2. Avoid splitting long sentences midway; 
3. Combine short sentences and paragraphs together and ensure the average length is similar across all sentence groups.;
4. Aim for a total of 4-6 separated paragraphs.
### Paragraph Alignment
1. If English punctuation doesn't match Chinese punctuation, split the English text.
2. Align the source text, reference text, and the text to evaluate.

## Workflow
1. Comprehend the main idea, paragraph structure, and sentence logic of the Chinese text.
2. Follow the rules and constraints to group and align sentences strictly.
3. Present the grouped and aligned sentences in JSON format.

## Output format
{
  "Group 1": [
    {"Source Text": "..."}, 
    {"Reference Text": "..."}, 
    {"Text to Evaluate": "..."}
  ],
  "Group 2": [
    {"Source Text": "..."}, 
    {"Reference Text": "..."}, 
    {"Text to Evaluate": "..."}
  ],
  ...
}

## Initialization
Strictly adhere to the <Rules> and output the grouped results in <output format> JSON:
"""

user_content = """
## Input text
### Source Text
2020年11月中国开始了第七次人口普查。
人口普查将为开启全面建设社会主义现代化国家新征程提供科学准确的统计信息支持。
开展第七次全国人口普查，是推动经济高质量发展的内在要求。
当前，我国经济正处于转变发展方式、优化经济结构、转换增长动力的攻关期。
### Reference Text
China carried out its Seventh National Population Census in November, 2020. 
The census will provide scientific and accurate statistical information support for China to embark on a new journey toward building a modern socialist country.
The census reflects the internal need for the advancement of quality economic development. 
At present, China’s economy is in the critical period of transforming the development mode, optimizing the economic structure, and transforming the growth momentum. 
### Text to Evaluate
China carried out its Seventh National Population Census in November, 2020. 
The census will provide scientific and accurate statistical information support for China to embark on a new journey toward building a modern socialist country.
The census reflects the internal need for the advancement of quality economic development. 
At present, China’s economy is in the critical period of transforming the development mode, optimizing the economic structure, and transforming the growth momentum. 
"""

data = {
    'model': 'gpt-4-0125-preview',
    'response_format': {"type": "json_object"},
    'temperature': 0,
    'messages': [
        {"role": "system", "content": system_content},
        {"role": "user", "content": user_content}
    ]
}

response = requests.post(url, headers=headers, json=data)
content = response.json().get('choices')[0].get('message').get('content')
# 打印全部内容
# content = response.json()

print(content)