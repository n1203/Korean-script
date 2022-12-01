

# https://krdict.korean.go.kr/chn
# 韩语每日一句
import requests
import time

def getDaily():
  _time = time.strftime("%Y-%m-%d", time.localtime())
  fileName = 'daily/'+_time+'.json'

  with open(fileName,"r") as file:
    if file:
      print('今日已经生成', file.read())
      return file.read()

  url = "https://krdict.korean.go.kr/chn"
  result = requests.get(url)
  content = result.text.split('<dl class="today_word">')[1].split('</dl>')[0]
  keyword = content.split('<strong>')[1].split('</strong>')[0]
  description = content.split('<dd>')[1].split('</dd>')[0]
  descriptionCN = content.split('<dd class="manyLang11">')[1].split('</dd>')[0]
  print (keyword)
  print (description)
  print (descriptionCN)
  with open(fileName,"w") as file:
    file.write(str({"keyword": keyword, "description": description, "descriptionCN": descriptionCN, "time": _time}).replace("'", "\"").replace('None', '""'))

getDaily()