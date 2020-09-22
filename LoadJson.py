import json
import re


with open('E:/python/ksomething/1234.txt', 'r') as fp ,open('E:/python/ksomething/videosource.txt', 'w') as f:
    
    for line in fp:
        line = str(line).replace("\n", "").replace(" ", "")
        f.write(line)


re_str = '(?<="name":)("[\w\d].+?")'
re_str2 = '(?<="url":)("[\w\d].+?")(?=},)'
re_co =  '(?<="name":)("[\w\d].+?").*?(?<="url":)(".+?")(?=},)'
pat = re.compile(re_co)

source_dic = {}

with open('E:/python/ksomething/videosource.txt', 'r') as f:
    
    for chk in pat.finditer(f.read()):       
        #print(chk.groups())
        source_dic[chk.group(1)] = chk.group(2)
        
            



jdic = json.dumps(source_dic, separators=(',',':'), ensure_ascii=False)
with open('E:/python/ksomething/MySource.json', 'w') as f:
    json.dump(source_dic, f)
with open('E:/python/ksomething/MySource.txt', 'w') as fp:
    fp.write(jdic)

with open('E:/python/ksomething/MySource.json') as f:
    dd = json.load()