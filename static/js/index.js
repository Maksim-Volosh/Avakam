const adSwiperMainPageNode = document.getElementById('js-ad-main-sw');

const adSwiperMainOptions = {
	loop: true,
	spaceBetween: 32,
	autoplay: {
		delay: 0,
		disableOnInteraction: false,
		pauseOnMouseEnter: false,
	},
	speed: 5000,
	slidesPerView: 3.5,
};

const swiperAdMainPage = new Swiper(adSwiperMainPageNode, adSwiperMainOptions);
