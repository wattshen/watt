<?php


$appid = "wx8e6567eed9bacb0e";
$appsecret = "8fb85851f0dadd8e7ba05c9af2ccd7a6";
$url = "https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=$appid&secret=$appsecret";

$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, $url);
curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, FALSE); 
curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, FALSE); 
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
$output = curl_exec($ch);
curl_close($ch);
$jsoninfo = json_decode($output, true);
$access_token = $jsoninfo["access_token"];


$jsonmenu = '{
      "button":[
      {
            "name":"�軰����",
           "sub_button":[
            {
               "type":"click",
               "name":"�軰����a",
               "key":"�軰����a"
            },
            {
               "type":"click",
               "name":"�軰����b",
               "key":"�軰����b"
            },
            {
               "type":"click",
               "name":"�軰����c",
               "key":"�軰����c"
            },
            {
               "type":"click",
               "name":"�軰����d",
               "key":"�軰����d"
            },
            {
                "type":"view",
                "name":"��������",
                "url":"http://m.hao123.com/a/tianqi"
            }]
      

       },
       {
           "name":"�������",
           "sub_button":[
            {
               "type":"click",
               "name":"�ҵĶ���",
               "key":"company"
            },
            {
               "type":"click",
               "name":"����",
               "key":"����"
            },
            {
                "type":"click",
                "name":"���",
                "key":"���"
            }]
       

       }]
 }';


$url = "https://api.weixin.qq.com/cgi-bin/menu/create?access_token=".$access_token;
$result = https_request($url, $jsonmenu);
var_dump($result);

function https_request($url,$data = null){
    $curl = curl_init();
    curl_setopt($curl, CURLOPT_URL, $url);
    curl_setopt($curl, CURLOPT_SSL_VERIFYPEER, FALSE);
    curl_setopt($curl, CURLOPT_SSL_VERIFYHOST, FALSE);
    if (!empty($data)){
        curl_setopt($curl, CURLOPT_POST, 1);
        curl_setopt($curl, CURLOPT_POSTFIELDS, $data);
    }
    curl_setopt($curl, CURLOPT_RETURNTRANSFER, 1);
    $output = curl_exec($curl);
    curl_close($curl);
    return $output;
}

?>