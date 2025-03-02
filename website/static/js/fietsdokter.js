$(() => {
    $(window).on('resize', () => {
        $('#paginaInhoud').css({
            minHeight: $(window).height() - $('#paginaVoet').outerHeight(true) - 60
        });
    }).resize();
});