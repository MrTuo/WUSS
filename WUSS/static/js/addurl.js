// /**
//  * Created by Arnold on 2016/12/4.
//  */
// var string=[];
// choose1=document.getElementById("1");
// choose2=document.getElementById("2");
// $(document).ready(function() {
//     $("input[type=radio][value=1]").click(function() {
//         var flag1 = $("input[type=radio][value=1]").attr("checked")=="checked"? false: "checked";
//         $("input[type=radio][value=1]").attr("checked",flag1);
//     })
//     $("input[type=radio][value=2]").click(function() {
//         var flag2 = $("input[type=radio][value=2]").attr("checked")=="checked"? false: "checked";
//         $("input[type=radio][value=2]").attr("checked",flag2);
//         if (flag2){
//             var url1=$("#urlpart").val();
//             var ifrm=document.getElementById("iframepart");
//             ifrm.hidden = false;
//         }
//     })
// })
function urlchange(){
    var url1=document.getElementById("urlpart").value;
    str="";
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
            if(at.name=="change"){

            }
            else {//去除掉change
                if(choose_property(at.value)){
                    b=at.name+":"+at.value+",";
                }
            }
        }
        else{
            if (at.name=="change"){

            }
            else {
                if(choose_property(at.value)){
                    b=b+at.name+":"+at.value+",";
                }
            }

        }
    });
    // b=b+"index:"+a.getAttribute("index")+";";
    b=b+";";
    return b;
}
function ced() {
    var deptObjs= document.getElementById("iframepart").contentWindow.document.getElementById("detailwuss");
    var b=document.getElementById("detailwuss");
    b.value=deptObjs.value;
    console.log(b.value);
}
function reindex(a) {//重新更新index
    if (a.getAttribute("change")=="yes"){

    }
    else{//没有改变过的才需要从新更新index
        allclass=a.className;//获得拥有该class所有相同的标签
        allclass=allclass.replace("hover","");//将hover去除
        spidernumber=document.getElementsByClassName(allclass)
        for (i in spidernumber){
            // console.log(spidernumber[i].getAttribute("index"));
            if (spidernumber[i].getAttribute("index")==a.getAttribute("index")){//如果该标签的index与所有标签的index相同，则保存
                // console.log("find"+i);
                a.setAttribute("index",i);
                a.setAttribute("change","yes");
                // console.log(a.getAttribute("index"));
                break;
            }
        }
    }

}
function onclickon(a) {
    if (a.style.backgroundColor!="rgba(76, 175, 80, 0.65098)"){
        a.style.backgroundColor="rgba(76, 175, 80, 0.65098)";
        a.wuss="no";
        var b=document.getElementsByName("spider_guide")[0];//b是要放的spider_guide
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
            // console.log(at.name);
            if (at.name=="index"){
                reindex(a);
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
            }
            else if (at.name=="change") {//这是用来记录是否已经改变过

            }
            else{
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
            }

        });
        // b.value=b.value+"index:"+a.getAttribute("index")+";";
        //PS这是尝试更新index的
        console.log(a.className);
        b.value=b.value+";";
        console.log(b.value);
        console.log(b);
        //当点击事件完成的时候，如果频率已经选好了，那么就可以点击提交了
        if(b.value==""){

        }
        else{
            btn=$("#onlyyes")[0];
            btn.disabled="";
        }
    }
    else{
        var b=document.getElementsByName("spider_guide")[0];
        console.log(b);
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
        //点去取消的时候可能会将所有的订阅部分取消掉，这时候需要将提交按钮取消
        if(b.value==""){
            btn=$("#onlyyes")[0];
            btn.disabled="disabled";
        }
        else{
            btn=$("#onlyyes")[0];
            btn.disabled="";
        }
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
function test() {//添加点击事件
    var type=["div","form","span","pre","table","ul"];
    var dont=["wuss","wuss1","wuss2","wuss3","wuss4","wuss5","wuss6","wuss7","wuss8","wuss9","wuss10"
    ,"wuss11","wuss12","wuss13","wuss15","wuss16","wuss17","wuss18","wuss19","wuss20"];
    for (i in type){
        // console.log(type[i]);
        lala=document.getElementsByTagName(type[i]);
        // console.log(lala);
        for (i=0;i<lala.length;i++){
            // console.log(lala[i].id);
            str=lala[i].id;
            if (str.indexOf("wuss")<0){//去除掉自定义选择框
                if (lala[i].classList.length>0){//至少有一个class才能订阅 这里只移除了点击事件 // hover事件可以不移除，因为点击没有click事件的区域会自动指向其父元素
                    lala[i].addEventListener("click",onclickon.bind(lala[i],lala[i]));
                    lala[i].setAttribute("index",i);
                }
                // console.log("i="+i+" wuss:"+lala[i].getAttribute("index"));
                // console.log(lala[i]);
            }

        }
    }
    $(function() {//添加hover事件
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
