<?php
$z[0]=Array("global","",236,264);
$z[0][4]['name']="cfg_soft_lang";
$z[1]=Array("global","",277,303);
$z[1][4]['name']="cfg_webname";
$z[2]=Array("global","",347,377);
$z[2][4]['name']="cfg_description";
$z[3]=Array("global","",414,441);
$z[3][4]['name']="cfg_keywords";
$z[4]=Array("global","",459,491);
$z[4][4]['name']="cfg_templets_skin";
$z[5]=Array("global","",621,646);
$z[5][4]['name']="cfg_cmsurl";
$z[6]=Array("global","",738,764);
$z[6][4]['name']="cfg_cmspath";
$z[7]=Array("global","",851,883);
$z[7][4]['name']="cfg_templets_skin";
$z[8]=Array("global","",1467,1493);
$z[8][4]['name']="cfg_cmspath";
$z[9]=Array("include","",1596,1631);
$z[9][4]['filename']="head.htm";
$z[10]=Array("arclist","\r\n    <h2><a href=\"[field:arcurl/]\">[field:title/]</a></h2>\r\n    <p>[field:info/]...<a href=\"[field:arcurl/]\">[�鿴ȫ��]</a></p>\r\n    ",1776,1974);
$z[10][4]['flag']="h";
$z[10][4]['limit']="0,1";
$z[10][4]['infolen']="230";
$z[11]=Array("arclist","\r\n    <div class='d1arc'><a href=\"[field:arcurl/]\">[field:title/]</a></div>\r\n    ",2025,2156);
$z[11][4]['flag']="h";
$z[11][4]['limit']="1,4";
$z[12]=Array("arclist","\r\n    <li><a href=\"[field:arcurl/]\">[field:title/]</a></li>\r\n    ",2275,2399);
$z[12][4]['row']="14";
$z[12][4]['titlelen']="32";
$z[12][4]['noflag']="h";
$z[13]=Array("arclist","\r\nlinkarr[[field:global.autoindex/]] = \"[field:arcurl/]\";\r\npicarr[[field:global.autoindex/]]  = \"[field:litpic/]\";\r\ntextarr[[field:global.autoindex/]] = \"[field:title function='html2text(@me)'/]\";\r\n",2958,3202);
$z[13][4]['flag']="f";
$z[13][4]['row']="5";
$z[14]=Array("global","",3776,3806);
$z[14][4]['name']="cfg_templeturl";
$z[15]=Array("global","",4137,4167);
$z[15][4]['name']="cfg_templeturl";
$z[16]=Array("arclist","\r\n      <li><span>[field:pubdate function=\"MyDate('m-d',@me)\"/]</span><a href=\"[field:arcurl/]\">[field:title/]</a></li>\r\n      ",4736,4927);
$z[16][4]['flag']="a";
$z[16][4]['row']="6";
$z[16][4]['orderby']="pubdate";
$z[17]=Array("arclist","\r\n        <li><a href=\"[field:arcurl/]\">[field:image/]<span class=\"title\">[field:title/]</span></a></li>\r\n        ",5229,5440);
$z[17][4]['row']="10";
$z[17][4]['orderby']="pubdate";
$z[17][4]['type']="image.";
$z[17][4]['imgwidth']="143";
$z[17][4]['imgheight']="106";
$z[18]=Array("channelartlist","\r\n   <dl class=\"tbox\">\r\n    <dt><strong><a href=\"{dede:field name='typeurl'/}\">{dede:field name='typename'/}</a></strong><span class=\"more\"><a href=\"{dede:field name='typeurl'/}\">����...</a></span></dt>\r\n    <dd>\r\n     <ul class=\"d1 ico3\">\r\n      {dede:arclist titlelen='60' row='8'}\r\n      <li><span>[field:pubdate function=\"MyDate('m-d',@me)\"/]</span><a href=\"[field:arcurl /]\">[field:title /]</a></li>\r\n      {/dede:arclist}\r\n     </ul>\r\n    </dd>\r\n   </dl>\r\n   ",5561,6069);
$z[19]=Array("arclist","\r\n      <li> <a href=\"[field:arcurl/]\">[field:title/]</a> <span><small>���:</small>[field:click/]</span> <span><small>����:</small>[field:scores/]</span></li>\r\n      ",6502,6749);
$z[19][4]['orderby']="scores";
$z[19][4]['row']="8";
$z[19][4]['subday']="30";
$z[19][4]['titlelen']="42";
$z[20]=Array("feedback","\r\n      <li> <small><a href=\"#\" class=\"username\">[field:username function=\"(@me=='guest' ? '�ο�' : @me)\"/]</a> ���� <a href=\"[field:global.cfg_phpurl/]/feedback.php?aid=[field:aid/]\" class=\"title\">[field:title/]</a></small>\r\n       <p>[field:msg/]</p>\r\n      </li>\r\n      ",6851,7190);
$z[20][4]['row']="5";
$z[20][4]['titlelen']="24";
$z[20][4]['infolen']="80";
$z[21]=Array("global","",7364,7392);
$z[21][4]['name']="cfg_memberurl";
$z[22]=Array("php","\r\n        if(preg_match(\"#2#\", \$safe_gdopen))\r\n        {\r\n        echo '\r\n        <div class=\"fb\"><span>��֤��:</span>\r\n         <input type=\"text\" name=\"vdcode\" size=\"8\" class=\"ipt-txt\" />\r\n         <img id=\"vdimgck\" align=\"absmiddle\" onClick=\"this.src=this.src+\\'?\\'\" style=\"cursor:pointer;margin-left:0px;text-transform:uppercase;\" alt=\"�����壿�������\" src=\"'.\$cfg_cmspath.'/include/vdimgck.php\"/></div>\r\n        ';\r\n        }\r\n        ",7882,8344);
$z[23]=Array("global","",8454,8482);
$z[23][4]['name']="cfg_memberurl";
$z[24]=Array("global","",8544,8572);
$z[24][4]['name']="cfg_memberurl";
$z[25]=Array("memberlist","\r\n       <li><a href=\"[field:spaceurl/]\" target=\"_blank\"><img src=\"[field:face/]\" alt='[field:spacename/]' width=\"52\" height=\"52\" />[field:uname/]</a></li>\r\n       ",8859,9075);
$z[25][4]['row']="6";
$z[25][4]['signlen']="30";
$z[26]=Array("arclist","\r\n      <li class='dotline'><a href=\"[field:arcurl/]\">[field:title/]</a></li>\r\n      ",9381,9554);
$z[26][4]['flag']="c";
$z[26][4]['titlelen']="42";
$z[26][4]['row']="16";
$z[26][4]['tagid']="dedecms";
$z[26][4]['pagesize']="8";
$z[27]=Array("arclist","\r\n      <li class='dotline'><a href=\"[field:arcurl/]\">[field:title/]</a></li>\r\n      ",9786,9941);
$z[27][4]['sort']="hot";
$z[27][4]['subday']="30";
$z[27][4]['titlelen']="42";
$z[27][4]['row']="6";
$z[28]=Array("global","",10133,10158);
$z[28][4]['name']="cfg_cmsurl";
$z[29]=Array("flinktype","\r\n			<a href=\"#\" _for=\"flink_[field:id/]\">[field:typename/]</a> \r\n		",10370,10486);
$z[29][4]['type']="dedecms";
$z[30]=Array("flinktype","\r\n  <dd id=\"flink_[field:id/]\">\r\n    <ul class=\"f5\">\r\n		{dede:flink/}\r\n    </ul>\r\n  </dd>\r\n  ",10618,10759);
$z[30][4]['type']="dedecms";
$z[31]=Array("include","",10796,10833);
$z[31][4]['filename']="footer.htm";

?>