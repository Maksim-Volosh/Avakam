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

//! dropdowns
const sortProductNode = document.getElementById('js-products-sort'),
	dropdownSortProductNode = document.getElementById('js-dropdown-sort'),
	dropdownItemSortProductNode = document.querySelectorAll('.dropdown__sort-btn');

//! sort
const handleSortDropdownOpen = () => {
	dropdownSortProductNode.classList.add('dropdown_open');
};
const handleSortDropdownClose = () => {
	dropdownSortProductNode.classList.remove('dropdown_open');
};
sortProductNode.addEventListener('click', event => {
	event.stopPropagation();

	dropdownSortProductNode.classList.add('dropdown_open');
});
window.addEventListener('click', handleSortDropdownClose);
dropdownItemSortProductNode.forEach(item => {
	item.addEventListener('click', handleSortDropdownClose);
});
