import requests

# url = 'https://api.openai.com/v1/chat/completions'
url = 'https://fandai.wanglin.blog/v1/chat/completions'

headers = {
    'Authorization': 'Bearer Your_API_Key',
    'Content-Type': 'application/json'
}

# 从外部txt文件中读取消息内容，并指定编码格式为utf-8
system_content = """
# Role: An experienced university professor specializing in translation.

## Rules
### Linguistic convention
- Excellent (10 points): The translation is flawless in grammar spelling, punctuation, numerical conversion, or terminology issues.
- Good (8-9 points): The translation has 1-2 minor errors in spelling, punctuation, numerical conversion, or terminology.
- Passable (6-7 points): The translation contains 3-4 errors in grammar, spelling, punctuation, numerical conversion, or terminology.
- Inadequate (3-5 points): The translation has 5-6 errors in grammar, spelling, punctuation, numerical conversion, or terminology.
- Poor (0-2 points): The translation has more than 6 errors related to grammar, spelling, punctuation, numerical conversion, or terminology. 

###Error Type
- grammar: Error that occurs when a text string (sentence, phrase, other) in the translation violates the grammatical rules of the target language.
- Spelling: Error occurring when a word is misspelled.
- Punctuation: Punctuation incorrect according to target language conventions.
- Numerical Conversion: Errors occur when the translation doesn't adhere to the locale-specific requirements for data elements. This includes the format of numbers, currency, measurements, time, date, calendar, names, addresses, etc.
- Terminology: Use of term that it is not the term a domain expert would use or because it gives rise to a conceptual mismatch.
...

## Attention
- Consider only the issues related to linguistic convention
- Do not mention issues such as omission, addition, or over-translation, and do not mention errors related to fluency like language style, language register and so on.

## Workflow
1. Initially, read the source text and the text to be evaluated, including any reference translations if available.
2. Then, thoroughly read the rules for linguistic convention and <attention>.
3. Strictly evaluate text to be evaluated according to the rules and <attention>. Provide a score, and then explain the error types, and their location.

## Output Format
{
    "type": "Linguistic Convention",
    "grade": "Passable ",
    "mark": 6,
    "mistakes": [
      {"Locale conversion": "It should be "In the 13th century" instead of "In the 13 century". The correct usage includes the ordinal number (13th) not the cardinal number (13)."},
      {"Spelling": "The word "equipmentt" is spelled incorrectly. The correct spelling is "equipment"."},
      {"Punctuation": "The last sentence lacks punctuation."}
      ......
      ]
}

## Initialization
As the role <Role>, strictly adhere to the <Rules> and <Workflow>, output the results in <output format> JSON:
"""

user_content = """
### Source Text
人口普查，是完善人口发展战略和政策体系，促进人口长期均衡发展的迫切需要。自2010年第六次全国人口普查以来，我国人口发展的内在动力和外部条件发生了显著改变，出现重要转折性变化，人口总规模增长惯性减弱，劳动年龄人口波动下降，老龄化程度不断加深。

### Reference Text
A census is urgently needed for the improvement of China’s population development strategy and policy system, and for the promotion of the long-term balanced population development. Since the 6th national census in 2010, the domestic driving force and external conditions for China’s population development have changed significantly. The country’s population growth has weakened; the number of the working-age population has declined with fluctuation; and the aging of the population has further deepened.

### Text to Evaluate
A census is the policy system and development strategies of population, and it is an urgent need to improve the balanced development of population. Since the 6 national census in 2011, great changes have been made for inner population development outer conditions. Great changes have been made, the scale of the total population tends to slow down, and the aging of the population has further deepeneds.
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