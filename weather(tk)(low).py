#encoding=utf8
print ('加载界面中...').decode('utf8')
import os,sys,time,Tkinter,codecs,platform
import tkMessageBox as messagebox
from functools import partial
import webbrowser
min_list = []
reload (sys)
default_encoding=sys.getdefaultencoding()#编码
sys.setdefaultencoding('utf8')
c = codecs.open('temprature.txt','w','utf-8')#创建或清除temprature文件
c.write(' ')
if platform.system() == 'Darwin':#检测mac
    os.chdir('/Users/'+os.getlogin())
else:
    pass
utf8 = 'utf8'
try:#使用try以在未安装模块是自动安装
 from bs4 import BeautifulSoup as bs
 import requests
 import lxml
 import echarts
except ImportError:#导入错误
    if platform.system() is 'Windows':#检测windows
        os.system('C:\Python27\Scripts\pip.exe install bs4')
        os.system('C:\Python27\Scripts\pip.exe install requests')
        os.system('C:\Python27\Scripts\pip.exe install lxml')
        os.system('C:\Python27\Scripts\pip.exe install echarts-python')
    else:#mac，linux
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
try:
    requests.get('http://www.baidu.com')
    net_good = True
except:
        net_good = False
def prov_check(prov,city):
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
    return (prov_type,city_type)
def get():#获取一个
    if not min_list == []:
     messagebox.showinfo('提示','已经获取过数据，请清空数据后再重新获取。',icon = 'warning')
     return()
    else:
     global city_type
     global prov_type
     global url
     global urls
     global all
     global links
     global link
     global ok
     global geted
     prov = e1.get()
     ok = False
     if prov == 'hb':
        link = url_head + 'hb.shtml'
        ok = True
     elif prov == 'hd':
        link = url_head + 'hd.shtml'
        ok = True
     elif prov == 'hz':
        link = url_head + 'hz.shtml'
        ok = True
     elif prov == 'hn':
        link = url_head + 'hn.shtml'
        ok = True
     elif prov == 'db':
        link = url_head + 'db.shtml'
        ok = True
     elif prov == 'xb':
        link = url_head + 'xb.shtml'
        ok = True
     elif prov == 'xn':
        link = url_head + 'xn.shtml'
        ok = True
     elif prov == '':
        messagebox.showerror('请输入地区'.decode(utf8),'请输入地区，全部地区请按全部按钮。'.decode(utf8),icon = 'error')
     else:
        messagebox.showerror('请输入正确地区'.decode(utf8), '请输入正确地区，全部地区请按全部按钮。'.decode(utf8),icon = 'error')
     if ok == False:
        return()
     else:
      if messagebox.askquestion('确认','开始获取？（如果三分钟内未响应，请重新运行程序。）') == 'no':
         return()
      else:
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
             print((prov + prov_type + ' ' + city + city_type + ' ' + '最高:' + max_temp + ' ' + '最低:' + min_temp).decode(utf8))
             city_insert = prov + prov_type + ' ' + city + city_type
             min_temp_int = float(min_temp)
             min_list.append({'city': city_insert, 'min': min_temp_int})
       messagebox.showinfo('获取完成！', '获取完成，点击保存图表开始保存图表。', icon='info')
    return(min_list)
def getall():  # 获取所有
    if not min_list == []:
     messagebox.showinfo('提示','已经获取过数据，请清空数据后再重新获取。',icon = 'warning')
     return()
    else:
     global city_type
     global prov_type
     global url
     global urls
     global all
     global links
     global link
     global geted
     if messagebox.askquestion('确认', '开始获取？（如果三分钟内未响应，请重新运行程序。）') == 'no':
        return ()
     else:
      urls = ('http://www.weather.com.cn/textFC/hb.shtmlv'
                'http://www.weather.com.cn/textFC/hd.shtmlv'
                'http://www.weather.com.cn/textFC/hz.shtmlv'
                'http://www.weather.com.cn/textFC/hn.shtmlv'
                'http://www.weather.com.cn/textFC/db.shtmlv'
                'http://www.weather.com.cn/textFC/xb.shtmlv'
                'http://www.weather.com.cn/textFC/xn.shtmlv')
      links = urls.split('v')
      for link in links:
       try:
        raw_content = requests.get(link)
       except:
          pass
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
             print (prov + prov_type + ' ' + city + city_type + ' ' + '最高:'.decode(utf8) + max_temp + ' ' + '最低:'.decode(utf8) + min_temp)
             city_insert = prov + prov_type + ' ' + city + city_type
             min_temp_int = int(min_temp)
             min_list.append({'city': city_insert, 'min': min_temp_int})
      messagebox.showinfo('获取完成！', '获取完成，点击确认开始保存图表。', icon='info')
     return (min_list)
