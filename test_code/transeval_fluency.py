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
### Fluency Criteria
- Excellent（10 points）: Text to be evaluated is smooth, the logic is clear, and the language style is completely consistent with the original text.
- Good(8-9 points): Text to be evaluated is relatively smooth, the logic is relatively clear, and the language style is highly consistent with the original text.
- Passable(6-7 points): Text to be evaluated is basically smooth, the logic is basically clear, and the language style is similar to the original text.
- Inadequate(3-5 points): Text to be evaluated is somewhat rigid, the logic is not very clear, and the language style is significantly different from the original text.
- Poor(0-2 points): The language of the text to be evaluated is obscure, the logic is chaotic, there are more than 4 minor grammatical errors, and there is a phenomenon of over literal translation.

###Error Types
- smoothness
- logic chaotic
- Language register: Characteristic of text that uses a level of formality higher or lower than required by the specifications or general language conventions.
- language style: Errors occuring when text fails to conform wth a declared external style reference.
- over literal translation: Translating word-for-word from the original text without considering the customs and expressions of the target language.
...

## Attention
- Consider only the issues related to fluency evaluation criteria
- Do not mention issues such as omission, addition, or over-translation, and do not mention errors related to grammar, punctuation, numbers, or dates.

## Workflow
1. Initially, read the source text and the text to be evaluated, including any reference translations if available.
2. Then, thoroughly read the rules for fluency and <attention>.
3. Strictly evaluate text to be evaluated according to the rules and <attention>. Provide a score, and then explain the error types, and their location.

## Output Format
{
    "type": "Fluency",
    "grade": "Good",
    "mark": 8,
    "mistakes": [
      {"smoothness": "The translation lacks fluency and does not conform to the reading habits of the target language readers."},
      {"over literal translation": "Four Persistences” should be exlained in the translation ranther than just translate the surface meaning."}
      ......
      ]
}

## Initialization
As the role <Role>, strictly adhere to the <Rules> and <Workflow>, output the results in <output format> JSON. Think step by step:
"""

user_content = """
### Source Text
人口普查，是完善人口发展战略和政策体系，促进人口长期均衡发展的迫切需要。自2010年第六次全国人口普查以来，我国人口发展的内在动力和外部条件发生了显著改变，出现重要转折性变化，人口总规模增长惯性减弱，劳动年龄人口波动下降，老龄化程度不断加深。

### Reference Text
A census is urgently needed for the improvement of China’s population development strategy and policy system, and for the promotion of the long-term balanced population development. Since the 6th national census in 2010, the domestic driving force and external conditions for China’s population development have changed significantly. The country’s population growth has weakened; the number of the working-age population has declined with fluctuation; and the aging of the population has further deepened.

### Text to be evaluated
A census is the policy system and development strategies of population, and it is an urgent need to improve the balanced development of population. Since the sixth national census in 2010, great changes have been made for inner population development outer conditions. Great changes have been made, the scale of the total population tends to slow down, and the aging of the population has further deepened.
"""

data = {
    'model': 'gpt-4-0125-preview',
    # 'model': 'gpt-3.5-turbo-0125',
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