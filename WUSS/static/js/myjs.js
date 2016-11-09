/**
 * Created by Arnold on 2016/11/2.
 */
var clock = '';
var nums = 3;
var btn;
function sendCode(thisBtn)
{
    email=$("#femail").val()
    mytext=$("#fyanzhengma")
    $.ajax({
        url:'/send_email_to_changepassword/',
        data:{
            name:name,
            email:email,
        },
        type:'post',
        success:function(arg){
            alert(arg)
            mytext.attr("disabled",false);
        }
    })
    btn = thisBtn;
    btn.disabled = true; //将按钮置为不可点击
    btn.value = nums+'秒后可重新获取';
    clock = setInterval(doLoop, 1000); //一秒执行一次

 }
function doLoop()
{
    nums--;
    if(nums > 0){
        btn.value = nums+'秒后可重新获取';
    } else {
        clearInterval(clock); //清除js定时器
        btn.disabled = false;
        btn.value = '点击发送验证码';
        nums = 3; //重置时间
        $("#test").hide();
    }
}
function send()
{
    var email=$("#inputEmail").val()
    var password=$("#inputPassword").val()
    $.ajax({
        url:"../login/",
        data:{
            lognameforajax:email,
            logpasswordforajax:password
        },
        type:'post',
        success:function(arg){
            if (arg=="账号或密码错误")
                alert(arg)
            else
                windows.location.reload()
        }
    })
}
function judgeforexisting(thisbtn)
{
    var name=$("#inputName").val()
    var btn=thisbtn
    $.ajax({
        url:"/Registerajax/",
        data:{
            name:name,
        },
        type:'post',
        success:function (arg) {
            btn.value=arg
        }
    })
}
function judgeforemail(thisbtn)
{
    var email=$("#inputEmail").val()
    var btn=thisbtn
    $.ajax({
        url:"/Registerajaxemail/",
        data:{
            email:email,
        },
        type:'post',
        success:function (arg) {
            btn.value=arg
        }
    })
}
function myFunction()
{
    var btn1=$("#btnname").val()
    var btn2=$("#btnemail").val()
    if (btn1!="可以使用该用户"||btn2!="可以使用该邮箱")
        alert("用户名或注册邮箱重复")
}
function apply()
{
    email=$("#femail").val()
    yanzhengma=$("#fyanzhengma").val()
    $.ajax({
        url:"/applyfor/",
        data:{
            email:email,
            yanzhengma:yanzhengma,
        },
        type:'post',
        success:function(arg){
            alert(arg)
            if (arg=="验证成功")
                window.location.href='/forgetandchangepassword?email='+email
        }
    })
}
function text() {

}