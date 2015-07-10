$(document).ready(function(){
	alert("文档加载完毕");
	$("h6").click(function(){
		$(this).hide();
	});
	
	$("button").click(function(){
		$("h1").text("修改后的 标题一");
		$("#p1").text("修改后的 hello1");
		$(".p2").text("修改后的 hello2");
		$("button").on("click",clickHandle1);
		$("button").bind("click",clickHandle2);
		$("button").on("click",clickHandle3);
		$("button").off("click",clickHandle1);
		$("button").unbind("click",clickHandle2);

	});
});

function clickHandle1(e){
console.log("clickHandle1");
}
function clickHandle2(e){
console.log("clickHandle2");
}
function clickHandle3(e){
console.log("clickHandle3");
}