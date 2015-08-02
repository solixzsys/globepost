/// <reference path="_references.js" />

$(window).load(function () {
    $("#roll_it").carouFredSel({

        //items: 5,
        width: '100%',
        height: 'auto',
        items: 5,
        responsive: true,
        scroll: {
            items: 3,
            easing: "linear",
            duration: 1000,
            pauseOnHover: true
        }
    });

});




var limit = {
    beg: 0,
    end: 2
};
$(document).ready(function () {

    var l = 0
    //$(".navbar-default").css({ 'background-color': 'Transparent', 'border-color': 'Transparent', 'width': '100%' }).removeClass("toTop")
    // $(window).scroll(function (evt) {
    //     l = $(window).scrollTop()
    //     //console.log(l)

    //     if ((l > 80) && (window.outerWidth > 1000)) {
    //         console.log(window.outerWidth)
    $(".navbar-default").css({ 'background-color': '#f8f8f8', 'border-color': '#e7e7e7', 'border-radius': '0 0 2px 2px', }).addClass("toTop").slideToggle("3000")
    //     } else {
    //         $(".navbar-default").css({ 'background-color': 'Transparent', 'border-color': 'Transparent','width':'100%' }).removeClass("toTop").fadeOut(3000)
    //     }
    // });

    $(".nav li").mouseover(function () {
        $(this).css({ "text-decoration-line": "underline", "text-decoration-style": "solid" })
    });
    $(".nav li").mouseleave(function () {
        $(this).css({ "text-decoration-line": "none" })
    });
    $(".navbar-header a").mouseover(function () {
        $(this).css({ "text-decoration-line": "underline", "text-decoration-style": "solid" })
    });
    $(".navbar-header a").mouseleave(function () {
        $(this).css({ "text-decoration-line": "none" })
    });


    /*	CarouFredSel: a circular, responsive jQuery carousel.
	Configuration created by the "Configuration Robot"
	at caroufredsel.dev7studios.com
*/




    var count = 11;
    var data = []



    var ajaxreq = function () {
        $.ajax({
            url: "/ajax1",
            dataType: "json",
            success: function (data1) {
                data = data1


                console.log("Inside ajax...................")
                console.log(data)
                populate(limit.beg, limit.end);
                pop_thumb();
            }


        });

        console.log("Done !!!!")

    };

    var str1 = '<div class="row" style="margin-bottom:10px">' +

                            '<div class="col-md-2 thumbnail">' +

                                //'<img src="../static/image/Koala.jpg" height="100" width="150" />'+

                            '</div>' +
                            '<div class="col-md-10" style="padding:5px;">' +
                                '<p></p></div></div>'





    function populate(beg, end) {
        console.log("Inside Populate...................")
        console.log("befor loop ", beg, end);
        for (var i = beg; i < end; i++) {


            $(str1).attr({ "id": i }).appendTo("#listing");
            $("#" + i + " p").html('<a href="#">' + data[i].fields.title + "</a>")
                .append("<p>" + data[i].fields.summary + "</p>")
                .append('<div id="note" style="float:right"><i style="font-size:8px">' + data[i].fields.pub_date + " </i></div>")
                .append('<div id="note" style="float:right"><i style="font-size:8px">' + data[i].fields.site + ":&nbsp&nbsp</i></div>");
            $("#" + i + " .thumbnail").html('<img src=' + data[i].fields.thumbnail + ' height="100" width="150" />')
        };
        limit.beg = limit.end + 1;
        limit.end = limit.end + 2;
        console.log("after loop", limit.beg, limit.end);
    }

    ajaxreq();
    var bench = 700;
    var winhoff = window.document.body.offsetHeight;
    var winh = window.innerHeight
    var mymap = document.getElementById("mymap")
    var ca = document.getElementById("contentarea")
    var sb = $("#sidebar")
    var listcont = $("#listcont")
    var st = $("#story")
    var sbl = sb.position().left
    var sbt = sb.position().top
    var sbw = sb.width()
    $(window).scroll(function () {
        winhoff = window.document.body.offsetHeight;
        if ((($(window).scrollTop() + winh + 50) > winhoff) && (limit.end < data.length)) {

            console.log("inside scroll ", limit.beg, limit.end);
            populate(limit.beg, limit.end);

            console.log("down....................................");
            bench = bench + 500;
        }
        //console.log("st ",$(window).scrollTop(),"winhoff ",winhoff);
        var offmap = mymap.offsetTop - window.scrollY;
        //console.log("offmapp..... ",offmap)
        if ((offmap) < 50) {
            $("#navigator").css({ "visibility": "hidden" });
        } else {
            $("#navigator").css({ "visibility": "visible" });
        }
        console.log("sbl sbt..... ", sbl, sbt)
        if (window.innerWidth > 1000) {
            if ((ca.offsetTop - window.scrollY) < 2) {
                console.log("inside sbl sbt..... ", sbl, (sbt - window.scrollY))
                listcont.css({ "float": "right" });
                sb.css({ "position": "fixed" });
                //st.css({ "position": "fixed" });
                sb.css({ "top": "20px" })
                //sb.css({ "float": "left" });
                //sb.css({ "clear": "both" });
                //st.css({ "top": "0" })
                sb.css({ "left": ca.offsetLeft + "px" });
                sb.css({ "width": sbw + "px" });


            } else {
                sb.css({ "position": "relative", "top": "0", "left": "0", "clear": "none" });
                listcont.css({ "top": "0" });
            }
        }
    });





    var pop_thumb = function () {
        var w = 0;
        var mydata = [];
        var thumbimg = $("#roll_it img");

        for (k = 0; k < data.length; k++) {
            temp = data[k].fields.site;
            
            if ((temp.search("Reuters") == -1) & (mydata.length<20) ) {
                mydata[w] = data[k];
                //console.log('mydata................................................',mydata)
                w = w + 1;
            }
        }
        //console.log("mydata................................................",mydata)
        for (var j = 0; j < thumbimg.length; j++) {
            thumbimg[j]["src"] = mydata[j].fields.thumbnail;
           $('<a href="#">' + mydata[j].fields.title + "</a>").insertAfter(thumbimg[j]);
        }

        

       
        



    };

    


});