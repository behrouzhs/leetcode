import os
import re
import sys
import json
import requests
from bs4 import BeautifulSoup


def usage():
    print('Usage: \n\tpython extract_question.py leetcode_url')


def to_snake_case(text: str):
    text = re.sub(r'[^a-zA-Z0-9]', '_', text)
    text = re.sub(r'(?<!^)(?=[A-Z])', '_', text).lower()
    text = re.sub(r'__+', '_', text)
    return text.strip('_')


def extract_question_info(url: str):
    title_slug = url[url.rfind('/') + 1:]
    headers = {
        'origin': 'https://leetcode.com',
        'accept-encoding': 'gzip, deflate',
        'accept-language': 'zh-CN,zh;q=0.9,und;q=0.8,en;q=0.7',
        'cookie': '__cfduid=dae082e425ee3916c04a5170b832e268e1524142659; _ga=GA1.2.1432146910.1524142661; _gid=GA1.2.650843898.1529736240; csrftoken=iSKedVXxGDkBBXbP9chsyXhbIrRedF7iw2EMRZiemtzKD8vjHSWZJKkKQVIwZKp7; __atuvc=2%7C25; __atuvs=5b2ded02313c83c4001; _gat=1',
        'x-csrftoken': 'iSKedVXxGDkBBXbP9chsyXhbIrRedF7iw2EMRZiemtzKD8vjHSWZJKkKQVIwZKp7',
        'pragma': 'no-cache',
        'content-type': 'application/json',
        'accept': '*/*',
        'cache-control': 'no-cache',
        'authority': 'leetcode.com',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36',
        'referer': url
    }

    payload = {
        "operationName": "questionData",
        "variables": {"titleSlug": title_slug},
        "query": "query questionData($titleSlug: String!) {\n  question(titleSlug: $titleSlug) {\n    questionId\n    questionFrontendId\n    boundTopicId\n    title\n    titleSlug\n    content\n    translatedTitle\n    translatedContent\n    isPaidOnly\n    difficulty\n    likes\n    dislikes\n    isLiked\n    similarQuestions\n    contributors {\n      username\n      profileUrl\n      avatarUrl\n      __typename\n    }\n    langToValidPlayground\n    topicTags {\n      name\n      slug\n      translatedName\n      __typename\n    }\n    companyTagStats\n    codeSnippets {\n      lang\n      langSlug\n      code\n      __typename\n    }\n    stats\n    hints\n    solution {\n      id\n      canSeeDetail\n      __typename\n    }\n    status\n    sampleTestCase\n    metaData\n    judgerAvailable\n    judgeType\n    mysqlSchemas\n    enableRunCode\n    enableTestMode\n    envInfo\n    __typename\n  }\n}\n"
    }

    res = requests.post('https://leetcode.com/graphql', headers=headers, json=payload)
    return res.json()


def initialize_question(dct_question_info: dict):
    dct_question_info['data']['question']['topics'] = [item['name'] for item in dct_question_info['data']['question']['topicTags']]
    dct_question_info['data']['question']['similarQuestionsLink'] = [f"https://leetcode.com/problems/{item['titleSlug']}" for item in json.loads(dct_question_info['data']['question']['similarQuestions'])]
    
    dct_info = dct_question_info['data']['question']
    title = to_snake_case(dct_info['title'])
    question_id = dct_info['questionFrontendId'].zfill(4)
    difficulty = dct_info['difficulty'].lower()
    code = [item for item in dct_info['codeSnippets'] if item['lang'].lower() == 'python3']
    if len(code) == 0:
        code = [item for item in dct_info['codeSnippets'] if item['lang'].lower() == 'python']
    code = code[0]['code'] if len(code) > 0 else ''
    question_text = BeautifulSoup(dct_info['content'], 'html.parser').text.replace('\xa0', ' ')
    qid = f'{question_id}_{title}'
    folder = f'./{difficulty}/{qid}/'

    if not os.path.exists(folder):
        os.makedirs(folder)
    with open(f'{folder}/{qid}.json', 'wt') as fp:
        json.dump(dct_question_info, fp, indent=4)
        fp.write('\n')
    with open(f'{folder}/{qid}.html', 'wt') as fp:
        fp.write(dct_info['content'] + '\n')
    
    with open(f'{folder}/{qid}.py', 'wt') as fp:
        fp.write(f'# URL: https://leetcode.com/problems/{dct_info["titleSlug"]}\n')
        fp.write(f'# Title: {dct_info["questionFrontendId"]}. {dct_info["title"]}\n')
        fp.write(f'# Difficulty: {dct_info["difficulty"]}\n')
        fp.write(f'# Topics: {", ".join(dct_info["topics"])}\n\n\n')
        fp.write(f'question = """\n{question_text}\n"""\n\n')
        fp.write(f'{code}pass\n')


if __name__ == '__main__':
    if len(sys.argv) < 2:
        usage()
    else:
        url = sys.argv[1]
        res = extract_question_info(url)
        initialize_question(res)