

$(document).ready(function () {
    
    $('.clients').owlCarousel({
        loop: true,
        margin: 55,
        dots: true,
        loop: true,
        autoplay: true,
        smartSpeed: 1000,
        responsive: {
            0:{
                items:4
            },
            576:{
                items:6
            },
            768:{
                items:8
            },
            992:{
                items:10
            }
        }
    })

 
});
