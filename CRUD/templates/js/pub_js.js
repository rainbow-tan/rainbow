$(function () {
  // 查看文件
  $("#seeFileBtn").click(function () {
    $("#file_for_see").click();
    $("#file_for_see").change(function () {
      $("#see_file_form").submit();
    });
  });

  // 导入文件
  $("#importBtn").click(function () {
    $("#file_for_import").click();
    $("#file_for_import").change(function () {
      $("#importBtn").prop('disabled','disabled')
      $("#import_file_form").submit();
    });
  });

  // 设置滚动条
  $.set_scroll = function () {
    $("#tbody_div").scrollTop(10); //控制滚动条下移10px
    if ($("#tbody_div").scrollTop() > 0) {
      // alert('有滚动条')
      $("#thead_div").css("overflow-y", "scroll");
    } else {
      // alert('无滚动条')
      $("#thead_div").css("overflow-y", "hidden");
    }
    $("#tbody_div").scrollTop(0); //滚动条返回顶部
  };

  //设置权限
  $.set_authority = function () {
    if ($.cookie("is_admin") === "True") {
      $("#delete").attr("disabled", false);
    }
  };

  //全选全不选
  $("#checkboxs").click(function () {
    if (this.checked === true) {
      $("#tbody :checkbox").prop("checked", true);
    } else {
      $("#tbody :checkbox").prop("checked", false);
    }
  });

  //清空查询选择
  $("#clear_select").click(function () {
    $("select").val("");
    $("input").val("");
  });

  //删除
  $.delete = function (index) {
    var checked_boxs = $("#tbody :checked");
    var delete_ids = "";
    if (checked_boxs.length < 1) {
      alert("至少选择一条数据");
    } else {
      checked_boxs.each(function () {
        delete_ids += $(this).val() + "_";
      });
      var real_do = confirm("确认删除");
      if (real_do == true) {
        $.get(
          "/" + index + "/delete/",
          {
            delete_ids: delete_ids,
          },
          function (data, status) {
            $(window).attr("location", "/" + index + "/select.html/");
          }
        );
      } else {
      }
    }
  };
});