def save_graph(min_list):#保存图表
    if not min_list == []:
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
        messagebox.showinfo('最冷城市', '最冷城市:' + ' ' + coldest_city + ' ' + '最低温度:' + ' ' + coldest_temp)  # 显示最冷城市
        min_canvas = echarts.Echart('最冷前五城市', '来自中国天气网')
        min_bar = echarts.Bar('最低温度', final_min)  # 柱状图
        min_axis = echarts.Axis('category', 'bottom', data=final_city)  # 横向坐标
        min_canvas.use(min_bar)
        min_canvas.use(min_axis)
        if platform.system() is 'Windows':
            try:
             min_canvas.save(os.getcwd(), '\Low Graph')
            except:
                messagebox.showerror('错误', '文件未储存或储存失败，直接打开图表。', icon='warning')
                min_canvas.plot()
        else:
            try:
              min_canvas.save(os.getcwd(), '/Low Graph')
            except:
                messagebox.showerror('错误', '文件未储存或储存失败，直接打开图表。', icon='warning')
                min_canvas.plot()
        if os.path.exists(os.getcwd() + '/Low Graph.html') is True:
            if messagebox.askquestion('确认','文件保存在' + ' ' + os.getcwd() + '/' + 'Low Graph' + '.html'+'  '+'打开文件？') == 'no':
             pass
            else:
                if platform.system() == 'Windows':
                    webbrowser.open(os.getcwd() + '\Low Graph' + '.html')
                elif platform.system == 'Linux':
                    webbrowser.open(os.getcwd() + '/Low Graph' + '.html')
                else:
                    webbrowser.open('file://' + os.getcwd() + '/Low Graph' + '.html')
		    exit()
        else:
            messagebox.showerror('错误','文件未储存或储存失败，直接打开图表。',icon = 'warning')
            min_canvas.plot()

    else:
        messagebox.showerror('请先获取数据', '请先获取数据，再保存图表', icon='error')
        return()
def clear_data():
 if messagebox.askquestion('确认','是否清空数据?') == 'no':
  return()
 else:
  min_list[:] = []
  messagebox.showinfo('成功','成功清空数据!',icon = 'info')
 return(min_list)
def print_min_list(min_list):
 if not min_list == []:
  messagebox.showinfo('数据',min_list)
 else:
  messagebox.showinfo('数据', '空')
root1 = Tkinter.Tk()
t_var1 = Tkinter.Variable()
areas = Tkinter.StringVar()
l1 = Tkinter.Label(root1,text='在文本框输入选择的地区', font=('', 18))
areas.set(('''地区: 华北=hb 华东=hd 华中=hz 华南=hn 东北=db 西北=xb 西南=xn 全部=全部按钮''').decode('utf8'))
e1 = Tkinter.Entry(root1, textvariable = t_var1)#文本框
b3 = Tkinter.Button(root1,text = '退出'.decode('utf-8'),command = exit)#按钮
b1 = Tkinter.Button(root1,text = '确定'.decode('utf-8'),command = get)
b2 = Tkinter.Button(root1,text = '全部'.decode('utf-8'),command = getall)
b4 = Tkinter.Button(root1,text = '保存图表'.decode('utf-8'),command = partial(save_graph, min_list))
b5 = Tkinter.Button(root1,text = '清空数据'.decode('utf-8'),command = clear_data)
b6 = Tkinter.Button(root1,text = '显示数据源码'.decode('utf-8'),command = partial(print_min_list, min_list))
area_list = Tkinter.Listbox(root1,listvariable = areas)#选项
l1.pack()
e1.pack()
b1.pack()
b2.pack()
b4.pack()
b6.pack()
b5.pack()
b3.pack()#包装
area_list.pack()
root1.title("中国哪个城市最冷?".decode('utf8'))
root1.resizable(width=False, height=False)
print('加载完成！')
if net_good == False:
    messagebox.showerror('网络问题', '网络出现问题，请检查!', icon='error')
    exit(1)
else:
    root1.mainloop()
sys.setdefaultencoding(default_encoding)#编码设定
