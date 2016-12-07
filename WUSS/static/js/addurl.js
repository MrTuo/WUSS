/**
 * Created by Arnold on 2016/12/4.
 */
var string=[];
choose1=document.getElementById("1");
choose2=document.getElementById("2");
$(document).ready(function() {
                $("input[type=radio][value=1]").click(function() {
                    var flag1 = $("input[type=radio][value=1]").attr("checked")=="checked"? false: "checked";
                    $("input[type=radio][value=1]").attr("checked",flag1);
                })
                $("input[type=radio][value=2]").click(function() {
                    var flag2 = $("input[type=radio][value=2]").attr("checked")=="checked"? false: "checked";
                    $("input[type=radio][value=2]").attr("checked",flag2);
                    if (flag2){
                        var url1=$("#urlpart").val();
                        var ifrm=document.getElementById("iframepart");
                        ifrm.hidden = false;
                    }
                })

            })
// {#       捕捉url变化，一旦url变化，iframe实时更新     #}
function urlchange(){
    var url1=$("#urlpart").val();
    // alert("aass");
//     var ifrm=document.getElementById("iframepart");
//     ifrm.hidden = false;
//     ifrm.src = "/addhtmlurl/?url1="+url1;
//     ifrm.onload = function(){
//         var div=ifrm.contentWindow.document.getElementsByTagName("div")
//         // alert(div.length)
// // {#                  alert(ifrm.contentWindow.document.getElementById('page').innerHTML);//弹出恭喜你操作到内部iframe中的元素了！！！#}
//         };
    str="http://";
    if (url1.indexOf(str)>=0 && url1){
    }
    else{
        url1=str+url1;
    }
    if (url1){
        window.location.href="/addhtmlurl/?url1="+url1;
    }
}
function choose_property(str){
    s=str.toString();
    //console.log(s);
    for (i in s){
        if(s[i]==','||s[i]==':'||s[i]==';')
            return false;
    }
    return true;
}
function deletechoose(a){
    b="";
    $.each(a.attributes,function (ii,at) {
        if (b==null){
            // alert(at.value);
            if(choose_property(at.value)){
                b=at.name+":"+at.value+",";
            }
        }
        else{
            if(choose_property(at.value)){
                b=b+at.name+":"+at.value+",";
            }
        }
    });
    b=b+";";
    // console.log(b);
    return b;
}
function ced() {
    var deptObjs= document.getElementById("iframepart").contentWindow.document.getElementById("detailwuss");
    var b=document.getElementById("detailwuss");
    b.value=deptObjs.value;
    console.log(b.value);
    // alert(deptObjs.value);
}
function onclickon(a) {
    if (a.style.backgroundColor!="rgba(76, 175, 80, 0.65098)"){
        a.style.backgroundColor="rgba(76, 175, 80, 0.65098)";
        a.wuss="no";
        var b=document.getElementsByName("spider_guide");
        var bb=b[0];
        (function(e){
            var e = window.event || e;
            if (e.stopPropagation) e.stopPropagation();
            else e.cancelBubble = true;
        })(event);

        // alert(a.toString())
        $.each(a.attributes,function (ii,at) {
           // console.log(ii+"name:"+at.name+"value:"+at.value);
            if (b.value==null){
                // alert(at.value);
                if(choose_property(at.value)){
                    b.value=at.name+":"+at.value+",";
                }
            }
            else{
                if(choose_property(at.value)){
                    b.value=b.value+at.name+":"+at.value+",";
                }
            }
        });
        b.value=b.value+";";
    }
    else{
        var b=document.getElementsByName("spider_guide");
        a.wuss="yes";
        a.style.backgroundColor="";
        c=deletechoose(a);
        b.value=b.value.replace(c,"");
        // alert(b.wuss);
        (function(e){
            var e = window.event || e;
            if (e.stopPropagation) e.stopPropagation();
            else e.cancelBubble = true;
        })(event)
    }
    var qq=document.getElementById("detailwuss");
    qq.value=b.value;
    // console.log(qq);
    // console.log(b.value);
}
function mousemoveon(a) {
    if (a.wuss=="yes" || a.wuss==null)
        a.style.backgroundColor="rgba(33, 150, 243, 0.68)";
}
function mousemoveout(a){
    if (a.wuss=="yes" || a.wuss==null)
        a.style.backgroundColor="";
}
function firm() {
        //利用对话框返回的值 （true 或者 false）
        if (confirm("你确定提交吗？")) {
            alert("点击了确定");
        }
        else {
            alert("点击了取消");
        }

    }
function test() {
    var type=["div","form","a","span","p","h1","h2","h3","h4","h5","h6","pre","table","ul","li"];
    var dont=["wuss","wuss1","wuss2","wuss3","wuss4","wuss5","wuss6","wuss7"];
    for (i in type){
        // console.log(type[i]);
        lala=document.getElementsByTagName(type[i]);
        // console.log(lala);
        for (i=0;i<lala.length;i++){
            // console.log(lala[i].id);
            str=lala[i].id;
            if (str.indexOf("wuss")<0)
                lala[i].addEventListener("click",onclickon.bind(lala[i],lala[i]));
        }
    }

    $(function() {
        for (i in type){
            $(type[i]).mouseover(function(e) {
                $(this).addClass("hover");
                e.stopPropagation();
            });
            $(type[i]).mouseout(function(e) {
                $(this).removeClass("hover");
                e.stopPropagation();
            });
        }
        for(i in dont){
            $("#"+dont[i]).mouseover(function() {
                $(this).removeClass("hover");
            })
        }
    })

}

var baseText = null;

function showPopup(){
    var popUp = document.getElementById("popupcontent");
    popUp.style.visibility = "visible";
}
function hidePopup(){
    var popUp = document.getElementById("popupcontent");
    popUp.style.visibility = "hidden";
}
function linkRSS(){
    window.location.href="../add_url/";
}
function linkHTML() {
    htmlurl=prompt("请输入您要订阅的网页地址","");
    // str1="http://";
    // if (htmlurl.indexOf(str)>=0){
    // }
    // else{
    //     htmlurl=str+htmlurl;
    // }
    if (htmlurl){
        window.location.href="/addhtmlurl/?url1="+htmlurl;
    }
// {#            window.location.href="../add_url_HTML/";#}
}