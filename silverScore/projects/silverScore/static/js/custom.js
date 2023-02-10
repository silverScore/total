// window.onload = function(){
//     console.log("document load!");
//     // control checked
//     mainTitle = document.querySelector("#mainTitle");
//     mainTitle.innerText = "Main to mainTitle";
//     mainTitle.style.setProperty("color","#0071c1");


// }
// window.onresize= ()=> {
//     // navbar control
//     //alert("window onresize!");
//     nav_menubar = document.querySelector(".navbar-toggler");
//     if(nav_menubar.style.display == "none"){
//         alert("nav bar menu icon gone");
//     }
// }

// JQuery ver.
$(document).ready(function(){
    //check page loaded
    console.log("document load!");
    // care_detail.html detailmenu control
    // all hide
    $(".detailmenu li").removeClass("on");
    $(".detailarea div").removeClass("show").css("display","none");
    // default basic show
    $(".detailmenu li.basic").addClass("on");
    $(".detailarea div.basic").addClass("show").css("display","block");
    $(".detailmenu li").on("click", function(){
        let className = $(this).attr('class');
        if ($(this).hasClass("disable") == false){
            $(this).toggleClass("on");
            $(this).siblings().removeClass("on");
            $(`.detailarea .${className}`).addClass("show").css("display","block");
            $(`.detailarea .${className}`).siblings().removeClass("show").css("display","none");
            $(`.detailarea .${className}`).addClass("show").css("display","block");
        }
    });
});

