# -*- coding: utf-8 -*-
"""
调用线上以图搜图接口识别图片
input: urllist file
output: json file

@author: pengyuyan
"""

import requests
import json
from qiniu import QiniuMacAuth
import argparse
import datetime
from multiprocessing import Pool

def retrieval_search_group(url):
    """
    根据以图搜图算法搜查图片返回相似图结果
    :param url: 要识别的图片URL
    :return:
    """
    access_key=args.access_key
    secret_key = args.secret_key
    req_url = 'http://argus.atlab.ai/v1/image/group/fy_test/search'
    data = {
	"data": {
		"uri": url
	},
	"params": {
		"limit": 15
	}
}
    token = QiniuMacAuth(access_key, secret_key).token_of_request(
        method='POST',
        host='argus.atlab.ai',
        url="/v1/image/group/fy_test/search",
        content_type='application/json',
        qheaders='',
        body=json.dumps(data)
    )
    token = 'Qiniu ' + token
    headers = {"Content-Type": "application/json", "Authorization": token}
    response = requests.post(req_url, headers=headers, data=json.dumps(data))

    print response.text
    print response.headers
    print response.text.replace('false', 'False').replace('true', 'True')
    ret = eval(response.text.replace('false', 'False').replace('true', 'True'))
    ret['url'] = url

    # json.load(ret, encoding="utf-8", ensure_ascii=False)
    print json.dumps(ret, encoding="utf-8", ensure_ascii=False)
    return json.dumps(ret, encoding="utf-8", ensure_ascii=False)


def parse_args():
    """
    Parse input arguments.
    :return:
    """
    parser = argparse.ArgumentParser(description='以图搜图API测试')
    parser.add_argument('--ak', dest='access_key', help='access_key for qiniu account',
                        type=str)

    parser.add_argument('--sk', dest='secret_key', help='secret_key for qiniu account',
                        type=str)

    parser.add_argument('--in', dest='urllist_file', help='urllist file',
                        type=str)

    return parser.parse_args()

def get_list_all(file_name):
    url_list=[]
    with open(file_name,"r") as f:
        lines = f.readlines()
        for i in range(len(lines)):
            url_list.append(lines[i].strip('\n'))
    return url_list

if __name__ == '__main__':
    args = parse_args()

    with open(args.urllist_file) as urllist_f, \
            open(args.urllist_file+'.retrieval.json', 'w+') as json_f,\
            open(args.urllist_file+'.error.log', 'w+') as error_f:

        list_all = get_list_all(args.urllist_file)
        try: 
            pool = Pool(processes=1)
            result = pool.map(retrieval_search_group,list_all)
            pool.close()
            pool.join()
            for j in range(len(result)):
                json_f.write(str(result[j])+'\n')
        except Exception, e:
             print(e)
            # error_f.writelines(str(result)+', '+str(e)+'\n')   
 
    print datetime.datetime.now(), 'done'
