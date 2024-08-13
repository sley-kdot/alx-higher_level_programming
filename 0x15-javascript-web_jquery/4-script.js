var element = $("#toggle_header").on("click", function() {
    var css_element = $(".green")
    if (css_element.hasClass("green")) {
        css_element.removeClass("green").addClass("red");
    } else {
        css_element.removeClass("red").addClass("green");
    }
});