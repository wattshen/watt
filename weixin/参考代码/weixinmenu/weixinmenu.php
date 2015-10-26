<?php
/**
 * 微信API  www.netpopo.net
 */
 
//curl函数 
function curlOpen($url, $cfg)
{
	$ch = curl_init();	
	curl_setopt($ch, CURLOPT_URL, $url);
	curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
	curl_setopt($ch, CURLOPT_HEADER, 0);
	if($cfg['ssl'])
    {
        curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
        curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, false);
    }
	$result = curl_exec($ch);	
	curl_close($ch);
	return $result;
}

function recursive_iconv($in_charset, $out_charset, $arr)
{ 
    if (!is_array($arr)){ 
        return iconv($in_charset, $out_charset, $arr); 
    } 
    $ret = $arr;
    array_walk_recursive($ret, "array_iconv", array($in_charset, $out_charset)); 
    return $ret; 
}

//utf8转gb函数
function utf82gb($utfstr)
{   
    return recursive_iconv('utf-8','gbk//ignore',$utfstr);
}

class Weixin
{  
    var $token;   
    
    function __construct()
    {   
    }  
    
    /**
	 * 获取ACCESS TOKEN
	 */
	public function getAccessToken($AppId, $AppSecret)
	{		
		$cfg['ssl'] = true;
        $result = curlOpen("https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=$AppId&secret=$AppSecret", $cfg);
		return json_decode($result,true);
	}    
    
    /**
	 * 添加菜单
	 */
	public function creatMenu($menuArr, $accessToken)
	{			
        $cfg['post'] = json_encode2(gb2utf8($menuArr)); 
        $cfg['ssl'] = true;
        $result = curlOpen("https://api.weixin.qq.com/cgi-bin/menu/create?access_token=".$accessToken, $cfg);
		return json_decode($result,true);
	}
    
    /**
	 * 查询菜单
	 */
	public function getMenu($accessToken)
	{	
        $cfg['ssl'] = true;	   
        $result = curlOpen("https://api.weixin.qq.com/cgi-bin/menu/get?access_token=".$accessToken, $cfg);
		return utf82gb(json_decode($result,true));
	}
    
    /**
	 * 删除菜单
	 */
	public function delMenu($accessToken)
	{			
        $cfg['ssl'] = true;
        $result = curlOpen("https://api.weixin.qq.com/cgi-bin/menu/delete?access_token=".$accessToken, $cfg);
		return json_decode($result,true);
	}
        
}    



define("APPID", "wx8e6567eed9bacb0e");//AppId
define("APPSECRET", "8fb85851f0dadd8e7ba05c9af2ccd7a6");//AppSecret

$weixin = new Weixin();
$tokenarr = $weixin->getAccessToken(APPID, APPSECRET);
$menuArr['button'][] = array('name'=>'服务内容', 'sub_button'=>array(array('type'=>'click', 'name'=>'网站建设', 'key'=>'WEBSITE'),array('type'=>'click', 'name'=>'wap站建设', 'key'=>'WAP'),array('type'=>'click', 'name'=>'app开发', 'key'=>'APP'),array('type'=>'click', 'name'=>'微站开发', 'key'=>'SITE'),array('type'=>'click', 'name'=>'微接口服务', 'key'=>'API')));
$menuArr['button'][] = array('name'=>'旗下产品', 'sub_button'=>array(array('type'=>'click', 'name'=>'网址导航', 'key'=>'NAVSIE'),array('type'=>'click', 'name'=>'生活助手', 'key'=>'TOO'),array('type'=>'click', 'name'=>'交通出行', 'key'=>''),array('type'=>'click', 'name'=>'手机游戏', 'key'=>'GAME'),array('type'=>'click', 'name'=>'购物淘宝', 'key'=>'OU')));
$menuArr['button'][] = array('name'=>'关于我们', 'sub_button'=>array(array('type'=>'click', 'name'=>'网尚介绍', 'key'=>'ABOUT'),array('type'=>'click', 'name'=>'客服QQ', 'key'=>'QQ'),array('type'=>'click', 'name'=>'联系地址', 'key'=>'ADDRESS'),array('type'=>'click', 'name'=>'公司网站', 'key'=>'WEBURL'),array('type'=>'click', 'name'=>'合作伙伴', 'key'=>'ARTNER')));
var_dump($weixin->creatMenu($menuArr, $tokenarr['access_token']));
var_dump($weixin->getMenu($tokenarr['access_token']));


