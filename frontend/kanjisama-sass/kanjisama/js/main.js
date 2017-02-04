$(document).ready(function(){
    $('.js-level-slider').slick({
        slidesToShow: 5,
        responsive: [
            {
                breakpoint: 768,
                settings: {
                    slidesToShow: 3
                }
            },
            {
                breakpoint: 420,
                settings: {
                    slidesToShow: 2
                }
            }
        ]
    });
});