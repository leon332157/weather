# coding=utf8
import os
import platform
import time, sys
import webbrowser
import codecs

utf8 = 'utf8'
all = False
reload(sys)
default_encoding = sys.getdefaultencoding()  # 编码
sys.setdefaultencoding('utf8')  # 编码
global urls
global type
global prov
global city
global city_add
urls = []
min_list = []
city_list = []
max_list = []
c = codecs.open('temprature.txt', 'w', 'utf-8')  # 创建或清除temprature文件
if platform.system() == 'Darwin':  # 检测mac
    os.chdir('/Users/' + os.getlogin())
    # if os.getuid() == 0:
    #    pass
    # else:
    #    print('mac系统权限问题，可能无法储存，请使用root').decode(utf8)
    #    exit()
else:
    pass
try:  # 使用try以在未安装模块是自动安装
    from bs4 import BeautifulSoup as bs
    import requests
    import lxml
    import echarts
except ImportError:  # 导入错误
    if platform.system() is 'Windows':  # 检测windows
        os.system('C:\Python27\Scripts\pip.exe install bs4')
        os.system('C:\Python27\Scripts\pip.exe install requests')
        os.system('C:\Python27\Scripts\pip.exe install lxml')
        os.system('C:\Python27\Scripts\pip.exe install echarts-python')
    else:  # mac，linux
        os.system('easy_install pip')
        os.system('pip install bs4')
        os.system('pip install requests')
        os.system('pip install lxml')
        os.system('pip install echarts-python')
    from bs4 import BeautifulSoup as bs
    import requests
    import lxml
    import echarts
url_head = ('http://www.weather.com.cn/textFC/')


def prov_check(prov, city):
    global city_type
    global prov_type
    if prov == '北京':  # 直辖市，自治区
        prov_type = '市'
        if city == prov:
            city_type = '市'
        else:
            city_type = '区'
    elif prov == '天津':
        prov_type = '市'
        if city == prov:
            city_type = '市'
        else:
            city_type = '区'
    elif prov == '上海':
        prov_type = '市'
        if city == prov:
            city_type = '市'
        elif city == '浦东新区':
            city_type = ''
    elif prov == '重庆':
        prov_type = '市'
        if city == prov:
            city_type = '市'
        else:
            city_type = '区'
    elif prov == '内蒙古':
        prov_type = '自治区'
        city_type = '市'
    elif prov == '西藏':
        prov_type = '自治区'
        city_type = '市'
    elif prov == '广西':
        prov_type = '壮族自治区'
        city_type = '市'
    elif prov == '宁夏':
        prov_type = '回族自治区'
        city_type = '市'
    else:
        prov_type = '省'
        city_type = '市'
    return (prov_type, city_type)


def get_all(link):  # 下载
    global min_list
    global city_type
    global prov_type
    raw_content = requests.get(link)
    content = (raw_content.content)
    soup = bs(content, 'lxml')
    conMidtab = soup.find('div', class_='conMidtab')
    conMidtab2_list = conMidtab.find_all('div', class_='conMidtab2')
    for x in conMidtab2_list:  # 网页源码信息
        tr_list = x.find_all('tr')[2:]
        for index, tr in enumerate(tr_list):
            if index == 0:  # 第一行包括省
                td_list = tr.find_all('td')
                prov = td_list[0].text.replace('\n', '')
                city = td_list[1].text.replace('\n', '')
                min_temp = td_list[7].text.replace('\n', '')
                max_temp = td_list[4].text.replace('\n', '')
                prov_check(prov, city)
            else:  # 第二行开始
                td_list = tr.find_all('td')
                city = td_list[0].text.replace('\n', '')
                min_temp = td_list[6].text.replace('\n', '')
                max_temp = td_list[3].text.replace('\n', '')
                prov_check(prov, city)
            min_temp_int = int(min_temp)
            city_add = prov + prov_type + ' ' + city + city_type
            min_list.append({'city': city_add, 'min': min_temp_int})
            print(prov + prov_type + ' ' + city + city_type + ' ' + '最高:' + max_temp + ' ' + '最低:' + min_temp).decode(
                utf8)
            c.write(prov + prov_type + ' ' + city + city_type + ' ' + '最高:' + max_temp + ' ' + '最低:' + min_temp + '\n')
    return (min_list)


prov_slect_list = ('''(地区) 华北=hb 华东=hd 华中=hz 华南=hn 东北=db 西北=xb 西南=xn  全部=all 退出=e 此列表=h (强迫症请忽略细节...)''').encode(utf8)
print(prov_slect_list).decode(utf8)
print('输入选择').decode('utf8')


