import {
	dropdownLocationController
} from '../controllers/dropdownControllers.js';
import { createChoices } from '../create/createChoices.js';
import { locationSelectCity, locationSelectDistrict } from '../vars/const.js';

// dropdowns
dropdownLocationController();

// choices.js(selects)
createChoices(locationSelectDistrict);
createChoices(locationSelectCity);
