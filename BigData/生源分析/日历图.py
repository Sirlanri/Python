import datetime
import random

from pyecharts import options as opts
from pyecharts.charts import Calendar

#日历图(需要使用visualMap组件)
def Calendar_base()->Calendar:
    begin=datetime.date(2018,1,1)
    end=datetime.date(2018,12,31)
    data=[
        [str(begin+datetime.timedelta(days=i)),random.randint(1000,25000)]
        for i in range((end-begin).day+1)
    ]
    c = (
        Calendar()
        .add('',data,calendar_opts=opts.CalendarOpts(range_="2018"))
        .set_global_opts(
            title_opts=opts.TitleOpts(title="2018模拟步数"),
            visualmap_opts=opts.VisualMapOpts(
                max=20000,
                min=500,
                orient="horizontal",
                is_piecewise=True,
                pos_top="230px",
                pos_left="100px",
            ),
        )
    )
    return c
Calendar_base()


#饼图基本
from pyecharts.charts import Page, Pie
def pie_base() ->Pie:
    c=(
        Pie()
        .add('',[list(z) for z in zip(Faker.choose(),Faker.values)])
        .set_global_opts(title_opts=opts.TitleOpts(title='饼图基本'))
        .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}:{c}"))
    )
    c.render()
pie_base()