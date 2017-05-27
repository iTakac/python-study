# coding:utf-8

import urllib.request
with urllib.request.urlopen("https://api.a3rt.recruit-tech.co.jp/text_classification/v1/classify?apikey=Y2cVVtAN2iNijAy47M4Ju6pXijdJ8zo1&model_id=&text=java") as res:
    html = res.read().decode("utf-8")
    print(html)

