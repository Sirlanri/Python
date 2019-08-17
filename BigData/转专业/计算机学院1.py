from openpyxl import load_workbook
from pyecharts.charts import Pie
from pyecharts import options as opts  # 我去！这行代码搞了半天

majors_com = {'数据科学与大数据技术': 0, '计算机科学与技术': 0,
              '软件工程': 0, '网络空间安全': 0, '物联网工程': 0}


def getnum():
    wb = load_workbook(r'E:\代码\云端同步\保护\计算机.xlsx', read_only=True)
    sheet = wb['Sheet1']

    # 用切片获取全部格子
    all_cells = sheet['H2':'J168']
    for row in all_cells:
        for cell in row:
            if cell.value in majors_com.keys():
                majors_com[cell.value] += 1


def picture() -> Pie:
    c = (
        Pie()
        .add(

            '',
            [list(z) for z in zip(majors_com.keys(), majors_com.values())],
            radius=['40%', '75%'],
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(title='计算机类各专业报名情况'),
            legend_opts=opts.LegendOpts(
                orient="vertical", pos_top="15%", pos_left="2%"
            ),
        )
        .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    )

    c.render('转专业.html')

# 可视化例子


def pie_radius() -> Pie:

    c = (
        Pie()
        .add(
            "",
            [list(z) for z in zip(Faker.choose(), Faker.values())],
            radius=["40%", "75%"],
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(title="Pie-Radius"),
            legend_opts=opts.LegendOpts(
                orient="vertical", pos_top="15%", pos_left="2%"
            ),
        )
        .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    )


    # c.render()
getnum()
picture()
