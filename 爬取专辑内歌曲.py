# import requests
#
# url = 'https://m10.music.126.net/20190730085044/771b0fa0b18f4ff8a665512d4b868b93/yyaac/545e/065b/0e52/c4653bbfee11db0fa6039818fe9869d9.m4a'
#
# results = requests.get(url).content
# with open('./hhh.m4a','wb') as f:
#     f.write(results)
# 实现爬取一个专辑里的所有歌曲
# 该代码的链接是https://blog.csdn.net/qq_35557718/article/details/97755431

import requests
from lxml import etree
# 确定url地址
url = 'https://music.163.com/artist?id=44266'
base_url = 'https://link.hhtjim.com/163/'

# 请求
results = requests.get(url).text  #以文本方式显示
# print(results)

# 筛选数据
dom = etree.HTML(results)
ids = dom.xpath('//a[contains(@href,"song")]/@href')
# print(ids)

for song_id in ids:
    #过滤切割
    count_id = song_id.strip('/song?id=')
    # 过滤$符号
    if('$' in count_id )== False:
        # print(count_id)
        song_url = base_url + '%s'%count_id+'.mp3'
        # print(song_url)
        song_name = song_url.split('/')[-1]#切割url，以歌的id命名
        print(song_name)
        music = requests.get(song_url).content
        # 写入文件
        with open('./%s'%song_name,'wb') as file:
            file.write(music)
