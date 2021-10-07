# -*- encoding=utf-8 -*-
def html_begin():
    string = """<!DOCTYPE html>
<html lang="en">

"""
    return string


def html_end():
    string = """</html>"""
    return string


def head(html_type, title_string, fields):
    head_string = """<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{}{}</title>

  <link href="/static/bootstrap_3.3.0/css/bootstrap.min.css" rel="stylesheet" type="text/css" />
  <script src="/static/jquery/jquery-2.0.0-.min.js" type="text/javascript"></script>
  <script src="/static/jquery/jquery.cookie.js" type="text/javascript"></script>
  <script src="/static/bootstrap_3.3.0/js/bootstrap.min.js" type="text/javascript"></script>

  <link rel="stylesheet" href="https://cdn.staticfile.org/twitter-bootstrap/3.3.7/css/bootstrap.min.css">
  <script src="https://cdn.staticfile.org/jquery/2.1.1/jquery.min.js"></script>
  <script src="https://cdn.staticfile.org/twitter-bootstrap/3.3.7/js/bootstrap.min.js"></script>
</head>

""".format(html_type, title_string)
    style_string = style()
    head_string += style_string
    script_string = script(fields)
    head_string += script_string
    return head_string


def style():
    string = """<style>

</style>

"""
    return string


def get_necessary_field(fields):
    """获取必填项"""
    needful = []
    for field in fields:
        english_name = field[1]
        is_necessary = field[3]
        if is_necessary:
            needful.append(english_name)
    string = "', '".join(needful)
    if string:
        string = "'" + string + "'"
    return string


def script(fields):
    needful_string = get_necessary_field(fields)
    string = """<script>
  $(function () {{

    // 检查表单
    $.check_form = function () {{
      let can_submit = true
      let all_id = [{}]
      $.each(all_id, function (index, item) {{
        var data_value = $.trim($('#' + item).val())
        if (data_value == '') {{
          alert('请完善必填项')
          can_submit = false
          return can_submit
        }}
      }})
      return can_submit
    }}

  }})
</script>

""".format(needful_string)
    return string


def body_begin():
    string = """<body>

  <div class="container-fluid">
"""
    return string


def body_end():
    string = """  </div>

</body>

"""
    return string


def title(html_type, name):
    string = """
    <!-- 标题 -->
    <div class="row">
      <div class="col-md-12">
        <h3 class="text-center">{}{}</h3>
      </div>
    </div>
    <br>
""".format(html_type, name)
    return string


def button(html_type, select_url):
    string = """          <div class="form-group" style="margin-top: 39px;">
            <div class="col-md-6">
              <a class="btn btn-info btn-block" href="{}">返回</a>
            </div>
            <div class="col-md-6">
              <button type="submit" form="my_form" class="btn btn-success btn-block">{}</button>
            </div>
          </div>

""".format(select_url, html_type)
    return string


def form_begin(add_url):
    string = """
    <!--表单 -->
    <div class="row">

      <form id="my_form" onsubmit="return $.check_form()" action="{}" method="post">
""".format(add_url)
    return string


def form_end():
    string = """      </form>

    </div>

"""
    return string


BITIANXIANG = '<span style="color: red;">(必填项)</span>'


def text(chinese, english, bitian=False):
    if bitian:
        bitian_string = BITIANXIANG
    else:
        bitian_string = ''

    string = """          <div class="form-group">
            <label>{}{}</label>
            <input type="text" class="form-control" id="{}" name="{}" value="{{{{{}}}}}">
          </div>

""".format(chinese, bitian_string, english, english, english)
    return string


def riqi(chinese, english, bitian=False):
    if bitian:
        bitian_string = BITIANXIANG
    else:
        bitian_string = ''

    string = """          <div class="form-group">
            <label>{}{}</label>
            <input type="date" class="form-control" id="{}" name="{}" value="{{{{{}}}}}">
          </div>

""".format(chinese, bitian_string, english, english, english)
    return string


def xialakuang(chinese, english, bitian=False):
    if bitian:
        bitian_string = BITIANXIANG
    else:
        bitian_string = ''
    string = """          <div class="form-group">
            <label>{}{}</label>
            <select class="form-control" id="{}" name="{}">
              {{% if {} %}}
              <option>{{{{{}}}}}</option>
              {{% endif %}}
              <option></option>
              {{% for name in {}s %}}
              <option>{{{{name}}}}</option>
              {{% endfor %}}
            </select>
          </div>

""".format(chinese, bitian_string, english, english, english, english, english)
    return string


def generate(html_type, title_string, select_url, add_url, fields):
    html = ''
    html += html_begin()
    html += head(html_type, title_string, fields)
    html += body_begin()
    html += title(html_type, title_string)

    html += form_begin(add_url)
    html += add_label(html_type, select_url, fields)
    html += form_end()

    html += body_end()
    html += html_end()

    with open('add.html', 'w', encoding='utf-8') as f:
        f.write(html)
    return html


WENBEN = 'wenben'
XIALA = 'xiala'
RIQI = 'riqi'
CHOOSE = {WENBEN: text, XIALA: xialakuang, RIQI: riqi}


