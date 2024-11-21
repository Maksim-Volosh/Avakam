//! swiper

const adSwiperMainPageNode = document.getElementById('js-ad-main-sw');

const adSwiperMainOptions = {
	slidesPerView: 4,
	spaceBetween: 30,
	centeredSlides: true,
	loop: true,
	speed: 2500,
	autoplay: {
		delay: 3000,
		disableOnInteraction: false,
		pauseOnMouseEnter: false,
		reverseDirection: false,
	},
	fadeEffect: { crossFade: true },
};

const swiperAdMainPage = new Swiper(adSwiperMainPageNode, adSwiperMainOptions);

//! path listing_not_found.html
