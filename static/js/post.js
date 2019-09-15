var SS = null;

$(document).ready(function () {
	$("span[class*='tagged-sentence']").click(function () {
		if (SS === this) {
			$('div#commenter').slideUp();
			SS = null;
		} else {
			$(SS).removeClass('active');
			SS = this;
			$('div#commenter').slideDown();
		}
		$(this).toggleClass('active');
	});
})