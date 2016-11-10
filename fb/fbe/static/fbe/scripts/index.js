function changeIndexTipBtn(obj) {
	obj.css({"border":"2px #08423a solid"});
	obj.children(".btn_word").css({"color":"#08423a"});
	obj.children(".btn_deco").attr("src","images/deco1b.png");
}
function backIndexTipBtn (obj) {
	obj.css({"border":"2px white solid"});
	obj.children(".btn_word").css({"color":"white"});
	obj.children(".btn_deco").attr("src","images/deco1.png");
}
function changeIndexBottleBtn(obj) {
	obj.css({"border":"2px #08423a solid"});
	obj.children(".btn_word").css({"color":"#08423a"});
	obj.children(".btn_deco.l").attr("src","images/deco2b_l.png");
	obj.children(".btn_deco.r").attr("src","images/deco2b_r.png");
}
function backIndexBottleBtn (obj) {
	obj.css({"border":"2px white solid"});
	obj.children(".btn_word").css({"color":"white"});
	obj.children(".btn_deco.l").attr("src","images/deco2_l.png");
	obj.children(".btn_deco.r").attr("src","images/deco2_r.png");
}
function changeDarkTipBtn(obj) {
	obj.css({"border":"2px #04cbc5 solid"});
	obj.children(".btn_word").css({"color":"#04cbc5"});
	obj.children(".btn_deco").attr("src","images/deco1b_h.png");
}
function backDarkTipBtn (obj) {
	obj.css({"border":"2px #08423a solid"});
	obj.children(".btn_word").css({"color":"#08423a"});
	obj.children(".btn_deco").attr("src","images/deco1b.png");
}
function changeDarkBottleBtn (obj) {
	obj.css({"border":"2px #04cbc5 solid"});
	obj.children(".btn_word").css({"color":"#04cbc5"});
	obj.children(".btn_deco.l").attr("src","images/deco2b_l_h.png");
	obj.children(".btn_deco.r").attr("src","images/deco2b_r_h.png");
}
function backDarkBottleBtn (obj) {
	obj.css({"border":"2px #08423a solid"});
	obj.children(".btn_word").css({"color":"#08423a"});
	obj.children(".btn_deco.l").attr("src","images/deco2b_l.png");
	obj.children(".btn_deco.r").attr("src","images/deco2b_r.png");
}
function closeTip () {
	$(".tip").css({"visibility":"hidden"});
	$(".tip").find(".word.alert").css({"visibility":"hidden"});
}
function closeTip2 () {
	$(".tip.fail").css({"visibility":"hidden"});
	$(".tip.fail").find(".word.alert").css({"visibility":"hidden"});
}
function openSexTip () {
	$(".tip.sex_tip").css({"visibility":"visible"});
}
function openInformTip () {
	$(".tip.inform").css({"visibility":"visible"});
}
function openEmailTip () {
	$(".tip.email").css({"visibility":"visible"});
}

function loadInfo (pagecode,theUrl) {
	$.post(theUrl,{"type":pagecode},function(info,status){
			var oSex = info.o_sex;
			if (oSex == 0) {
				$("#obj_sex").text("男");
			} else{
				$("#obj_sex").text("女");
			};

			if (pagecode == 0) {
				/*sentence*/
				var content = info.type0;
				$("#obj_content").text(content);
			} else if (pagecode == 1) {
				var content = info.type1;
				$("#obj_content").text(content);
			} else {
				var email = info.type1_email;
				var content = info.type1;
				$("#obj_email").text(email);
				$("#obj_content").text(content);
				loadCipher();
			};
		});
}
function loadCipher () {
	/*alert($("#cipher").html());*/
	var ramNum = Math.floor(Math.random()*10);
	$("#cipher").html((chooseCipher(ramNum)));
}
function chooseCipher (code) {
	if (code == 0) {
		return "ta：这是你的益达吗<br>你：不，是你的益达"
	} else if (code == 1) {
		return "ta：今天天气好晴朗~~~~<br>你：处处好风光，好风光"
	} else if (code == 2) {
		return "ta：长江长江!我是黄河!<br>你：地瓜地瓜!我是土豆!"
	} else if (code == 3) {
		return "ta：奇变偶不变<br>你：符号看象限"
	} else if (code == 4) {
		return "ta：38324？<br>你：14122！"
	} else if (code == 5) {
		return "ta：齐楚秦燕赵魏韩？<br>你：东南西北到中央！"
	} else if (code == 6) {
		return "ta：团战可以输？<br>你：提莫必须死！"
	} else if (code == 7) {
		return "ta：取次花丛懒回顾<br>你：半缘修道半缘君"
	} else if (code == 8) {
		return "ta：生当复来归<br>你：死当长相思"
	} else {
		return "ta：有美人兮，见之不忘<br>你：一日不见兮，思之如狂"
	};
}


