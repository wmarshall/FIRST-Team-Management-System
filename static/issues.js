$(document).ready(function() {
	$("#showaddissue").click(function(e) {
		e.preventDefault();
		$("#addissueformdiv").slideDown("fast");
	});
	$("#canceladdissue").click(function(e) {
		e.preventDefault();
		$("#addissueformdiv").slideUp("fast");
	});
	$("#addissueform").submit(function(e) {
		e.preventDefault();
		$("#tableissues").html("<tr>\
		<td width='600px'>" + $("[name=issuetext]").val() + "</td>\
		<td>" + $("[name=issuepriority]").val() + "</td>\
		<td>" + "5/11" + "</td>\
		<td>" + "Pat" + "</td>\
		</tr>" + $("#tableissues").html());
		
		$("#addissueformdiv").slideUp("fast");
		$("[name=issuetext]").html("");
		
		$.post("issues", $("#addissueform").serialize());
	});
	
	$("#showsettings").click(function(e) {
		e.preventDefault();
		$("#settings").slideDown("fast");
	});
	$("#donesettings").click(function(e) {
		$("#settings").slideUp("fast");
	});
});