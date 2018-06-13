import json,os,sys
name= sys.argv[1] if len(sys.argv)>1 else 'in.txt'
urls = [i for i in open(name).read().split('\n') if i.count('http')>0]
def gen(url):
    return {"url": url, "ops": "", "type": "image", "label": {"detect": {"general_d": {"bbox": []}}}, "source_url": ""}
r = '\n'.join([json.dumps(gen(i)) for i in urls])
with open(name+'.dataset', 'w') as f: f.write(r)
