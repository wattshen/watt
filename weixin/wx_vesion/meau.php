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
            "name":"茶话天下",
           "sub_button":[
            {
               "type":"click",
               "name":"茶话天下a",
               "key":"茶话天下a"
            },
            {
               "type":"click",
               "name":"茶话天下b",
               "key":"茶话天下b"
            },
            {
               "type":"click",
               "name":"茶话天下c",
               "key":"茶话天下c"
            },
            {
               "type":"click",
               "name":"茶话天下d",
               "key":"茶话天下d"
            },
            {
                "type":"view",
                "name":"本地天气",
                "url":"http://m.hao123.com/a/tianqi"
            }]
      

       },
       {
           "name":"玉壶春茶",
           "sub_button":[
            {
               "type":"click",
               "name":"我的订单",
               "key":"company"
            },
            {
               "type":"click",
               "name":"春茶",
               "key":"春茶"
            },
            {
                "type":"click",
                "name":"玉壶",
                "key":"玉壶"
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