def add_label(html_type, select_url, fields):
    length = len(fields)
    if length % 2 == 0:
        half = length // 2
    else:
        half = length // 2 + 1
    string = ''
    for index in range(half):
        name = fields[index]
        chinese = name[0]
        english = name[1]
        leixing = name[2]
        bitian = name[3]
        string += CHOOSE[leixing.lower()](chinese, english, bitian)
    string_col = """        <div class="col-md-6 column">

"""
    string_end_div = '        </div>\n\n'
    string1 = string_col + string + string_end_div

    string2 = ''
    for index in range(half, length):
        name = fields[index]
        chinese = name[0]
        english = name[1]
        leixing = name[2]
        bitian = name[3]
        string2 += CHOOSE[leixing.lower()](chinese, english, bitian)
    button_string = button(html_type, select_url)
    string3 = string_col + string2 + button_string + string_end_div
    string4 = string1 + string3
    return string4


if __name__ == '__main__':
    names = [
        ('序号1', 'xuhao1', 'wenben', False),
        ('序号2', 'xuhao2', 'xiala', True),
        ('序号3', 'xuhao3', 'riqi', False),
        ('序号4', 'xuhao4', 'wenben', False),
        ('序号5', 'xuhao5', 'wenben', True),
        ('序号6', 'xuhao6', 'wenben', False),
        ('序号7', 'xuhao7', 'xiala', False),
        ('序号8', 'xuhao8', 'xiala', False),
        ('序号9', 'xuhao9', 'riqi', True),
        ('序号10', 'xuhao10', 'riqi', True),
        ('序号11', 'xuhao11', 'riqi', False),
        ('序号12', 'xuhao12', 'xiala', True),
        ('序号13', 'xuhao13', 'wenben', False),
        ('序号14', 'xuhao14', 'riqi', False),
        ('序号15', 'xuhao15', 'wenben', False),
        ('序号16', 'xuhao16', 'xiala', False),
        ('序号17', 'xuhao17', 'xiala', True),
        ]
    names1 = [
        ('线别','xianbie','xiala',True),
        ('车间','chejian','xiala',True),
        ('车站','chezhan','xiala',True),
        ('站内区间','zhanneiqujian','xiala',True),
        ('行别','hangbie','xiala',True),
        ('信号机位置名称','xinhaojimingcheng','wenben',False),
        ('信号机位置信号机里程','xinhaojilicheng','wenben',False),
        ('运营里程区段名称','yunyingquduan','wenben',False),
        ('设计区段名','shejiquduan','wenben',False),
        ('载频频率','zaipin','xiala',True),
        ('区段长度','quduanchangdu','wenben',False),
        ('段属','duanshu','wenben',False),
        ('备注1','beizhu1','wenben',False),
        ('电容规格','dianrongguige','wenben',False),

        ('电容数量','dianrongshuliang','wenben',False),
        ('功出电平理论等级','gongchulilundengji','wenben',False),
        ('功出电平理论封线','gongchulilunfengxian','wenben',False),
        ('功出电平变更等级','gongchubiangengdengji','wenben',False),
        ('功出电平变更封线','gongchubiangengfengxian','wenben',False),
        ('接收电平理论等级','jieshoulilundengji','wenben',False),
        ('接收电平理论封线','jieshoulilunfengxian','wenben',False),
        ('接收电平变更等级','jieshoubiangengdengji','wenben',False),
        ('接收电平变更封线','jieshoubiangengfengxian','wenben',False),
        ('轨道类型','guidaoleixing','xiala',True),
        ('电缆规定总长度','dianlangchangdu','wenben',False),
        ('发送模拟电缆环阻','fasonghuanzu','wenben',False),
        ('发送模拟电缆电缆长度','fasongchangdu','wenben',False),
        ('发送模拟电缆实际电缆长度档位','fasongdangwei','wenben',False),
        ('发送模拟电缆模拟长度','fasongmonichangdu','wenben',False),

        ('发送模拟电缆模拟固定长度','fasonggudingchangdu','wenben',False),
        ('发送模拟电缆补偿连接线','fasongbuchang','wenben',False),
        ('接收模拟电缆环阻','jieshouhuanzu','wenben',False),
        ('接收模拟电缆电缆长度','jieshouchangdu','wenben',False),
        ('接收模拟电缆实际电缆长度档位','jieshoudangwei','wenben',False),
        ('接收模拟电缆模拟长度','jieshoumonichangdu','wenben',False),
        ('接收模拟电缆模拟固定长度','jieshougudingchangdu','wenben',False),
        ('接收模拟电缆补偿连接线','jieshoubuchang','wenben',False),
        ('调整表固定区段','tiaozhengguding','wenben',False),
        ('有无小轨','youwuxiaogui','wenben',False),
        ('小轨调整正向等级','xiaoguizhengxiangdengji','wenben',False),
        ('小轨调整正向封线','xiaoguizhengxiangfengxian','wenben',False),
        ('小轨调整反向等级','xiaoguifanxiangdengji','wenben',False),
        ('小轨调整反向封线','xiaoguifanxiangfengxian','wenben',False),
        ('备注2','beizhu2','wenben',False),
        ]
    ret = generate('新增', 'ZPW-2000无绝缘轨道移频自动闭塞技术参数表', '/Model3/select.html/', '/Model3/add/', names)
    print(ret)
