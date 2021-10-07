# -*- encoding=utf-8 -*-

CHAXUN = 'chaxun'
WENBEN = 'wenben'
XIALA = 'xiala'
RIQI = 'riqi'


def html_begin():
    string = """<!DOCTYPE html>
<html>

"""
    return string


def html_end():
    string = """</html>"""
    return string


def head(title):
    string = """<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{}阅览</title>

    <link href="/static/bootstrap_3.3.0/css/bootstrap.min.css" rel="stylesheet" type="text/css" />
    <script src="/static/jquery/jquery-1.11.1-min.js" type="text/javascript"></script>
    <script src="/static/jquery/jquery.cookie.js" type="text/javascript"></script>
    <script src="/static/bootstrap_3.3.0/js/bootstrap.min.js" type="text/javascript"></script>

    <link rel="stylesheet" href="https://cdn.staticfile.org/twitter-bootstrap/3.3.7/css/bootstrap.min.css">
    <script src="https://cdn.staticfile.org/jquery/2.1.1/jquery.min.js"></script>
    <script src="https://cdn.staticfile.org/jquery-cookie/1.4.1/jquery.cookie.min.js"></script>
    <script src="https://cdn.staticfile.org/twitter-bootstrap/3.3.7/js/bootstrap.min.js"></script>
</head>

""".format(title)
    return string


def get_english_names(data):
    needful = []
    for one_data in data:
        needful.append(one_data[1])
    return needful


def get_need_select_fields(fields):
    needful = []
    for data in fields:
        value = data[4]
        if value.lower() == CHAXUN.lower():
            needful.append(data)
    return needful


def get_chinese_names(fields):
    needful = []
    for data in fields:
        value = data[0]
        needful.append(value)
    return needful


def set_select(fields):
    need = get_need_select_fields(fields)
    string = ''
    for data in need:
        ret = CHOOSE[data[2].lower()](data[0], data[1])
        string += ret
    return string


def list_to_string(data):
    string = "', '".join(data)
    if string:
        string = "'" + string + "'"
    return string


def data_to_string(data):
    string = "</td>\n                                <td>".join(data)
    if string:
        string = "<td>" + string + "</td>"
    return string


def script(delete_url, select_url, update_url, fields):
    need = get_need_select_fields(fields)
    data = get_english_names(need)
    list_string = list_to_string(data)
    string = """<script>
    $(function () {{

        // 设置滚动条
        $.set_scroll = function () {{
            $("#tbody_div").scrollTop(10); //  控制滚动条下移10px
            if ($("#tbody_div").scrollTop() > 0) {{
                $("#thead_div").css("overflow-y", "scroll");// alert('有滚动条')
            }} else {{
                $("#thead_div").css("overflow-y", "hidden");// alert('无滚动条')
            }}
            $("#tbody_div").scrollTop(0); //滚动条返回顶部
        }};
        $.set_scroll()

        //设置权限
        $.set_authority = function () {{
            if ($.cookie("can_delete") === "True") {{
                $("#delete").attr("disabled", false);
            }}
        }};
        $.set_authority()

        //全选全不选
        $("#checkboxs").click(function () {{
            if (this.checked === true) {{
                $("#tbody :checkbox").prop("checked", true);
            }} else {{
                $("#tbody :checkbox").prop("checked", false);
            }}
        }});

        //清空查询选择
        $("#clear_select").click(function () {{
            $("select").val("");
            $("input").val("");
        }});

        //删除
        $('#delete').click(function () {{
            var checked_boxs = $("#tbody :checked");
            var delete_ids = "";
            if (checked_boxs.length < 1) {{
                alert("至少选择一条数据");
            }} else {{
                checked_boxs.each(function () {{
                    delete_ids += $(this).val() + "_";
                }});
                var real_do = confirm("确认删除");
                if (real_do == true) {{
                    window.location.href = "{}?delete_ids=" + delete_ids
                }}
            }}
        }})

        //第几页url
        var id_names = [{}]
        $.currentpage = function (current_page) {{
            let herf_head = "{}?current_page=" + current_page + "&pagesize=" + $.trim(
                $("#pagesize").text())
            let herf_body = "";
            $.each(id_names, function (index, item) {{
                let parameter = "&" + item + "=" + $.trim($("#" + item).val());
                herf_body += parameter;
            }})
            let href = herf_head + herf_body;
            $(window).attr("location", href);
        }}

        // 每页显示多少条记录
        $.pagesize = function (page_size) {{
            let herf_head = "{}?current_page=1" + "&pagesize=" + page_size
            let herf_body = "";
            $.each(id_names, function (index, item) {{
                let parameter = "&" + item + "=" + $.trim($("#" + item).val());
                herf_body += parameter;
            }})
            let href = herf_head + herf_body;
            $(window).attr("location", href);
        }}

        //修改按钮
        $('#updateModalBtn').click(function () {{
            var checked_boxs = $("#tbody :checked")
            var update_id = ''
            if (checked_boxs.length != 1) {{
                alert('请选择一条数据')
            }} else {{
                checked_boxs.each(function () {{
                    update_id += $(this).val()
                }})
                window.location.href = '{}?update_id=' + update_id
            }}
        }})

    }});
</script>

""".format(delete_url, list_string, select_url, select_url, update_url)
    return string


