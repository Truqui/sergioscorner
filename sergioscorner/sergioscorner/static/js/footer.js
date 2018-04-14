 $(document).ready(function() {
    var windows_height = $(window).height();
    var body_height = $('body').height();
    if (body_height < windows_height) {
        $('footer.main').addClass("fixed");
    }
 });
