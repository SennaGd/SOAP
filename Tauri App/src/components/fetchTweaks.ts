export default function sortTweaksOnCategory(jsonObj, category: String) {
	const tweaks = Object.values(jsonObj)
	const tweakCategoryMap = tweaks.map(tweak => tweak.category)

	var sortedTweaks = [] // will hold all the tweaks based on category
	
	for (var i = 0; i <= tweakCategoryMap.length-1; i++) {
		if (tweaks[i].category == category){
			sortedTweaks.push(tweaks[i])
		}
	}
	return sortedTweaks
}
