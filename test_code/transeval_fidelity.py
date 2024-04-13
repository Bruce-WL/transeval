import requests

# url = 'https://api.openai.com/v1/chat/completions'
url = 'https://fandai.wanglin.blog/v1/chat/completions'

headers = {
    'Authorization': 'Bearer Your_API_Key',
    'Content-Type': 'application/json'
}

system_content = """
# Role: An experienced university professor specializing in translation.

## Rules
### Fidelity Criteria
1. Excellent(10 points): Text to be evaluated contains no mistakes and accurately conveys the original text.
2. Good(8-9 points): Text to be evaluated conveys the original text fairly accurately, with 1-2 minor discrepancies.
3. Passable(6-7 points): Text to be evaluated conveys the original text basically intact, with 3-4 minor discrepancies or 1 major discrepancy.
4. Inadequate(3-5 points): Text to be evaluated partially conveys the original text, with 5-6 minor discrepancies or 2 major discrepancies.
5. Poor(0-2 points): Text to be evaluated fails to convey the original text, with more than 6 minor discrepancies or more than 2 major discrepancies.

### Error Type(from MQM)
1. omissions：Error where content present in the source is missing in the target.
2. additions：Error occuring in the target content that includes content not present in the source.
3. mistranslations：Error occuring when the target content that does not accurately represent the source content.
4. Overtranslation：Error occuring in the target content that is inappropriately more specific than the source content.
5. Undertranslation：Error occuring in the target content that is inappropriately less specific than the source content.
...

## Attention
- Do not point out errors solely based on grammar, number convetion, or writing style.
- Fidelity errors are based on comparing the source text and the text to be evaluated. Only point out differences in understanding, form.


## Workflow
1. First, thoroughly read the source text and the text to be evaluated. If there is a reference translation, please also consider it.
2. Then, thoroughly read the rules for fidelity and <attention>.
3. Strictly evaluate text to be evaluated according to the rules and <attention>. Provide a score, and then explain the error types, and their location.

## Output Format
{
    "type": "Fidelity",
    "grade": "Passable",
    "mark": 6,
    "mistakes": [
      {"omissions": "The original text has mentioned “the price was steep no matter where couples chose to get hitched”， but it doesn't mentioned in the text to evaluate"},
      {"mistranslation": "The phrase 'At the present critical period' in the text to evaluate simplifies the original text's meaning."},
      ......
      ]
}
 
## Initialization
As the role <Role>, strictly adhere to the <Rules> and <Workflow>, output the results in <output format> JSON. Think step by step:
"""

user_content = """
### Source Text
2020年11月中国开始了第七次人口普查。人口普查将为开启全面建设社会主义现代化国家新征程提供科学准确的统计信息支持。开展第七次全国人口普查，是推动经济高质量发展的内在要求。当前，我国经济正处于转变发展方式、优化经济结构、转换增长动力的攻关期。

### Reference Text
China carried out its Seventh National Population Census in November, 2020. The census will provide scientific and accurate statistical information support for China to embark on a new journey toward building a modern socialist country. The census reflects the internal need for the advancement of quality economic development. At present, China’s economy is in the critical period of transforming the development mode, optimizing the economic structure, and transforming the growth momentum.

### Text to Evaluate
China carried out its Seventh National Population Census in 11, 2020. The census will provide scientific and accurate information support for China to embark on a new journey toward building a modern socialist country. The census reflect the internal urgent need for the advancement of quality economic development. At the present critical period, China is transforming the development mode, optimizing the economic structure, and transforming the growth momentum.
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