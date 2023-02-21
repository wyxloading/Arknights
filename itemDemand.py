import requests
from requests.utils import requote_uri
from urllib.parse import urlencode, quote_plus

apiBase = 'https://api.prts.wiki/widget/itemDemand/'

items = ['模组数据块', '数据增补仪', '数据增补条', '烧结核凝晶', '晶体电子单元', 'D32钢', '双极纳米片', '聚合剂', '转质盐聚块', '转质盐组', '切削原液', '化合切削液', '精炼溶剂', '半自然溶剂', '晶体电路', '晶体元件', '炽合金块', '炽合金', '聚合凝胶', '凝胶', '白马醇', '扭转醇', '三水锰矿', '轻锰矿', '五水研磨石', '研磨石', 'RMA70-24', 'RMA70-12', '提纯源岩', '固源岩组', '固源岩', '源岩', '改量装置', '全新装置', '装置', '破损装置', '聚酸酯块', '聚酸酯组', '聚酸酯', '酯原料', '糖聚块', '糖组', '糖', '代糖', '异铁块', '异铁组', '异铁', '异铁碎片', '酮阵列', '酮凝集组', '酮凝集', '双酮']

def getItemDemand(item):
    api = apiBase + requote_uri(item)
    r = requests.get(api)
    total = 0
    data = r.json()
    for key in data:
        if key == 'char_1001_amiya2':
            continue
        val = data[key]
        total += val['elite'] + val['skill'] + val['uniequip']
        for i in val['mastery']:
            total += i
    return total

print(len(items))
for item in items:
    print(item, getItemDemand(item))