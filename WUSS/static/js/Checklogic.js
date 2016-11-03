/**
 * Created by Arnold on 2016/10/30.
 */

// {#    根据<input>的id获取设定输入框焦点离开时的操作#}
    $('#username').blur(function(){
// {#       获取用户输入的用户名 #}
        var input_sex=$('#sex').val();
        var input_interests=$('#interests').val();
        var input_name=$(this).val();
// {#        创建一个数组将要提交的数据都放在数组里#}
        var submit_data=[
            {sex:input_sex},
            {interests:input_interests},
            {username:input_name}
        ];
// {#       调用ajax提交数据 #}
        $.ajax({
// {#                指定提交的url#}
                url:"/checkuser/",
// {#                这里提交的方式还是字典方式，不过key就是data本身 value的值就是上面定义的数组#}
                data:{data:submit_data},
// {#                指定提交的数据的格式#}
                type:'POST',
// {#                success用来接收login()函数执行之后的return HttpResponse返回值#}
                success:function(arg){
// {#                    用arg接收到返回值后通过alert将返回的内容输出到页面上#}
                    alert(arg)
                }
            });
    });
