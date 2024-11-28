export const createSwiper = swiperNode => {
	return new Swiper(swiperNode, {
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
	});
};


