<?php
		
      	 public function receiveText($postObj)
                {
                       $keyword = trim($postObj->Content);
     					if($keyword == "wb")
                    	{
                    		$contentStr = "����һ���ı���Ϣ������������ı���"."$keyword";
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
 

?>