# -*- coding: utf-8 -*-
"""
调用线上以图搜图接口识别图片
input: urllist file
output: json file

@author: pengyuyan
"""
import time
import requests
import json
from qiniu import QiniuMacAuth
import argparse
import datetime
from multiprocessing import Pool

#def retrieval_upload_img(access_key, secret_key, url):
def retrieval_upload_img(url):
    """
    以图搜图传图
    :return:
    """
    access_key=args.access_key
    secret_key = args.secret_key
    req_url = 'http://argus.atlab.ai/v1/image/group/fy_test/add'
    data = {
        "data": [
            {"uri": url}
            ]
    }
    # data = 
    # {
	# "data": [
	# 	{
	# 		"uri": "",
	# 		"attribute": {
	# 			"label": "fy_testsimilar"
	# 		}
	# 	}
	# ]
    # }
    token = QiniuMacAuth(access_key, secret_key).token_of_request(
        method='POST',
        host='argus.atlab.ai',
        url="/v1/image/group/fy_test/add",
        content_type='application/json',
        qheaders='',
        body=json.dumps(data)
    )
    token = 'Qiniu ' + token
    headers = {"Content-Type": "application/json", "Authorization": token}
    response = requests.post(req_url, headers=headers, data=json.dumps(data))

    print( '-'*80)
    print(response.text)
    print(response.text).replace('false', 'False').replace('true', 'True')
    ret = eval(response.text.replace('false', 'False').replace('true', 'True'))

    print(json.dumps(ret, encoding="utf-8", ensure_ascii=False))
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
        url = urllist_f.readlines()
        len_file = len(url)
        list_all = get_list_all(args.urllist_file)
        try: 
            pool = Pool(processes=20)
            result = pool.map(retrieval_upload_img,list_all)
            pool.close()
            pool.join()
            for j in range(len(result)):
                json_f.write(str(result[j])+'\n')
        except Exception, e:
             print(e)
             error_f.writelines(url+', '+str(e)+'\n')

    print (datetime.datetime.now(), 'done')
