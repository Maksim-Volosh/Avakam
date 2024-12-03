import {
	dropdownLocationController,
	dropdownOptionsController,
	dropdownSortController,
} from '../controllers/dropdownControllers.js';
import { filterCategoryController } from '../controllers/popupController.js';
import { createChoices } from '../create/createChoices.js';
import { createSwiper } from '../create/createSwiper.js';
import {
	adSwiperMainPageNode,
	locationFilterSelectCity,
	locationFilterSelectRegion,
	locationSelectCity,
	locationSelectDistrict,
} from '../vars/const.js';

// swiper
createSwiper(adSwiperMainPageNode);

// dropdowns
dropdownSortController();
dropdownLocationController();
dropdownOptionsController();

// choices.js(selects)
createChoices(locationSelectDistrict);
createChoices(locationSelectCity);
createChoices(locationFilterSelectRegion);
createChoices(locationFilterSelectCity);

// filter
filterCategoryController();

// popup
const POPUP_OPENED_CLASS_NAME = 'popup_open',
	BODY_OPENED_CLASS_NAME = 'body_fixed';
const bodyNode = document.querySelector('body'),
	filterPopupBtn = document.getElementById('js-filter-popup-btn'),
	popupNode = document.getElementById('js-popup'),
	popupContentNode = document.getElementById('js-popup-content');

const popupToggle = () => {
	popupNode.classList.toggle(POPUP_OPENED_CLASS_NAME);
	bodyNode.classList.toggle(BODY_OPENED_CLASS_NAME);
};

filterPopupBtn.addEventListener('click', popupToggle);
popupNode.addEventListener('click', event => {
	const isClickOutsideContent = !event
		.composedPath()
		.includes(popupContentNode);

	if (isClickOutsideContent) popupToggle();
});
