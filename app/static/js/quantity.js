(function($){"use strict";$(".input-group").on("click",".button-plus",function(n){var t,a;(n=n).preventDefault(),t=$(n.target).data("field"),n=$(n.target).closest("div"),a=parseInt(n.find("input[name="+t+"]").val(),10),isNaN(a)?n.find("input[name="+t+"]").val(0):n.find("input[name="+t+"]").val(a+1)}),$(".input-group").on("click",".button-minus",function(n){var t,a;(n=n).preventDefault(),t=$(n.target).data("field"),n=$(n.target).closest("div"),a=parseInt(n.find("input[name="+t+"]").val(),10),!isNaN(a)&&0<a?n.find("input[name="+t+"]").val(a-1):n.find("input[name="+t+"]").val(0)});})(jQuery);
(function($) {
    "use strict";
    $(".input-group").on("click", ".button-plus", function(n) {
        var t, a;
        (n = n).preventDefault(),
        t = $(n.target).data("field"),
        n = $(n.target).closest("div"),
        a = parseInt(n.find("input[name=" + t + "]").val(), 10),
        isNaN(a) ? n.find("input[name=" + t + "]").val(0) : n.find("input[name=" + t + "]").val(a + 1)
    }),
    $(".input-group").on("click", ".button-minus", function(n) {
        var t, a;
        (n = n).preventDefault(),
        t = $(n.target).data("field"),
        n = $(n.target).closest("div"),
        a = parseInt(n.find("input[name=" + t + "]").val(), 10),
        !isNaN(a) && 0 < a ? n.find("input[name=" + t + "]").val(a - 1) : n.find("input[name=" + t + "]").val(0)
    });
}
)(jQuery);