export const createChoices = choicesNode => {
	return new Choices(choicesNode, {
		searchEnabled: false,
		shouldSortItems: false,
		itemSelectText: '',
		shouldSort: false,
		placeholder: false,
	});
};
