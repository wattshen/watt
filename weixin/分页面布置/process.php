<?php
		
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
 

?>