def style():
    string = """<style>
    /* 表格字体且换行 */
    table {
        font-size: 8px;
        word-break: break-all;
    }

    /* 固定表格布局，取消外边距 */
    .table {
        margin-bottom: -1px;
        table-layout: fixed;
    }

    /* 水平垂直居中 */
    td,
    td {
        text-align: center;
        vertical-align: middle !important;
    }

    /* body_div下边框 */
    .tbody_div {
        height: 900px;
        overflow-y: auto;
        border-bottom-style: groove;
    }

    /* 固定某行的宽度 */
    table tr td:nth-child(1) {
        width: 30px;
    }
</style>

"""
    return string


def body_begin():
    string = """<body>

    <div class="container-fluid">

"""
    return string


def body_end():
    string = """    </div>

</body>

"""
    return string


def h3(title):
    string = """        <!-- 标题 -->
        <div class="row">
            <div class="col-md-12">
                <h3 class="text-center">{}阅览</h3>
            </div>
        </div>

        <br>

""".format(title)
    return string


def button(add_url, select_url, import_url, index):
    string = """        <!-- 增删改查按钮组 -->
        <div class="row">
            <div class="col-md-12">

                <div class="btn-group">
                    <a href="{}" class="btn btn-primary">
                        <span class="glyphicon glyphicon-plus">添加</span>
                    </a>
                    <button class="btn btn-warning" id="updateModalBtn" type="button">
                        <span class="glyphicon glyphicon-pencil"> 修改</span>
                    </button>
                    <button class="btn btn-danger" disabled="disabled" id="delete" type="button">
                        <span class="glyphicon glyphicon-minus"> 删除</span>
                    </button>
                </div>

                <div class="btn-group">
                    <a href="{}" class="btn btn-default">
                        <span class="glyphicon glyphicon-import"> 导入</span>
                    </a>
                    <button class="btn btn-default" onclick="window.open('{{file}}')" type="button">
                        <span class="glyphicon glyphicon-export"> 导出</span>
                    </button>
                </div>

                <div class="btn-group">
                    <a href="{}" class="btn btn-info" target="_blank">
                        <span class="glyphicon glyphicon-gift"> 详情</span>
                    </a>
                    <a href="/index.html/?index={}" class="btn btn-primary">
                        <span class="glyphicon glyphicon-home"> 首页</span>
                    </a>
                </div>

            </div>

        </div>

""".format(add_url, import_url, select_url, index)
    return string


def text(chinexe_name, english_name):
    string = """                    <div class="form-group">
                        <div class="input-group">
                            <div class="input-group-addon">{}</div>
                            <input class="form-control" id="{}" name="{}" type="text" value="{{{{{}}}}}">
                        </div>
                    </div>

""".format(chinexe_name, english_name, english_name, english_name)
    return string


def xialakuang(chinexe_name, english_name):
    string = """                    <div class="form-group">
                        <div class="input-group">
                            <div class="input-group-addon">{}</div>
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
                    </div>

""".format(chinexe_name, english_name, english_name, english_name, english_name, english_name)
    return string


