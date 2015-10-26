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
                    	       	$contentStr = "����һ���ı���Ϣ������������ı���"."$keyword"."     Say \"Happy Valentine's Day\" to my �� "."--Design by Watt";
                    	       	$resultStr = $this->transmitText($postObj, $contentStr); 
                    	       	return $resultStr;
                    	}else if($keyword == "tw")
                    	{
            					$dateArray = array();
            					$dateArray[] = array("Title"=>"��ͼ�ı���", 
                                					"Description"=>"��ͼ������", 
                               						"Picurl"=>"http://yuhuc.sinaapp.com/index.php?=PHPE9568F34-D428-11d2-A769-00AA001ACF42", 
                              						"Url" =>"http://yuhuc.sinaapp.com/");
           						$resultStr = $this->transmitNews($postObj, $dateArray);
           						return $resultStr;
        				}else if($keyword == "dtw")
        				{
                                $dateArray = array();
                                $dateArray[] = array("Title"=>"��ͼ��1����",
                               						"Description"=>"",
                               						"Picurl"=>"http://discuz.comli.com/weixin/weather/icon/cartoon.jpg",
                                 					"Url" =>"http://m.cnblogs.com/?u=txw1958");
                                $dateArray[] = array("Title"=>"��ͼ��2����",
                                					"Description"=>"",
                                 					"Picurl"=>"http://d.hiphotos.bdimg.com/wisegame/pic/item/f3529822720e0cf3ac9f1ada0846f21fbe09aaa3.jpg",
                                					"Url" =>"http://m.cnblogs.com/?u=txw1958");
                                $dateArray[] = array("Title"=>"��ͼ��3����",
                                 					"Description"=>"",
                                 				"Picurl"=>"http://g.hiphotos.bdimg.com/wisegame/pic/item/18cb0a46f21fbe090d338acc6a600c338644adfd.jpg",
                                   					"Url" =>"http://m.cnblogs.com/?u=txw1958");
                                $resultStr = $this->transmitNews($postObj, $dateArray);
           											return $resultStr;
  						}else if($keyword == "yy")
      					{
                                $musicArray = array("Title"=>"���������",
                                					"Description"=>"���֣���˴���",
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
                          $contentStr = "��ӭ��ע�������";
                          break;
                      case "unsubscribe":
                          $contentStr = "";
                          break;
                      case "CLICK":
                          switch ($object->EventKey)
                          {
                              default:
                                    $contentStr = "�����˲˵�: ".$object->EventKey;
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
                  $contentStr = "�㷢�͵�����Ƶ��ý��IDΪ��".$object->MediaId;
                  $resultStr = $this->transmitText($object, $contentStr, $funcFlag);
                  return $resultStr;
              }
              
         private function receiveImage($object)
              {
                  $funcFlag = 0;
                  $contentStr = "�㷢�͵���ͼƬ����ַΪ��".$object->PicUrl;
                  $resultStr = $this->transmitText($object, $contentStr, $funcFlag);
                  return $resultStr;
              }     
         private function receiveLocation($object)
              {
                    $funcFlag = 0;
    				$contentStr = "�㷢�͵���λ�ã�γ��Ϊ��".$object->Location_X."������Ϊ��".$object->Location_Y."�����ż���Ϊ��".$object->Scale."��λ��Ϊ��".$object->Label;
                    $resultStr = $this->transmitText($object, $contentStr, $funcFlag);
		          return $resultStr;
		      }     

         private function receiveLink($object)
              {
                  $funcFlag = 0;
                  $contentStr = "�㷢�͵������ӣ�����Ϊ��".$object->Title."������Ϊ��".$object->Description."�����ӵ�ַΪ��".$object->Url;
                  $resultStr = $this->transmitText($object, $contentStr, $funcFlag);
                  return $resultStr;
              }  
 
//***********************************echo fomart************************************
       //text fomart
         private function transmitText($postObj, $contentStr)
              {

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
                  $resultStr = sprintf($textTpl, $postObj->FromUserName, $postObj->ToUserName, $time, $contentStr);
                  return $resultStr;
              }
              
        //picture & text fomart      
        private function transmitNews($postObj, $arr_item, $flag = 0)
                   {
                       if(!is_array($arr_item))
                       {
                           return;
                       }else
                       {
                       $itemTpl = "<item>
                                        <Title><![CDATA[%s]]></Title>
                                        <Description><![CDATA[%s]]></Description>
                                        <PicUrl><![CDATA[%s]]></PicUrl>
                                        <Url><![CDATA[%s]]></Url>
         					     </item>";
                       $item_str = "";
                       foreach ($arr_item as $item)
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