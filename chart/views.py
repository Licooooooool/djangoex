from __future__ import unicode_literals

from django.shortcuts import render
import math

from django.http import HttpResponse
from django.template import loader
from pyecharts import Line3D
from pyecharts import Bar,Pie,Polar
import random


REMOTE_HOST = "https://pyecharts.github.io/assets/js"


def index(request):
    return render(request,'chart/chartinfo.html')


def line3d(request):
    _data = []
    template = loader.get_template('chart/chart.html')
    for t in range(0, 25000):
        _t = t / 1000
        x = (1 + 0.25 * math.cos(75 * _t)) * math.cos(_t)
        y = (1 + 0.25 * math.cos(75 * _t)) * math.sin(_t)
        z = _t + 2.0 * math.sin(75 * _t)
        _data.append([x, y, z])
    range_color = [
        '#313695', '#4575b4', '#74add1', '#abd9e9', '#e0f3f8', '#ffffbf',
        '#fee090', '#fdae61', '#f46d43', '#d73027', '#a50026']
    line3d = Line3D("3D line plot demo", width=1200, height=600)
    line3d.add("", _data, is_visualmap=True,
               visual_range_color=range_color, visual_range=[0, 30],
               is_grid3D_rotate=True, grid3D_rotate_speed=180)
    context = dict(
        myechart=line3d.render_embed(),
        host=REMOTE_HOST,
        script_list=line3d.get_js_dependencies()
    )
    return HttpResponse(template.render(context, request))


def bar_zome(request):
    template = loader.get_template('chart/chart.html')
    attr = ["{}天".format(i) for i in range(30)]
    v1 = [random.randint(200, 1000) for _ in range(30)]
    bar = Bar("本月销售情况", width=1200, height=600)
    bar.add("", attr, v1, is_label_show=True, is_datazoom_show=True)
    context = dict(
        myechart=bar.render_embed(),
        host=REMOTE_HOST,
        script_list=bar.get_js_dependencies()
    )
    return HttpResponse(template.render(context, request))

def pie(request):
    template = loader.get_template('chart/chart.html')
    attr = ['菜品A', '菜品B', '菜品C', '菜品D', '菜品E', '菜品F']
    pie = Pie("菜品销售占比", width=1400, height=700)
    pie.add("", attr, [random.randint(0, 100) for _ in range(6)],
            radius=[50, 55], center=[25, 50], is_random=True)
    pie.add("", attr, [random.randint(20, 100) for _ in range(6)],
            radius=[0, 45], center=[25, 50], rosetype='area')
    pie.add("", attr, [random.randint(0, 100) for _ in range(6)],
            radius=[50, 55], center=[65, 50], is_random=True)
    pie.add("", attr, [random.randint(20, 100) for _ in range(6)],
            radius=[0, 45], center=[65, 50], rosetype='radius')
    context = dict(
        myechart=pie.render_embed(),
        host=REMOTE_HOST,
        script_list=pie.get_js_dependencies()
    )
    return HttpResponse(template.render(context, request))

def polar(request):
    template = loader.get_template('chart/chart.html')
    radius = ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
    polar = Polar("一周各天销售情况", width=1200, height=600)
    polar.add("菜品A", [random.randint(0, 100) for _ in range(7)], radius_data=radius,
              type='barAngle', is_stack=True)
    polar.add("菜品B", [random.randint(0, 100) for _ in range(7)], radius_data=radius,
              type='barAngle', is_stack=True)
    polar.add("菜品C", [random.randint(0, 100) for _ in range(7)], radius_data=radius,
              type='barAngle', is_stack=True)
    polar.add("菜品D", [random.randint(0, 100) for _ in range(7)], radius_data=radius,
              type='barAngle', is_stack=True)
    polar.add("菜品E", [random.randint(0, 100) for _ in range(7)], radius_data=radius,
              type='barAngle', is_stack=True)
    context = dict(
        myechart=polar.render_embed(),
        host=REMOTE_HOST,
        script_list=polar.get_js_dependencies()
    )
    return HttpResponse(template.render(context, request))
