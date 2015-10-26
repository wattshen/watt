<?php
/**
 * ΢��API  www.netpopo.net
 */
 
//curl���� 
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

//utf8תgb����
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
	 * ��ȡACCESS TOKEN
	 */
	public function getAccessToken($AppId, $AppSecret)
	{		
		$cfg['ssl'] = true;
        $result = curlOpen("https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=$AppId&secret=$AppSecret", $cfg);
		return json_decode($result,true);
	}    
    
    /**
	 * ��Ӳ˵�
	 */
	public function creatMenu($menuArr, $accessToken)
	{			
        $cfg['post'] = json_encode2(gb2utf8($menuArr)); 
        $cfg['ssl'] = true;
        $result = curlOpen("https://api.weixin.qq.com/cgi-bin/menu/create?access_token=".$accessToken, $cfg);
		return json_decode($result,true);
	}
    
    /**
	 * ��ѯ�˵�
	 */
	public function getMenu($accessToken)
	{	
        $cfg['ssl'] = true;	   
        $result = curlOpen("https://api.weixin.qq.com/cgi-bin/menu/get?access_token=".$accessToken, $cfg);
		return utf82gb(json_decode($result,true));
	}
    
    /**
	 * ɾ���˵�
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
$menuArr['button'][] = array('name'=>'��������', 'sub_button'=>array(array('type'=>'click', 'name'=>'��վ����', 'key'=>'WEBSITE'),array('type'=>'click', 'name'=>'wapվ����', 'key'=>'WAP'),array('type'=>'click', 'name'=>'app����', 'key'=>'APP'),array('type'=>'click', 'name'=>'΢վ����', 'key'=>'SITE'),array('type'=>'click', 'name'=>'΢�ӿڷ���', 'key'=>'API')));
$menuArr['button'][] = array('name'=>'���²�Ʒ', 'sub_button'=>array(array('type'=>'click', 'name'=>'��ַ����', 'key'=>'NAVSIE'),array('type'=>'click', 'name'=>'��������', 'key'=>'TOO'),array('type'=>'click', 'name'=>'��ͨ����', 'key'=>''),array('type'=>'click', 'name'=>'�ֻ���Ϸ', 'key'=>'GAME'),array('type'=>'click', 'name'=>'�����Ա�', 'key'=>'OU')));
$menuArr['button'][] = array('name'=>'��������', 'sub_button'=>array(array('type'=>'click', 'name'=>'���н���', 'key'=>'ABOUT'),array('type'=>'click', 'name'=>'�ͷ�QQ', 'key'=>'QQ'),array('type'=>'click', 'name'=>'��ϵ��ַ', 'key'=>'ADDRESS'),array('type'=>'click', 'name'=>'��˾��վ', 'key'=>'WEBURL'),array('type'=>'click', 'name'=>'�������', 'key'=>'ARTNER')));
var_dump($weixin->creatMenu($menuArr, $tokenarr['access_token']));
var_dump($weixin->getMenu($tokenarr['access_token']));


