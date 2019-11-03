import pandas as pd

from selenium import webdriver

options = webdriver.ChromeOptions()

options.add_argument('–headless')

options.add_argument('–no-sandbox')

options.add_argument('–disable-dev-shm-usage')

driver = webdriver.Chrome('chromedriver',options=options)

url="https://www.jisilu.cn/data/cbnew/#cb"

driver.get(url)

x=driver.find_element_by_css_selector("#flex_cb").text

y=x.find("(万元) 操作")

z=x[y+7:].strip().split("\n")

cols=["代码","转债名称","现价","涨跌幅","正股名称","正股价","正股涨跌","PB","转股价","转股价值","溢价率","纯债价值","评级","期权价值","回售触发价","强赎触发价","转债占比","机构持仓","到期时间","剩余年限","到期税前收益","到期税后收益","回售收益","成交额","双低"]

df1=pd.DataFrame(columns=cols)

for i in z:

    data=i.strip().split()

    if data[2].strip()=="!":

        data.pop(2)

    if data[5].strip()=="R":

        data.pop(5)

    data[2] = float(data[2])
    data[10] = data[10].strip('%')
    data[10] = float(data[10])

    data[24] = data[2] + data[10]
    dic=dict()

    for j in range(len(cols)):

        dic.update({cols[j]:[data[j]]})

    df2=pd.DataFrame(dic)

    df1=df1.append(df2)

df1=df1.reset_index(drop=True)

df1.sort_values(by="双低",ascending=True)

df1.drop(["纯债价值","期权价值","机构持仓","回售收益"], axis=1, inplace=True)

df1.to_excel("C:\\Users\Administrator\\Desktop\\jisilu.xls")

print(df1)
