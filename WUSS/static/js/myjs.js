/**
 * Created by Arnold on 2016/11/2.
 */
var clock = '';
var nums = 3;
var btn;
function sendCode(thisBtn)
{
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
    var email=$("#inputEmail").val();
    var password=$("#inputPassword").val()
    $.ajax({
        url:"../logic/",
        data:{
            lognameforajax:email,
            logpasswordforajax:password
        },
        type:'post',
        success:function(arg){
            if (arg=="账号或密码错误")
                alert(arg)
            else
                window.location.href='/'
        }
    })
}