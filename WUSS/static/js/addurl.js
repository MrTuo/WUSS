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
function urlchange(){
    var url1=$("#urlpart").val();
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
    b="tag:"+(a.tagName).toLowerCase()+",";
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
    return b;
}
function ced() {
    var deptObjs= document.getElementById("iframepart").contentWindow.document.getElementById("detailwuss");
    var b=document.getElementById("detailwuss");
    b.value=deptObjs.value;
    console.log(b.value);
}
function onclickon(a) {
    if (a.style.backgroundColor!="rgba(76, 175, 80, 0.65098)"){
        a.style.backgroundColor="rgba(76, 175, 80, 0.65098)";
        a.wuss="no";
        var b=document.getElementsByName("spider_guide");
        (function(e){
            var e = window.event || e;
            if (e.stopPropagation) e.stopPropagation();
            else e.cancelBubble = true;
        })(event);
        // console.log(a.tagName);
        if (b.value==null) {
            b.value="tag:"+(a.tagName).toLowerCase()+",";
        }
        else {
            b.value=b.value+"tag:"+(a.tagName).toLowerCase()+",";
        }

        $.each(a.attributes,function (ii,at) {
            if (b.value==null){
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
        console.log(b.value);
    }
    else{
        var b=document.getElementsByName("spider_guide");
        a.wuss="yes";
        a.style.backgroundColor="";
        c=deletechoose(a);
        b.value=b.value.replace(c,"");
        console.log(b.value);
        (function(e){
            var e = window.event || e;
            if (e.stopPropagation) e.stopPropagation();
            else e.cancelBubble = true;
        })(event)
    }
    var qq=document.getElementById("detailwuss");
    qq.value=b.value;
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
    var type=["div","form","a","span","p","h1","h2","h3","h4","h5","h6","pre","table","ul","li"];
    var dont=["wuss","wuss1","wuss2","wuss3","wuss4","wuss5","wuss6","wuss7","wuss8","wuss9","wuss10"
    ,"wuss11"];
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
    str="http://";
    if (htmlurl.indexOf(str)>=0){
    }
    else{
        htmlurl=str+htmlurl;
    }
    if (htmlurl){
        window.location.href="/addhtmlurl/?url1="+htmlurl;
    }
// {#            window.location.href="../add_url_HTML/";#}
}

