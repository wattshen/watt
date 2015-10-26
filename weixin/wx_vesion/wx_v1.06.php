<?php
	/*
	* wechat php test
	*/

define("TOKEN", "abc123");

$wechatObj = new wechatCallbackapiTest();
//$wechatObj->valid();
$wechatObj->responseMsg();

class wechatCallbackapiTest
{
   			 public function valid()
              {
                  $echoStr = $_GET["echostr"];
                  //valid signature , option
                  if($this->checkSignature()){
                  	echo $echoStr;
                  	exit;
                  }
              }
              
         private function checkSignature()
          	{
                  $signature = $_GET["signature"];
                  $timestamp = $_GET["timestamp"];
                  $nonce = $_GET["nonce"];
                 	$token = TOKEN;
          				$tmpArr = array($token, $timestamp, $nonce);
          				sort($tmpArr);
          				$tmpStr = implode( $tmpArr );
          				$tmpStr = sha1( $tmpStr );
          		if( $tmpStr == $signature )
          			{
          				return true;
          			}else{
          						return false;
          					 }
          	}
           
//*******************Follow seg by msgtype********************       
      
         public function responseMsg()
          {
              $postStr = $GLOBALS["HTTP_RAW_POST_DATA"];
              if (!empty($postStr))
              {
                       $postObj = simplexml_load_string($postStr, 'SimpleXMLElement', LIBXML_NOCDATA);
                       $RX_TYPE = trim($postObj->MsgType);
                  switch ($RX_TYPE)
                  {
                      case "text":
                          $resultStr = $this->receiveText($postObj);
                          break;
                      case "image":
                          $resultStr = $this->receiveImage($postObj);
                          break;
                      case "location":
                          $resultStr = $this->receiveLocation($postObj);
                          break;
                      case "voice":
                          $resultStr = $this->receiveVoice($postObj);
                          break;
                      case "video":
                          $resultStr = $this->receiveVideo($postObj);
                          break;
                      case "link":
                          $resultStr = $this->receiveLink($postObj);
                          break;
                      case "event":
                          $resultStr = $this->receiveEvent($postObj);
                          break;
                      default:
                          $resultStr = "unknow msg type: ".$RX_TYPE;
                          break;
                  }
                  		echo $resultStr;
              }else {
                  		echo "";
                  		exit;
              			}
          }
                          

 //******************Follow process by msgtype*************************

				
      	 public function receiveText($postObj)
                {
                       $keyword = trim($postObj->Content);
     					if($keyword == "wb")
                    	{
                    	       	$contentStr = "这是一个文本消息，您所输入的文本是"."$keyword";
                    	       	$resultStr = $this->transmitText($postObj, $contentStr); 
                    	       	return $resultStr;
                    	}else if($keyword == "tw")
                    	{
            					$dateArray = array();
            					$dateArray[] = array("Title"=>"单图文标题", 
                                					"Description"=>"单图文内容", 
                               						"Picurl"=>"http://yuhuc.sinaapp.com/index.php?=PHPE9568F34-D428-11d2-A769-00AA001ACF42", 
                              						"Url" =>"http://yuhuc.sinaapp.com/");
           						$resultStr = $this->transmitNews($postObj, $dateArray);
           						return $resultStr;
        				}else if($keyword == "dtw")
        				{
                                $dateArray = array();
                                $dateArray[] = array("Title"=>"多图文1标题",
                               						"Description"=>"",
                               						"Picurl"=>"http://discuz.comli.com/weixin/weather/icon/cartoon.jpg",
                                 					"Url" =>"http://m.cnblogs.com/?u=txw1958");
                                $dateArray[] = array("Title"=>"多图文2标题",
                                					"Description"=>"",
                                 					"Picurl"=>"http://d.hiphotos.bdimg.com/wisegame/pic/item/f3529822720e0cf3ac9f1ada0846f21fbe09aaa3.jpg",
                                					"Url" =>"http://m.cnblogs.com/?u=txw1958");
                                $dateArray[] = array("Title"=>"多图文3标题",
                                 					"Description"=>"",
                                 					"Picurl"=>"http://g.hiphotos.bdimg.com/wisegame/pic/item/18cb0a46f21fbe090d338acc6a600c338644adfd.jpg",
                                   					"Url" =>"http://m.cnblogs.com/?u=txw1958");
                                $resultStr = $this->transmitNews($postObj, $dateArray);
           											return $resultStr;
  						}else if($keyword == "yy")
      					{
                                $musicArray = array("Title"=>"最炫民族风",
                                					"Description"=>"歌手：凤凰传奇",
                                 					"MusicUrl"=>"http://121.199.4.61/music/zxmzf.mp3",
                                 					"HQMusicUrl"=>"http://121.199.4.61/music/zxmzf.mp3");
                                $resultStr = $this->transmitMusic($postObj, $musicArray);
                                return $resultStr;
       					}
                }
                
