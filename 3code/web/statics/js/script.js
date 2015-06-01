function getCookie(name){
    var x = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return x ? x[1]:undefined;
}
$(document).ready(function(){
    $("#login").click(function(){
        var user = $("#username").val();
        var pwd = $("#password").val();
        var pd = {"username":user, "password":pwd, "_xsrf":getCookie("_xsrf")};
        $.ajax({
            type:"post",
            url:"/",
            data:pd,
            cache:false,
            success:function(data){
                if (data=="-1"){
                    window.location.href="/error";
                }else{
                    window.location.href = "/user?user="+data;
                }
            },
            error:function(){
                alert("error!");
            },
        });
    });
});
