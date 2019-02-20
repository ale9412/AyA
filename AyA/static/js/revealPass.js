var selectInput = document.getElementById('Selection');
var button = document.getElementById('buttonSelector');

if (selectInput.value === "") {
	button.setAttribute('disabled',"");
	}else{
		button.removeAttribute('disabled',"")
	}
selectInput.addEventListener("change",function(){
	if (selectInput.value === ""){
	button.setAttribute('disabled',"");
	}else{
		button.removeAttribute('disabled',"")
	};
})

function mdown(obj) {
	obj.src = "/static/img/glyphicons-halflings-26-eye-off@2x.png";
	obj.parentElement.firstElementChild.type = "text";
}
function mup(obj) {
		obj.src = "/static/img/glyphicons-halflings-25-eye%402x.png";
		obj.parentElement.firstElementChild.type = "password";
	}

function showIcon(obj) {
	var img = obj.nextElementSibling
	if (obj.value === "") {
		img.style.visibility = "hidden";
	} else {
		img.style.visibility = "visible";
	};
}