         private function receiveEvent($object)
              {
                  $contentStr = "";
                  switch ($object->Event)
                  {
                      case "subscribe":
                          $contentStr = "欢迎关注玉壶春茶";
                          break;
                      case "unsubscribe":
                          $contentStr = "";
                          break;
                      case "CLICK":
                          switch ($object->EventKey)
                          {
                              default:
                                    $contentStr = "你点击了菜单: ".$object->EventKey;
                                     break;
                          }
                          break;
                      default:
                          $contentStr = "receive a new event: ".$object->Event;
                          break;
                  }
                     $resultStr = $this->transmitText($object, $contentStr);
                     return $resultStr;
              }
              
         private function receiveVideo($object)
              {
                  $funcFlag = 0;
                  $contentStr = "你发送的是视频，媒体ID为：".$object->MediaId;
                  $resultStr = $this->transmitText($object, $contentStr, $funcFlag);
                  return $resultStr;
              }
              
         private function receiveImage($object)
              {
                  $funcFlag = 0;
                  $contentStr = "你发送的是图片，地址为：".$object->PicUrl;
                  $resultStr = $this->transmitText($object, $contentStr, $funcFlag);
                  return $resultStr;
              }     
         private function receiveLocation($object)
              {
                    $funcFlag = 0;
    				$contentStr = "你发送的是位置，纬度为：".$object->Location_X."；经度为：".$object->Location_Y."；缩放级别为：".$object->Scale."；位置为：".$object->Label;
                    $resultStr = $this->transmitText($object, $contentStr, $funcFlag);
		          return $resultStr;
		      }     

         private function receiveLink($object)
              {
                  $funcFlag = 0;
                  $contentStr = "你发送的是链接，标题为：".$object->Title."；内容为：".$object->Description."；链接地址为：".$object->Url;
                  $resultStr = $this->transmitText($object, $contentStr, $funcFlag);
                  return $resultStr;
              }  
 
//***********************************echo fomart************************************
       //text fomart
         private function transmitText($postObj, $contentStr)
              {
                  $postStr = $GLOBALS["HTTP_RAW_POST_DATA"];
              	  $fromUsername = $postObj->FromUserName;
                  $toUsername = $postObj->ToUserName;
                  $time = time();
                  $textTpl = "<xml>
                                   <ToUserName><![CDATA[%s]]></ToUserName>
                                   <FromUserName><![CDATA[%s]]></FromUserName>
                                   <CreateTime>%s</CreateTime>
                                   <MsgType><![CDATA[text]]></MsgType>
                                   <Content><![CDATA[%s]]></Content>
                             </xml>";
                  $resultStr = sprintf($textTpl, $fromUsername, $toUsername, $time, $contentStr);
                  return $resultStr;
              }
              
        //picture & text fomart      
        private function transmitNews($postObj, $arr_item, $flag = 0)
                   {
                       if(!is_array($arr_item))
                       {
                           return;
                       }elseif
                       {
                       $itemTpl = "<item>
                                        <Title><![CDATA[%s]]></Title>
                                        <Description><![CDATA[%s]]></Description>
                                        <PicUrl><![CDATA[%s]]></PicUrl>
                                        <Url><![CDATA[%s]]></Url>
         					     </item>";
                       $item_str = "";
                       foreach ($arr_item as $item);
                       $item_str = sprintf($itemTpl, $item['Title'], $item['Description'], $item['Picurl'], $item['Url']);
                       $newsTpl = "<xml>
                                        <ToUserName><![CDATA[%s]]></ToUserName>
                                        <FromUserName><![CDATA[%s]]></FromUserName>
                                        <CreateTime>%s</CreateTime>
                                        <MsgType><![CDATA[news]]></MsgType>
                                        <Content><![CDATA[]]></Content>
                                        <ArticleCount><![CDATA[%s]]></ArticleCount>
                                        <Articles><![CDATA[%s]]></Articles>
                                        <FuncFlag>%d</FuncFlag>
                                  </xml>";
                       $resultStr = sprintf($newsTpl, $postObj->FromUserName, $postObj->ToUserName, time(), count($arr_item), $item_str, $flag);
                       return $resultStr;
                       }
                   }
         
         //muisc fomart          
         private function transmitMusic($object, $musicArray, $flag = 0)
                        {
                            $itemTpl = "<Music>
                                            <Title><![CDATA[%s]]></Title>
                                            <Description><![CDATA[%s]]></Description>
                                            <MusicUrl><![CDATA[%s]]></MusicUrl>
                                            <HQMusicUrl><![CDATA[%s]]></HQMusicUrl>
                    					</Music>";
							$item_str = sprintf($itemTpl, $musicArray['Title'], $musicArray['Description'], $musicArray['MusicUrl'], $musicArray['HQMusicUrl']);
							$textTpl = "<xml>
                                             <ToUserName><![CDATA[%s]]></ToUserName>
                                             <FromUserName><![CDATA[%s]]></FromUserName>
                                             <CreateTime>%s</CreateTime>
                                             <MsgType><![CDATA[music]]></MsgType>
                                             $item_str
                                             <FuncFlag>%d</FuncFlag>
                                      </xml>";
                            $resultStr = sprintf($textTpl, $object->FromUserName, $object->ToUserName, time(), $flag);
                            return $resultStr;
                        }  
 
 
 

}

?>