const FILTER_BUTTONS_CLASS_NAME = '.filter__category-item-btn',
	FILTER_OPEN_CLASS_NAME = 'subcategory_open';

export const filterCategoryController = () => {
	const filterCategoryBtnNode = document.querySelectorAll(
		FILTER_BUTTONS_CLASS_NAME
	);

	filterCategoryBtnNode.forEach(btnNode => {
		btnNode.addEventListener('click', () => {
			const nextElement = btnNode.nextElementSibling;

			if (nextElement) {
				if (nextElement.classList.contains(FILTER_OPEN_CLASS_NAME)) {
					btnNode.classList.remove(FILTER_OPEN_CLASS_NAME);
					nextElement.classList.remove(FILTER_OPEN_CLASS_NAME);
				} else {
					btnNode.classList.add(FILTER_OPEN_CLASS_NAME);
					nextElement.classList.add(FILTER_OPEN_CLASS_NAME);
				}
			}
		});
	});
};
