

# https://krdict.korean.go.kr/chn
# 韩语翻译

import requests
import json

def translate(word = '위'):
  fileName = 'translate/'+word+'.json'

  try:
    with open(fileName,"r") as file:
      if file:
        print('已经生成', file.read())
        return file.read()
  except:
    url = "https://krdict.korean.go.kr/chn/smallDic/searchResult?nation=chn&nationCode=11&ParaWordNo=&mainSearchWord=" + word
    result = requests.get(url)
    content = result.text.split('<span class="word_att_type1">')[1]
    phoneticSymbols = content.split('<span class="manyLang11">')
    content = phoneticSymbols[1]
    phoneticSymbols = phoneticSymbols[0].strip()
    partOfSpeech = content.split('</span>')[0].strip()
    sentence = list(filter(None, content.split('</dl>')[0].split('</dt>')[1].replace('\t', '').replace('\n', '').replace('\r', '').split('</dd>')))
    data = []
    for i in range(len(sentence)):
      _index = len(data)
      index = i % 3
      text = sentence[i].split('</strong>.')
      if len(text) > 1:
        sentence[i] = text[1]
      else:
        text2 = sentence[i].split('>')
        sentence[i] = len(text2) > 1 and text2[1] or text2[0]

      if index == 0:
        data.append({
          'title': '',
          'korean': '',
          'chinese': ''
        })

      key = [
        'title',
        'korean',
        'chinese'
      ][index];
      data[_index-1][key] = sentence[i]


    result = str({"word": word, "phoneticSymbols": phoneticSymbols, "partOfSpeech": partOfSpeech, "sentence": data}).replace("'", "\"").replace('None', '""')
    with open(fileName,"w") as file:
      file.write(result)
    print(result)
    return result

translate('게')