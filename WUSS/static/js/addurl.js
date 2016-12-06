/**
 * Created by Arnold on 2016/12/4.
 */
var string=[]
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
    var ifrm=document.getElementById("iframepart");
    ifrm.hidden = false;
    ifrm.src = "/addhtmlurl/?url1="+url1;
    ifrm.onload = function(){
        var div=ifrm.contentWindow.document.getElementsByTagName("div")
        // alert(div.length)
// {#                  alert(ifrm.contentWindow.document.getElementById('page').innerHTML);//弹出恭喜你操作到内部iframe中的元素了！！！#}
        };
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
function test() {
    var lala=document.getElementsByTagName("div");
    for (i=0;i<lala.length;i++){
        lala[i].wuss="yes";
// {#                    alert(lala[i].wuss);#}
// {#                    lala[i].addEventListener("mousemove",mousemoveon.bind(lala[i],lala[i]));#}
// {                    lala[i].addEventListener("mouseout",mousemoveout.bind(lala[i],lala[i]));
        lala[i].addEventListener("click",onclickon.bind(lala[i],lala[i]));
    }
    var lala=document.getElementsByTagName("form");
    for (i=0;i<lala.length;i++){
        lala[i].wuss="yes";
        lala[i].addEventListener("click",onclickon.bind(lala[i],lala[i]));
    }
    var lala=document.getElementsByTagName("a");
    for (i=0;i<lala.length;i++){
        lala[i].wuss="yes";
        lala[i].addEventListener("click",onclickon.bind(lala[i],lala[i]));
    }
    var lala=document.getElementsByTagName("span");
    for (i=0;i<lala.length;i++){
        lala[i].wuss="yes";
        lala[i].addEventListener("click",onclickon.bind(lala[i],lala[i]));
    }
    var lala=document.getElementsByTagName("p");
    for (i=0;i<lala.length;i++){
        lala[i].wuss="yes";
        lala[i].addEventListener("click",onclickon.bind(lala[i],lala[i]));
    }
    var lala=document.getElementsByTagName("h1");
    for (i=0;i<lala.length;i++){
        lala[i].wuss="yes";
        lala[i].addEventListener("click",onclickon.bind(lala[i],lala[i]));
    }
    var lala=document.getElementsByTagName("h2");
    for (i=0;i<lala.length;i++){
        lala[i].wuss="yes";
        lala[i].addEventListener("click",onclickon.bind(lala[i],lala[i]));
    }
    var lala=document.getElementsByTagName("h3");
    for (i=0;i<lala.length;i++){
        lala[i].wuss="yes";
        lala[i].addEventListener("click",onclickon.bind(lala[i],lala[i]));
    }
    var lala=document.getElementsByTagName("h4");
    for (i=0;i<lala.length;i++){
        lala[i].wuss="yes";
        lala[i].addEventListener("click",onclickon.bind(lala[i],lala[i]));
    }
    var lala=document.getElementsByTagName("h5");
    for (i=0;i<lala.length;i++){
        lala[i].wuss="yes";
        lala[i].addEventListener("click",onclickon.bind(lala[i],lala[i]));
    }
    var lala=document.getElementsByTagName("h6");
    for (i=0;i<lala.length;i++){
        lala[i].wuss="yes";
        lala[i].addEventListener("click",onclickon.bind(lala[i],lala[i]));
    }
    var lala=document.getElementsByTagName("pre");
    for (i=0;i<lala.length;i++){
        lala[i].wuss="yes";
        lala[i].addEventListener("click",onclickon.bind(lala[i],lala[i]));
    }
    var lala=document.getElementsByTagName("table");
    for (i=0;i<lala.length;i++){
        lala[i].wuss="yes";
        lala[i].addEventListener("click",onclickon.bind(lala[i],lala[i]));
    }
    var lala=document.getElementsByTagName("ul");
    for (i=0;i<lala.length;i++){
        lala[i].wuss="yes";
        lala[i].addEventListener("click",onclickon.bind(lala[i],lala[i]));
    }
    var lala=document.getElementsByTagName("li");
    for (i=0;i<lala.length;i++){
        lala[i].wuss="yes";
        lala[i].addEventListener("click",onclickon.bind(lala[i],lala[i]));
    }
    $(function() {
        $("div").mouseover(function(e) {
            $(this).addClass("hover");
            e.stopPropagation();
        });
        $("div").mouseout(function(e) {
            $(this).removeClass("hover");
            e.stopPropagation();
        });
        $("ul").mouseover(function(e) {
            $(this).addClass("hover");
            e.stopPropagation();
        });
        $("ul").mouseout(function(e) {
            $(this).removeClass("hover");
            e.stopPropagation();
        });
        $("table").mouseover(function(e) {
            $(this).addClass("hover");
            e.stopPropagation();
        });
        $("table").mouseout(function(e) {
            $(this).removeClass("hover");
            e.stopPropagation();
        });
        $("span").mouseover(function(e) {
            $(this).addClass("hover");
            e.stopPropagation();
        });
        $("span").mouseout(function(e) {
            $(this).removeClass("hover");
            e.stopPropagation();
        });
        $("p").mouseover(function(e) {
            $(this).addClass("hover");
            e.stopPropagation();
        });
        $("p").mouseout(function(e) {
            $(this).removeClass("hover");
            e.stopPropagation();
        });
        $("input").mouseover(function(e) {
            $(this).addClass("hover");
            e.stopPropagation();
        });
        $("input").mouseout(function(e) {
            $(this).removeClass("hover");
            e.stopPropagation();
        });
        $("h1").mouseover(function(e) {
            $(this).addClass("hover");
            e.stopPropagation();
        });
        $("h1").mouseout(function(e) {
            $(this).removeClass("hover");
            e.stopPropagation();
        });
        $("h2").mouseover(function(e) {
            $(this).addClass("hover");
            e.stopPropagation();
        });
        $("h2").mouseout(function(e) {
            $(this).removeClass("hover");
            e.stopPropagation();
        });
        $("h3").mouseover(function(e) {
            $(this).addClass("hover");
            e.stopPropagation();
        });
        $("h3").mouseout(function(e) {
            $(this).removeClass("hover");
            e.stopPropagation();
        });
        $("h4").mouseover(function(e) {
            $(this).addClass("hover");
            e.stopPropagation();
        });
        $("h4").mouseout(function(e) {
            $(this).removeClass("hover");
            e.stopPropagation();
        });
        $("h5").mouseover(function(e) {
            $(this).addClass("hover");
            e.stopPropagation();
        });
        $("h5").mouseout(function(e) {
            $(this).removeClass("hover");
            e.stopPropagation();
        });
        $("h6").mouseover(function(e) {
            $(this).addClass("hover");
            e.stopPropagation();
        });
        $("h6").mouseout(function(e) {
            $(this).removeClass("hover");
            e.stopPropagation();
        });
        $("pre").mouseover(function(e) {
            $(this).addClass("hover");
            e.stopPropagation();
        });
        $("pre").mouseout(function(e) {
            $(this).removeClass("hover");
            e.stopPropagation();
        });
    });
}
