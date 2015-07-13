$(document).ready(function(){
	$(".control").click(function(){
		$(".signup-form").submit();	
	});
	
	$(".sign-up").click(function(){
		$(".dialog-bg").fadeIn();		
	});

	$("input").blur(function(){
		if ($(this).is("#name")){
			if (this.value=="" || this.value.length < 3){
				var errMsg = $("<div class='errMsg'>至少3个字符</div>");
				alert("test");
				$(this).append(errMsg);
				$(this).animate({
					backgroundColor: Jquery.Color("red")
				},500);
			}else{
				$(this).animate({
					backgroundColor: Jquery.Color("green")
				},500);
			}
		}

		if ($(this).is("#email")){
			if (this.value=="" || this.value!="" && !/.+@.+\.[a-zA-Z]{2,4}$/.test(this.value)){
				var errMsg = $("<div class='errMsg'>请Email地址正确</div>")
				$(this).append(errMsg);
				$(this).animate({
					backgroundColor: Jquery.Color("red")
				},500);
			}else{
				$(this).animate({
					backgroundColor: Jquery.Color("green")
				},500);
			}
		}

		if ($(this).is("#password")){
			if (this.value=="" || this.value.length < 5){
				var errMsg = $("<div class='errMsg'>至少5个字符</div>");
				$(this).append(errMsg);
				$(this).animate({
					backgroundColor: Jquery.Color("red")
				},500);
			}else{
				$(this).animate({
					backgroundColor: Jquery.Color("green")
				},500);
			}
		}

		if ($(this).is("#pw2")){
			if (this.value != $("#password").get(0).value){
				var errMsg = $("<div class='errMsg'>密码不一致</div>");
				$(this).append(errMsg);
				$(this).animate({
					backgroundColor: Jquery.Color("red")
				},500);
			}else{
				$(this).animate({
					backgroundColor: Jquery.Color("green")
				},500);
			}
		}
	});
});
