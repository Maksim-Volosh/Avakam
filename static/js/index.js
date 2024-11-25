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

//! popups
const sortProductNode = document.getElementById('js-products-sort'),
	popupSortProductNode = document.getElementById('js-popup-sort'),
	popupItemSortProductNode = document.querySelectorAll('.popup__sort-btn');

//! sort
const handleSortPopupOpen = () => {
	popupSortProductNode.classList.add('popup_open');
};
const handleSortPopupClose = () => {
	popupSortProductNode.classList.remove('popup_open');
};
sortProductNode.addEventListener('click', event => {
	event.stopPropagation();

	popupSortProductNode.classList.add('popup_open');
});
window.addEventListener('click', handleSortPopupClose);
popupItemSortProductNode.forEach(item => {
	item.addEventListener('click', handleSortPopupClose);
});
