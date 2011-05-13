$(document).ready(function() {
	$("#showaddissue").click(function(e) {
		e.preventDefault();
		$("#addissueform").slideDown("fast");
	});
	$("#canceladdissue").click(function(e) {
		e.preventDefault();
		$("#addissueform").slideUp("fast");
	});
	
	$("#showsettings").click(function(e) {
		e.preventDefault();
		$("#settings").slideDown("fast");
	});
	$("#donesettings").click(function(e) {
		$("#settings").slideUp("fast");
	});
});