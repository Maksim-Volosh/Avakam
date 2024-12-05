import { createChoices } from '../create/createChoices.js';
import {
	locationFirstEntrySelectCountry,
	locationFirstEntrySelectRegion,
} from '../vars/const.js';

const POPUP_OPEN_CLASS_NAME = 'popup_open';

// choices.js(selects)
createChoices(locationFirstEntrySelectCountry);
createChoices(locationFirstEntrySelectRegion);

// popup
const firstEntryPopupNode = document.getElementById('js-first-entry-popup'),
	firstEntryPopupContentNode = document.getElementById(
		'js-first-entry-popup-content'
	);

firstEntryPopupNode.addEventListener('click', event => {
	const isClickOutsideContent = !event
		.composedPath()
		.includes(firstEntryPopupContentNode);

	if (isClickOutsideContent) {
		firstEntryPopupNode.classList.remove(POPUP_OPEN_CLASS_NAME);
	}
});

// setInterval(firstEntryPopupNode.classList.add(POPUP_OPEN_CLASS_NAME), 500);
