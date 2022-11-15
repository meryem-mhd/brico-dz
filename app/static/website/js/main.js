(function ($) {
    "use strict";

    // Spinner
    var spinner = function () {
        setTimeout(function () {
            if ($('#spinner').length > 0) {
                $('#spinner').removeClass('show');
            }
        }, 1);
    };
    spinner();
    
    
    // Initiate the wowjs
    new WOW().init();


    // Sticky Navbar
    $(window).scroll(function () {
        if ($(this).scrollTop() > 300) {
            $('.sticky-top').css('top', '0px');
        } else {
            $('.sticky-top').css('top', '-100px');
        }
    });
    
    
    // Back to top button
    $(window).scroll(function () {
        if ($(this).scrollTop() > 300) {
            $('.back-to-top').fadeIn('slow');
        } else {
            $('.back-to-top').fadeOut('slow');
        }
    });
    $('.back-to-top').click(function () {
        $('html, body').animate({scrollTop: 0}, 1500, 'easeInOutExpo');
        return false;
    });


    // Header carousel
    $(".header-carousel").owlCarousel({
        autoplay: true,
        smartSpeed: 1500,
        items: 1,
        dots: true,
        loop: true,
        nav : true,
        navText : [
            '<i class="bi bi-chevron-left"></i>',
            '<i class="bi bi-chevron-right"></i>'
        ]
    });


    // Testimonials carousel
    $(".testimonial-carousel").owlCarousel({
        autoplay: true,
        smartSpeed: 1000,
        center: true,
        margin: 24,
        dots: true,
        loop: true,
        nav : false,
        responsive: {
            0:{
                items:1
            },
            768:{
                items:2
            },
            992:{
                items:3
            }
        }
    });
    
})(jQuery);

const modal = [...document.getElementsByClassName('modal-button')];
const modalBody = document.getElementsByClassName('modal-body')[0];
const start = document.getElementById('start-button');
const link = window.location.href;

modal.forEach(modal => modal.addEventListener('click', () => {
    // console.log(modal);
    const pk = modal.getAttribute('data-pk');
    const name = modal.getAttribute('data-quize');
    const numberQuestions = modal.getAttribute('data-questions')   
    const time = modal.getAttribute('data-time')   
    const pass = modal.getAttribute('data-pass') 
    const questionsLength = modal.getAttribute('questions-length')  

    modalBody.innerHTML = `
        <div class="h5 mb-3" >Ready to start  "<b>${name}</b>" ?</div>
        <div class="text-muted">
            <ul>
                <li>number of questions :  <b>${numberQuestions}</b></li>
                <li>score required to passs :  <b>${pass}</b></li>
                <li>time :  <b>${time} min</b></li>
            </ul>
        </div>
        
    `
    start.addEventListener('click', () => {
        
        window.location.href = link  + pk 
    
    })
}))
