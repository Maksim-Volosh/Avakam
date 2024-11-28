import {
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

// choices.js(selects)
createChoices(locationSelectDistrict);
createChoices(locationSelectCity);
