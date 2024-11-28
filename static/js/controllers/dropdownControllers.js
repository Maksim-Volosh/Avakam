const SORT_BTN_CLASS_NAME = 'js-products-sort',
	SORT_DROPDOWN_CLASS_NAME = 'js-dropdown-sort',
	LOCATION_BTN_CLASS_NAME = 'js-products-location',
	LOCATION_DROPDOWN_CLASS_NAME = 'js-dropdown-location',
	OPTIONS_BTN_CLASS_NAME = 'js-products-options',
	OPTIONS_DROPDOWN_CLASS_NAME = 'js-dropdown-options',
	DROPDOWN_OPEN_CLASS_NAME = 'dropdown_open';

//! handlers
const handleDropdownOpen = dropdownNode => {
	dropdownNode.classList.add(DROPDOWN_OPEN_CLASS_NAME);
};
const handleDropdownClose = (event, dropdownNode, dropdownBtnNode) => {
	if (dropdownNode.classList.contains(DROPDOWN_OPEN_CLASS_NAME)) {
		if (
			!dropdownNode.contains(event.target) &&
			!dropdownBtnNode.contains(event.target)
		) {
			dropdownNode.classList.remove(DROPDOWN_OPEN_CLASS_NAME);
		}
	}
};

//! sort
export const dropdownSortController = () => {
	const sortProductNode = document.getElementById(SORT_BTN_CLASS_NAME),
		dropdownSortProductNode = document.getElementById(SORT_DROPDOWN_CLASS_NAME);

	sortProductNode.addEventListener('click', () => {
		handleDropdownOpen(dropdownSortProductNode);
	});

	document.addEventListener('click', event => {
		handleDropdownClose(event, dropdownSortProductNode, sortProductNode);
	});
};

//! location
export const dropdownLocationController = () => {
	const locationProductNode = document.getElementById(LOCATION_BTN_CLASS_NAME),
		dropdownLocationProductNode = document.getElementById(
			LOCATION_DROPDOWN_CLASS_NAME
		);

	locationProductNode.addEventListener('click', () => {
		handleDropdownOpen(dropdownLocationProductNode);
	});

	document.addEventListener('click', event => {
		handleDropdownClose(
			event,
			dropdownLocationProductNode,
			locationProductNode
		);
	});
};

//! options
export const dropdownOptionsController = () => {
	const optionsProductNode = document.getElementById(OPTIONS_BTN_CLASS_NAME),
		dropdownOptionsProductNode = document.getElementById(
			OPTIONS_DROPDOWN_CLASS_NAME
		);

	optionsProductNode.addEventListener('click', () => {
		handleDropdownOpen(dropdownOptionsProductNode);
	});

	document.addEventListener('click', event => {
		handleDropdownClose(event, dropdownOptionsProductNode, optionsProductNode);
	});
};
