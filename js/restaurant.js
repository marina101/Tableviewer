var $page=$("<div class='popup'><div><button class='submit'>Submit</button></div></div>");

$("#TableSelect li").click(function() {
	$page.show();
	$(".containermap").append($page);
	console.log($(this).text());
	
});
$page.click(function(){
	$(this).hide();
	
});