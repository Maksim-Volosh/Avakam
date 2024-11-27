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
const handleDropdownOpen = dropdownNode => {
	dropdownNode.classList.add('dropdown_open');
};
const handleDropdownClose = (event, dropdownNode, dropdownBtnNode) => {
	if (
		!dropdownNode.contains(event.target) &&
		!dropdownBtnNode.contains(event.target)
	) {
		dropdownNode.classList.remove('dropdown_open');
	}
};

//! sort
const sortProductNode = document.getElementById('js-products-sort'),
	dropdownSortProductNode = document.getElementById('js-dropdown-sort'),
	dropdownItemSortProductNode = document.querySelectorAll('.dropdown_sort-btn');

sortProductNode.addEventListener('click', () => {
	handleDropdownOpen(dropdownSortProductNode);
});
dropdownItemSortProductNode.forEach(item => {
	item.addEventListener('click', () => {
		dropdownSortProductNode.classList.remove('dropdown_open');
	});
});

//! location
const locationProductNode = document.getElementById('js-products-location'),
	dropdownLocationProductNode = document.getElementById('js-dropdown-location'),
	locationSelectDistrict = document.getElementById(
		'js-location-select-district'
	),
	locationSelectCity = document.getElementById('js-location-select-city');

locationProductNode.addEventListener('click', () => {
	handleDropdownOpen(dropdownLocationProductNode);
});

//! options
const optionsProductNode = document.getElementById('js-products-options'),
	dropdownOptionsProductNode = document.getElementById('js-dropdown-options');

	optionsProductNode.addEventListener('click', () => {
		handleDropdownOpen(dropdownOptionsProductNode);
	});

//! close dropdown
document.addEventListener('click', event => {
	if (dropdownSortProductNode.classList.contains('dropdown_open')) {
		handleDropdownClose(event, dropdownSortProductNode, sortProductNode);
	}

	if (dropdownLocationProductNode.classList.contains('dropdown_open')) {
		handleDropdownClose(
			event,
			dropdownLocationProductNode,
			locationProductNode
		);
	}

	if (dropdownOptionsProductNode.classList.contains('dropdown_open')) {
		handleDropdownClose(
			event,
			dropdownOptionsProductNode,
			optionsProductNode
		);
	}
});

//! choices.js
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
