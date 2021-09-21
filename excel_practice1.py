#coding=utf-8

def get_excel():
  """
  生成excel
  :return: 
  """
  import xlsxwriter
  workbook = xlsxwriter.Workbook("test1.xlsx")
  worksheet = workbook.add_worksheet()
  # 样式
  formats = Struct() # 字典转化为点语法
  formats.base = {"font_name": u"宋体", "font_size": 11, "align": "center", "valign": "vcenter", "text_wrap": True}
  # formats.condition = dict_merge(formats.base, {"align": "left"})
  formats.bold = {"bold": True} # 加粗
  formats.row = dict_merge(formats.base, {"border": 1})
  formats.first_row = dict_merge(formats.row, {"bold": True}) # 首行
  formats.more_row = dict_merge(formats.row, {}) # 普通行
  formats.more_row_even = dict_merge(formats.row, {"bg_color": "#dddddd"}) # 普通行-奇数
  # 筛选条件行
  worksheet.merge_range('A1:F1', "") # 合并单元格
  conditions_list = [] # 条件
  province = '省'
  city = '市'
  county = '地区'
  name = '姓名'
  phone = '电话'
  date = '2018-6'
  if province or city or county:
    area_name = province + city + county
    conditions_list.append(workbook.add_format(formats.bold))
    conditions_list.append(u'地区：')
    conditions_list.append(u'%s ' % area_name)
  if name:
    conditions_list.append(workbook.add_format(formats.bold))
    conditions_list.append(u'姓名：')
    conditions_list.append(u'%s ' % name)
  if phone:
    conditions_list.append(workbook.add_format(formats.bold))
    conditions_list.append(u'手机：')
    conditions_list.append(u'%s ' % phone)
  if date:
    year, month = date[0:4], date[5:7]
    conditions_list.append(workbook.add_format(formats.bold))
    conditions_list.append(u'创建时间：')
    conditions_list.append(u'%s/%s ' % (year, month))
  if conditions_list: # 如果有条件
    worksheet.write_rich_string('A1', *conditions_list) # 首行

  # 表格首行
  cols = ["姓名", "电话", "地区"]
  for col_index, col in enumerate(cols):
    worksheet.write(1, col_index, col, workbook.add_format(formats.first_row)) # 第二行，col_index列, col_index从0开始,也就是第一列开始

  data_list = [{"name": "Spencer", "tel": "13888888888", "reg": "中国"},{"name": "Jeff", "tel": "139999999999", "reg": "台湾省"}]
  # 表格其余行
  for row_index, u in enumerate(data_list, start=2): # 因为前两行都被占用了，所以从第三行第一列开始
    # 斑马条
    if row_index % 2 != 0:
      row_format = formats.more_row # excel格式普通行
    else:
      row_format = dict_merge(formats.more_row_even) # excel格式奇数行
    
    # 日期格式
    date_format = dict_merge(row_format, {"num_format": "yyyy/mm/dd hh:mm"})
    # 靠左
    left_format = dict_merge(row_format, {"align": "left"}) 

    # 第一个参数：行，第二个参数：列，第三个参数：数据，第四个参数：属性
    worksheet.write(row_index, 0, u['name'], workbook.add_format(row_format))
    worksheet.write(row_index, 1, u['tel'], workbook.add_format(row_format))
    worksheet.write(row_index, 2, u['reg'], workbook.add_format(row_format))

    # 列宽 
    # 第一个参数是第几列开始，第二个人参数是从第几列结束
    # 比如下方第一个就是设置第一列为20，第二个就是设置第二列为10，第三个就是设置3到6列为20
  worksheet.set_column(0, 0, 20)
  worksheet.set_column(1, 1, 10)
  worksheet.set_column(2, 5, 20)
  workbook.close()

def dict_merge(*args):
  """
  功能说明：合并字典
  """
  all = {}
  for arg in args:
    if not isinstance(arg, dict):
      continue
    all.update(arg)
  return all

class Struct(dict):
  """
  - 为字典加上点语法. 例如:
  >>> o = Struct({'a':1})
  >>> o.a
  >>> 1
  >>> o.b
  >>> None
  """

  def __init__(self, dictobj={}):
    self.update(dictobj)

  def __getattr__(self, name):
    # 如果有则返回值，没有则返回None
    if name.startswith('__'):
      raise AttributeError
    return self.get(name)

  def __setattr__(self, name, val):
    self[name] = val

  def __hash__(self):
    return id(self)

if __name__ == '__main__':
  get_excel()