def riqi(chinexe_name, english_name):
    string = """                    <div class="form-group">
                        <div class="input-group">
                            <div class="input-group-addon">{}</div>
                            <input class="form-control" id="{}" name="{}" type="date" value="{{{{{}}}}}">
                        </div>
                    </div>

""".format(chinexe_name, english_name, english_name, english_name)
    return string


CHOOSE = {WENBEN: text, XIALA: xialakuang, RIQI: riqi}


def select_begin():
    string = """        <!-- 查询 -->
        <div class="row">
            <div class="col-md-12">
                <form class="form-inline" role="form">

"""
    return string


def select_end():
    string = """                    <div class="form-group">
                        <div class="btn-group">
                            <button class="btn btn-info" id="clear_select" type="button">清空</button>
                            <button class="btn btn-primary" type="submit">查询</button>
                        </div>
                    </div>

                </form>
            </div>
        </div>

        <br>

"""
    return string


def table(fields):
    chinese_names = get_chinese_names(fields)
    string1 = data_to_string(chinese_names)
    string = """        <!-- 表格 -->
        <div class="row">
            <div class="col-md-12">
                <div id="thead_div">
                    <table class="table table-bordered  table-hover table-condensed">
                        <thead>
                            <tr>
                                <td><input id="checkboxs" type="checkbox" value="all"></td>
                                {}
                            </tr>
                        </thead>
                    </table>
                </div>
                <div id="tbody_div" class="tbody_div">
                    <table class="table table-bordered  table-hover table-condensed">
                        <tbody id="tbody">
                            {{% for one_data in data %}}
                            <tr>
                                <td><input type="checkbox" value="{{{{i.0}}}}"></td>
                                <td>{{{{forloop.counter}}}}</td>
                                {{% for value in one_data %}}
                                {{% if forloop.first %}}
                                {{% else %}}
                                <td>{{{{value}}}}</td>
                                {{% endif %}}
                                {{% endfor %}}
                            </tr>
                            {{% endfor %}}
                        </tbody>
                    </table>
                </div>
            </div>
        </div>

""".format(string1)
    return string


def page():
    string = """        <!-- 分页 -->
        <div class="row">
            <div class="col-md-12 form-group text-center form-group">

                <div class="btn-group">
                    <button class="btn btn-default" type="button">共</button>
                    <button class="btn btn-default" type="button">{{count}}</button>
                    <button class="btn btn-default" type="button">条记录</button>
                </div>

                <div class="btn-group">
                    <button class="btn btn-default" type="button">显示</button>
                    <div class="btn-group dropup">
                        <button class="btn btn-default dropdown-toggle" data-toggle="dropdown" id="pagesize"
                            value="{{pagesize}}" type="button">
                            {{pagesize}}
                        </button>
                        <ul class="dropdown-menu" id="pagesizechoose" role="menu">
                            <li><a href="javascript: $.pagesize(100)">100</a></li>
                            <li><a href="javascript: $.pagesize(50)">50</a></li>
                            <li><a href="javascript: $.pagesize(20)">20</a></li>
                        </ul>
                    </div>
                    <button class="btn btn-default" type="button">条/页</button>
                </div>

                <div class="btn-group">
                    <a class="btn btn-primary" href="javascript:$.currentpage(1)">首页</a>
                    <a class="btn btn-success" href="javascript:$.currentpage({{previous_page}})">上一页</a>
                    <a class="btn btn-success" href="javascript:$.currentpage({{next_page}})">下一页</a>
                    <a class="btn btn-primary" href="javascript:$.currentpage({{last_page}})">末页</a>
                </div>

                <div class="btn-group">
                    <button class="btn btn-default" type="button">当前</button>
                    <button class="btn btn-default" type="button">{{current_page}}</button>
                    <button class="btn btn-default" type="button">页</button>
                </div>

                <div class="btn-group">
                    <button class="btn btn-default" type="button">共</button>
                    <button class="btn btn-default" type="button">{{last_page}}</button>
                    <button class="btn btn-default" type="button">页</button>
                </div>

            </div>
        </div>

"""
    return string


