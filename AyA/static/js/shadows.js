function iniciar(){
		window.addEventListener('mousemove', shadow, false);
}
function shadow(e){
		var shadowText = document.getElementById('shadowMove');
		var posElement = shadowText.getBoundingClientRect();
		var xmouse = e.clientX;
		var ymouse = e.clientY;
		var xcenter = posElement.x + posElement.width/2;
		var ycenter = posElement.y + posElement.height/2;
		var xshadow = Math.round((xcenter-xmouse)*0.01);
		var yshadow = Math.round((ycenter-ymouse)*0.015);
		shadowText.style.textShadow=xshadow+"px "+yshadow+"px 3px #8a5353";
		//test.innerHTML = xmouse +"x "+ymouse +"y";
}

window.addEventListener("load", iniciar, false);