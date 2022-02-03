import json
import requests


def json_parser(json_obj):
    jsonLoad = json.loads(json_obj)
    return jsonLoad["ISSUE_TRACKER"]

def find_state(query_url):
    params = {'accept': 'application/vnd.github.v3+json',
              'state': 'all'}
    try:
        response = requests.get(query_url, params=params).json()
        json_str = json.dumps(response)
        return json.loads(json_str)["state"]
    except:
        print("An exception occurred! Url is invalid")

def main():
    base_url = f'https://api.github.com/repos/'
    f = open('ProblemList.json',)
    data = json.load(f)
    
    for j in data:
        str_json = json.dumps(j)
        git_issue_url = json_parser(str_json)
        repo_issueUrl = git_issue_url.replace("https://github.com/", "")
        final_url = base_url + repo_issueUrl
        state = find_state(final_url)
        j["ISSUE_TRACKER_STATUS"] = state  
    
    with open('output.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    main()



