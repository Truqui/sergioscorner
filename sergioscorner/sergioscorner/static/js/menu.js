$(window).bind('scroll', function () {
    var banner_height = $('div.banner').height();
    if ($(window).scrollTop() > banner_height) {
        $('nav.menu').addClass('fixed');
        $('section').addClass('menu_fixed');
    } else {
        $('nav.menu').removeClass('fixed');
        $('section').removeClass('menu_fixed');
    }
});