# -*- coding:utf-8 -*-
# import xlrd,xlsxwriter,xlwt
# # 创建工作簿
# workbook = xlsxwriter.Workbook('test.xlsx')
# # 创建表单
# sh = workbook.add_worksheet('test')
# fmt1 = workbook.add_format()
# fmt2 = workbook.add_format()
# # 字体加粗
# fmt1.set_bold(True)
# # 设置左对齐
# fmt2.set_align('left')
# # 数据
# data = [
#     ['', '姓名', '年龄'],
#     ['', '张三', 50],
#     ['', '李四', 30],
#     ['', '王五', 40],
#     ['', '赵六', 60],
#     ['平均年龄', '', ]
# ]
# sh.write_row('A1', data[0], fmt1)
# sh.write_row('A2', data[1], fmt2)
# sh.write_row('A3', data[2], fmt2)
# sh.write_row('A4', data[3], fmt2)
# sh.write_row('A5', data[4], fmt2)
# sh.write_row('A6', data[5], fmt1)

# chart = workbook.add_chart({'type': 'line'})
# workbook.close()

import xlwt
import json

# 创建工作簿
wb = xlwt.Workbook()
# 创建表单
sh = wb.add_sheet('图片')
# 创建字体对象
font = xlwt.Font()
# 字体加粗
font.bold = True
alm = xlwt.Alignment()
# 设置左对齐
alm.horz = 0x01
# 创建样式对象
style1 = xlwt.XFStyle()
style2 = xlwt.XFStyle()
style1.font = font
style2.alignment = alm
filename = 'url.json'
filename_name = 'name.json'
with open(filename) as f:
    film_url_list =json.load(f)
with open(filename_name) as f:
    filmname_list = json.load(f)
print(len(film_url_list))
# write 方法参数1：行，参数2：列，参数3：内容
row = 0
col = 0
for filmname,film_url in zip(filmname_list,film_url_list):
    sh.write(row,col,filmname,style1)
    sh.write(row,col+1,film_url,style2)
    row += 1
# 保存
wb.save('test.xls')


