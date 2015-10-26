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
          			}else
                      {
          				return false;
       			      }
          	}
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
}

?>