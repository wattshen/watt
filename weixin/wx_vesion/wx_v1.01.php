<?php
/**
  * wechat php test
  */

//define your token
define("TOKEN", "weixin");
/*
define 是用来给常量赋值的函数，这句话的意思是赋予“TOKEN”这个常量值为“weixin”。TOKEN 是用来进行交互安全认证的，开发者可以随意定义，要和公众平台里设置的一样。
*/

$wechatObj = new wechatCallbackapiTest();//创建实例对象
$wechatObj->valid();//调用类的valid()方法执行接口验证，接口设置成功后将其注释掉。


class wechatCallbackapiTest//声明一个类 wechatCallbackapiTest，该类中包含有三个方法（函数）。
{
	public function valid()//用于申请 成为开发者 时向微信发送验证信息。
    {
        $echoStr = $_GET["echostr"];//随机字符串

        //valid signature , option
        if($this->checkSignature()){
        	echo $echoStr;
        	exit;
        }
    }

    public function responseMsg()//处理并回复用户发送过来的消息，也是用的最多的一个函数，几乎所有的功能都在这里实现
    {
		//get post data, May be due to the different environments
		$postStr = $GLOBALS["HTTP_RAW_POST_DATA"];//接收微信公众平台发送过来的用户消息，该消息数据结构为XML，不是php默认的识别数据类型，因此这里用了$GLOBALS['HTTP_RAW_POST_DATA']来接收，同时赋值给了$postStr
      	//extract post data
		if (!empty($postStr)){
                
              	$postObj = simplexml_load_string($postStr, 'SimpleXMLElement', LIBXML_NOCDATA);//使用simplexml_load_string() 函数将接收到的XML消息数据载入对象$postObj中。这个严谨的写法后面还得加个判断是否载入成功的条件语句，不过不写也没事。
                $fromUsername = $postObj->FromUserName;//将对象$postObj中的发送消息用户的OPENID赋值给$fromUsername变量
                $toUsername = $postObj->ToUserName;//将对象$postObj中的公众账号的ID赋值给$toUsername变量
                $keyword = trim($postObj->Content);//trim() 函数从字符串的两端删除空白字符和其他预定义字符，这里就可以得到用户输入的关键词
                $time = time();//time() 函数返回当前时间的 Unix 时间戳，即自从 Unix 纪元（格林威治时间 1970 年 1 月 1 日 00:00:00）到当前时间的秒数。
                $textTpl = "<xml>
							<ToUserName><![CDATA[%s]]></ToUserName>
							<FromUserName><![CDATA[%s]]></FromUserName>
							<CreateTime>%s</CreateTime>
							<MsgType><![CDATA[%s]]></MsgType>
							<Content><![CDATA[%s]]></Content>
							<FuncFlag>0</FuncFlag>
							</xml>";
				//$textTpl是存放微信输出内容的模板
				if(!empty( $keyword ))
                {
				//使用sprintf() 函数将格式化的数据写入到变量中去;$fromUsername, $toUsername, $time, $msgType, $contentStr 分别顺序替换模板里“%s”位置
              		$msgType = "text";
                	$contentStr = "Welcome to wechat world!";
                	$resultStr = sprintf($textTpl, $fromUsername, $toUsername, $time, $msgType, $contentStr);
                	echo $resultStr;
                }else{
                	echo "Input something...";
                }

        }else {
        	echo "";
        	exit;
        }
    }

	private function checkSignature()
//开发者通过检验signature对请求进行校验（下面有校验方式）。若确认此次GET请求来自微信服务器，请求原样返回echostr参数内容，则接入生效，否则接入失败。
	{
        $signature = $_GET["signature"];//微信加密签名
        $timestamp = $_GET["timestamp"];//时间戳
        $nonce = $_GET["nonce"];//随机数
        		
		$token = TOKEN;
		$tmpArr = array($token, $timestamp, $nonce);
		sort($tmpArr);//进行字典序排序
		$tmpStr = implode( $tmpArr );
		$tmpStr = sha1( $tmpStr );
		//sha1加密后与签名对比
		if( $tmpStr == $signature ){
			return true;
		}else{
			return false;
		}
	}
}

?>