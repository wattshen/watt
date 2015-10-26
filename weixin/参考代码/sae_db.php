<?php

show_source('wx.php');

show_source('sae_db.php');

header("Content-Type:text/html;charset=utf-8"); 
echo "用户名:".SAE_MYSQL_USER."<br>";
echo "密码:". SAE_MYSQL_PASS.'<br>';
echo "主库域名:".SAE_MYSQL_HOST_M."<br>";
echo "从库域名:".SAE_MYSQL_HOST_S."<br>";
echo "端口".SAE_MYSQL_PORT."<br>";
echo "数据库名:".SAE_MYSQL_DB."<br>";


$mysql = new SaeMysql();

//insert data
for($i = 1;$i < 11;$i++)
{
        $timeline = date('Y-m-d H:i:s',time());
        $content = 'This num is'.$i;
        $sql = "insert into mysqldemo(content,timeline)values('$content','$timeline')";
        $mysql->runSql($sql);
}
//close db connection
//$mysql->closeDb();


//查询单条数据
$sql = "select * from mysqldemo limit 1";
$result = $mysql->getLine($sql);
var_dump($result);
//发现这个已经是按数组的方式返回的
echo "<hr>";
//查询多条数据
$sql = "select * from mysqldemo";
$mut_data = $mysql->getData($sql);
var_dump($mut_data);
//发现这个就是按二维数组输出的了，下面一个foreach输出
echo "<hr>";
foreach($mut_data as $small)
{
        echo "No ".$small['id']." Content:".$small['content'].' Timeline:'.$small['timeline'].'<br>';
}
    
?>