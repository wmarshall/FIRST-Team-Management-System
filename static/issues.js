$(document).ready(function() {
	//shows add issue form
	$("#showaddissue").click(function(e) {
		e.preventDefault();
		$("#addissueformdiv").slideDown("fast");
	});
	
	//hides add issue form when cancel is clicked
	$("#canceladdissue").click(function(e) {
		e.preventDefault();
		$("#addissueformdiv").slideUp("fast");
	});
	
	//adds an issue to correct tables
	$("#addissueform").submit(function(e) {
		e.preventDefault();
		
		var id;
		$.post("issues", $("#addissueform").serialize(), function(data) {
			id = parseInt(data);
			
			text = $("[name=issuetext]").val();
			text = text.replace(/\n/g, "<br />");
			
			$("#" + $("[name=issuesubteam]").val() + "issues").html("<tr class='issue' id='" + id + "'>\
			<td width='600px'>" + text + "</td>\
			<td>" + $("[name=issuepriority]").val() + "</td>\
			<td>" + "5/11" + "</td>\
			<td>" + "Pat" + "</td>\
			</tr>" + $("#" + $("[name=issuesubteam]").val() + "issues").html());
			
			$("#addissueformdiv").slideUp("fast");
			
			$("[name=issuetext]").val("");
		});
	});
	
	//shows comments of an issue
	$(".issue").click(function(e) {
		e.preventDefault();
		var id = parseInt($(this).attr("id"));
		if ($("#comments" + id).css("display") != "none") {
			$("#comments" + id).hide();
		} else {
			$(".issuedetail").hide();
			$("#comments" + id).show();
		}
		
		$.post("getcomments", {id: id}, function(data) {
			$("#comments" + id).html('<td>' + data + '</td>');
		});
	});
	
	//shows user settings
	$("#showsettings").click(function(e) {
		e.preventDefault();
		$("#settings").slideDown("fast");
	});
	
	//hides user settings
	$("#donesettings").click(function(e) {
		$("#settings").slideUp("fast");
	});
});