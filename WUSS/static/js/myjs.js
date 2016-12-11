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
    var next=window.location.search.substr(6)

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
                if (next.length>0)
                    window.location.href=next
                else
                    window.location.reload()
        }
    })
}
function judgeforexisting(thisbtn)
{
    var a=$("#inputName");
    var name=a.val();
    var btn=thisbtn
    console.log(a[0].readOnly);
    if (a[0].readOnly==true){
        btn.value="查看用户是否存在";
        a[0].readOnly=false;
    }
    else {
        $.ajax({
            url:"/Registerajax/",
            data:{
                name:name,
            },
            type:'post',
            success:function (arg) {
                btn.value=arg;
                if (btn.value=="用户已存在"){

                }
                else {
                    a[0].readOnly=true;
                    changede();
                }
            }
        })
    }

}
function judgeforemail(thisbtn)
{
    var a=$("#inputEmail");
    var email=a.val();
    var btn=thisbtn
    if (a[0].readOnly==true){
        btn.value="查看邮箱是否注册";
        a[0].readOnly=false;
    }
    else {
        $.ajax({
            url:"/Registerajaxemail/",
            data:{
                email:email,
            },
            type:'post',
            success:function (arg) {
                btn.value=arg;
                if (btn.value=="邮箱已注册"){

                }
                else {
                    a[0].readOnly=true;
                    changede();
                }
            }
        })
    }

}
function changede(){
    console.log("yes");
    var btn=document.getElementById('onlyyes');
    var btnname=document.getElementById("btnname").value;
    var btnemail=document.getElementById("btnemail").value;
    var check1=document.getElementById("wuss1");
    var check2=document.getElementById("wuss2");
    var check3=document.getElementById("wuss3");
    var check4=document.getElementById("wuss4");
    var mima1=document.getElementById("inputPassword").value;
    var mima2=document.getElementById("inputPasswordAgain").value;
    console.log(btnname);
    if (btnname=="可以使用该用户名：点击此处修改" &&btnemail=="可以使用该邮箱：点击此处修改"){
        console.log("1");
        console.log(check1.style.display);
        if(!(check1.style.display&&check2.style.display&&check3.style.display&&check4.style.display)){
            console.log("2");
            console.log(mima1);
            console.log(mima2);
            if(mima1==mima2){
                console.log(btn.disabled);
                btn.disabled=false;
            }
        }
        else{
            btn.disabled=true;
        }
    }
}
function checktime1(time){
    str=time.value;
    mydiv=$("#wuss1");
    var re = /^([a-z]|[A-Z]|[0-9]){1,20}$/;
    btn=$("#onlyyes")[0];
    if (re.test(str)){
    }
    else{
        mydiv[0].style.display="block";
        btn.disabled="disable";
    }
}
function hiddenchecktime1(time){
    mydiv=$("#wuss1");
    mydiv[0].style.display="";
}
function checktime2(time){
    str=time.value;
    console.log(str);
    mydiv=$("#wuss2");
    btn=$("#onlyyes")[0];
    var re = /^([a-z]|[A-Z]|[0-9]){1,20}@([a-z]|[A-Z]|[0-9]|.){1,10}$/;
    if (re.test(str)){
    }
    else{
        mydiv[0].style.display="block";
        btn.disabled="disable";
    }
}
function hiddenchecktime2(time){
    mydiv=$("#wuss2");
    mydiv[0].style.display="";
}
function checktime3(time){
    str=time.value;
    console.log(str);
    mydiv=$("#wuss3");
    btn=$("#onlyyes")[0];
    var re = /^([a-z]|[A-Z]|[0-9]){1,14}$/;
    if (re.test(str)){
    }
    else{
        mydiv[0].style.display="block";
        btn.disabled="disable";
    }
}
function hiddenchecktime3(time){
    mydiv=$("#wuss3");
    mydiv[0].style.display="";
}
function checktime4(time){
    str=time.value;
    mydiv=$("#wuss4");
    btn=$("#onlyyes")[0];
    mima=document.getElementById("inputPassword").value;
    if (mima==str){
    }
    else {
        mydiv[0].style.display="block";
        btn.disabled="disable";
    }

}
function hiddenchecktime4(time){
    mydiv=$("#wuss4");
    mydiv[0].style.display="";
}
    ///-------------------------------
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
            if (arg=="验证成功"){
                window.location.href='/forgetandchangepassword?email='+email
            }

        }
    })
}

function open_and_close(thistext)
{
    // alert("test")
}

var myid="1";
var myid2=0;
function mytest1() {
    var id=document.getElementById("general");
    id.id=myid;
    // alert(id.id)
    // alert(myid)
    var b;

    b=$('#'+myid).text()
    $('#'+myid).html(b)
    // alert(id.id)
    myid++;

}
function mytest2() {
    var number=["One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Eleven","Twelve",
    "Threeteen","Fourteen","Fifteen","Sixteen"]
    var generala=document.getElementById("generala");
    var generalb=document.getElementById("generalb");
    // alert(generala.href)
    generala.href="#collapse"+number[myid2]
    generala.id="collapse"+number[myid2]+number[myid2]
    // alert(generala.href)
    generalb.id="collapse"+number[myid2]
    myid2++;
    // alert(1)
}
