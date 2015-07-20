var xiaowang=(function(argument){
	var xiaowangjia=funcgion(){
	
	
	}
	var men;
	var info={
		sendMessage:function(){
			if(!men){
				men=new xiaowangjia(message);
			};
			return men;
		}
	};
	return info;
})();


var xiaoli={
	callXiaowang:function(){
		var _xw=xiaowang.sendMessage();
		alert(_xw.menling);
		_xw=null;
	}
};

xiaoli.callXiaowang('didi');