def prov_slect():
    global url
    global urls
    global all
    all = False
    prov = raw_input('>')
    if prov == 'hb':
        url = url_head + 'hb.shtml'
    elif prov == 'hd':
        url = url_head + 'hd.shtml'
    elif prov == 'hz':
        url = url_head + 'hz.shtml'
    elif prov == 'hn':
        url = url_head + 'hn.shtml'
    elif prov == 'db':
        url = url_head + 'db.shtml'
    elif prov == 'xb':
        url = url_head + 'xb.shtml'
    elif prov == 'xn':
        url = url_head + 'xn.shtml'
    elif prov == 'all':
        all = True
        urls = ['http://www.weather.com.cn/textFC/hb.shtmlv'
                'http://www.weather.com.cn/textFC/hd.shtmlv'
                'http://www.weather.com.cn/textFC/hz.shtmlv'
                'http://www.weather.com.cn/textFC/hn.shtmlv'
                'http://www.weather.com.cn/textFC/db.shtmlv'
                'http://www.weather.com.cn/textFC/xb.shtmlv'
                'http://www.weather.com.cn/textFC/xn.shtmlv']
    elif prov == 'e':
        exit(0)
    elif prov == 'h':
        print(prov_slect_list).decode(utf8)
        prov_slect()
    elif prov == '':
        print('输入选择').decode('utf8')
        prov_slect()
    else:
        print('输入错误!').decode(utf8)
        prov_slect()
    if all == True:
        url = ''
    else:
        pass
    return urls, url


prov_slect()
if all == True:  # 都是交互...
    for url in urls:
        url = url.split('v')
        links = url
    for link in links:
        print('获取中...').decode(utf8)
        try:
            get_all(link)
        except:
            print('错误！跳过').decode(utf8)
            pass
else:
    print('获取网址:' + url).decode(utf8)
    print('获取中...').decode(utf8)
    try:
        get_all(url)
    except requests.exceptions.MissingSchema:
        pass
sorted_min_temp = sorted(min_list, lambda x, y: cmp(int(x['min']), int(y['min'])))  # lambda比较温度，升序排列
final_list = sorted_min_temp[0:5]  # 取前五城市
final_city = []
final_min = []
for city_min in final_list:
    final_city.append(city_min['city'])
    final_min.append(city_min['min'])
coldest_city_raw = str(final_city[0])
coldest_city = coldest_city_raw.decode('utf-8')
coldest_temp = str(final_min[0])
print('最冷城市:' + ' ' + coldest_city + ' ' + '最低温度:' + ' ' + coldest_temp).decode(utf8)  # 显示最冷城市


def chk_saved(min_canvas):  # 检查是否保存
    if os.path.exists(os.getcwd() + '/Graph.html') is True:
        print('图表储存成功!').decode(utf8)
        print('图表储存在' + ' ' + os.getcwd() + ' ' + '名称:' + ' ' + 'Graph' + '.html').decode(utf8)
        print('打开文件中...').decode(utf8)
        if platform.system() == 'Windows':
            webbrowser.open(os.getcwd() + '\Graph' + '.html')
        elif platform.system == 'Linux':
            webbrowser.open(os.getcwd() + '/Graph' + '.html')
        else:
            webbrowser.open('file://' + os.getcwd() + '/Graph' + '.html')
    else:
        print('未储存!').decode(utf8)
        print('直接在浏览器打开!').decode(utf8)
        min_canvas.plot()
    if os.path.exists(os.getcwd() + '/temprature.txt') is True:
        print('温度储存成功!').decode(utf8)
        print('温度储存在' + ' ' + os.getcwd() + ' ' + '名称:' + ' ' + 'temprature' + '.txt').decode(utf8)
        print('打开文件中...').decode(utf8)
        if platform.system() == 'Windows':
            os.system(os.getcwd() + '/temprature' + '.txt')
        else:
            os.system('cat' + ' ' + os.getcwd() + '/temprature' + '.txt')
    else:
        print('未储存温度,跳过!').decode(utf8)
        pass


def save_graph(final_min, final_city):  # 保存图表
    min_canvas = echarts.Echart('最低温度统计', '来自中国天气网')
    min_bar = echarts.Bar('最低温度', final_min)  # 柱状图
    min_axis = echarts.Axis('category', 'bottom', data=final_city)  # 横向坐标
    min_canvas.use(min_bar)
    min_canvas.use(min_axis)
    if platform.system() is 'Windows':
        min_canvas.save(os.getcwd(), '\Graph')
        chk_saved(min_canvas)
    else:
        min_canvas.save(os.getcwd(), '/Graph')
        chk_saved(min_canvas)


save_graph(final_min, final_city)
# 理论效果图：
#
#                              #
#                              #
#                          #   #
#                      #   #   #
#                      #   #   #
################################################ 0c
#     #    #   #   #
#     #    #   #
#     #    #
#     #
#     #
#     #
################################################
sys.setdefaultencoding(default_encoding)  # 编码设定
c.close()