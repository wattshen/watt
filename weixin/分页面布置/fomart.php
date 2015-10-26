  <?php
         //text fomart
   private function transmitText($postObj, $contentStr, $flag = 0)
              {
              	  $fromUsername = $postObj->FromUserName;
                  $toUsername = $postObj->ToUserName;
                  $msgType = "text";
                  $time = time();
                  $textTpl = "<xml>
                                   <ToUserName><![CDATA[%s]]></ToUserName>
                                   <FromUserName><![CDATA[%s]]></FromUserName>
                                   <CreateTime>%s</CreateTime>
                                   <MsgType><![CDATA[text]]></MsgType>
                                   <Content><![CDATA[%s]]></Content>
                                   <FuncFlag>%d</FuncFlag>
                             </xml>";
                  $resultStr = sprintf($textTpl, $fromUsername, $toUsername, $time, $contentStr, $flag);
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
 
?>
 