function checkThrow(theUrl) {
	var submitOK = true;
	var typeVal=$('input:radio[name="type"]:checked').val();
	var oSexVal=$('input:radio[name="o_sex"]:checked').val();
	var targetVal=$('input:radio[name="target"]:checked').val();
	var type0Val=$('textarea[name="type0"]').val().length;
	var type1EmailVal=$('input:text[name="type1_email"]').val().length;
	var type1Val=$('textarea[name="type1"]').val().length;

	if (oSexVal == null || targetVal == null) {
		$(".tip.fail").children(".word").text("你的信息不完善哦，请回去填写完整吧！");
		submitOK = false;	
	};

	if (typeVal == 0) {
		/*sentence*/
		if (type0Val == 0) {
			$(".tip.fail").children(".word").text("漂流瓶内空空如也哦，请回去写上你的一句话吧！");
			submitOK = false;
		};
	} else{
		if (type1EmailVal == 0 || type1Val == 0) {
			$(".tip.fail").children(".word").text("漂流瓶内空空如也哦，请回去写上你的邀约和邮箱吧！");
			submitOK = false;
		};
	};

	if (submitOK == false) {
		$(".tip.fail").css({"visibility":"visible"});
	} else {
		$(".tip.fail").css({"visibility":"hidden"});
		/*alert('success');*/
		$.post(theUrl,$("#theform").serialize(),function(code,status){
			if (status == 'success') {
				if (typeVal == 0) {
					/*sentence*/
					$(".tip.success.B").children(".word").text("一句话提交成功");
					$(".tip.success.B").css({"visibility":"visible"});
				} else{
					$(".tip.success.A").children(".email_address").text($('input:text[name="type1_email"]').val())
					$(".tip.success.A").css({"visibility":"visible"});
				};
			} else {
				$(".tip.fail").children(".word").text("抱歉，提交失败了，请重新提交");
				$(".tip.fail").css({"visibility":"visible"});
			};
		});
	};
}
function checkSex (theUrl,theUrl0,theUrl1) {
	var submitOK = true;
	var sSexVal = $('input:radio[name="s_sex"]:checked').val();
	if (sSexVal == null) {
		submitOK = false;
	};

	if (submitOK == false) {
		$(".word.alert").css({"visibility":"visible"});
	} else{
		$(".word.alert").css({"visibility":"hidden"});
		/*alert('success');*/
		$.post(theUrl,$("#theform").serialize(),function(code,status){
			goToget(theUrl0,theUrl1);
		});
	};
}
function checkEmail(theUrl) {
	var submitOK = true;
	var sEmailVal=$('input:text[name="s_email"]').val().length;
	if (sEmailVal == 0) {
		submitOK = false;	
	};

	if (submitOK == false) {
		$(".word.alert").css({"visibility":"visible"});
	} else {
		$(".word.alert").css({"visibility":"hidden"});
		$.post(theUrl,$("#theform").serialize(),function(code,status){
			if (code.error != '0') {
				$(".tip.fail").children(".word").text("抱歉，提交失败了，请重新提交");
				$(".tip.fail").css({"visibility":"visible"});
			} else{
				location.href = theUrl;
			};
		});
	};
}

function checkRadio (obj) {
	obj.parent().find(".opt_pic").css({"display":"inline-block"});
	obj.parent().find(".opt_pic.opt_h").css({"display":"none"});
	obj.parent().find("p").css({"color":"#08423a"});

	obj.find(".opt_pic").css({"display":"none"});
	obj.find(".opt_pic.opt_h").css({"display":"inline-block"});
	obj.find("p").css({"color":"#04cbc5"});
}
function changeUnfix (code) {
	if (code == 0) {
		/*sentence*/
		$(".unfix.invite").slideUp();
		$(".unfix.sentence").slideDown();		
	} else{
		$(".unfix.sentence").slideUp();
		$(".unfix.invite").slideDown();
	};
}

function goToget (theUrl0,theUrl1) {
	/*alert(theUrl0+theUrl1);*/
	var ramNum = Math.floor(Math.random()*2);
	/*alert(ramNum);*/
	if (ramNum == 0) {
		location.href = theUrl0;
	} else{
		location.href = theUrl1;
	};
}

(function() {
	function getCookie(name) {
	    var cookieValue = null;
	    if (document.cookie && document.cookie !== '') {
	        var cookies = document.cookie.split(';');
	        for (var i = 0; i < cookies.length; i++) {
	            var cookie = jQuery.trim(cookies[i]);
	            // Does this cookie string begin with the name we want?
	            if (cookie.substring(0, name.length + 1) === (name + '=')) {
	                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
	                break;
	            }
	        }
	    }
	    return cookieValue;
	}
	var csrftoken = getCookie('csrftoken');
	function csrfSafeMethod(method) {
	    // these HTTP methods do not require CSRF protection
	    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
	}
	$.ajaxSetup({
	    beforeSend: function(xhr, settings) {
	        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
	            xhr.setRequestHeader("X-CSRFToken", csrftoken);
	        }
	    }
	});
}).call(this);


function deleteItem(id) {
    alert ('aaa');
    $.ajax({
        type: "get",
        url: '/fbe/in_cancel/',
        data: {
            id: id
        },
        success: function (data) {
            if (data == 0) {
                console.log(id + "删除成功");
                $obj.html('删除成功');
            }
        }
    })
}

$('.content tbody tr').each(function () {
    $(this).find("td").eq(4).find('a').click(function () {
        var id = $(this).parent().siblings('td').eq(0).html();
        //if (id == "id") console.log(false);
        //else {
        deleteItem(id, $(this).parent());
        window.location.reload();
        //}
    });
})


function deleteItem(id) {
    //alert ('aaa');
    $.ajax({
        type: "get",
        url: '/fbe/one_cancel/',
        data: {
            id: id
        },
        success: function (data) {
            if (data == 0) {
                console.log(id + "删除成功");
                $obj.html('删除成功');
            }
        }
    })
}

$('.content tbody tr').each(function () {
    $(this).find("td").eq(2).find('a').click(function () {
        var id = $(this).parent().siblings('td').eq(0).html();
        //if (id == "id") console.log(false);
        //else {
        deleteItem(id, $(this).parent());
        window.location.reload();
        //}
    });
})
