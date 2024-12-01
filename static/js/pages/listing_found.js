import {
	dropdownFilterController,
	dropdownLocationController,
	dropdownOptionsController,
	dropdownSortController,
} from '../controllers/dropdownControllers.js';
import { createChoices } from '../create/createChoices.js';
import { createSwiper } from '../create/createSwiper.js';
import {
	adSwiperMainPageNode,
	locationSelectCity,
	locationSelectDistrict,
} from '../vars/const.js';

// swiper
createSwiper(adSwiperMainPageNode);

// dropdowns
dropdownSortController();
dropdownLocationController();
dropdownOptionsController();
dropdownFilterController();

const filterForm = document.querySelector('.dropdown__form_filter');
const filterCategoryBtnNode = document.querySelectorAll(
	'.filter__category-btn'
);

filterCategoryBtnNode.forEach(btnNode => {
	btnNode.addEventListener('click', () => {
		const nextElement = btnNode.nextElementSibling;

		if (nextElement) {
			if (nextElement.classList.contains('subcategory_open')) {
				btnNode.classList.remove('subcategory_open');
				nextElement.classList.remove('subcategory_open');
			} else {
				btnNode.classList.add('subcategory_open');
				nextElement.classList.add('subcategory_open');
			}
		}
	});
});

// choices.js(selects)
createChoices(locationSelectDistrict);
createChoices(locationSelectCity);
