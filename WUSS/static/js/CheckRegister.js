/**
 * Created by Arnold on 2016/10/14.
 */
function gspan(cobj){       //获取表单后的span 标签 显示提示信息

    if (cobj.nextSibling.nodeName != 'SPAN'){

        gspan(cobj.nextSibling);

    } else {

        return cobj.nextSibling;
    }
}
//检查表单 obj【表单对象】， info【提示信息】 fun【处理函数】  click 【是否需要单击， 提交时候需要触发】
function check(obj, info, fun, click){
	console.log(obj);
    var sp = gspan(obj);

    obj.onfocus = function(){

        sp.innerHTML = info;

        sp.style.color = "black";

    }
    obj.onblur = function(){

        if (fun(this.value)){

            sp.innerHTML = "输入正确！";

            sp.style.color = "green";

        } else {

            sp.innerHTML = info;
            sp.style.color = "#05ffe3";
        }
    }

    if (click == 'click'){

        obj.onblur();

    }

}



onload = regs;//页面载入完执行

function regs(click){

    var stat = true;        //返回状态， 提交数据时用到
    inputEmail = document.getElementById('inputEmail');
    inputPassword = document.getElementById('inputPassword');
    inputPasswordAgain = document.getElementById('inputPasswordAgain');


    check(inputEmail, "用户名由邮箱组成，例如user@host.domainnames", function(val){
        var re = /^([a-z]|[A-Z]|[0-9]){1,20}@([a-z]|[A-Z]|[0-9]|.){1,10}$/;
        console.log(val);
        if (re.test(val)){
            return true;
        }
        else{
            stat = false;
            return false;
        }

    }, click);
    check(inputPassword, "密码由最多14位数字或英文组成", function(val){

        var re = /^([a-z]|[A-Z]|[0-9]){1,14}$/;
        console.log(val);
        if (re.test(val)){
            return true;
        }
        else{
            stat = false;
            return false;
        }

    }, click);

    check(inputPasswordAgain, "两次输入密码不相同", function(val){
        if(inputPasswordAgain.value=="")
            return false;
        if(inputPassword.value!=inputPasswordAgain.value)
            return false;
        else
            return true;
    }, click);

    return stat;

}