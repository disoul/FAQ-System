$(document).ready(function(){
	var check_array = [false,false,false,false]
	$(".yes").click(function(){
		var ischeck = function(){
			for (var i in check_array)
				if (check_array[i] === false)
					return false;
			return true;
		};
		if (ischeck() == true)
			$(".signup-form").submit();	
	});
	
	$("#sign-up").click(function(){
		$(".dialog-bg").fadeIn();		
	});

	$("input").blur(function(){
		$(".errMsg").remove()
		if ($(this).is("#name")){
			if (this.value=="" || this.value.length < 3){
				var errMsg = $("<div class='errMsg'><p>至少3个字符</p></div>");
				$(this).parent().append(errMsg);
				$(this).animate({
					backgroundColor: jQuery.Color("#ff6666")
				},500);
				check_array[0] = false;
			}else{
				$(this).animate({
					backgroundColor: jQuery.Color("#87b68b")
				},500);
				check_array[0] = true;
			}
		}

		if ($(this).is("#email")){
			if (this.value=="" || this.value!="" && !/.+@.+\.[a-zA-Z]{2,4}$/.test(this.value)){
				var errMsg = $("<div class='errMsg'>请确认Email地址正确</div>");
				$(this).parent().append(errMsg);
				$(this).animate({
					backgroundColor: jQuery.Color("#ff6666")
				},500);
				check_array[1] = false;
			}else{
				$(this).animate({
					backgroundColor: jQuery.Color("#87b68b")
				},500);
				check_array[1] = true;
			}
		}

		if ($(this).is("#password")){
			if (this.value=="" || this.value.length < 5){
				var errMsg = $("<div class='errMsg'>至少5个字符</div>");
				$(this).parent().append(errMsg);
				$(this).animate({
					backgroundColor: jQuery.Color("#ff6666")
				},500);
				check_array[2] = false;
			}else{
				$(this).animate({
					backgroundColor: jQuery.Color("#87b68b")
				},500);
				check_array[2] = true;
			}
		}

		if ($(this).is("#pw2")){
			if (this.value != $("#password").get(0).value){
				var errMsg = $("<div class='errMsg'>密码不一致</div>");
				$(this).parent().append(errMsg);
				$(this).animate({
					backgroundColor: jQuery.Color("#ff6666")
				},500);
				check_array[3] = false;
			}else{
				$(this).animate({
					backgroundColor: jQuery.Color("#87b68b")
				},500);
				check_array[3] = true;
			}
		}
	});
});
