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
// {#                    alert(ifrm.contentWindow.document.getElementById('page').innerHTML);//弹出恭喜你操作到内部iframe中的元素了！！！#}
        };
            }
            function onclickon(a) {
// {#                alert(a.style.backgroundColor);#}
                if (a.style.backgroundColor!="rgba(76, 175, 80, 0.65098)"){
                    a.style.backgroundColor="rgba(76, 175, 80, 0.65098)";
                    a.wuss="no";
                    (function(e){
                        var e = window.event || e;
                        if (e.stopPropagation) e.stopPropagation();
                        else e.cancelBubble = true;
                    })(event);
                }
                else{
                    a.wuss="yes";
                    a.style.backgroundColor="";
                    (function(e){
                        var e = window.event || e;
                        if (e.stopPropagation) e.stopPropagation();
                        else e.cancelBubble = true;
                    })(event)
                }
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
// {#                    lala[i].addEventListener("mouseout",mousemoveout.bind(lala[i],lala[i]));#}
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
            }