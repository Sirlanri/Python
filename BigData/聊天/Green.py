import datetime
import re
from collections import Counter
from pyecharts import options as opts
from pyecharts.charts import Bar, Calendar, Pie

#聊天记录的路径
recordpath = r'E:\代码\云端同步\保护\record1.txt'
messages = []
myname = ''
hername = ''


def openfile(path):  # 读取文件,为数据分析初始化
    global messages, myname, hername
    with open(recordpath, 'r', encoding='utf-8') as f:
        temps = f.readlines()
        while '\n' in temps:
            temps.remove('\n')  # 删除空格，剩余的元素就是时间/聊天记录
        messages = temps

    # 寻找对方的ID
    for message in messages:
        if re.search(r'消息对象:(\S+)\n', message):
            hername = re.search(r'消息对象:(\S+)\n', message).group(1)

            print(hername)
            break

    # 寻找自己的ID
    for i in range(20, 60):
        if messages[i]:
            message = messages[i]
            result1 = re.search(r'20\d{2}\-\d{2}\-\d{2}\s', message)
            if result1 and hername in result1.string:
                continue
            else:
                if result1 and re.search(r'\d{1,2}\:\d{2}\:\d{2}\s(\S)', result1.string):
                    myname = re.search(
                        r'\d{1,2}\:\d{2}\:\d{2}\s(\S+)', result1.string).group(1)
                    print(myname)
                    break
                else:
                    continue
        else:
            break


def whoSpeak():  # 两人各自的发言数量
    global myname, hername
    me = her = 0
    data = {}
    for message in messages:
        if myname in message:  # 自己名字
            me += 1
        if hername in message:  # 对方的名字
            her += 1
    print('me{0},her{1}'.format(me, her))
    z = [{"我发送的": me}, {"她发送的": her}]

    # 可视化
    c = (
        Pie()
        .add('', [('我', me), ('她', her)])
        .set_global_opts(title_opts=opts.TitleOpts(title='发送消息数量', subtitle='那些年我们追过的女孩'))

    )
    c.render(path='发言数量.html')


def time():  # 发言时间(几点),返回一个字典
    times = []
    all = {}
    for message in messages:
        if '2019-' in message or '2018-' in message:
            first = re.search(r'(\d{1,2})\:', message).group()
            after = re.sub(':', '', first)
            times.append(after)
    result = dict(Counter(times))
    
    return result


def start():  # 聊天发起次数
    global myname, hername
    me = her = 0
    last = '05:33:45'

    def period(time):  # flase是同一段对话，true是另一端对话开始
        nonlocal last

        # 换一种方式，尽量不用正则表达式，用切片提高速度
        if time[1] == ':':
            time = '0'+time
        hour1 = int(last[0:2])
        minute1 = int(last[3:5])
        hour2 = int(time[0:2])
        minute2 = int(time[3:5])

        if hour1 == hour2:
            long = minute2-minute1
        elif hour1+1 == hour2:
            long = 60+(60-minute1)+minute2
            if long >= 30:
                last = time
                return True
            else:
                last = time
                return False
        else:
            last = time
            return True

    for message in messages:
        look1 = re.search(r'\d{1,2}\:\d{2}\:\d{2}', message)

        if look1 != None:
            lookfor = look1.group()
            if period(lookfor):  # 发起了新对话
                if myname in message:
                    me += 1
                elif hername in message:
                    her += 1
            else:  # 仍然是当前对话
                continue

    print('我{} 她{}'.format(me, her))


def calender():  # 日历图
    # https://pyecharts.org/#/zh-cn/basic_charts?id=calendar%ef%bc%9a%e6%97%a5%e5%8e%86%e5%9b%be
    alldata = []  # 里面是元组类型的数据
    alldata2 = {}
    temp1 = ''
    count = 0
    flag = False
    
    def getdays(ndate):
        year = ndate[0:4]
        month = ndate[4:6]
        day = ndate[6:8]

        begin = datetime.date(2019, 1, 1)
        end = datetime.date(2019, 11, 1)

    # 获得日期,尼玛这算法还是有问题，最后一天无法统计
    for message in messages:
        date1 = re.search(r'(201\d\-\d{2}\-\d{2})', message)
        if date1:
            if temp1 == date1.group(1):
                count += 1
                flag = True
            else:
                if flag:

                    alldata.append([before, count])
                count = 0
            temp1 = date1.group(1)
            before = temp1
    print(alldata)

    # 渲染html
    c = (
        Calendar()
        .add('', alldata, calendar_opts=opts.CalendarOpts(range_=['2019-2', '2019-11']))
        .set_global_opts(
            title_opts=opts.TitleOpts(title="2019聊天频率"),
            visualmap_opts=opts.VisualMapOpts(
                max_=800,
                min_=0,
                orient="horizontal",
                is_piecewise=True,
                pos_top="230px",
                pos_left="100px",
            ),
        )
    )
    c.render('聊天分析3.html')


def test():
    openfile(recordpath)
    


test()
