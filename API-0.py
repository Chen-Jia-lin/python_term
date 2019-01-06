from __future__ import unicode_literals
from flask import Flask, render_template, request
import requests
import csv

app = Flask(__name__)

def request1(consName,type)->str:
    parameters = {'consName': consName,'type':type,'key': '62e686c22822cea83b4d203852ac6bda'}
    base = 'http://web.juhe.cn:8080/constellation/getAll'
    response = requests.get(base, parameters)
    answer = response.json()
    return str(answer)


def ipadress(ip:str)->str:
    parameters = {'ip': ip,'key': '21475495a9917fab6f81bb0dd411841a'}
    base = 'http://apis.juhe.cn/ip/ip2addr'
    response = requests.get(base, parameters)
    answer= response.json()
    answer=answer['result']
    return str(answer)

def request2(phone)->str:
    parameters = {'phone': phone,'key': 'c7b0ce17c29e5bf5d93fbe6e66c7eb59'}
    base = 'http://apis.juhe.cn/mobile/get'
    response = requests.get(base, parameters)
    answer = response.json()
    answer = answer['result']
    return str(answer)

def request3(type)->str:
    parameters = {'type':type ,'key': '903233e320e161e9f2f1dd5a5baff356'}
    base = 'http://v.juhe.cn/toutiao/index'
    response = requests.get(base, parameters)
    answer = response.json()
    answer=answer['result']['title']
    return str(answer)

def request4(word)->str:
    parameters = {'word':word ,'key': 'b8a5244076bac9ccd55edbb1e36a9c54'}
    base = 'http://v.juhe.cn/chengyu/query'
    response = requests.get(base, parameters)
    answer = response.json()
    answer=answer['result']
    return str(answer)



@app.route('/search4_cjl', methods=['POST','GET'])
def do_cjl_search() -> 'html':
    consName = request.form['consName']
    type = request.form['type']
    title = '这是查询结果:'
    results = request1(consName,type)
    return render_template('results_cjl.html',
                           the_title=title,
                           the_phrase=consName,
                           the_letters=type,
                           the_results=results,)

@app.route('/')
def entry_page() -> 'html':
    return render_template('entry.html',
                           the_title='欢迎来到B班第三小组Python世界')


@app.route('/cjl')
def entry_cjl_page() -> 'html':
    return render_template('entry_cjl.html',
                           the_title='欢迎使用星座运势查询')


@app.route('/search4_ywm', methods=['POST'])
def do_ywm_search() -> 'html':
    ipl = request.form['ipl']
    title = '这是查询结果:'
    results = ipadress(ipl)
    return render_template('results_ywm.html',
                           the_title=title,
                           the_phrase=ipl,
                           the_results=results,)


@app.route('/ywm', methods=['POST'])
def entry_ywm_page() -> 'html':
    return render_template('entry_ywm.html',
                           the_title='欢迎使用ip地址查询')


@app.route('/search4_tkx', methods=['POST'])
def do_tkx_search() -> 'html':
    phone = request.form['phone']
    title = '这是查询结果:'
    results = requests2(phone)
    return render_template('results_tkx.html',
                           the_title=title,
                           the_phrase=phone,
                           the_results=results,)
    

@app.route('/tkx', methods=['POST'])
def entry_tkx_page() -> 'html':
    return render_template('entry_tkx.html',
                           the_title='欢迎使用电话号码查询')




@app.route('/dyz', methods=['POST'])
def entry_dyz_page() -> 'html':
    return render_template('entry_dyz.html',
                           the_title='欢迎使用新闻头条查询')


@app.route('/search4_dyz', methods=['POST'])
def do_dyz_search() -> 'html':
    type = request.form['type']
    title = '这是查询结果:'
    results = request3(type)
    return render_template('results_dyz.html',
                           the_title=title,
                           the_phrase=type,
                           the_results=results,)

@app.route('/dyj', methods=['POST'])
def entry_dyj_page() -> 'html':
    return render_template('entry_dyj.html',
                           the_title='欢迎使用成语大全查询')


@app.route('/search4_dyj', methods=['POST'])
def do_dyj_search() -> 'html':
    word = request.form['word']
    title = '这是查询结果:'
    results = request4(word)
    return render_template('results_dyj.html',
                           the_title=title,
                           the_phrase=word,
                           the_results=results,)




if __name__ == '__main__':
    app.run(debug=True)
