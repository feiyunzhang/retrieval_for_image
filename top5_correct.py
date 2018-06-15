# -*- coding: utf-8 -*-
import json
import argparse

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

    parser.add_argument('--in', dest='json_file', help='json file',
                        type=str)

    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()

    file = open(args.json_file,'r')
    res = []
    a = 0

    for line in file.readlines():
        dic = json.loads(line)
        img_url = dic["url"]
        t = {"url": img_url, "true":0, "simialr_uri":[]}
        if not "error" in dic.keys():
            a += 1
            #im_num = img_url.split('.')[-2].split('/')[-1].lstrip('image_group_test_')
            im_num = img_url.split('.')[-2].split('/')[-1]#.lstrip('image_group_test_')
            print(im_num)
            for i in dic["result"]:
                uri = []
                #print((i["uri"].split('/'))[4].split('__')[0]=="eval",(i["uri"].split('/'))[4].split('-')[0])
                print((i["uri"].split('/'))[4])
                if ((i["uri"].split('/'))[4].split('__')[0]=="eval") and (im_num in (i["uri"].split('/'))[4].split('-')[0]):
                    t["simialr_uri"].append(i)
                    t["true"] += 1
            res.append(t)

    r = 0
    for i in range(a):
        r += res[i]["true"]

    correct = r/(float(a)*15)
    print ("The top-5 correct percentage is %f" % correct)