def auto_select_html():
    title = '某某信息'
    add_url = '/Model3/add.html/'
    select_url = '/Model3/select.html/'
    update_url = '/Model3/update.html/'
    delete_url = '/Model3/delete/'
    import_url = '/Model3/import.html/'
    index = '3'
    fields = [
        ('序号1', 'xuhao1', 'wenben', False, 'chaxun'),
        ('序号2', 'xuhao2', 'xiala', True, 'chaxun'),
        ('序号3', 'xuhao3', 'riqi', False, 'chaxun'),
        ('序号4', 'xuhao4', 'wenben', False, 'chaxun'),
        ('序号5', 'xuhao5', 'wenben', True, 'chaxun'),
        ('序号6', 'xuhao6', 'wenben', False, 'chaxun'),
        ('序号7', 'xuhao7', 'xiala', False, 'chaxun'),
        ('序号8', 'xuhao8', 'xiala', False, 'chaxun'),
        ('序号9', 'xuhao9', 'riqi', True, 'chaxun'),
        ('序号10', 'xuhao10', 'riqi', True, ''),
        ('序号11', 'xuhao11', 'riqi', False, ''),
        ('序号12', 'xuhao12', 'xiala', True, ''),
        ('序号13', 'xuhao13', 'wenben', False, ''),
        ('序号14', 'xuhao14', 'riqi', False, ''),
        ('序号15', 'xuhao15', 'wenben', False, ''),
        ('序号16', 'xuhao16', 'xiala', False, ''),
        ('序号17', 'xuhao17', 'xiala', True, ''),
        ]
    names1 = [
        ('线别','xianbie','xiala',True,'chaxun'),
        ('车间','chejian','xiala',True,'chaxun'),
        ('车站','chezhan','xiala',True,'chaxun'),
        ('站内区间','zhanneiqujian','xiala',True,'chaxun'),
        ('行别','hangbie','xiala',True,'chaxun'),
        ('信号机位置名称','xinhaojimingcheng','wenben',False, ''),
        ('信号机位置信号机里程','xinhaojilicheng','wenben',False, ''),
        ('运营里程区段名称','yunyingquduan','wenben',False, ''),
        ('设计区段名','shejiquduan','wenben',False, ''),
        ('载频频率','zaipin','xiala',True,'chaxun'),
        ('区段长度','quduanchangdu','wenben',False, ''),
        ('段属','duanshu','wenben',False, ''),
        ('备注1','beizhu1','wenben',False, ''),
        ('电容规格','dianrongguige','wenben',False, ''),

        ('电容数量','dianrongshuliang','wenben',False, ''),
        ('功出电平理论等级','gongchulilundengji','wenben',False, ''),
        ('功出电平理论封线','gongchulilunfengxian','wenben',False, ''),
        ('功出电平变更等级','gongchubiangengdengji','wenben',False, ''),
        ('功出电平变更封线','gongchubiangengfengxian','wenben',False, ''),
        ('接收电平理论等级','jieshoulilundengji','wenben',False, ''),
        ('接收电平理论封线','jieshoulilunfengxian','wenben',False, ''),
        ('接收电平变更等级','jieshoubiangengdengji','wenben',False, ''),
        ('接收电平变更封线','jieshoubiangengfengxian','wenben',False, ''),
        ('轨道类型','guidaoleixing','xiala',True, ''),
        ('电缆规定总长度','dianlangchangdu','wenben',False, ''),
        ('发送模拟电缆环阻','fasonghuanzu','wenben',False, ''),
        ('发送模拟电缆电缆长度','fasongchangdu','wenben',False, ''),
        ('发送模拟电缆实际电缆长度档位','fasongdangwei','wenben',False, ''),
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
    html = ''
    html += html_begin()
    html += head(title)
    html += script(delete_url,
                   select_url,
                   update_url,
                   names1)
    html += style()
    html += body_begin()
    html += h3(title)
    html += select_begin()
    html += set_select(fields)
    html += select_end()
    html += button(add_url, select_url, import_url, index)
    html += table(fields)
    html += page()
    html += body_end()
    html += html_end()

    with open('select.html', 'w', encoding='utf-8') as f:
        f.write(html)
    return html


if __name__ == '__main__':
    print(auto_select_html())
