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
//! func
const handleDropdownOpen = (event, dropdownNode) => {
	event.stopPropagation();
	dropdownNode.classList.add('dropdown_open');
};
const handleSortDropdownClose = () => {
	dropdownSortProductNode.classList.remove('dropdown_open');
};
const handleLocationDropdownClose = () => {
	dropdownLocationProductNode.classList.remove('dropdown_open');
};

//! sort
const sortProductNode = document.getElementById('js-products-sort'),
	dropdownSortProductNode = document.getElementById('js-dropdown-sort'),
	dropdownItemSortProductNode = document.querySelectorAll('.dropdown_sort-btn');

sortProductNode.addEventListener('click', event => {
	handleDropdownOpen(event, dropdownSortProductNode);
});
dropdownItemSortProductNode.forEach(item => {
	item.addEventListener('click', handleSortDropdownClose);
});

//! location
const locationProductNode = document.getElementById('js-products-location'),
	dropdownLocationProductNode = document.getElementById('js-dropdown-location'),
	locationSelectDistrict = document.getElementById(
		'js-location-select-district'
	),
	locationSelectCity = document.getElementById('js-location-select-city');

locationProductNode.addEventListener('click', event => {
	handleDropdownOpen(event, dropdownLocationProductNode);
});

//! close dropdown
// window.addEventListener('click', handleSortDropdownClose);
// window.addEventListener('click', handleLocationDropdownClose);

const choicesSelectOptions = {
	searchEnabled: false,
	shouldSortItems: false,
	itemSelectText: '',
	shouldSort: false,
	placeholder: false,
};

const districtChoices = new Choices(
		locationSelectDistrict,
		choicesSelectOptions
	),
	cityChoices = new Choices(locationSelectCity, choicesSelectOptions);
