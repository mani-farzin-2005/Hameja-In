(function($) {
    'use strict';

    // Mean Menu JS
    jQuery('.mean-menu').meanmenu({ 
        meanScreenWidth: "991"
    });

    // Navbar Area
    $(window).on('scroll', function() {
        if ($(this).scrollTop() >150){  
            $('.navbar-area').addClass("sticky-nav");
        }
        else{
            $('.navbar-area').removeClass("sticky-nav");
        }
    });

    // Search Overlay JS
	$(".nav-side .search-box i").on("click", function(){
		$(".search-overlay").toggleClass("search-overlay-active");
	});
    $("#ng-search").on("click", function(){
        $(".search-overlay").toggleClass("search-overlay-active");
    });
	$(".search-close").on("click", function(){
		$(".search-overlay").removeClass("search-overlay-active");
    });

    // Others Option For Responsive JS
	$(".side-nav-responsive .dot-menu").on("click", function(){
		$(".side-nav-responsive .container-max .container").toggleClass("active");
    });

    // Banner Slider 
    if($('.banner-slider').length){
        
    $('.banner-slider').owlCarousel({
        loop: true,
        margin: 30,
        nav: false ,
        items: 1,
        rtl: true,
        dots: true,
        autoplay: true,
        autoHeight: true,
        autoplayHoverPause: true,
    })
    }

    // Case Study Slider
    if($('.case-study-slider').length){
    $('.case-study-slider').owlCarousel({
        loop: true,
        margin: 30,
        nav: false,
        dots: false,
        rtl: true,
        center: true,
        autoplay: true,
        autoplayHoverPause: true,
        responsive:{
            0:{
                items: 1
            },
            600:{
                items: 2
            },
            1024:{
                items: 3
            },
            1200:{
                items: 4
            },
        },
    })
    }

    // Brand Slider
    if($('.brand-slider').length){
    $('.brand-slider').owlCarousel({
        loop: true,
        margin: 60,
        nav: false,
        rtl: true,
        dots: false,
        autoplay: true,
        autoplayHoverPause: true,
        responsive:{
            0:{
                items: 2
            },
            600:{
                items: 2
            },
            700:{
                items: 3
            },
            1024:{
                items: 5
            }
        },
    })
    }

    // Brand Seven Slider JS New
    if($('.banner-seven-slide').length){
    $('.banner-seven-slide').owlCarousel({
        rtl: true,
        loop: true,
        margin: 0,
        items: 1,
        nav: true,
        dots: false,
        autoplay: true,
        autoHeight: true,
        autoplayHoverPause: true,
    })
    }

    // Clients Slider
    if($('.clients-slider').length){
    $('.clients-slider').owlCarousel({
        loop: true,
        margin: 30,
        nav: true,
        dots: false,
        rtl: true,
        autoplay: true,
        autoplayHoverPause: true,
        responsive:{
            0:{
                items: 1
            },
            992:{
                items: 2
            }
        },
        navText: [
            "<i class='bx bx-chevron-left'></i>",
            "<i class='bx bx-chevron-right'></i>"
        ],
    })
    }

    // Clients Slider
    if($('.clients-slider-two').length){
    $('.clients-slider-two').owlCarousel({
        loop: true,
        margin: 30,
        nav: true,
        dots: false,
        rtl: true,
        autoplay: true,
        autoplayHoverPause: true,
        items: 1,
        navText: [
            "<i class='bx bx-chevron-left'></i>",
            "<i class='bx bx-chevron-right'></i>"
        ],
    })
    }

    // Banner Sub Slider
    if($('.banner-sub-slider').length){
    $('.banner-sub-slider').owlCarousel({
        loop: true,
        margin: 30,
        nav: false,
        rtl: true,
        dots: false,
        autoplay: true,
        autoplayHoverPause: true,
        responsive:{
            0:{
                items: 1
            },
            1024:{
                items: 3
            }
        },
    })
    }

    // Popup Video
    if($('.popup-btn').length){
    $('.popup-btn').magnificPopup({
        disableOn: 320,
        type: 'iframe',
        mainClass: 'mfp-fade',
        removalDelay: 160,
        preloader: false,
        fixedContentPos: false
    });
    }

    ////////////////////////////////////
        $('.menu-toggle').click(function(){
            $('#mobile-sidedar').fadeIn();
            setTimeout(function(){
                $('body').addClass('out');
            }, 300);
        })
         $('#mobile-sidedar .close').click(function(){
                $('body').removeClass('out');
            setTimeout(function(){
            $('#mobile-sidedar ').fadeOut();
            }, 500);
        })
         $('#sidemenu li').each(function(){
            if($(this).children('ul').length){   
            $(this).addClass('dropdown');
             $(this).append('<i class="dropdown-btn"><svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-chevron-down" width="20" height="20" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round"><path stroke="none" d="M0 0h24v24H0z" fill="none"/><path d="M6 9l6 6l6 -6" /></svg></i>')
            }
         })
////////////////////////////////////
         $('.dropdown-btn').click(function(){
    $(this).toggleClass('active').siblings('ul').slideToggle();
    $(this).parents('li').siblings().find('ul').slideUp();
    $(this).parents('li').siblings().find('.dropdown-btn').removeClass('active');
})
////////////////////////////////////

    // Nice Select JS
    // $('select').niceSelect();

    // FAQ Accordion JS
	$('.accordion').find('.accordion-title').on('click', function(){
		// Adds Active Class
		$(this).toggleClass('active');
		// Expand or Collapse This Panel
		$(this).next().slideToggle('fast');
		// Hide The Other Panels
		$('.accordion-content').not($(this).next()).slideUp('fast');
		// Removes Active Class From Other Titles
		$('.accordion-title').not($(this)).removeClass('active');		
    });

    // Skill JS
	$('.skill-bar').each(function() {
		$(this).find('.progress-content').animate({
		width:$(this).attr('data-percentage')
		},2000);
		
		$(this).find('.progress-number-mark').animate(
		{right:$(this).attr('data-percentage')},
		{
			duration: 2000,
			step: function(now, fx) {
			var data = Math.round(now);
			$(this).find('.percent').html(data + '%');
			}
		});  
	});

    // WOW JS
    // new WOW().init();

    // Preloader JS
    $(window).on('load',function(){
        $(".preloader").fadeOut(500);
    });

    // Back To Top
    $('body').append("<div class='go-top'><i class='bx bx-chevrons-up'></i></div>");
    $(window).on('scroll', function() {
        var scrolled = $(window).scrollTop();
        if (scrolled > 600) $('.go-top').addClass('active');
        if (scrolled < 600) $('.go-top').removeClass('active');
    });
    $('.go-top').on('click', function() {
        $('html, body').animate({
            scrollTop: '0',
        }, 50 );
    });
    
        var lightboxDescription = GLightbox({
            selector: '.glightbox4'
        });


    if($('.elem').length){
        lc_lightbox('.elem', {
            wrap_class: 'lcl_fade_oc',
            gallery : true,
            thumb_attr: 'data-lcl-thumb',

            skin: 'minimal',
            radius: 0,
            padding : 0,
            border_w: 0,
        });
    }

    // Count Time JS
	function makeTimer() {
		var endTime = new Date("December 30, 2024 17:00:00 PDT");			
		var endTime = (Date.parse(endTime)) / 1000;
		var now = new Date();
		var now = (Date.parse(now) / 1000);
		var timeLeft = endTime - now;
		var days = Math.floor(timeLeft / 86400); 
		var hours = Math.floor((timeLeft - (days * 86400)) / 3600);
		var minutes = Math.floor((timeLeft - (days * 86400) - (hours * 3600 )) / 60);
		var seconds = Math.floor((timeLeft - (days * 86400) - (hours * 3600) - (minutes * 60)));
		if (hours < "10") { hours = "0" + hours; }
		if (minutes < "10") { minutes = "0" + minutes; }
		if (seconds < "10") { seconds = "0" + seconds; }
		$("#days").html(days + "<span>روز</span>");
		$("#hours").html(hours + "<span>ساعت</span>");
		$("#minutes").html(minutes + "<span>دقیقه</span>");
		$("#seconds").html(seconds + "<span>ثانیه</span>");
	}
    setInterval(function() { makeTimer(); }, 300);

    // Subscribe form

        
    // AJAX MailChimp


})(jQuery);

// function to set a given theme/color-scheme
function setTheme(themeName) {
    localStorage.setItem('theme', themeName);
    document.documentElement.className = themeName;
}

// function to toggle between light and dark theme
function toggleTheme() {
    if (localStorage.getItem('theme') === 'theme-dark') {
        setTheme('theme-light');
    } else {
        setTheme('theme-dark');
    }
}

// Immediately invoked function to set the theme on initial load
/* (function () {
    if (localStorage.getItem('theme') === 'theme-dark') {
        setTheme('theme-dark');
        document.getElementById('slider').checked = false;
    } else {
        setTheme('theme-light');
      document.getElementById('slider').checked = true;
    }
})(); */