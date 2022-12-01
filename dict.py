import requests
import json

def getDictData(page = 1):
  url = "https://gateway.dict.naver.com/cndict/zh_CN/zhko/user/search/words?_callback=window.__jindo_callback._1652&sort=desc&sort_type=&language=ko&page_size=100&page=" + str(page)
  result = requests.get(url)
  result = result.text.replace("window.__jindo_callback._1652(", "").replace("}})", "}}");
  result = json.loads(result).get("data").get("m_items")
  # 生成文件
  with open('dict/第'+str(page)+'页.json',"w") as file:
    file.write(str({"data": result}).replace("'", "\"").replace('None', '""'))
  print("第"+str(page)+"页生成成功")
  if len(result) > 0:
    getDictData(page + 1)

getDictData(1)