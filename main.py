from cgitb import reset
from re import U
from PtSites import Siteinfo
from PtSites import PtSites
from DB import DB
import pymysql
import requests
from lxml import etree
import time


html = """"
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml"><head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<meta name="generator" content="NexusPHP">
<title>PT时间 :: 种子 - Powered by NexusPHP</title>
<link rel="shortcut icon" href="favicon.ico" type="image/x-icon">
<link rel="search" type="application/opensearchdescription+xml" title="PT时间 Torrents" href="opensearch.php">
<link rel="stylesheet" href="styles/mediumfont.css" type="text/css">
<link rel="stylesheet" href="styles/sprites.css" type="text/css">
<link rel="stylesheet" href="pic/forum_pic/chs/forumsprites.css" type="text/css">
<link rel="stylesheet" href="styles/PTtimeBlack/theme.css" type="text/css">
<link rel="stylesheet" href="styles/PTtimeBlack/DomTT.css" type="text/css">
<link rel="stylesheet" href="styles/curtain_imageresizer.css" type="text/css">
<link rel="stylesheet" href="styles/common.css" type="text/css">
<!-- ali_icon_xiugai -->
<link rel="stylesheet" href="//at.alicdn.com/t/font_1856866_569kkrcjsot.css" type="text/css">
<link rel="stylesheet" href="styles/mp.css" type="text/css">
<link rel="stylesheet" href="pic/category/chd/scenetorrents/catsprites.css" type="text/css">
<link rel="alternate" type="application/rss+xml" title="Latest Torrents" href="torrentrss.php">
<script type="text/javascript" src="js/jquery-1.11.3.min.js"></script>
<script type="text/javascript" src="js/polyfill.js"></script>
<script type="text/javascript" src="curtain_imageresizer.js"></script><style type="text/css">body {overflow-y:scroll;}</style>
<script type="text/javascript" src="ajaxbasic.js"></script>
<script type="text/javascript" src="common.js"></script>
<script type="text/javascript" src="domLib.js"></script>
<script type="text/javascript" src="domTT.js"></script>
<script type="text/javascript" src="domTT_drag.js"></script>
<script type="text/javascript" src="fadomatic.js"></script>
<style>
.clock {
	height:50px;
	border-radius:50%;
	position:relative;
}
.clock span{
    display:inline-block;
	position:absolute;
	height:50px;
    left:33.5px;
    top:2px;
}
.clock span:before{
    position:absolute;
    display:inline-block;
	width:2px;
    bottom:50%;

}
.clock span:first-of-type {
	animation:zhuanquan_s 60s ease infinite;
}
.clock span:nth-of-type(2) {
	animation:zhuanquan_m 3600s ease infinite
}
.clock span:last-of-type {
	animation:zhuanquan_h 43200s ease infinite
}
/* 秒针 */
.clock span:first-of-type:before {
    left:-1px;
	height:11px;
	background:#27A;
	content:"";
}
/* 分针 */
.clock span:nth-of-type(2):before {
    left:-1px;
	height:9px;
	background:#FF9900;
	content:"";
}
/* 时针 */
.clock span:last-of-type:before {
    left:-1px;
	height:7px;
	background:#C00;
	content:"";
}

@keyframes zhuanquan_s {
	0% {
        transform:rotate(30deg)
    }
    100% {
        transform:rotate(390deg)
    }
}

@keyframes zhuanquan_m {
	0% {
        transform:rotate(210deg)
    }
    100% {
        transform:rotate(570deg)
    }
}

@keyframes zhuanquan_h {
	0% {
        transform:rotate(330deg)
    }
    100% {
        transform:rotate(690deg)
    }
}
</style>
</head>
<body>
<table class="head auto mb10" cellspacing="0" cellpadding="0" align="center">
	<tbody><tr>
		<td class="clear">
            <div class="w18 clearfix auto pt10">
                <div class="left">
                                    <div class="logo_img">
                        <!-- 针 -->
                        <div class="clock dib">
                            <span></span><span></span><span></span>
                        </div>
                        <!-- logo -->
                        <a class="pr" href="index.php"><img height="50" src="/pic/ptt.png" alt="PT时间" title="PT时间 - 分享你所爱，他所需，得你所愿！语言设置为中文简体，获得最佳体验。祝大家玩得愉快！欢迎捐赠，鼓励站长和管理！"></a>
                        <!-- 广告 -->
                        <p class="fcb">分享你所爱，他所需，得你所愿！语言设置为中文简体，获得最佳体验。祝大家玩得愉快！欢迎捐赠，鼓励站长和管理！</p>
                    </div>
                                </div>
                <div class="right">
                                                <a href="/donate.php" class="btn btn-danger"><i class="icon pt-aixinjuankuan"></i> 捐赠&amp;说明</a>
                                        <a href="/complains.php" class="btn btn-success"><i class="icon pt-shensu"></i> 申诉</a>
                </div>
            </div>
		</td>
	</tr>
</tbody></table>

<!-- 导航结构 -->
<table id="nav_list" class="mainouter mt20 mb5" width="90%" cellspacing="0" cellpadding="5" align="center">
    <tbody>
    <tr>
    <td id="nav_block" class="text" align="center">
        <table class="main" width="1200" border="0" cellspacing="0" cellpadding="0"><tbody><tr><td class="embedded"><div id="nav"><ul id="mainmenu" class="menu mt10 main_nav"><li><a href="index.php">&nbsp;首&nbsp;&nbsp;页&nbsp;</a></li><li><a href="forums.php">&nbsp;论&nbsp;&nbsp;坛&nbsp;</a></li><li class="selected"><a href="torrents.php">&nbsp;综&nbsp;&nbsp;合&nbsp;</a></li><li><a href="adults.php">&nbsp;9kg&nbsp;</a></li><li><a href="upload.php">&nbsp;发布种子&nbsp;</a><ul class="drop menu5"><li><a href="upload_adults.php">发布9kg</a></li></ul></li><li><a href="offers.php">&nbsp;候&nbsp;&nbsp;选&nbsp;(48)</a></li><li><a href="viewrequest.php">&nbsp;求&nbsp;&nbsp;种&nbsp;(223)</a></li><li><a href="topten.php">排&nbsp;行&nbsp;榜</a></li><li><a href="log.php">&nbsp;日&nbsp;&nbsp;志&nbsp;</a></li><li><a href="usercp.php">&nbsp;控制面板&nbsp;</a></li><li><a href="usercp.php?action=special">&nbsp;特殊设定&nbsp;</a></li><li><a style=" background:#017A85" href="sendmessage.php?receiver=2">&nbsp;联系管理&nbsp;</a></li><li><a style=" background:#116677" href="https://yao.pttime.org/Vip/index" target="_blank"> 贵宾礼包专区 </a></li><li><a style=" background:#D30D15" href="/forums.php?action=viewtopic&amp;topicid=16&amp;page=0">致新用户</a></li></ul></div></td></tr></tbody></table>
        <!-- 用户信息 -->
        <table id="info_block" cellpadding="4" cellspacing="0" border="0" width="95%">

                    <tbody><tr>
                    <td class="bottom clearfix" align="left">
                        <span class="medium left">嗨,
                            <a href="userdetails.php?id=47272" class="User_Name"><b>fjr</b></a>[UID=47272][(幼儿园)User][<a href="userdetails.php?id=47272" class="fcs fwb User">个人中心</a>]                            [<a href="logout.php"><b>退出</b></a>]
                            
                            
                            <span>[<a href="bookmarks.php?inclbookmarked=1&amp;allsec=1&amp;incldead=0">收藏</a>]</span>
                            
                            <span>[<a href="myrss.php">RSS 下载筐</a>]</span>
                            
                                                            <span>[<a href="getrss.php">获取RSS</a>]</span>
                                                        <font class="ml10"><b>邀请注册</b></font>
                            [<a class="fcs" href="invite.php?id=47272">邀请</a>]:
                            5/0                            <!-- 邀请码 -->
                            <span class="ml10">
                                <font><b>开注邀请码</b>:</font>
                                <font class="fwb">groszx</font>
                                                                <font class="fcg">(开放注册日，无限邀请)</font>
                                                            </span>
                            
                        </span>
                        <!-- 大包免费提醒 -->
                        <div class="medium right">
                            <!-- 单种限速 -->
                            <span class="ml5 fcr">单种上传限速：<b>100M/s</b></span>
                            <!-- 大包免费 -->
                            <span class="ml5 fcr">大包免费(限时)：<b>≥</b><b>100G</b></span>
                            <!-- 0流量包大小 -->
                            <span class="ml5 fcr">0流量(<a class="fcs" href="/sendmessage.php?receiver=2">发布者申请</a>)：<b>≥</b><b>500G</b></span>
                            <!-- 当前时间 -->
                            <span class="ml10 fwb">当前时间:23:35</span>
                        </div>
                    </td>
                    </tr>
                    <tr>
                        <td class="bottom clearfix" align="right">
                            <div class="left">
                                <span class="mr5"><font class="color_ratio">分享率:</font>12.84</span>
                                <span class="mr5"><font class="color_uploaded">上传:</font>2.996TB</span>
                                <span class="mr5"><font class="color_downloaded"> 下载:</font>238.88GB</span>
                                <span class="mr5"><font class="color_active">当前活动:</font><i alt="Torrents seeding" title="当前做种" class="arrowup icon pt-shangsheng fcr"></i>22                                    <i alt="Torrents seeding" title="当前下载" class="arrowdown icon pt-xiajiang fcg"></i>1</span>
                                <span class="mr5">可连接:<font color="green">是</font></span>
                                <!-- 最大连接数系统，目的是让用户只能下载有限多个链接。 -->
                                <span class="mr5">连接数:<font color="green">无限制</font></span>
                                <span class="mr5"><font>魔力值 (106.76魔力/小时,补签卡:0)</font>
                                    [<a href="mybonus.php" class="fcs">魔力使用&amp;说明</a>]: 19,173.6(获得35,<a href="attendance.php" class="fcs">详情</a>)</span>
                                
                            </div>
                            <div class="right">
                                <a class="mr10" href="messages.php">收件箱:21 (0 新)</a><a class="mr10" href="messages.php?action=viewmailbox&amp;box=-1">发件箱:2</a>                             </div>
                        </td>
                    </tr>
 
            <tr><td>
                <span class="tal mr10"><a class="fcr" href="/forums.php?action=viewtopic&amp;topicid=9&amp;page=p11#pid11"><i class="icon pt-jinggao"></i> 发种及三严说明(必读)</a></span><span class="tal mr10"><a class="fcs" href="/forums.php?action=viewforum&amp;forumid=7"><i class="icon pt-taolun"></i> 合集奖励计划</a></span><span class="tal mr10"><a class="fcs" href="https://yao.pttime.org" target="_blank"><i class="icon pt-guanfang"></i> 官窑直达</a></span><span class="tal mr10"><a class="fcs" href="/forums.php?action=viewforum&amp;forumid=11"><i class="icon pt-yaopin"></i> 开注、发药、求药</a></span><span class="tal mr10"><a class="fcs" href="/forums.php?action=viewtopic&amp;topicid=971&amp;page=p4877#pid4877"><i class="icon pt-anonymous-full"></i> 我有情报</a></span><div class="right"> <a class="mr10" href="friends.php"><i class="icon pt-luntan fcb"></i> 好友列表</a><i class="icon pt-weixin fcg"></i> 微信(备注邮箱，防走丢):doudoutf88<i class="icon pt-qqqun-copy ml10 fcs"></i> QQ群(捐赠5元):818369831
	            <a target="_blank" href="//shang.qq.com/wpa/qunwpa?idkey=37d1441cc5a7c08d8a676f675719ef1447536b3b4c3fea31984aa783547cdf9b"><img border="0" src="//pub.idqqimg.com/wpa/images/group.png" alt="PT时间-www.pttime.org" title="PT时间-www.pttime.org"></a></div>            </td></tr>
        </tbody></table>
    </td>
    </tr>
    </tbody>
</table>
<!-- 信息+资源结构 -->
    <table id="msg_list" class="mainouter" width="90%" cellspacing="0" cellpadding="5" align="center">
        <tbody>
            <tr>
                <td id="outer" align="center" class="outer" style="padding:0">
                <div align="center" style="margin-bottom: 10px;margin-top: 10px;" id="ad_belownav"><font size="4"><span style="color: #D30D15;">无数据要求、新手免考核、资源全免费……永久VIP贵宾请捐赠：458RMB！</span><font size="2"><span style="color: #459961;">附赠礼包看捐赠页说明，感谢大家支持！</span></font><font size="2"><span style="color: gray;">(<a class="fcs" href="adredir.php?id=6&amp;url=%2Fforums.php%3Faction%3Dviewtopic%26amp%3Bforumid%3D3%26amp%3Btopicid%3D23" target="_blank">查看贵宾详细特权</a>)</span></font></font> <br>
<span style="color: #2277AA;">推广邀请：邀请可获得5%的上传分成。将你的邀请，发给信得过的人吧。注意：特殊设定，可控制被邀请人的分类访问权限。</span>欢迎参加：<a class="fcs" href="adredir.php?id=6&amp;url=%2Fforums.php%3Faction%3Dviewtopic%26amp%3Bforumid%3D1%26amp%3Btopicid%3D912" target="_blank">本站logo征集活动</a><br>
<b>异常答疑：</b>0、<a class="fcs" href="adredir.php?id=6&amp;url=%2Fforums.php%3Faction%3Dviewtopic%26amp%3Bforumid%3D8%26amp%3Btopicid%3D1722" target="_blank">月经性访问异常说明</a>。1、<a class="fcs" href="adredir.php?id=6&amp;url=%2Fforums.php%3Faction%3Dviewtopic%26amp%3Bforumid%3D8%26amp%3Btopicid%3D955" target="_blank">tracker异常，访问异常的解决思路</a>。2、统一回复账号升级问题：请查看《致新用户》第五部分内容。3、个别用户的插件请求首页、点赞、签到、RSS频率极为反常，请注意调整或关闭。</div><table border="0" cellspacing="0" cellpadding="10" style="margin:10px 0"><tbody><tr><td style="border: none; padding: 10px; background: orange">
<b><a href="userdetails.php?id=47272"><font color="white"><p class="fcg">不论你是老PTer，还是萌新，建议先看下"致新用户"</p>离新人考核结束还有 <span title="2022-06-15 13:39:12">23天14时</span><br>上传: <span style="color: green">已通过</span><br>下载: <span style="color: green">已通过</span><br>魔力值: <span style="color: green">已通过</span><br><span style="color: #D30D15">注意：在考核期限内，请保持以上数据均处于通过状态！</span><span class="fcg">你也可以通过捐赠直接通过新手考核：</span></font></a><font color="white"><a class="fcr" href="/donate.php"><i class="icon pt-aixinjuankuan"></i> 捐赠&amp;说明</a></font></b></td></tr></tbody></table></td></tr></tbody></table><table class="mainouter mt5" width="90%" cellspacing="0" cellpadding="5" align="center"><tbody>
                <tr>
                    <td id="outer" align="center" class="outer"><table align="center" width="1200" class="main" border="0" cellspacing="0" cellpadding="0"><tbody><tr><td class="embedded">
<form method="get" name="searchbox" action="?">
	<table class="searchbox tac" cellspacing="0" cellpadding="5" width="100%">
        <!-- 搜索项目 -->
		<tbody id="ksearchboxmain">
		<tr>
			<td class="rowfollow" align="left">
				<table width="100%">
                    <!-- 分类数据 -->
					<tbody><tr class="search_cat"><td class="embedded" colspan="13" align="left"><b>类型:</b></td></tr><tr><td class="cat_item" width="68px" align="left" style="padding-bottom: 4px; padding-right: 10px;">
                                        <input type="checkbox" id="cat401" name="cat401" value="1"><a class="dib" href="?cat=401"><img src="pic/dot.png" alt="Movies(电影)" title="Movies(电影)"><span class="category dib c_movies" alt="Movies(电影)" title="Movies(电影)"></span></a></td>
<td class="cat_item" width="68px" align="left" style="padding-bottom: 4px; padding-right: 10px;">
                                        <input type="checkbox" id="cat402" name="cat402" value="1"><a class="dib" href="?cat=402"><img src="pic/dot.png" alt="TV Series(电视剧)" title="TV Series(电视剧)"><span class="category dib c_tvseries" alt="TV Series(电视剧)" title="TV Series(电视剧)"></span></a></td>
<td class="cat_item" width="68px" align="left" style="padding-bottom: 4px; padding-right: 10px;">
                                        <input type="checkbox" id="cat403" name="cat403" value="1"><a class="dib" href="?cat=403"><img src="pic/dot.png" alt="TV Shows(综艺)" title="TV Shows(综艺)"><span class="category dib c_tvshows" alt="TV Shows(综艺)" title="TV Shows(综艺)"></span></a></td>
<td class="cat_item" width="68px" align="left" style="padding-bottom: 4px; padding-right: 10px;">
                                        <input type="checkbox" id="cat404" name="cat404" value="1"><a class="dib" href="?cat=404"><img src="pic/dot.png" alt="Documentaries(纪录片)" title="Documentaries(纪录片)"><span class="category dib c_doc" alt="Documentaries(纪录片)" title="Documentaries(纪录片)"></span></a></td>
<td class="cat_item" width="68px" align="left" style="padding-bottom: 4px; padding-right: 10px;">
                                        <input type="checkbox" id="cat405" name="cat405" value="1"><a class="dib" href="?cat=405"><img src="pic/dot.png" alt="Sport(体育、竞技、武术及相关)" title="Sport(体育、竞技、武术及相关)"><span class="category dib c_sport" alt="Sport(体育、竞技、武术及相关)" title="Sport(体育、竞技、武术及相关)"></span></a></td>
<td class="cat_item" width="68px" align="left" style="padding-bottom: 4px; padding-right: 10px;">
                                        <input type="checkbox" id="cat406" name="cat406" value="1"><a class="dib" href="?cat=406"><img src="pic/dot.png" alt="Games(游戏及相关)" title="Games(游戏及相关)"><span class="category dib c_game" alt="Games(游戏及相关)" title="Games(游戏及相关)"></span></a></td>
<td class="cat_item" width="68px" align="left" style="padding-bottom: 4px; padding-right: 10px;">
                                        <input type="checkbox" id="cat408" name="cat408" value="1"><a class="dib" href="?cat=408"><img src="pic/dot.png" alt="Music(音乐、专辑、MV、演唱会)" title="Music(音乐、专辑、MV、演唱会)"><span class="category dib c_music" alt="Music(音乐、专辑、MV、演唱会)" title="Music(音乐、专辑、MV、演唱会)"></span></a></td>
<td class="cat_item" width="68px" align="left" style="padding-bottom: 4px; padding-right: 10px;">
                                        <input type="checkbox" id="cat409" name="cat409" value="1"><a class="dib" href="?cat=409"><img src="pic/dot.png" alt="Art(舞蹈、歌剧、戏曲、相声、评书等)" title="Art(舞蹈、歌剧、戏曲、相声、评书等)"><span class="category dib c_art" alt="Art(舞蹈、歌剧、戏曲、相声、评书等)" title="Art(舞蹈、歌剧、戏曲、相声、评书等)"></span></a></td>
<td class="cat_item" width="68px" align="left" style="padding-bottom: 4px; padding-right: 10px;">
                                        <input type="checkbox" id="cat411" name="cat411" value="1"><a class="dib" href="?cat=411"><img src="pic/dot.png" alt="Science(科学、知识、技能)" title="Science(科学、知识、技能)"><span class="category dib c_ability" alt="Science(科学、知识、技能)" title="Science(科学、知识、技能)"></span></a></td>
<td class="cat_item" width="68px" align="left" style="padding-bottom: 4px; padding-right: 10px;">
                                        <input type="checkbox" id="cat412" name="cat412" value="1"><a class="dib" href="?cat=412"><img src="pic/dot.png" alt="School(应试、考级、初中以上教育)" title="School(应试、考级、初中以上教育)"><span class="category dib c_school" alt="School(应试、考级、初中以上教育)" title="School(应试、考级、初中以上教育)"></span></a></td>
<td class="cat_item" width="68px" align="left" style="padding-bottom: 4px; padding-right: 10px;">
                                        <input type="checkbox" id="cat413" name="cat413" value="1"><a class="dib" href="?cat=413"><img src="pic/dot.png" alt="Book(书籍、有声书)" title="Book(书籍、有声书)"><span class="category dib c_book" alt="Book(书籍、有声书)" title="Book(书籍、有声书)"></span></a></td>
<td class="cat_item" width="68px" align="left" style="padding-bottom: 4px; padding-right: 10px;">
                                        <input type="checkbox" id="cat420" name="cat420" value="1"><a class="dib" href="?cat=420"><img src="pic/dot.png" alt="Code(IT、编程、大数据、人工智能）" title="Code(IT、编程、大数据、人工智能）"><span class="category dib c_computer" alt="Code(IT、编程、大数据、人工智能）" title="Code(IT、编程、大数据、人工智能）"></span></a></td>
<td class="cat_item" width="68px" align="left" style="padding-bottom: 4px; padding-right: 10px;">
                                        <input type="checkbox" id="cat430" name="cat430" value="1"><a class="dib" href="?cat=430"><img src="pic/dot.png" alt="Animate(3D动画、2.5次元)" title="Animate(3D动画、2.5次元)"><span class="category dib c_x3" alt="Animate(3D动画、2.5次元)" title="Animate(3D动画、2.5次元)"></span></a></td>
<td class="cat_item" width="68px" align="left" style="padding-bottom: 4px; padding-right: 10px;">
                                        <input type="checkbox" id="cat431" name="cat431" value="1"><a class="dib" href="?cat=431"><img src="pic/dot.png" alt="ACGN(二次元、漫画)" title="ACGN(二次元、漫画)"><span class="category dib c_acgn" alt="ACGN(二次元、漫画)" title="ACGN(二次元、漫画)"></span></a></td>
<td class="cat_item" width="68px" align="left" style="padding-bottom: 4px; padding-right: 10px;">
                                        <input type="checkbox" id="cat432" name="cat432" value="1"><a class="dib" href="?cat=432"><img src="pic/dot.png" alt="Baby(婴幼、早教、小学及相关)" title="Baby(婴幼、早教、小学及相关)"><span class="category dib c_baby" alt="Baby(婴幼、早教、小学及相关)" title="Baby(婴幼、早教、小学及相关)"></span></a></td>
<td class="cat_item" width="68px" align="left" style="padding-bottom: 4px; padding-right: 10px;">
                                        <input type="checkbox" id="cat450" name="cat450" value="1"><a class="dib" href="?cat=450"><img src="pic/dot.png" alt="Resource(资源、素材、模板)" title="Resource(资源、素材、模板)"><span class="category dib c_resource" alt="Resource(资源、素材、模板)" title="Resource(资源、素材、模板)"></span></a></td>
<td class="cat_item" width="68px" align="left" style="padding-bottom: 4px; padding-right: 10px;">
                                        <input type="checkbox" id="cat451" name="cat451" value="1"><a class="dib" href="?cat=451"><img src="pic/dot.png" alt="Software(软件、系统、 程序、APP等)" title="Software(软件、系统、 程序、APP等)"><span class="category dib c_soft" alt="Software(软件、系统、 程序、APP等)" title="Software(软件、系统、 程序、APP等)"></span></a></td>
<td class="cat_item" width="68px" align="left" style="padding-bottom: 4px; padding-right: 10px;">
                                        <input type="checkbox" id="cat490" name="cat490" value="1"><a class="dib" href="?cat=490"><img src="pic/dot.png" alt="Other(其它)" title="Other(其它)"><span class="category dib c_other" alt="Other(其它)" title="Other(其它)"></span></a></td>
<td colspan="" class="bottom" align="left" style="padding-left: 15px"><input name="cat_check" value="全选" class="btn btn-mini" type="button" onclick="javascript:SetChecked('cat','cat_check','全选','全不选',-1,10)"></td>
</tr>                    <tr><td class="embedded" colspan="20" align="left"><b>其他:</b></td></tr>
                    <tr>
                        <td class="bottom clearfix" colspan="10">
                            <div class="left">
                            <font class="medium">显示断种/活种</font>

                            <select class="med" name="incldead" style="width: 100px;">
                                <option value="0">包括断种</option>
                                <option value="1" selected="selected">活种 </option>
                                <option value="2">断种</option>
                            </select></div>
                            <div class="left ml20">
                            <font class="medium">显示促销种子</font>

                            <select class="med" name="spstate" style="width: 100px;">
                                <option value="0">全部</option><option value="1">普通</option><option value="2">免费</option><option value="3">2X上传</option><option value="4">2X免费</option><option value="5">50%免费</option><option value="6">2X上传&amp;50%免费</option><option value="7">30%免费</option><option value="8">0流量</option>                            </select></div>
                            <div class="left ml20">
                            <font class="medium">显示收藏</font>

                            <select class="med" name="inclbookmarked" style="width: 100px;">
                                <option value="0">全部</option>
                                <option value="1">仅收藏</option>
                                <option value="2">仅未收藏</option>
                            </select></div>
                        </td>
                        <td class="embedded clearfix" colspan="10">
                            <div class="left">
                                <b>搜索词:</b>
                                <input id="searchinput" name="search" type="text" value="" autocomplete="off" style="width: 200px" ondblclick="suggest(event.keyCode,this.value);" onkeyup="suggest(event.keyCode,this.value);" onkeypress="return noenter(event.keyCode);">
                                <script src="suggest.js" type="text/javascript"></script>
                                <div id="suggcontainer" style="text-align: left; display: none;margin-left:49px; line-height:25px;">
                                    <div id="suggestions" style="width: 198px;
                                                                border: 1px solid #ccc;
                                                                border-top-color: rgb(204, 204, 204);
                                                                border-top-style: solid;
                                                                border-top-width: 1px;
                                                                cursor: default;
                                                                position: absolute;
                                                                color: rgb(0,0,0);
                                                                background-color: rgb(255, 255, 255);
                                                                margin-top: -1px;
                                                                border-top: none;"></div>
                                </div>
                            </div>

                            <div class="left ml20">
                                 范围：                                <select name="search_area">
                                    <option value="0">标题</option>
                                    <option value="1">简介</option>
                                                                            <option value="2">副标题</option>
                                                                        <option value="3">发布者</option>
                                    <option value="4">IMDb链接</option>
                                    <option value="5">豆瓣链接或ID</option>
                                </select>
                            </div>

                            <div class="left ml20">

                                 匹配模式：
                                <select name="search_mode" style="width: 60px;">
                                    <option value="0">与</option>
                                    <option value="1">或</option>
                                    <option value="2">准确</option>
                                </select>
                            </div>

                            <div class="left ml10">
                                                                <input class="btn" type="submit" value="搜索一下">
                            </div>
                        </td>
                    </tr>
                    				</tbody></table>
			</td>
		</tr>
		</tbody>
	</table>
</form>
<!-- 高亮种子搜索按钮 -->
<div class="tac">
    <span>高亮种子搜索：</span>
    <a href="torrents.php?incldead=1&amp;spstate=0&amp;inclbookmarked=0&amp;search=&amp;search_area=0&amp;search_mode=0">全部</a> |
    <a href="torrents.php?incldead=1&amp;spstate=1&amp;inclbookmarked=0&amp;search=&amp;search_area=0&amp;search_mode=0"><font class="fc8">普通</font></a> | <a href="torrents.php?incldead=1&amp;spstate=2&amp;inclbookmarked=0&amp;search=&amp;search_area=0&amp;search_mode=0"><font class="promotion free">免费</font></a> | <a href="torrents.php?incldead=1&amp;spstate=3&amp;inclbookmarked=0&amp;search=&amp;search_area=0&amp;search_mode=0"><font class="promotion twoup">2X上传</font></a> | <a href="torrents.php?incldead=1&amp;spstate=4&amp;inclbookmarked=0&amp;search=&amp;search_area=0&amp;search_mode=0"><font class="promotion twoupfree">2X免费</font></a> | <a href="torrents.php?incldead=1&amp;spstate=5&amp;inclbookmarked=0&amp;search=&amp;search_area=0&amp;search_mode=0"><font class="promotion halfdown">50%免费</font></a> | <a href="torrents.php?incldead=1&amp;spstate=6&amp;inclbookmarked=0&amp;search=&amp;search_area=0&amp;search_mode=0"><font class="promotion twouphalfdown">2X上传&amp;50%免费</font></a> | <a href="torrents.php?incldead=1&amp;spstate=7&amp;inclbookmarked=0&amp;search=&amp;search_area=0&amp;search_mode=0"><font class="promotion thirtypercent">30%免费</font></a> | <a href="torrents.php?incldead=1&amp;spstate=8&amp;inclbookmarked=0&amp;search=&amp;search_area=0&amp;search_mode=0"><font class="promotion zeroupzerodown">0流量</font></a>    <!-- 贵宾专属搜索 -->
        <!-- 贵宾礼包搜索 -->
    </div>
<script type="text/javascript">
    var MenuOutTime = 0;
    var ShowDivList = [];
    function hiddmenu(t) {
        MenuOutTime = 0;
        t=t>500?t:500;
        setTimeout(function() {
            if (MenuOutTime != 1) {
                for(var objname in ShowDivList){
                    $(objname).style.display='none';
                }
            }
        },t);
    }
    function setmenutime() {
        MenuOutTime = 1
    }
    function CPos(x, y){
        this.x = x;
        this.y = y;
    }

    function showmenu(obj,objname,url){
        for(var rowname in ShowDivList){
            $(rowname).style.display='none';
        }
        if (!url) return false;


        if (!$(objname)) {
            var objdiv = document.createElement("div");
            objdiv.id = objname;
        } else {
            var objdiv = $(objname);
        }
        var target = obj;
        var pos = new CPos(target.offsetLeft, target.offsetTop);

        var target = target.offsetParent;
        while (target)
        {
            pos.x += target.offsetLeft;
            pos.y += target.offsetTop;

            target = target.offsetParent
        }
        objdiv.style.display = 'block';
        objdiv.onmousemove = function(){setmenutime();};
        objdiv.onmouseout = function(){hiddmenu(objname);};
        objdiv.onclick = function(){objdiv.style.display='none';};

        objdiv.style.position='absolute';
        objdiv.style.left = (pos.x)+42+'px';
        objdiv.style.top = (pos.y+25)-25+'px';
        if (!$(objname+'_img')) {
            objdiv.innerHTML='';
            var picdiv = document.createElement("img");
            picdiv.setAttribute('src',url);
            picdiv.setAttribute('height','400');
            picdiv.setAttribute('id',objname+'_img');
            //picdiv.style.display = 'none';
            picdiv.onload=function (){
                //picdiv.style.display = '';
                resource_drawimage(objname+'_img',325,400);
            };
            objdiv.appendChild(picdiv);
        }
        document.body.appendChild(objdiv);
        ShowDivList[objname]=1;
        MenuOutTime = 1;

        return false;
    }
    function resource_drawimage(objname,iwidth,iheight){
        var ImgD=$(objname);
        var image=new Image();
        image.src=ImgD.src;
        if(image.width>0 && image.height>0){
            if(image.width/image.height>= iwidth/iheight){
                if(image.width>iwidth){
                    ImgD.width=iwidth;
                    ImgD.height=(image.height*iwidth)/image.width;
                }else{
                    ImgD.width=image.width;
                    ImgD.height=image.height;
                }
                ImgD.alt=image.width+"X"+image.height;
            }else{
                if(image.height>iheight){
                    ImgD.height=iheight;
                    ImgD.width=(image.width*iheight)/image.height;
                }else{
                    ImgD.width=image.width;
                    ImgD.height=image.height;
                }
                ImgD.alt=image.width+"X"+image.height;
            }
        }
    }
</script>
<div align="left" style="margin-top: 10px" id="ad_belowsearchbox"><span style="color: #177cb0;">UPS电源：</span><span style="color: #459961;">山特TG-BOX600(<span style="color: #ED5226;">439元+1个月VIP</span>)，TG-BOX850(<span style="color: #ED5226;">509元+1个月VIP</span>)，施耐德APC-BK650M2(<span style="color: #ED5226;">475元+1个月VIP</span>)。</span><a class="fcs" href="adredir.php?id=4&amp;url=%2Fforums.php%3Faction%3Dviewtopic%26amp%3Btopicid%3D202%26amp%3Bpage%3Dlast%23pid910" target="_blank">全系列参数、报价及购买 &gt;&gt;</a><br>
<span style="color: #177cb0;">群晖NAS：</span><span style="color: #459961;">群晖DS220+(<span style="color: #ED5226;">2480元+半年VIP</span>)，DS920+(<span style="color: #ED5226;">4050元+1年VIP</span>)。</span><a class="fcs" href="adredir.php?id=4&amp;url=%2Fforums.php%3Faction%3Dviewtopic%26amp%3Bforumid%3D6%26amp%3Btopicid%3D217" target="_blank">全系列参数、报价及购买 &gt;&gt;</a> <br>
<span style="color: #177cb0;">西数16T硬盘：</span><span style="color: #459961;">西部数据16T全新5年国保硬盘(<span style="color: #ED5226;">1600元+3个月VIP</span>)</span>。<a class="fcs" href="adredir.php?id=4&amp;url=%2Fforums.php%3Faction%3Dviewtopic%26amp%3Btopicid%3D1102%26amp%3Bpage%3Dp5696%23pid5696" target="_blank">参数、报价及购买 &gt;&gt;</a> <br>
<span style="color: #666666;">产品都支持全国官方联保，有问题可咨询本站、销售方、相关技术群或官方联保！</span><a class="fcs" href="adredir.php?id=4&amp;url=%2Fforums.php%3Faction%3Dviewforum%26amp%3Bforumid%3D6" target="_blank">所有产品列表 &gt;&gt;</a></div><p align="center"><font class="gray"><b title="Alt+Pageup">&lt;&lt;&nbsp;上一页</b></font>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="?inclbookmarked=0&amp;incldead=1&amp;spstate=0&amp;page=1"><b title="Alt+Pagedown">下一页&nbsp;&gt;&gt;</b></a><br><font class="gray"><b>1&nbsp;-&nbsp;50</b></font> | <a href="?inclbookmarked=0&amp;incldead=1&amp;spstate=0&amp;page=1"><b>51&nbsp;-&nbsp;100</b></a> | <a href="?inclbookmarked=0&amp;incldead=1&amp;spstate=0&amp;page=2"><b>101&nbsp;-&nbsp;150</b></a> | ... | <a href="?inclbookmarked=0&amp;incldead=1&amp;spstate=0&amp;page=321"><b>16051&nbsp;-&nbsp;16100</b></a> | <a href="?inclbookmarked=0&amp;incldead=1&amp;spstate=0&amp;page=322"><b>16101&nbsp;-&nbsp;16150</b></a> | <a href="?inclbookmarked=0&amp;incldead=1&amp;spstate=0&amp;page=323"><b>16151&nbsp;-&nbsp;16158</b></a></p>
<table class="torrents" cellspacing="0" cellpadding="5" width="100%" id="torrenttable"><tbody><tr>
            <td class="colhead" align="center">类型</td>
            <td class="colhead"><a href="?sort=1&amp;type=asc">标题</a></td>

                            <!-- PTR分数 -->
                <td class="colhead"><a href="?sort=10&amp;type="><img class="time" src="pic/trans.gif" alt="time" title="平台打分">PTR</a></td>
                <!-- 打分 -->
                <td class="colhead"><a href="?sort=3&amp;type=desc"><img class="comments" src="pic/trans.gif" alt="comments" title="评论数">评论</a></td>
                
                <td class="colhead"><a href="?sort=4&amp;type=desc"><img class="time" src="pic/trans.gif" alt="time" title="存活时间">存活</a></td>
                <td class="colhead"><a href="?sort=5&amp;type=desc"><img class="size" src="pic/trans.gif" alt="size" title="大小">大小</a></td>
                <td class="colhead"><a href="?sort=7&amp;type=desc"><img class="seeders" src="pic/trans.gif" alt="seeders" title="种子数">做种</a></td>
                <td class="colhead"><a href="?sort=8&amp;type=desc"><img class="leechers" src="pic/trans.gif" alt="leechers" title="下载数">下载</a></td>
                <td class="colhead"><a href="?sort=6&amp;type=desc"><img class="snatched" src="pic/trans.gif" alt="snatched" title="完成数">完成</a></td>
                <td class="colhead">进度</td>
                <td class="colhead"><a href="?sort=9&amp;type=desc">发布者</a></td>
                <td class="colhead">行为</td>
        </tr>
        <tr class="sticky_top">
<td class="rowfollow nowrap" valign="middle"><a class="dib" href="?cat=420"><img src="pic/dot.png" alt="Code(IT、编程、大数据、人工智能）" title="Code(IT、编程、大数据、人工智能）"><span class="category dib c_computer" alt="Code(IT、编程、大数据、人工智能）" title="Code(IT、编程、大数据、人工智能）"></span></a></td>
<td class="rowfollow" width="100%" align="left"><table class="torrentname" width="100%"><tbody><tr class="sticky_top"><td class="embedded"><i class="sticky icon pt-huobao fcr" alt="Sticky" title="完全置顶"></i><i class="sticky icon pt-huobao fcr" alt="Sticky" title="完全置顶"></i>&nbsp;<a target="_blank" class="torrentname" title="PTT种子搬运助手（附带油猴脚本）-- 2022.05.17 更新音乐、9kg等详情不能搬运问题、增加搬运到候选、改善PT时间搬运按钮（因缓存，请等明天更新）" href="details.php?id=2245&amp;hit=1"><b class="promotion zeroupzerodown">PTT种子搬运助手（附带油猴脚本）-- 2022.05.17 更新音乐、9kg等详情不能搬运问题、增加搬运到候选、改善PT时间搬运按钮（因缓存，请等明天更新）</b></a> <b>[<font class="hot">热门</font>]</b> <font class="promotion zeroupzerodown">0流量</font> <br>一键搬运其他PT站资源，超级方便 | 包含油猴插件、pt助手脚本和安装使用说明<div class="progressarea" title="已完成"><div class="progress"><div class="progress_seeding" style="width:100%;"></div></div></div></td><td width="20" class="embedded" style="text-align: right; " valign="middle"><table><tbody><tr><td class="embedded"></td><td class="embedded"><a href="download.php?id=2245&amp;passkey=cc0f2413d63a3a7f43964154d23ac2bb"><i class="download icon pt-xiazai fcg" alt="download" title="下载本种"></i></a><br><a id="bookmark0" href="javascript: bookmark(2245,0);"><i class="delbookmark icon pt-wuxing fca" alt="Unbookmarked" title="收藏"></i></a><a id="myrss0" href="javascript: myrss(2245,0);"><i class="delmyrss icon pt-rss fca" alt="Unmyrssed" title="加入"></i></a></td></tr></tbody></table>
</td>
</tr></tbody></table></td><td class="rowfollow" width="40"><div class="w30"><span class="fwb">14</span><br><a id="traffic0" href="javascript: traffic(2245,0);"><i class="deltraffic icon pt-dianzan fc3" alt="Untrafficed" title="点赞"></i></a></div></td><td class="rowfollow"><b><a href="details.php?id=2245&amp;hit=1&amp;cmtpage=1#startcomments">92</a></b></td><td class="rowfollow nowrap"><span title="2020-12-09 15:08:23">1年<br>5月</span></td><td class="rowfollow">1.27<br>MB</td><td class="rowfollow" align="center"><b><a href="details.php?id=2245&amp;hit=1&amp;dllist=1#seeders">728</a></b></td>
<td class="rowfollow">0</td>
<td class="rowfollow"><a href="viewsnatches.php?id=2245"><b>4,157</b></a></td>
<td class="rowfollow">100%</td><td class="rowfollow"><a href="userdetails.php?id=2" class="StaffLeader_Name"><b>匿名者</b></a></td>
<td class="rowfollow"></td>
</tr>
<tr class="sticky_top">
<td class="rowfollow nowrap" valign="middle"><a class="dib" href="?cat=450"><img src="pic/dot.png" alt="Resource(资源、素材、模板)" title="Resource(资源、素材、模板)"><span class="category dib c_resource" alt="Resource(资源、素材、模板)" title="Resource(资源、素材、模板)"></span></a></td>
<td class="rowfollow" width="100%" align="left"><table class="torrentname" width="100%"><tbody><tr class="sticky_top"><td class="embedded"><i class="sticky icon pt-huobao fcr" alt="Sticky" title="完全置顶"></i><i class="sticky icon pt-huobao fcr" alt="Sticky" title="完全置顶"></i>&nbsp;<a target="_blank" class="torrentname" title="视频播放器合集" href="details.php?id=14360&amp;hit=1"><b class="promotion zeroupzerodown">视频播放器合集</b></a> <b>[<font class="hot">热门</font>]</b> <font class="promotion zeroupzerodown">0流量</font> <br>kodi+emby+potplayer+恒星播放器+迅雷影音+KolorEyes（播放VR）</td><td width="20" class="embedded" style="text-align: right; " valign="middle"><table><tbody><tr><td class="embedded"></td><td class="embedded"><a href="download.php?id=14360&amp;passkey=cc0f2413d63a3a7f43964154d23ac2bb"><i class="download icon pt-xiazai fcg" alt="download" title="下载本种"></i></a><br><a id="bookmark1" href="javascript: bookmark(14360,1);"><i class="delbookmark icon pt-wuxing fca" alt="Unbookmarked" title="收藏"></i></a><a id="myrss1" href="javascript: myrss(14360,1);"><i class="delmyrss icon pt-rss fca" alt="Unmyrssed" title="加入"></i></a></td></tr></tbody></table>
</td>
</tr></tbody></table></td><td class="rowfollow" width="40"><div class="w30"><span class="fwb">6</span><br></div></td><td class="rowfollow"><b><a href="details.php?id=14360&amp;hit=1&amp;cmtpage=1#startcomments">24</a></b></td><td class="rowfollow nowrap"><span title="2021-11-24 10:46:02">5月<br>29天</span></td><td class="rowfollow">373.84<br>MB</td><td class="rowfollow" align="center"><b><a href="details.php?id=14360&amp;hit=1&amp;dllist=1#seeders">444</a></b></td>
<td class="rowfollow"><b><a href="details.php?id=14360&amp;hit=1&amp;dllist=1#leechers">3</a></b></td>
<td class="rowfollow"><a href="viewsnatches.php?id=14360"><b>1,922</b></a></td>
<td class="rowfollow">-</td><td class="rowfollow"><a href="userdetails.php?id=2" class="StaffLeader_Name"><b>匿名者</b></a></td>
<td class="rowfollow"></td>
</tr>
<tr class="sticky_top">
<td class="rowfollow nowrap" valign="middle"><a class="dib" href="?cat=420"><img src="pic/dot.png" alt="Code(IT、编程、大数据、人工智能）" title="Code(IT、编程、大数据、人工智能）"><span class="category dib c_computer" alt="Code(IT、编程、大数据、人工智能）" title="Code(IT、编程、大数据、人工智能）"></span></a></td>
<td class="rowfollow" width="100%" align="left"><table class="torrentname" width="100%"><tbody><tr class="sticky_top"><td class="embedded"><i class="sticky icon pt-huobao fcr" alt="Sticky" title="完全置顶"></i><i class="sticky icon pt-huobao fcr" alt="Sticky" title="完全置顶"></i>&nbsp;<a target="_blank" class="torrentname" title="PT做种、发布、下载教程（多做种，多保种，谢谢站友们的支持）" href="details.php?id=3407&amp;hit=1"><b class="promotion zeroupzerodown">PT做种、发布、下载教程（多做种，多保种，谢谢站友们的支持）</b></a> <b>[<font class="hot">热门</font>]</b> <font class="promotion zeroupzerodown">0流量</font> <font class="promotion b4">字幕/附件(5)</font> <br>我为人人，人人为我，欢迎加入PT大家庭 | 感谢捐赠者对本站的支持！<div class="progressarea" title="已完成"><div class="progress"><div class="progress_seeding" style="width:100%;"></div></div></div></td><td width="20" class="embedded" style="text-align: right; " valign="middle"><table><tbody><tr><td class="embedded"></td><td class="embedded"><a href="download.php?id=3407&amp;passkey=cc0f2413d63a3a7f43964154d23ac2bb"><i class="download icon pt-xiazai fcg" alt="download" title="下载本种"></i></a><br><a id="bookmark2" href="javascript: bookmark(3407,2);"><i class="delbookmark icon pt-wuxing fca" alt="Unbookmarked" title="收藏"></i></a><a id="myrss2" href="javascript: myrss(3407,2);"><i class="delmyrss icon pt-rss fca" alt="Unmyrssed" title="加入"></i></a></td></tr></tbody></table>
</td>
</tr></tbody></table></td><td class="rowfollow" width="40"><div class="w30"><span class="fwb">17</span><br><a id="traffic2" href="javascript: traffic(3407,2);"><i class="deltraffic icon pt-dianzan fc3" alt="Untrafficed" title="点赞"></i></a></div></td><td class="rowfollow"><b><a href="details.php?id=3407&amp;hit=1&amp;cmtpage=1#startcomments">222</a></b></td><td class="rowfollow nowrap"><span title="2021-01-26 11:56:32">1年<br>4月</span></td><td class="rowfollow">48.20<br>MB</td><td class="rowfollow" align="center"><b><a href="details.php?id=3407&amp;hit=1&amp;dllist=1#seeders">561</a></b></td>
<td class="rowfollow"><b><a href="details.php?id=3407&amp;hit=1&amp;dllist=1#leechers">2</a></b></td>
<td class="rowfollow"><a href="viewsnatches.php?id=3407"><b>3,659</b></a></td>
<td class="rowfollow">100%</td><td class="rowfollow"><a href="userdetails.php?id=2" class="StaffLeader_Name"><b>匿名者</b></a></td>
<td class="rowfollow"></td>
</tr>
<tr class="sticky_top">
<td class="rowfollow nowrap" valign="middle"><a class="dib" href="?cat=450"><img src="pic/dot.png" alt="Resource(资源、素材、模板)" title="Resource(资源、素材、模板)"><span class="category dib c_resource" alt="Resource(资源、素材、模板)" title="Resource(资源、素材、模板)"></span></a></td>
<td class="rowfollow" width="100%" align="left"><table class="torrentname" width="100%"><tbody><tr class="sticky_top"><td class="embedded"><i class="sticky icon pt-huobao fcr" alt="Sticky" title="完全置顶"></i><i class="sticky icon pt-huobao fcr" alt="Sticky" title="完全置顶"></i>&nbsp;<a target="_blank" class="torrentname" title="PT辅种工具合集" href="details.php?id=2188&amp;hit=1"><b class="promotion zeroupzerodown">PT辅种工具合集</b></a> <b>[<font class="hot">热门</font>]</b> <font class="promotion zeroupzerodown">0流量</font> <br>IYUU、PT-Plugin-Plus、IYUU GUI</td><td width="20" class="embedded" style="text-align: right; " valign="middle"><table><tbody><tr><td class="embedded"></td><td class="embedded"><a href="download.php?id=2188&amp;passkey=cc0f2413d63a3a7f43964154d23ac2bb"><i class="download icon pt-xiazai fcg" alt="download" title="下载本种"></i></a><br><a id="bookmark3" href="javascript: bookmark(2188,3);"><i class="delbookmark icon pt-wuxing fca" alt="Unbookmarked" title="收藏"></i></a><a id="myrss3" href="javascript: myrss(2188,3);"><i class="delmyrss icon pt-rss fca" alt="Unmyrssed" title="加入"></i></a></td></tr></tbody></table>
</td>
</tr></tbody></table></td><td class="rowfollow" width="40"><div class="w30"><span class="fwb">10</span><br></div></td><td class="rowfollow"><b><a href="details.php?id=2188&amp;hit=1&amp;cmtpage=1#startcomments">33</a></b></td><td class="rowfollow nowrap"><span title="2020-12-07 15:16:05">1年<br>5月</span></td><td class="rowfollow">100.07<br>MB</td><td class="rowfollow" align="center"><b><a href="details.php?id=2188&amp;hit=1&amp;dllist=1#seeders">651</a></b></td>
<td class="rowfollow">0</td>
<td class="rowfollow"><a href="viewsnatches.php?id=2188"><b>4,025</b></a></td>
<td class="rowfollow">-</td><td class="rowfollow"><a href="userdetails.php?id=2" class="StaffLeader_Name"><b>匿名者</b></a></td>
<td class="rowfollow"></td>
</tr>
<tr class="sticky_normal">
<td class="rowfollow nowrap" valign="middle"><a class="dib" href="?cat=401"><img src="pic/dot.png" alt="Movies(电影)" title="Movies(电影)"><span class="category dib c_movies" alt="Movies(电影)" title="Movies(电影)"></span></a></td>
<td class="rowfollow" width="100%" align="left"><table class="torrentname" width="100%"><tbody><tr class="sticky_normal"><td class="torrentimg"><img class="pr5" src="/public/douban/1291841.jpg" height="52" onmouseover="showmenu(this,'tid_507','/public/douban/1291841.jpg');" onmouseout="hiddmenu(this,'tid_507');"></td><td class="embedded"><i class="sticky icon pt-huobao fcr" alt="Sticky" title="置顶"></i>&nbsp;<a target="_blank" class="torrentname" title="The Godfather Trilogy 1972-1990 Blu-ray 1080p AVC TrueHD5.1-HDSky" href="details.php?id=507&amp;hit=1"><b class="promotion">The Godfather Trilogy 1972-1990 Blu-ray 1080p AVC TrueHD5.1-HDSky</b></a> <b>[<font class="hot">热门</font>]</b> <font class="promotion halfdown">50%免费</font>  <i class="icon pt-shipin fc2"></i> <font class="promotion b4">字幕/附件(1)</font> <br>【豆瓣250-21】【豆瓣250-51】【豆瓣250-143】泰盛版《教父三部曲》（科波拉认可修复版） "一世一经典"教父 布鲁收藏版 ..</td><td width="20" class="embedded" style="text-align: right; " valign="middle"><table><tbody><tr><td class="embedded"><div style="text-align:right;margin-right:3px;width:50px"><a class="fwb" target="_blank" href="https://movie.douban.com/subject/1291841/"><i class="icon pt-douban fcg"></i> 9.3</a><br><a class="fwb" target="_blank" href="https://www.imdb.com/title/tt0068646/"><i class="icon pt-imdb" style="color:#E0C035"></i> 9.2</a></div></td><td class="embedded"><a href="download.php?id=507&amp;passkey=cc0f2413d63a3a7f43964154d23ac2bb"><i class="download icon pt-xiazai fcg" alt="download" title="下载本种"></i></a><br><a id="bookmark4" href="javascript: bookmark(507,4);"><i class="delbookmark icon pt-wuxing fca" alt="Unbookmarked" title="收藏"></i></a><a id="myrss4" href="javascript: myrss(507,4);"><i class="delmyrss icon pt-rss fca" alt="Unmyrssed" title="加入"></i></a></td></tr></tbody></table>
</td>
</tr></tbody></table></td><td class="rowfollow" width="40"><div class="w30"><span class="fwb">18</span><br></div></td><td class="rowfollow"><b><a href="details.php?id=507&amp;hit=1&amp;cmtpage=1#startcomments">85</a></b></td><td class="rowfollow nowrap"><span title="2020-09-30 23:22:28">1年<br>7月</span></td><td class="rowfollow">158.57<br>GB</td><td class="rowfollow" align="center"><b><a href="details.php?id=507&amp;hit=1&amp;dllist=1#seeders">335</a></b></td>
<td class="rowfollow"><b><a href="details.php?id=507&amp;hit=1&amp;dllist=1#leechers">8</a></b></td>
<td class="rowfollow"><a href="viewsnatches.php?id=507"><b>2,030</b></a></td>
<td class="rowfollow">-</td><td class="rowfollow"><a href="userdetails.php?id=2" class="StaffLeader_Name"><b>匿名者</b></a></td>
<td class="rowfollow"></td>
</tr>
<tr class="sticky_normal">
<td class="rowfollow nowrap" valign="middle"><a class="dib" href="?cat=402"><img src="pic/dot.png" alt="TV Series(电视剧)" title="TV Series(电视剧)"><span class="category dib c_tvseries" alt="TV Series(电视剧)" title="TV Series(电视剧)"></span></a></td>
<td class="rowfollow" width="100%" align="left"><table class="torrentname" width="100%"><tbody><tr class="sticky_normal"><td class="torrentimg"><img class="pr5" src="/public/douban/6952149.jpg" height="52" onmouseover="showmenu(this,'tid_412','/public/douban/6952149.jpg');" onmouseout="hiddmenu(this,'tid_412');"></td><td class="embedded"><i class="sticky icon pt-huobao fcr" alt="Sticky" title="置顶"></i>&nbsp;<a target="_blank" class="torrentname" title="Breaking Bad S01-S05 2160p WEB-DL 5xRus Ukr Eng TrollUHD-ULTRAHDCLUB" href="details.php?id=412&amp;hit=1"><b class="promotion">Breaking Bad S01-S05 2160p WEB-DL 5xRus Ukr Eng TrollUHD-ULTRAHDCLUB</b></a> <font class="promotion halfdown">50%免费</font>  <i class="icon pt-shipin fc2"></i> <font class="promotion b4">字幕/附件(1)</font> <br>绝命毒师 全五季 4K录制版 顶级片源</td><td width="20" class="embedded" style="text-align: right; " valign="middle"><table><tbody><tr><td class="embedded"><div style="text-align:right;margin-right:3px;width:50px"><a class="fwb" target="_blank" href="https://movie.douban.com/subject/6952149/"><i class="icon pt-douban fcg"></i> 9.6</a><br><a class="fwb" target="_blank" href="https://www.imdb.com/title/tt2081647/"><i class="icon pt-imdb" style="color:#E0C035"></i> 9.2</a></div></td><td class="embedded"><a href="download.php?id=412&amp;passkey=cc0f2413d63a3a7f43964154d23ac2bb"><i class="download icon pt-xiazai fcg" alt="download" title="下载本种"></i></a><br><a id="bookmark5" href="javascript: bookmark(412,5);"><i class="delbookmark icon pt-wuxing fca" alt="Unbookmarked" title="收藏"></i></a><a id="myrss5" href="javascript: myrss(412,5);"><i class="delmyrss icon pt-rss fca" alt="Unmyrssed" title="加入"></i></a></td></tr></tbody></table>
</td>
</tr></tbody></table></td><td class="rowfollow" width="40"><div class="w30"><span class="fwb">5</span><br></div></td><td class="rowfollow"><b><a href="details.php?id=412&amp;hit=1&amp;cmtpage=1#startcomments">42</a></b></td><td class="rowfollow nowrap"><span title="2020-08-19 23:29:08">1年<br>9月</span></td><td class="rowfollow">1.704<br>TB</td><td class="rowfollow" align="center"><b><a href="details.php?id=412&amp;hit=1&amp;dllist=1#seeders">205</a></b></td>
<td class="rowfollow"><b><a href="details.php?id=412&amp;hit=1&amp;dllist=1#leechers">9</a></b></td>
<td class="rowfollow"><a href="viewsnatches.php?id=412"><b>464</b></a></td>
<td class="rowfollow">-</td><td class="rowfollow"><a href="userdetails.php?id=2" class="StaffLeader_Name"><b>匿名者</b></a></td>
<td class="rowfollow"></td>
</tr>
<tr class="sticky_normal">
<td class="rowfollow nowrap" valign="middle"><a class="dib" href="?cat=401"><img src="pic/dot.png" alt="Movies(电影)" title="Movies(电影)"><span class="category dib c_movies" alt="Movies(电影)" title="Movies(电影)"></span></a></td>
<td class="rowfollow" width="100%" align="left"><table class="torrentname" width="100%"><tbody><tr class="sticky_normal"><td class="torrentimg"><img class="pr5" src="/public/douban/1291843.jpg" height="52" onmouseover="showmenu(this,'tid_446','/public/douban/1291843.jpg');" onmouseout="hiddmenu(this,'tid_446');"></td><td class="embedded"><i class="sticky icon pt-huobao fcr" alt="Sticky" title="置顶"></i>&nbsp;<a target="_blank" class="torrentname" title="The Matrix Trilogy 1999-2003 UHD Blu-Ray 2160p&amp;1080p HEVC&amp;VC-1 Atmos TrueHD 7 1&amp;5.1-CHDBits" href="details.php?id=446&amp;hit=1"><b class="promotion">The Matrix Trilogy 1999-2003 UHD Blu-Ray 2160p&amp;1080p HEVC&amp;VC-1 Atmos TrueHD 7 1&amp;5.1-CHDBits</b></a> <font class="promotion halfdown">50%免费</font>  <i class="icon pt-shipin fc2"></i> <br>【豆瓣250-59】【豆瓣250-243】【豆瓣250-170】【黑客60-5】黑客帝国三部曲 UHD 4K原盘 &amp; 蓝光1080p原盘..</td><td width="20" class="embedded" style="text-align: right; " valign="middle"><table><tbody><tr><td class="embedded"><div style="text-align:right;margin-right:3px;width:50px"><a class="fwb" target="_blank" href="https://movie.douban.com/subject/1291843/"><i class="icon pt-douban fcg"></i> 9.1</a><br><a class="fwb" target="_blank" href="https://www.imdb.com/title/tt0133093/"><i class="icon pt-imdb" style="color:#E0C035"></i> 8.7</a></div></td><td class="embedded"><a href="download.php?id=446&amp;passkey=cc0f2413d63a3a7f43964154d23ac2bb"><i class="download icon pt-xiazai fcg" alt="download" title="下载本种"></i></a><br><a id="bookmark6" href="javascript: bookmark(446,6);"><i class="delbookmark icon pt-wuxing fca" alt="Unbookmarked" title="收藏"></i></a><a id="myrss6" href="javascript: myrss(446,6);"><i class="delmyrss icon pt-rss fca" alt="Unmyrssed" title="加入"></i></a></td></tr></tbody></table>
</td>
</tr></tbody></table></td><td class="rowfollow" width="40"><div class="w30"><span class="fwb">9</span><br></div></td><td class="rowfollow"><b><a href="details.php?id=446&amp;hit=1&amp;cmtpage=1#startcomments">47</a></b></td><td class="rowfollow nowrap"><span title="2020-09-01 00:14:35">1年<br>8月</span></td><td class="rowfollow">317.89<br>GB</td><td class="rowfollow" align="center"><b><a href="details.php?id=446&amp;hit=1&amp;dllist=1#seeders">240</a></b></td>
<td class="rowfollow"><b><a href="details.php?id=446&amp;hit=1&amp;dllist=1#leechers">40</a></b></td>
<td class="rowfollow"><a href="viewsnatches.php?id=446"><b>1,491</b></a></td>
<td class="rowfollow">-</td><td class="rowfollow"><a href="userdetails.php?id=2" class="StaffLeader_Name"><b>匿名者</b></a></td>
<td class="rowfollow"></td>
</tr>
<tr class="sticky_normal">
<td class="rowfollow nowrap" valign="middle"><a class="dib" href="?cat=412"><img src="pic/dot.png" alt="School(应试、考级、初中以上教育)" title="School(应试、考级、初中以上教育)"><span class="category dib c_school" alt="School(应试、考级、初中以上教育)" title="School(应试、考级、初中以上教育)"></span></a></td>
<td class="rowfollow" width="100%" align="left"><table class="torrentname" width="100%"><tbody><tr class="sticky_normal"><td class="embedded"><i class="sticky icon pt-huobao fcr" alt="Sticky" title="置顶"></i>&nbsp;<a target="_blank" class="torrentname" title="高中数学" href="details.php?id=9353&amp;hit=1"><b class="promotion zeroupzerodown">高中数学</b></a> <b>[<font class="classic">经典</font>]</b> <font class="promotion zeroupzerodown">0流量</font> <br>高中数学教学视频 | 建议根据自身情况，下载里面某一部分即可 | 种子很大，你们要忍一忍（等一等才会下到种子文件）</td><td width="20" class="embedded" style="text-align: right; " valign="middle"><table><tbody><tr><td class="embedded"></td><td class="embedded"><a href="download.php?id=9353&amp;passkey=cc0f2413d63a3a7f43964154d23ac2bb"><i class="download icon pt-xiazai fcg" alt="download" title="下载本种"></i></a><br><a id="bookmark7" href="javascript: bookmark(9353,7);"><i class="delbookmark icon pt-wuxing fca" alt="Unbookmarked" title="收藏"></i></a><a id="myrss7" href="javascript: myrss(9353,7);"><i class="delmyrss icon pt-rss fca" alt="Unmyrssed" title="加入"></i></a></td></tr></tbody></table>
</td>
</tr></tbody></table></td><td class="rowfollow" width="40"><div class="w30"><span class="fwb">2</span><br></div></td><td class="rowfollow"><b><a href="details.php?id=9353&amp;hit=1&amp;cmtpage=1#startcomments">81</a></b></td><td class="rowfollow nowrap"><span title="2021-07-28 11:24:06">9月<br>28天</span></td><td class="rowfollow">1.607<br>TB</td><td class="rowfollow" align="center"><b><a href="details.php?id=9353&amp;hit=1&amp;dllist=1#seeders">30</a></b></td>
<td class="rowfollow"><b><a href="details.php?id=9353&amp;hit=1&amp;dllist=1#leechers">12</a></b></td>
<td class="rowfollow"><a href="viewsnatches.php?id=9353"><b>174</b></a></td>
<td class="rowfollow">-</td><td class="rowfollow"><i>匿名</i></td>
<td class="rowfollow"></td>
</tr>
<tr class="sticky_normal">
<td class="rowfollow nowrap" valign="middle"><a class="dib" href="?cat=450"><img src="pic/dot.png" alt="Resource(资源、素材、模板)" title="Resource(资源、素材、模板)"><span class="category dib c_resource" alt="Resource(资源、素材、模板)" title="Resource(资源、素材、模板)"></span></a></td>
<td class="rowfollow" width="100%" align="left"><table class="torrentname" width="100%"><tbody><tr class="sticky_normal"><td class="embedded"><i class="sticky icon pt-huobao fcr" alt="Sticky" title="置顶"></i>&nbsp;<a target="_blank" class="torrentname" title="Sci-Hub.852.torrents.in.one" href="details.php?id=8466&amp;hit=1"><b class="promotion free">Sci-Hub.852.torrents.in.one</b></a> <b>[<font class="hot">热门</font>]</b> <font class="promotion free">免费</font> <br>Sci-Hub所有850多个种子合集 | Sci-Hub就是一个免费的下载所有SCI文献的网站</td><td width="20" class="embedded" style="text-align: right; " valign="middle"><table><tbody><tr><td class="embedded"></td><td class="embedded"><a href="download.php?id=8466&amp;passkey=cc0f2413d63a3a7f43964154d23ac2bb"><i class="download icon pt-xiazai fcg" alt="download" title="下载本种"></i></a><br><a id="bookmark8" href="javascript: bookmark(8466,8);"><i class="delbookmark icon pt-wuxing fca" alt="Unbookmarked" title="收藏"></i></a><a id="myrss8" href="javascript: myrss(8466,8);"><i class="delmyrss icon pt-rss fca" alt="Unmyrssed" title="加入"></i></a></td></tr></tbody></table>
</td>
</tr></tbody></table></td><td class="rowfollow" width="40"><div class="w30"><span class="fwb">51</span><br></div></td><td class="rowfollow"><b><a href="details.php?id=8466&amp;hit=1&amp;cmtpage=1#startcomments">61</a></b></td><td class="rowfollow nowrap"><span title="2021-07-09 01:25:48">10月<br>17天</span></td><td class="rowfollow">103.60<br>MB</td><td class="rowfollow" align="center"><b><a href="details.php?id=8466&amp;hit=1&amp;dllist=1#seeders">998</a></b></td>
<td class="rowfollow"><b><a href="details.php?id=8466&amp;hit=1&amp;dllist=1#leechers">2</a></b></td>
<td class="rowfollow"><a href="viewsnatches.php?id=8466"><b>5,132</b></a></td>
<td class="rowfollow">-</td><td class="rowfollow"><a href="userdetails.php?id=2" class="StaffLeader_Name"><b>匿名者</b></a></td>
<td class="rowfollow"></td>
</tr>
<tr>
<td class="rowfollow nowrap" valign="middle"><a class="dib" href="?cat=401"><img src="pic/dot.png" alt="Movies(电影)" title="Movies(电影)"><span class="category dib c_movies" alt="Movies(电影)" title="Movies(电影)"></span></a></td>
<td class="rowfollow" width="100%" align="left"><table class="torrentname" width="100%"><tbody><tr><td class="torrentimg"><img class="pr5" src="https://www.pttime.org/attachments/202205/20220522215550299fc38c852c1b3ec97fb8f022651718.jpg" height="52" onmouseover="showmenu(this,'tid_27501','https://www.pttime.org/attachments/202205/20220522215550299fc38c852c1b3ec97fb8f022651718.jpg');" onmouseout="hiddmenu(this,'tid_27501');"></td><td class="embedded"><a target="_blank" class="torrentname" title="Serato.DJ.Pro.v2.0.3.CE-V.R 2018" href="details.php?id=27501&amp;hit=1"><b class="title">Serato.DJ.Pro.v2.0.3.CE-V.R 2018</b></a> <br>Serato 经典DJ软件</td><td width="20" class="embedded" style="text-align: right; " valign="middle"><table><tbody><tr><td class="embedded"><div style="text-align:right;margin-right:3px;width:50px"><a class="fwb" target="_blank" href=""><i class="icon pt-douban fcg"></i> 0.0</a><br><a class="fwb" target="_blank" href=""><i class="icon pt-imdb" style="color:#E0C035"></i> ----</a></div></td><td class="embedded"><a href="download.php?id=27501&amp;passkey=cc0f2413d63a3a7f43964154d23ac2bb"><i class="download icon pt-xiazai fcg" alt="download" title="下载本种"></i></a><br><a id="bookmark9" href="javascript: bookmark(27501,9);"><i class="delbookmark icon pt-wuxing fca" alt="Unbookmarked" title="收藏"></i></a><a id="myrss9" href="javascript: myrss(27501,9);"><i class="delmyrss icon pt-rss fca" alt="Unmyrssed" title="加入"></i></a></td></tr></tbody></table>
</td>
</tr></tbody></table></td><td class="rowfollow" width="40"><div class="w30"><span class="fwb">0</span><br></div></td><td class="rowfollow"><a href="comment.php?action=add&amp;pid=27501&amp;type=torrent" title="添加评论">0</a></td><td class="rowfollow nowrap"><span title="2022-05-22 21:57:06">1时<br>37分</span></td><td class="rowfollow">50.70<br>MB</td><td class="rowfollow"><span class="red">0</span></td>
<td class="rowfollow"><b><a href="details.php?id=27501&amp;hit=1&amp;dllist=1#leechers">1</a></b></td>
<td class="rowfollow">0</td>
<td class="rowfollow">-</td><td class="rowfollow"><i>匿名</i></td>
<td class="rowfollow"></td>
</tr>
<tr>
<td class="rowfollow nowrap" valign="middle"><a class="dib" href="?cat=402"><img src="pic/dot.png" alt="TV Series(电视剧)" title="TV Series(电视剧)"><span class="category dib c_tvseries" alt="TV Series(电视剧)" title="TV Series(电视剧)"></span></a></td>
<td class="rowfollow" width="100%" align="left"><table class="torrentname" width="100%"><tbody><tr><td class="torrentimg"><img class="pr5" src="/public/douban/35235301.jpg" height="52" onmouseover="showmenu(this,'tid_27500','/public/douban/35235301.jpg');" onmouseout="hiddmenu(this,'tid_27500');"></td><td class="embedded"><a target="_blank" class="torrentname" title="Day Breaker S01E01-E06 2022 1080p WEB-DL H.264 AAC-TJUPT" href="details.php?id=27500&amp;hit=1"><b class="title">Day Breaker S01E01-E06 2022 1080p WEB-DL H.264 AAC-TJUPT</b></a> <br>暗夜行者丨周日至周二20点更新丨主演: 李易峰 / 宋轶 / 冯德伦丨TJUPT小组出品 转载请注明转自北洋园PT</td><td width="20" class="embedded" style="text-align: right; " valign="middle"><table><tbody><tr><td class="embedded"><div style="text-align:right;margin-right:3px;width:50px"><a class="fwb" target="_blank" href="https://movie.douban.com/subject/35235301/"><i class="icon pt-douban fcg"></i> 0.0</a><br><a class="fwb" target="_blank" href=""><i class="icon pt-imdb" style="color:#E0C035"></i> ----</a></div></td><td class="embedded"><a href="download.php?id=27500&amp;passkey=cc0f2413d63a3a7f43964154d23ac2bb"><i class="download icon pt-xiazai fcg" alt="download" title="下载本种"></i></a><br><a id="bookmark10" href="javascript: bookmark(27500,10);"><i class="delbookmark icon pt-wuxing fca" alt="Unbookmarked" title="收藏"></i></a><a id="myrss10" href="javascript: myrss(27500,10);"><i class="delmyrss icon pt-rss fca" alt="Unmyrssed" title="加入"></i></a></td></tr></tbody></table>
</td>
</tr></tbody></table></td><td class="rowfollow" width="40"><div class="w30"><span class="fwb">0</span><br></div></td><td class="rowfollow"><a href="comment.php?action=add&amp;pid=27500&amp;type=torrent" title="添加评论">0</a></td><td class="rowfollow nowrap"><span title="2022-05-22 21:48:34">1时<br>46分</span></td><td class="rowfollow">3.71<br>GB</td><td class="rowfollow" align="center"><b><a href="details.php?id=27500&amp;hit=1&amp;dllist=1#seeders">6</a></b></td>
<td class="rowfollow">0</td>
<td class="rowfollow"><a href="viewsnatches.php?id=27500"><b>1</b></a></td>
<td class="rowfollow">-</td><td class="rowfollow"><i>匿名</i></td>
<td class="rowfollow"></td>
</tr>
<tr>
<td class="rowfollow nowrap" valign="middle"><a class="dib" href="?cat=402"><img src="pic/dot.png" alt="TV Series(电视剧)" title="TV Series(电视剧)"><span class="category dib c_tvseries" alt="TV Series(电视剧)" title="TV Series(电视剧)"></span></a></td>
<td class="rowfollow" width="100%" align="left"><table class="torrentname" width="100%"><tbody><tr><td class="torrentimg"><img class="pr5" src="/public/douban/35371695.jpg" height="52" onmouseover="showmenu(this,'tid_27499','/public/douban/35371695.jpg');" onmouseout="hiddmenu(this,'tid_27499');"></td><td class="embedded"><a target="_blank" class="torrentname" title="Defying the Storm S01E11-E12 2022 1080p WEB-DL H.264 AAC-TJUPT" href="details.php?id=27499&amp;hit=1"><b class="title">Defying the Storm S01E11-E12 2022 1080p WEB-DL H.264 AAC-TJUPT</b></a> <br>凭栏一片风云起丨每日20点更新丨TJUPT小组出品 转载请注明转自北洋园PT</td><td width="20" class="embedded" style="text-align: right; " valign="middle"><table><tbody><tr><td class="embedded"><div style="text-align:right;margin-right:3px;width:50px"><a class="fwb" target="_blank" href="https://movie.douban.com/subject/35371695/"><i class="icon pt-douban fcg"></i> 0.0</a><br><a class="fwb" target="_blank" href=""><i class="icon pt-imdb" style="color:#E0C035"></i> ----</a></div></td><td class="embedded"><a href="download.php?id=27499&amp;passkey=cc0f2413d63a3a7f43964154d23ac2bb"><i class="download icon pt-xiazai fcg" alt="download" title="下载本种"></i></a><br><a id="bookmark11" href="javascript: bookmark(27499,11);"><i class="delbookmark icon pt-wuxing fca" alt="Unbookmarked" title="收藏"></i></a><a id="myrss11" href="javascript: myrss(27499,11);"><i class="delmyrss icon pt-rss fca" alt="Unmyrssed" title="加入"></i></a></td></tr></tbody></table>
</td>
</tr></tbody></table></td><td class="rowfollow" width="40"><div class="w30"><span class="fwb">0</span><br></div></td><td class="rowfollow"><a href="comment.php?action=add&amp;pid=27499&amp;type=torrent" title="添加评论">0</a></td><td class="rowfollow nowrap"><span title="2022-05-22 21:40:02">1时<br>55分</span></td><td class="rowfollow">1.14<br>GB</td><td class="rowfollow" align="center"><b><a href="details.php?id=27499&amp;hit=1&amp;dllist=1#seeders">3</a></b></td>
<td class="rowfollow"><b><a href="details.php?id=27499&amp;hit=1&amp;dllist=1#leechers">2</a></b></td>
<td class="rowfollow">0</td>
<td class="rowfollow">-</td><td class="rowfollow"><i>匿名</i></td>
<td class="rowfollow"></td>
</tr>
<tr>
<td class="rowfollow nowrap" valign="middle"><a class="dib" href="?cat=402"><img src="pic/dot.png" alt="TV Series(电视剧)" title="TV Series(电视剧)"><span class="category dib c_tvseries" alt="TV Series(电视剧)" title="TV Series(电视剧)"></span></a></td>
<td class="rowfollow" width="100%" align="left"><table class="torrentname" width="100%"><tbody><tr><td class="torrentimg"><img class="pr5" src="/public/douban/35134545.jpg" height="52" onmouseover="showmenu(this,'tid_27498','/public/douban/35134545.jpg');" onmouseout="hiddmenu(this,'tid_27498');"></td><td class="embedded"><a target="_blank" class="torrentname" title="Lady of Law S01E31-32 2022 1080p WEB-DL H.264 AAC-TJUPT" href="details.php?id=27498&amp;hit=1"><b class="title">Lady of Law S01E31-32 2022 1080p WEB-DL H.264 AAC-TJUPT</b></a> <br>女士的法则 / 漂亮的她们 / 她们的生活 1080P | 第31-32集 | 主演：江疏影 / 刘敏涛 / 彭昱畅 | TJUPT小组..</td><td width="20" class="embedded" style="text-align: right; " valign="middle"><table><tbody><tr><td class="embedded"><div style="text-align:right;margin-right:3px;width:50px"><a class="fwb" target="_blank" href="https://movie.douban.com/subject/35134545/"><i class="icon pt-douban fcg"></i> 0.0</a><br><a class="fwb" target="_blank" href=""><i class="icon pt-imdb" style="color:#E0C035"></i> ----</a></div></td><td class="embedded"><a href="download.php?id=27498&amp;passkey=cc0f2413d63a3a7f43964154d23ac2bb"><i class="download icon pt-xiazai fcg" alt="download" title="下载本种"></i></a><br><a id="bookmark12" href="javascript: bookmark(27498,12);"><i class="delbookmark icon pt-wuxing fca" alt="Unbookmarked" title="收藏"></i></a><a id="myrss12" href="javascript: myrss(27498,12);"><i class="delmyrss icon pt-rss fca" alt="Unmyrssed" title="加入"></i></a></td></tr></tbody></table>
</td>
</tr></tbody></table></td><td class="rowfollow" width="40"><div class="w30"><span class="fwb">0</span><br></div></td><td class="rowfollow"><a href="comment.php?action=add&amp;pid=27498&amp;type=torrent" title="添加评论">0</a></td><td class="rowfollow nowrap"><span title="2022-05-22 21:36:29">1时<br>58分</span></td><td class="rowfollow">897.37<br>MB</td><td class="rowfollow" align="center"><b><a href="details.php?id=27498&amp;hit=1&amp;dllist=1#seeders">1</a></b></td>
<td class="rowfollow"><b><a href="details.php?id=27498&amp;hit=1&amp;dllist=1#leechers">1</a></b></td>
<td class="rowfollow">0</td>
<td class="rowfollow">-</td><td class="rowfollow"><i>匿名</i></td>
<td class="rowfollow"></td>
</tr>
<tr>
<td class="rowfollow nowrap" valign="middle"><a class="dib" href="?cat=401"><img src="pic/dot.png" alt="Movies(电影)" title="Movies(电影)"><span class="category dib c_movies" alt="Movies(电影)" title="Movies(电影)"></span></a></td>
<td class="rowfollow" width="100%" align="left"><table class="torrentname" width="100%"><tbody><tr><td class="torrentimg"><img class="pr5" src="https://www.pttime.org/attachments/202205/20220522213552e09fddb73ce95bc05b2cbcda62cd9a3e.jpg" height="52" onmouseover="showmenu(this,'tid_27497','https://www.pttime.org/attachments/202205/20220522213552e09fddb73ce95bc05b2cbcda62cd9a3e.jpg');" onmouseout="hiddmenu(this,'tid_27497');"></td><td class="embedded"><a target="_blank" class="torrentname" title="Redshift3D Redshift Renderer V 2.6.41 For Cinema4D 64Bit Win" href="details.php?id=27497&amp;hit=1"><b class="title">Redshift3D Redshift Renderer V 2.6.41 For Cinema4D 64Bit Win</b></a> <br>红移渲染 2.6.4.1 Cinema4D x64</td><td width="20" class="embedded" style="text-align: right; " valign="middle"><table><tbody><tr><td class="embedded"><div style="text-align:right;margin-right:3px;width:50px"><a class="fwb" target="_blank" href=""><i class="icon pt-douban fcg"></i> 0.0</a><br><a class="fwb" target="_blank" href=""><i class="icon pt-imdb" style="color:#E0C035"></i> ----</a></div></td><td class="embedded"><a href="download.php?id=27497&amp;passkey=cc0f2413d63a3a7f43964154d23ac2bb"><i class="download icon pt-xiazai fcg" alt="download" title="下载本种"></i></a><br><a id="bookmark13" href="javascript: bookmark(27497,13);"><i class="delbookmark icon pt-wuxing fca" alt="Unbookmarked" title="收藏"></i></a><a id="myrss13" href="javascript: myrss(27497,13);"><i class="delmyrss icon pt-rss fca" alt="Unmyrssed" title="加入"></i></a></td></tr></tbody></table>
</td>
</tr></tbody></table></td><td class="rowfollow" width="40"><div class="w30"><span class="fwb">0</span><br></div></td><td class="rowfollow"><a href="comment.php?action=add&amp;pid=27497&amp;type=torrent" title="添加评论">0</a></td><td class="rowfollow nowrap"><span title="2022-05-22 21:36:08">1时<br>58分</span></td><td class="rowfollow">413.89<br>MB</td><td class="rowfollow" align="center"><b><a href="details.php?id=27497&amp;hit=1&amp;dllist=1#seeders">1</a></b></td>
<td class="rowfollow"><b><a href="details.php?id=27497&amp;hit=1&amp;dllist=1#leechers">2</a></b></td>
<td class="rowfollow">0</td>
<td class="rowfollow">-</td><td class="rowfollow"><i>匿名</i></td>
<td class="rowfollow"></td>
</tr>
<tr>
<td class="rowfollow nowrap" valign="middle"><a class="dib" href="?cat=402"><img src="pic/dot.png" alt="TV Series(电视剧)" title="TV Series(电视剧)"><span class="category dib c_tvseries" alt="TV Series(电视剧)" title="TV Series(电视剧)"></span></a></td>
<td class="rowfollow" width="100%" align="left"><table class="torrentname" width="100%"><tbody><tr><td class="torrentimg"><img class="pr5" src="/public/douban/34991672.jpg" height="52" onmouseover="showmenu(this,'tid_27494','/public/douban/34991672.jpg');" onmouseout="hiddmenu(this,'tid_27494');"></td><td class="embedded"><a target="_blank" class="torrentname" title="With You 2020 2160p WEB-DL H.265 10bit HDR DDP-LeagueWEB" href="details.php?id=27494&amp;hit=1"><b class="promotion thirtypercent">With You 2020 2160p WEB-DL H.265 10bit HDR DDP-LeagueWEB</b></a> <font class="promotion thirtypercent">30%免费</font> <span title="2022-05-29 21:28:09">6天21时</span><br>在一起 全20集 | 类型:剧情/医疗 主演:张嘉益/周一围/谭卓/张天爱/何蓝逗/梅婷/雷佳音/倪妮 国语中字 | *4K*10bit..</td><td width="20" class="embedded" style="text-align: right; " valign="middle"><table><tbody><tr><td class="embedded"><div style="text-align:right;margin-right:3px;width:50px"><a class="fwb" target="_blank" href="https://movie.douban.com/subject/34991672/"><i class="icon pt-douban fcg"></i> 8.5</a><br><a class="fwb" target="_blank" href="https://www.imdb.com/title/tt12342516/"><i class="icon pt-imdb" style="color:#E0C035"></i> 7.7</a></div></td><td class="embedded"><a href="download.php?id=27494&amp;passkey=cc0f2413d63a3a7f43964154d23ac2bb"><i class="download icon pt-xiazai fcg" alt="download" title="下载本种"></i></a><br><a id="bookmark14" href="javascript: bookmark(27494,14);"><i class="delbookmark icon pt-wuxing fca" alt="Unbookmarked" title="收藏"></i></a><a id="myrss14" href="javascript: myrss(27494,14);"><i class="delmyrss icon pt-rss fca" alt="Unmyrssed" title="加入"></i></a></td></tr></tbody></table>
</td>
</tr></tbody></table></td><td class="rowfollow" width="40"><div class="w30"><span class="fwb">0</span><br></div></td><td class="rowfollow"><a href="comment.php?action=add&amp;pid=27494&amp;type=torrent" title="添加评论">0</a></td><td class="rowfollow nowrap"><span title="2022-05-22 21:28:09">2时<br>6分</span></td><td class="rowfollow">87.24<br>GB</td><td class="rowfollow"><span class="red">0</span></td>
<td class="rowfollow"><b><a href="details.php?id=27494&amp;hit=1&amp;dllist=1#leechers">4</a></b></td>
<td class="rowfollow">0</td>
<td class="rowfollow">-</td><td class="rowfollow"><i>匿名</i></td>
<td class="rowfollow"></td>
</tr>
<tr>
<td class="rowfollow nowrap" valign="middle"><a class="dib" href="?cat=402"><img src="pic/dot.png" alt="TV Series(电视剧)" title="TV Series(电视剧)"><span class="category dib c_tvseries" alt="TV Series(电视剧)" title="TV Series(电视剧)"></span></a></td>
<td class="rowfollow" width="100%" align="left"><table class="torrentname" width="100%"><tbody><tr><td class="torrentimg"><img class="pr5" src="/public/douban/26864184.jpg" height="52" onmouseover="showmenu(this,'tid_27490','/public/douban/26864184.jpg');" onmouseout="hiddmenu(this,'tid_27490');"></td><td class="embedded"><a target="_blank" class="torrentname" title="Lost in Love 2018 Complete 2160p WEB-DL H.265 AAC-LeagueWEB" href="details.php?id=27490&amp;hit=1"><b class="promotion twoup">Lost in Love 2018 Complete 2160p WEB-DL H.265 AAC-LeagueWEB</b></a> <font class="promotion twoup">2X上传</font> <span title="2022-05-29 21:17:09">6天21时</span><br>脱身/脱身者 DVD版 全46集 *4K* 国语中字</td><td width="20" class="embedded" style="text-align: right; " valign="middle"><table><tbody><tr><td class="embedded"><div style="text-align:right;margin-right:3px;width:50px"><a class="fwb" target="_blank" href="https://movie.douban.com/subject/26864184/"><i class="icon pt-douban fcg"></i> 6.6</a><br><a class="fwb" target="_blank" href="https://www.imdb.com/title/tt8703272/"><i class="icon pt-imdb" style="color:#E0C035"></i> 8.1</a></div></td><td class="embedded"><a href="download.php?id=27490&amp;passkey=cc0f2413d63a3a7f43964154d23ac2bb"><i class="download icon pt-xiazai fcg" alt="download" title="下载本种"></i></a><br><a id="bookmark15" href="javascript: bookmark(27490,15);"><i class="delbookmark icon pt-wuxing fca" alt="Unbookmarked" title="收藏"></i></a><a id="myrss15" href="javascript: myrss(27490,15);"><i class="delmyrss icon pt-rss fca" alt="Unmyrssed" title="加入"></i></a></td></tr></tbody></table>
</td>
</tr></tbody></table></td><td class="rowfollow" width="40"><div class="w30"><span class="fwb">0</span><br></div></td><td class="rowfollow"><a href="comment.php?action=add&amp;pid=27490&amp;type=torrent" title="添加评论">0</a></td><td class="rowfollow nowrap"><span title="2022-05-22 21:17:09">2时<br>17分</span></td><td class="rowfollow">55.35<br>GB</td><td class="rowfollow" align="center"><b><a href="details.php?id=27490&amp;hit=1&amp;dllist=1#seeders"><font color="#550000">1</font></a></b></td>
<td class="rowfollow"><b><a href="details.php?id=27490&amp;hit=1&amp;dllist=1#leechers">4</a></b></td>
<td class="rowfollow">0</td>
<td class="rowfollow">-</td><td class="rowfollow"><i>匿名</i></td>
<td class="rowfollow"></td>
</tr>
<tr>
<td class="rowfollow nowrap" valign="middle"><a class="dib" href="?cat=402"><img src="pic/dot.png" alt="TV Series(电视剧)" title="TV Series(电视剧)"><span class="category dib c_tvseries" alt="TV Series(电视剧)" title="TV Series(电视剧)"></span></a></td>
<td class="rowfollow" width="100%" align="left"><table class="torrentname" width="100%"><tbody><tr><td class="torrentimg"><img class="pr5" src="/public/douban/35359490.jpg" height="52" onmouseover="showmenu(this,'tid_27489','/public/douban/35359490.jpg');" onmouseout="hiddmenu(this,'tid_27489');"></td><td class="embedded"><a target="_blank" class="torrentname" title="Be Reborn S01 2022 4K WEB-DL H.265 AAC-HaresWEB" href="details.php?id=27489&amp;hit=1"><b class="title">Be Reborn S01 2022 4K WEB-DL H.265 AAC-HaresWEB</b></a>  <i class="icon pt-shipin fc2"></i> <br><span class="tags zz">中字</span><span class="tags gy">国语</span>重生之门 全26集 | 导演：杨冬 | 主演：张译 王俊凯 冯文娟 普通话 中字</td><td width="20" class="embedded" style="text-align: right; " valign="middle"><table><tbody><tr><td class="embedded"><div style="text-align:right;margin-right:3px;width:50px"><a class="fwb" target="_blank" href="https://movie.douban.com/subject/35359490/"><i class="icon pt-douban fcg"></i> 0.0</a><br><a class="fwb" target="_blank" href=""><i class="icon pt-imdb" style="color:#E0C035"></i> ----</a></div></td><td class="embedded"><a href="download.php?id=27489&amp;passkey=cc0f2413d63a3a7f43964154d23ac2bb"><i class="download icon pt-xiazai fcg" alt="download" title="下载本种"></i></a><br><a id="bookmark16" href="javascript: bookmark(27489,16);"><i class="delbookmark icon pt-wuxing fca" alt="Unbookmarked" title="收藏"></i></a><a id="myrss16" href="javascript: myrss(27489,16);"><i class="delmyrss icon pt-rss fca" alt="Unmyrssed" title="加入"></i></a></td></tr></tbody></table>
</td>
</tr></tbody></table></td><td class="rowfollow" width="40"><div class="w30"><span class="fwb">0</span><br></div></td><td class="rowfollow"><a href="comment.php?action=add&amp;pid=27489&amp;type=torrent" title="添加评论">0</a></td><td class="rowfollow nowrap"><span title="2022-05-22 21:15:36">2时<br>19分</span></td><td class="rowfollow">33.84<br>GB</td><td class="rowfollow" align="center"><b><a href="details.php?id=27489&amp;hit=1&amp;dllist=1#seeders">3</a></b></td>
<td class="rowfollow"><b><a href="details.php?id=27489&amp;hit=1&amp;dllist=1#leechers">8</a></b></td>
<td class="rowfollow">0</td>
<td class="rowfollow">-</td><td class="rowfollow"><i>匿名</i></td>
<td class="rowfollow"></td>
</tr>
<tr>
<td class="rowfollow nowrap" valign="middle"><a class="dib" href="?cat=402"><img src="pic/dot.png" alt="TV Series(电视剧)" title="TV Series(电视剧)"><span class="category dib c_tvseries" alt="TV Series(电视剧)" title="TV Series(电视剧)"></span></a></td>
<td class="rowfollow" width="100%" align="left"><table class="torrentname" width="100%"><tbody><tr><td class="torrentimg"><img class="pr5" src="/public/douban/1830590.jpg" height="52" onmouseover="showmenu(this,'tid_27488','/public/douban/1830590.jpg');" onmouseout="hiddmenu(this,'tid_27488');"></td><td class="embedded"><a target="_blank" class="torrentname" title="Kang Xi Kingdom 2001 2160p WEB-DL H.265 AAC-HotWEB" href="details.php?id=27488&amp;hit=1"><b class="title">Kang Xi Kingdom 2001 2160p WEB-DL H.265 AAC-HotWEB</b></a> <br>Kang Xi di guo / 康熙帝国 / 康熙大帝 / Kang Xi Kingdom | 类别：剧情  爱情  传记  历史</td><td width="20" class="embedded" style="text-align: right; " valign="middle"><table><tbody><tr><td class="embedded"><div style="text-align:right;margin-right:3px;width:50px"><a class="fwb" target="_blank" href="https://movie.douban.com/subject/1830590/"><i class="icon pt-douban fcg"></i> 9.2</a><br><a class="fwb" target="_blank" href="https://www.imdb.com/title/tt0331137/"><i class="icon pt-imdb" style="color:#E0C035"></i> 8.1</a></div></td><td class="embedded"><a href="download.php?id=27488&amp;passkey=cc0f2413d63a3a7f43964154d23ac2bb"><i class="download icon pt-xiazai fcg" alt="download" title="下载本种"></i></a><br><a id="bookmark17" href="javascript: bookmark(27488,17);"><i class="delbookmark icon pt-wuxing fca" alt="Unbookmarked" title="收藏"></i></a><a id="myrss17" href="javascript: myrss(27488,17);"><i class="delmyrss icon pt-rss fca" alt="Unmyrssed" title="加入"></i></a></td></tr></tbody></table>
</td>
</tr></tbody></table></td><td class="rowfollow" width="40"><div class="w30"><span class="fwb">0</span><br></div></td><td class="rowfollow"><a href="comment.php?action=add&amp;pid=27488&amp;type=torrent" title="添加评论">0</a></td><td class="rowfollow nowrap"><span title="2022-05-22 21:15:30">2时<br>19分</span></td><td class="rowfollow">68.27<br>GB</td><td class="rowfollow" align="center"><b><a href="details.php?id=27488&amp;hit=1&amp;dllist=1#seeders">3</a></b></td>
<td class="rowfollow"><b><a href="details.php?id=27488&amp;hit=1&amp;dllist=1#leechers">3</a></b></td>
<td class="rowfollow">0</td>
<td class="rowfollow">-</td><td class="rowfollow"><a href="userdetails.php?id=47939" class="User_Name"><b>nanook</b></a></td>
<td class="rowfollow"></td>
</tr>
<tr>
<td class="rowfollow nowrap" valign="middle"><a class="dib" href="?cat=402"><img src="pic/dot.png" alt="TV Series(电视剧)" title="TV Series(电视剧)"><span class="category dib c_tvseries" alt="TV Series(电视剧)" title="TV Series(电视剧)"></span></a></td>
<td class="rowfollow" width="100%" align="left"><table class="torrentname" width="100%"><tbody><tr><td class="torrentimg"><img class="pr5" src="/public/douban/26344999.jpg" height="52" onmouseover="showmenu(this,'tid_27485','/public/douban/26344999.jpg');" onmouseout="hiddmenu(this,'tid_27485');"></td><td class="embedded"><a target="_blank" class="torrentname" title="The Princess Wei Yang 2016 Complete  2160p WEB-DL H.265 AAC-LeagueWEB" href="details.php?id=27485&amp;hit=1"><b class="title">The Princess Wei Yang 2016 Complete  2160p WEB-DL H.265 AAC-LeagueWEB</b></a> <br>锦绣未央 *全54集 2160p* 主演:唐嫣 罗晋 吴建豪</td><td width="20" class="embedded" style="text-align: right; " valign="middle"><table><tbody><tr><td class="embedded"><div style="text-align:right;margin-right:3px;width:50px"><a class="fwb" target="_blank" href="https://movie.douban.com/subject/26344999/"><i class="icon pt-douban fcg"></i> 4.8</a><br><a class="fwb" target="_blank" href="https://www.imdb.com/title/tt6353308/"><i class="icon pt-imdb" style="color:#E0C035"></i> 0.0</a></div></td><td class="embedded"><a href="download.php?id=27485&amp;passkey=cc0f2413d63a3a7f43964154d23ac2bb"><i class="download icon pt-xiazai fcg" alt="download" title="下载本种"></i></a><br><a id="bookmark18" href="javascript: bookmark(27485,18);"><i class="delbookmark icon pt-wuxing fca" alt="Unbookmarked" title="收藏"></i></a><a id="myrss18" href="javascript: myrss(27485,18);"><i class="delmyrss icon pt-rss fca" alt="Unmyrssed" title="加入"></i></a></td></tr></tbody></table>
</td>
</tr></tbody></table></td><td class="rowfollow" width="40"><div class="w30"><span class="fwb">0</span><br></div></td><td class="rowfollow"><a href="comment.php?action=add&amp;pid=27485&amp;type=torrent" title="添加评论">0</a></td><td class="rowfollow nowrap"><span title="2022-05-22 20:35:40">2时<br>59分</span></td><td class="rowfollow">55.44<br>GB</td><td class="rowfollow" align="center"><b><a href="details.php?id=27485&amp;hit=1&amp;dllist=1#seeders">3</a></b></td>
<td class="rowfollow"><b><a href="details.php?id=27485&amp;hit=1&amp;dllist=1#leechers">4</a></b></td>
<td class="rowfollow"><a href="viewsnatches.php?id=27485"><b>3</b></a></td>
<td class="rowfollow">-</td><td class="rowfollow"><i>匿名</i></td>
<td class="rowfollow"></td>
</tr>
<tr>
<td class="rowfollow nowrap" valign="middle"><a class="dib" href="?cat=402"><img src="pic/dot.png" alt="TV Series(电视剧)" title="TV Series(电视剧)"><span class="category dib c_tvseries" alt="TV Series(电视剧)" title="TV Series(电视剧)"></span></a></td>
<td class="rowfollow" width="100%" align="left"><table class="torrentname" width="100%"><tbody><tr><td class="torrentimg"><img class="pr5" src="/public/douban/20393797.jpg" height="52" onmouseover="showmenu(this,'tid_27483','/public/douban/20393797.jpg');" onmouseout="hiddmenu(this,'tid_27483');"></td><td class="embedded"><a target="_blank" class="torrentname" title="Wo De Kang Zhan Zhi Lie Bao Tu Ji 2012 S01 Complete 2160p WEB-DL H.265 AAC-LeagueWEB" href="details.php?id=27483&amp;hit=1"><b class="title">Wo De Kang Zhan Zhi Lie Bao Tu Ji 2012 S01 Complete 2160p WEB-DL H.265 AAC-LeagueWEB</b></a> <br>我的抗战之猎豹突击/我的抗战2/猎豹突击  全40集 |  类型:剧情/战争  主演:朱泳腾/刘思彤/魏春光  国语中字 | *4k*</td><td width="20" class="embedded" style="text-align: right; " valign="middle"><table><tbody><tr><td class="embedded"><div style="text-align:right;margin-right:3px;width:50px"><a class="fwb" target="_blank" href="https://movie.douban.com/subject/20393797/"><i class="icon pt-douban fcg"></i> 3.7</a><br><a class="fwb" target="_blank" href=""><i class="icon pt-imdb" style="color:#E0C035"></i> ----</a></div></td><td class="embedded"><a href="download.php?id=27483&amp;passkey=cc0f2413d63a3a7f43964154d23ac2bb"><i class="download icon pt-xiazai fcg" alt="download" title="下载本种"></i></a><br><a id="bookmark19" href="javascript: bookmark(27483,19);"><i class="delbookmark icon pt-wuxing fca" alt="Unbookmarked" title="收藏"></i></a><a id="myrss19" href="javascript: myrss(27483,19);"><i class="delmyrss icon pt-rss fca" alt="Unmyrssed" title="加入"></i></a></td></tr></tbody></table>
</td>
</tr></tbody></table></td><td class="rowfollow" width="40"><div class="w30"><span class="fwb">0</span><br></div></td><td class="rowfollow"><a href="comment.php?action=add&amp;pid=27483&amp;type=torrent" title="添加评论">0</a></td><td class="rowfollow nowrap"><span title="2022-05-22 20:29:40">3时<br>5分</span></td><td class="rowfollow">55.56<br>GB</td><td class="rowfollow" align="center"><b><a href="details.php?id=27483&amp;hit=1&amp;dllist=1#seeders">2</a></b></td>
<td class="rowfollow"><b><a href="details.php?id=27483&amp;hit=1&amp;dllist=1#leechers">3</a></b></td>
<td class="rowfollow"><a href="viewsnatches.php?id=27483"><b>1</b></a></td>
<td class="rowfollow">-</td><td class="rowfollow"><i>匿名</i></td>
<td class="rowfollow"></td>
</tr>
<tr>
<td class="rowfollow nowrap" valign="middle"><a class="dib" href="?cat=402"><img src="pic/dot.png" alt="TV Series(电视剧)" title="TV Series(电视剧)"><span class="category dib c_tvseries" alt="TV Series(电视剧)" title="TV Series(电视剧)"></span></a></td>
<td class="rowfollow" width="100%" align="left"><table class="torrentname" width="100%"><tbody><tr><td class="torrentimg"><img class="pr5" src="/public/douban/26614082.jpg" height="52" onmouseover="showmenu(this,'tid_27482','/public/douban/26614082.jpg');" onmouseout="hiddmenu(this,'tid_27482');"></td><td class="embedded"><a target="_blank" class="torrentname" title="Fighter of the Destiny 2017 S01 Complete 2160p WEB-DL H.265 AAC-LeagueWEB" href="details.php?id=27482&amp;hit=1"><b class="title">Fighter of the Destiny 2017 S01 Complete 2160p WEB-DL H.265 AAC-LeagueWEB</b></a> <br>择天记 第一季 全56集 | 类型:剧情/奇幻/古装 导演:钟澍佳 主演:鹿晗/古力娜扎/吴倩 国语中字 | *4K*</td><td width="20" class="embedded" style="text-align: right; " valign="middle"><table><tbody><tr><td class="embedded"><div style="text-align:right;margin-right:3px;width:50px"><a class="fwb" target="_blank" href="https://movie.douban.com/subject/26614082/"><i class="icon pt-douban fcg"></i> 4.2</a><br><a class="fwb" target="_blank" href="https://www.imdb.com/title/tt6283378/"><i class="icon pt-imdb" style="color:#E0C035"></i> 6.6</a></div></td><td class="embedded"><a href="download.php?id=27482&amp;passkey=cc0f2413d63a3a7f43964154d23ac2bb"><i class="download icon pt-xiazai fcg" alt="download" title="下载本种"></i></a><br><a id="bookmark20" href="javascript: bookmark(27482,20);"><i class="delbookmark icon pt-wuxing fca" alt="Unbookmarked" title="收藏"></i></a><a id="myrss20" href="javascript: myrss(27482,20);"><i class="delmyrss icon pt-rss fca" alt="Unmyrssed" title="加入"></i></a></td></tr></tbody></table>
</td>
</tr></tbody></table></td><td class="rowfollow" width="40"><div class="w30"><span class="fwb">0</span><br></div></td><td class="rowfollow"><a href="comment.php?action=add&amp;pid=27482&amp;type=torrent" title="添加评论">0</a></td><td class="rowfollow nowrap"><span title="2022-05-22 20:27:10">3时<br>7分</span></td><td class="rowfollow">55.62<br>GB</td><td class="rowfollow" align="center"><b><a href="details.php?id=27482&amp;hit=1&amp;dllist=1#seeders">2</a></b></td>
<td class="rowfollow"><b><a href="details.php?id=27482&amp;hit=1&amp;dllist=1#leechers">3</a></b></td>
<td class="rowfollow"><a href="viewsnatches.php?id=27482"><b>1</b></a></td>
<td class="rowfollow">-</td><td class="rowfollow"><i>匿名</i></td>
<td class="rowfollow"></td>
</tr>
<tr>
<td class="rowfollow nowrap" valign="middle"><a class="dib" href="?cat=402"><img src="pic/dot.png" alt="TV Series(电视剧)" title="TV Series(电视剧)"><span class="category dib c_tvseries" alt="TV Series(电视剧)" title="TV Series(电视剧)"></span></a></td>
<td class="rowfollow" width="100%" align="left"><table class="torrentname" width="100%"><tbody><tr><td class="torrentimg"><img class="pr5" src="/public/douban/30203553.jpg" height="52" onmouseover="showmenu(this,'tid_27481','/public/douban/30203553.jpg');" onmouseout="hiddmenu(this,'tid_27481');"></td><td class="embedded"><a target="_blank" class="torrentname" title="Reborn 2020 V2 2160p WEB-DL H.265 AAC-LeagueWEB" href="details.php?id=27481&amp;hit=1"><b class="title">Reborn 2020 V2 2160p WEB-DL H.265 AAC-LeagueWEB</b></a> <br>重生/白夜重生 全28集 主演：张译 赵子琪 张昊唯 刘冠成 *4K 60帧高码</td><td width="20" class="embedded" style="text-align: right; " valign="middle"><table><tbody><tr><td class="embedded"><div style="text-align:right;margin-right:3px;width:50px"><a class="fwb" target="_blank" href="https://movie.douban.com/subject/30203553/"><i class="icon pt-douban fcg"></i> 6.5</a><br><a class="fwb" target="_blank" href="https://www.imdb.com/title/tt11932060/"><i class="icon pt-imdb" style="color:#E0C035"></i> 6.6</a></div></td><td class="embedded"><a href="download.php?id=27481&amp;passkey=cc0f2413d63a3a7f43964154d23ac2bb"><i class="download icon pt-xiazai fcg" alt="download" title="下载本种"></i></a><br><a id="bookmark21" href="javascript: bookmark(27481,21);"><i class="delbookmark icon pt-wuxing fca" alt="Unbookmarked" title="收藏"></i></a><a id="myrss21" href="javascript: myrss(27481,21);"><i class="delmyrss icon pt-rss fca" alt="Unmyrssed" title="加入"></i></a></td></tr></tbody></table>
</td>
</tr></tbody></table></td><td class="rowfollow" width="40"><div class="w30"><span class="fwb">0</span><br></div></td><td class="rowfollow"><a href="comment.php?action=add&amp;pid=27481&amp;type=torrent" title="添加评论">0</a></td><td class="rowfollow nowrap"><span title="2022-05-22 20:24:35">3时<br>10分</span></td><td class="rowfollow">87.29<br>GB</td><td class="rowfollow" align="center"><b><a href="details.php?id=27481&amp;hit=1&amp;dllist=1#seeders"><font color="#550000">1</font></a></b></td>
<td class="rowfollow"><b><a href="details.php?id=27481&amp;hit=1&amp;dllist=1#leechers">4</a></b></td>
<td class="rowfollow"><a href="viewsnatches.php?id=27481"><b>2</b></a></td>
<td class="rowfollow">-</td><td class="rowfollow"><i>匿名</i></td>
<td class="rowfollow"></td>
</tr>
<tr>
<td class="rowfollow nowrap" valign="middle"><a class="dib" href="?cat=402"><img src="pic/dot.png" alt="TV Series(电视剧)" title="TV Series(电视剧)"><span class="category dib c_tvseries" alt="TV Series(电视剧)" title="TV Series(电视剧)"></span></a></td>
<td class="rowfollow" width="100%" align="left"><table class="torrentname" width="100%"><tbody><tr><td class="torrentimg"><img class="pr5" src="/public/douban/34923491.jpg" height="52" onmouseover="showmenu(this,'tid_27480','/public/douban/34923491.jpg');" onmouseout="hiddmenu(this,'tid_27480');"></td><td class="embedded"><a target="_blank" class="torrentname" title="Word of Honor 2021 2160p Complete WEB-DL 60fps H.265 10bit AAC-LeagueWEB" href="details.php?id=27480&amp;hit=1"><b class="promotion twoup">Word of Honor 2021 2160p Complete WEB-DL 60fps H.265 10bit AAC-LeagueWEB</b></a> <font class="promotion twoup">2X上传</font> <span title="2022-05-29 20:18:43">6天20时</span><br>山河令/天涯客 全36集+彩蛋 | 导演: 成志超/马华干 主演: 张哲瀚/龚俊/周也/马闻远/孙浠伦 国语中字 | *4K*60fps..</td><td width="20" class="embedded" style="text-align: right; " valign="middle"><table><tbody><tr><td class="embedded"><div style="text-align:right;margin-right:3px;width:50px"><a class="fwb" target="_blank" href="https://movie.douban.com/subject/34923491/"><i class="icon pt-douban fcg"></i> 8.6</a><br><a class="fwb" target="_blank" href="https://www.imdb.com/title/tt12458172/"><i class="icon pt-imdb" style="color:#E0C035"></i> 8.6</a></div></td><td class="embedded"><a href="download.php?id=27480&amp;passkey=cc0f2413d63a3a7f43964154d23ac2bb"><i class="download icon pt-xiazai fcg" alt="download" title="下载本种"></i></a><br><a id="bookmark22" href="javascript: bookmark(27480,22);"><i class="delbookmark icon pt-wuxing fca" alt="Unbookmarked" title="收藏"></i></a><a id="myrss22" href="javascript: myrss(27480,22);"><i class="delmyrss icon pt-rss fca" alt="Unmyrssed" title="加入"></i></a></td></tr></tbody></table>
</td>
</tr></tbody></table></td><td class="rowfollow" width="40"><div class="w30"><span class="fwb">0</span><br></div></td><td class="rowfollow"><a href="comment.php?action=add&amp;pid=27480&amp;type=torrent" title="添加评论">0</a></td><td class="rowfollow nowrap"><span title="2022-05-22 20:18:43">3时<br>16分</span></td><td class="rowfollow">87.49<br>GB</td><td class="rowfollow" align="center"><b><a href="details.php?id=27480&amp;hit=1&amp;dllist=1#seeders">2</a></b></td>
<td class="rowfollow"><b><a href="details.php?id=27480&amp;hit=1&amp;dllist=1#leechers">4</a></b></td>
<td class="rowfollow"><a href="viewsnatches.php?id=27480"><b>2</b></a></td>
<td class="rowfollow">-</td><td class="rowfollow"><i>匿名</i></td>
<td class="rowfollow"></td>
</tr>
<tr>
<td class="rowfollow nowrap" valign="middle"><a class="dib" href="?cat=402"><img src="pic/dot.png" alt="TV Series(电视剧)" title="TV Series(电视剧)"><span class="category dib c_tvseries" alt="TV Series(电视剧)" title="TV Series(电视剧)"></span></a></td>
<td class="rowfollow" width="100%" align="left"><table class="torrentname" width="100%"><tbody><tr><td class="torrentimg"><img class="pr5" src="/public/douban/27087788.jpg" height="52" onmouseover="showmenu(this,'tid_27479','/public/douban/27087788.jpg');" onmouseout="hiddmenu(this,'tid_27479');"></td><td class="embedded"><a target="_blank" class="torrentname" title="Growling Tiger And Roaring Dragon 2017 Complete  2160p WEB-DL H.265 10bit AAC-LeagueWEB" href="details.php?id=27479&amp;hit=1"><b class="title">Growling Tiger And Roaring Dragon 2017 Complete  2160p WEB-DL H.265 10bit AAC-LeagueWEB</b></a> <br>虎啸龙吟/军师联盟之虎啸龙吟 全44集 | 主演: 吴秀波 刘涛 李晨 张钧甯 唐艺昕 国语中字 | *10bit*4k*</td><td width="20" class="embedded" style="text-align: right; " valign="middle"><table><tbody><tr><td class="embedded"><div style="text-align:right;margin-right:3px;width:50px"><a class="fwb" target="_blank" href="https://movie.douban.com/subject/27087788/"><i class="icon pt-douban fcg"></i> 8.4</a><br><a class="fwb" target="_blank" href=""><i class="icon pt-imdb" style="color:#E0C035"></i> ----</a></div></td><td class="embedded"><a href="download.php?id=27479&amp;passkey=cc0f2413d63a3a7f43964154d23ac2bb"><i class="download icon pt-xiazai fcg" alt="download" title="下载本种"></i></a><br><a id="bookmark23" href="javascript: bookmark(27479,23);"><i class="delbookmark icon pt-wuxing fca" alt="Unbookmarked" title="收藏"></i></a><a id="myrss23" href="javascript: myrss(27479,23);"><i class="delmyrss icon pt-rss fca" alt="Unmyrssed" title="加入"></i></a></td></tr></tbody></table>
</td>
</tr></tbody></table></td><td class="rowfollow" width="40"><div class="w30"><span class="fwb">0</span><br></div></td><td class="rowfollow"><a href="comment.php?action=add&amp;pid=27479&amp;type=torrent" title="添加评论">0</a></td><td class="rowfollow nowrap"><span title="2022-05-22 20:15:35">3时<br>19分</span></td><td class="rowfollow">82.43<br>GB</td><td class="rowfollow" align="center"><b><a href="details.php?id=27479&amp;hit=1&amp;dllist=1#seeders">1</a></b></td>
<td class="rowfollow"><b><a href="details.php?id=27479&amp;hit=1&amp;dllist=1#leechers">2</a></b></td>
<td class="rowfollow"><a href="viewsnatches.php?id=27479"><b>2</b></a></td>
<td class="rowfollow">-</td><td class="rowfollow"><i>匿名</i></td>
<td class="rowfollow"></td>
</tr>
<tr>
<td class="rowfollow nowrap" valign="middle"><a class="dib" href="?cat=413"><img src="pic/dot.png" alt="Book(书籍、有声书)" title="Book(书籍、有声书)"><span class="category dib c_book" alt="Book(书籍、有声书)" title="Book(书籍、有声书)"></span></a></td>
<td class="rowfollow" width="100%" align="left"><table class="torrentname" width="100%"><tbody><tr><td class="embedded"><a target="_blank" class="torrentname" title="ELearning Pack 477" href="details.php?id=27476&amp;hit=1"><b class="promotion free">ELearning Pack 477</b></a> <font class="promotion free">免费</font> <span title="2022-05-24 20:02:06">1天20时</span><br>在线学习视频 第477包</td><td width="20" class="embedded" style="text-align: right; " valign="middle"><table><tbody><tr><td class="embedded"></td><td class="embedded"><a href="download.php?id=27476&amp;passkey=cc0f2413d63a3a7f43964154d23ac2bb"><i class="download icon pt-xiazai fcg" alt="download" title="下载本种"></i></a><br><a id="bookmark24" href="javascript: bookmark(27476,24);"><i class="delbookmark icon pt-wuxing fca" alt="Unbookmarked" title="收藏"></i></a><a id="myrss24" href="javascript: myrss(27476,24);"><i class="delmyrss icon pt-rss fca" alt="Unmyrssed" title="加入"></i></a></td></tr></tbody></table>
</td>
</tr></tbody></table></td><td class="rowfollow" width="40"><div class="w30"><span class="fwb">0</span><br></div></td><td class="rowfollow"><a href="comment.php?action=add&amp;pid=27476&amp;type=torrent" title="添加评论">0</a></td><td class="rowfollow nowrap"><span title="2022-05-22 20:02:06">3时<br>32分</span></td><td class="rowfollow">230.67<br>GB</td><td class="rowfollow" align="center"><b><a href="details.php?id=27476&amp;hit=1&amp;dllist=1#seeders"><font color="#990000">2</font></a></b></td>
<td class="rowfollow"><b><a href="details.php?id=27476&amp;hit=1&amp;dllist=1#leechers">13</a></b></td>
<td class="rowfollow"><a href="viewsnatches.php?id=27476"><b>2</b></a></td>
<td class="rowfollow">-</td><td class="rowfollow"><i>匿名</i></td>
<td class="rowfollow"></td>
</tr>
<tr>
<td class="rowfollow nowrap" valign="middle"><a class="dib" href="?cat=402"><img src="pic/dot.png" alt="TV Series(电视剧)" title="TV Series(电视剧)"><span class="category dib c_tvseries" alt="TV Series(电视剧)" title="TV Series(电视剧)"></span></a></td>
<td class="rowfollow" width="100%" align="left"><table class="torrentname" width="100%"><tbody><tr><td class="torrentimg"><img class="pr5" src="/public/douban/35436582.jpg" height="52" onmouseover="showmenu(this,'tid_27475','/public/douban/35436582.jpg');" onmouseout="hiddmenu(this,'tid_27475');"></td><td class="embedded"><a target="_blank" class="torrentname" title="Love, Death &amp; Robots.2022.S03.1080p.WEB-DL.H264.DDP5.1-HDHWEB" href="details.php?id=27475&amp;hit=1"><b class="promotion twoup">Love, Death &amp; Robots.2022.S03.1080p.WEB-DL.H264.DDP5.1-HDHWEB</b></a> <b>[<font class="hot">热门</font>]</b> <font class="promotion twoup">2X上传</font> <span title="2022-05-29 19:49:35">6天20时</span><br>爱x死x机器人</td><td width="20" class="embedded" style="text-align: right; " valign="middle"><table><tbody><tr><td class="embedded"><div style="text-align:right;margin-right:3px;width:50px"><a class="fwb" target="_blank" href="https://movie.douban.com/subject/35436582/"><i class="icon pt-douban fcg"></i> 0.0</a><br><a class="fwb" target="_blank" href="https://www.imdb.com/title/tt20192958/"><i class="icon pt-imdb" style="color:#E0C035"></i> 7.2</a></div></td><td class="embedded"><a href="download.php?id=27475&amp;passkey=cc0f2413d63a3a7f43964154d23ac2bb"><i class="download icon pt-xiazai fcg" alt="download" title="下载本种"></i></a><br><a id="bookmark25" href="javascript: bookmark(27475,25);"><i class="delbookmark icon pt-wuxing fca" alt="Unbookmarked" title="收藏"></i></a><a id="myrss25" href="javascript: myrss(27475,25);"><i class="delmyrss icon pt-rss fca" alt="Unmyrssed" title="加入"></i></a></td></tr></tbody></table>
</td>
</tr></tbody></table></td><td class="rowfollow" width="40"><div class="w30"><span class="fwb">0</span><br></div></td><td class="rowfollow"><a href="comment.php?action=add&amp;pid=27475&amp;type=torrent" title="添加评论">0</a></td><td class="rowfollow nowrap"><span title="2022-05-22 19:49:35">3时<br>45分</span></td><td class="rowfollow">13.38<br>GB</td><td class="rowfollow" align="center"><b><a href="details.php?id=27475&amp;hit=1&amp;dllist=1#seeders">40</a></b></td>
<td class="rowfollow"><b><a href="details.php?id=27475&amp;hit=1&amp;dllist=1#leechers">15</a></b></td>
<td class="rowfollow"><a href="viewsnatches.php?id=27475"><b>51</b></a></td>
<td class="rowfollow">-</td><td class="rowfollow"><i>匿名</i></td>
<td class="rowfollow"></td>
</tr>
<tr>
<td class="rowfollow nowrap" valign="middle"><a class="dib" href="?cat=406"><img src="pic/dot.png" alt="Games(游戏及相关)" title="Games(游戏及相关)"><span class="category dib c_game" alt="Games(游戏及相关)" title="Games(游戏及相关)"></span></a></td>
<td class="rowfollow" width="100%" align="left"><table class="torrentname" width="100%"><tbody><tr><td class="torrentimg"><img class="pr5" src="https://cdn.cloudflare.steamstatic.com/steam/apps/794260/header.jpg" height="52" onmouseover="showmenu(this,'tid_27473','https://cdn.cloudflare.steamstatic.com/steam/apps/794260/header.jpg');" onmouseout="hiddmenu(this,'tid_27473');"></td><td class="embedded"><a target="_blank" class="torrentname" title="Outward Definitive Edition" href="details.php?id=27473&amp;hit=1"><b class="title">Outward Definitive Edition</b></a> <br>物质世界决定版| v1 0 0_55718 Windows-GOG</td><td width="20" class="embedded" style="text-align: right; " valign="middle"><table><tbody><tr><td class="embedded"></td><td class="embedded"><a href="download.php?id=27473&amp;passkey=cc0f2413d63a3a7f43964154d23ac2bb"><i class="download icon pt-xiazai fcg" alt="download" title="下载本种"></i></a><br><a id="bookmark26" href="javascript: bookmark(27473,26);"><i class="delbookmark icon pt-wuxing fca" alt="Unbookmarked" title="收藏"></i></a><a id="myrss26" href="javascript: myrss(27473,26);"><i class="delmyrss icon pt-rss fca" alt="Unmyrssed" title="加入"></i></a></td></tr></tbody></table>
</td>
</tr></tbody></table></td><td class="rowfollow" width="40"><div class="w30"><span class="fwb">0</span><br></div></td><td class="rowfollow"><a href="comment.php?action=add&amp;pid=27473&amp;type=torrent" title="添加评论">0</a></td><td class="rowfollow nowrap"><span title="2022-05-22 19:25:29">4时<br>9分</span></td><td class="rowfollow">15.60<br>GB</td><td class="rowfollow" align="center"><b><a href="details.php?id=27473&amp;hit=1&amp;dllist=1#seeders"><font color="#cc0000">1</font></a></b></td>
<td class="rowfollow"><b><a href="details.php?id=27473&amp;hit=1&amp;dllist=1#leechers">11</a></b></td>
<td class="rowfollow">0</td>
<td class="rowfollow">-</td><td class="rowfollow"><a href="userdetails.php?id=49004" class="User_Name"><b>sayabao</b></a></td>
<td class="rowfollow"></td>
</tr>
<tr>
<td class="rowfollow nowrap" valign="middle"><a class="dib" href="?cat=401"><img src="pic/dot.png" alt="Movies(电影)" title="Movies(电影)"><span class="category dib c_movies" alt="Movies(电影)" title="Movies(电影)"></span></a></td>
<td class="rowfollow" width="100%" align="left"><table class="torrentname" width="100%"><tbody><tr><td class="torrentimg"><img class="pr5" src="/public/douban/30314848.jpg" height="52" onmouseover="showmenu(this,'tid_27472','/public/douban/30314848.jpg');" onmouseout="hiddmenu(this,'tid_27472');"></td><td class="embedded"><a target="_blank" class="torrentname" title="Everything Everywhere All At Once 2022.1080p" href="details.php?id=27472&amp;hit=1"><b class="title">Everything Everywhere All At Once 2022.1080p</b></a> <b>[<font class="hot">热门</font>]</b> <br><span class="tags zz">中字</span><span class="tags yz">英字</span><span class="tags gy">国语</span><span class="tags yy">英语</span>瞬息全宇宙 + 喜剧 / 奇幻 / 冒险</td><td width="20" class="embedded" style="text-align: right; " valign="middle"><table><tbody><tr><td class="embedded"><div style="text-align:right;margin-right:3px;width:50px"><a class="fwb" target="_blank" href="https://movie.douban.com/subject/30314848/"><i class="icon pt-douban fcg"></i> 8.8</a><br><a class="fwb" target="_blank" href="https://www.imdb.com/title/tt6710474/"><i class="icon pt-imdb" style="color:#E0C035"></i> 8.6</a></div></td><td class="embedded"><a href="download.php?id=27472&amp;passkey=cc0f2413d63a3a7f43964154d23ac2bb"><i class="download icon pt-xiazai fcg" alt="download" title="下载本种"></i></a><br><a id="bookmark27" href="javascript: bookmark(27472,27);"><i class="delbookmark icon pt-wuxing fca" alt="Unbookmarked" title="收藏"></i></a><a id="myrss27" href="javascript: myrss(27472,27);"><i class="delmyrss icon pt-rss fca" alt="Unmyrssed" title="加入"></i></a></td></tr></tbody></table>
</td>
</tr></tbody></table></td><td class="rowfollow" width="40"><div class="w30"><span class="fwb">0</span><br></div></td><td class="rowfollow"><a href="comment.php?action=add&amp;pid=27472&amp;type=torrent" title="添加评论">0</a></td><td class="rowfollow nowrap"><span title="2022-05-22 19:22:59">4时<br>12分</span></td><td class="rowfollow">6.41<br>GB</td><td class="rowfollow" align="center"><b><a href="details.php?id=27472&amp;hit=1&amp;dllist=1#seeders">21</a></b></td>
<td class="rowfollow"><b><a href="details.php?id=27472&amp;hit=1&amp;dllist=1#leechers">3</a></b></td>
<td class="rowfollow"><a href="viewsnatches.php?id=27472"><b>21</b></a></td>
<td class="rowfollow">-</td><td class="rowfollow"><a href="userdetails.php?id=47553" class="User_Name"><b>咕咕斗士</b></a></td>
<td class="rowfollow"></td>
</tr>
<tr>
<td class="rowfollow nowrap" valign="middle"><a class="dib" href="?cat=402"><img src="pic/dot.png" alt="TV Series(电视剧)" title="TV Series(电视剧)"><span class="category dib c_tvseries" alt="TV Series(电视剧)" title="TV Series(电视剧)"></span></a></td>
<td class="rowfollow" width="100%" align="left"><table class="torrentname" width="100%"><tbody><tr><td class="torrentimg"><img class="pr5" src="/public/douban/35436582.jpg" height="52" onmouseover="showmenu(this,'tid_27471','/public/douban/35436582.jpg');" onmouseout="hiddmenu(this,'tid_27471');"></td><td class="embedded"><a target="_blank" class="torrentname" title="Love Death and Robots S03 1080p NF WEB-DL DDP5.1 Atmos x264-SMURF" href="details.php?id=27471&amp;hit=1"><b class="title">Love Death and Robots S03 1080p NF WEB-DL DDP5.1 Atmos x264-SMURF</b></a> <b>[<font class="hot">热门</font>]</b> <br><span class="tags zz">中字</span>爱，死亡和机器人 第三季 全9集 | 内封中字</td><td width="20" class="embedded" style="text-align: right; " valign="middle"><table><tbody><tr><td class="embedded"><div style="text-align:right;margin-right:3px;width:50px"><a class="fwb" target="_blank" href="https://movie.douban.com/subject/35436582/"><i class="icon pt-douban fcg"></i> 0.0</a><br><a class="fwb" target="_blank" href=""><i class="icon pt-imdb" style="color:#E0C035"></i> ----</a></div></td><td class="embedded"><a href="download.php?id=27471&amp;passkey=cc0f2413d63a3a7f43964154d23ac2bb"><i class="download icon pt-xiazai fcg" alt="download" title="下载本种"></i></a><br><a id="bookmark28" href="javascript: bookmark(27471,28);"><i class="delbookmark icon pt-wuxing fca" alt="Unbookmarked" title="收藏"></i></a><a id="myrss28" href="javascript: myrss(27471,28);"><i class="delmyrss icon pt-rss fca" alt="Unmyrssed" title="加入"></i></a></td></tr></tbody></table>
</td>
</tr></tbody></table></td><td class="rowfollow" width="40"><div class="w30"><span class="fwb">0</span><br></div></td><td class="rowfollow"><a href="comment.php?action=add&amp;pid=27471&amp;type=torrent" title="添加评论">0</a></td><td class="rowfollow nowrap"><span title="2022-05-22 18:35:58">4时<br>59分</span></td><td class="rowfollow">4.89<br>GB</td><td class="rowfollow" align="center"><b><a href="details.php?id=27471&amp;hit=1&amp;dllist=1#seeders">58</a></b></td>
<td class="rowfollow"><b><a href="details.php?id=27471&amp;hit=1&amp;dllist=1#leechers">8</a></b></td>
<td class="rowfollow"><a href="viewsnatches.php?id=27471"><b>54</b></a></td>
<td class="rowfollow">-</td><td class="rowfollow"><a href="userdetails.php?id=29389" class="User_Name"><b>1192520202</b></a></td>
<td class="rowfollow"></td>
</tr>
<tr>
<td class="rowfollow nowrap" valign="middle"><a class="dib" href="?cat=403"><img src="pic/dot.png" alt="TV Shows(综艺)" title="TV Shows(综艺)"><span class="category dib c_tvshows" alt="TV Shows(综艺)" title="TV Shows(综艺)"></span></a></td>
<td class="rowfollow" width="100%" align="left"><table class="torrentname" width="100%"><tbody><tr><td class="torrentimg"><img class="pr5" src="/public/douban/35723926.jpg" height="52" onmouseover="showmenu(this,'tid_27470','/public/douban/35723926.jpg');" onmouseout="hiddmenu(this,'tid_27470');"></td><td class="embedded"><a target="_blank" class="torrentname" title="Descending On The Training Room S03E01 2022 1080p WEB-DL H.264 AAC-TJUPT" href="details.php?id=27470&amp;hit=1"><b class="title">Descending On The Training Room S03E01 2022 1080p WEB-DL H.264 AAC-TJUPT</b></a> <b>[<font class="hot">热门</font>]</b> <br>乘风破浪的姐姐 第三季 / 浪姐3 | 突袭训练室第1期：阿Sa坦言跟阿娇分开哭过 赵梦于文文组乐队即兴首秀 | TJUPT小组作品 转..</td><td width="20" class="embedded" style="text-align: right; " valign="middle"><table><tbody><tr><td class="embedded"><div style="text-align:right;margin-right:3px;width:50px"><a class="fwb" target="_blank" href="https://movie.douban.com/subject/35723926/"><i class="icon pt-douban fcg"></i> 0.0</a><br><a class="fwb" target="_blank" href=""><i class="icon pt-imdb" style="color:#E0C035"></i> ----</a></div></td><td class="embedded"><a href="download.php?id=27470&amp;passkey=cc0f2413d63a3a7f43964154d23ac2bb"><i class="download icon pt-xiazai fcg" alt="download" title="下载本种"></i></a><br><a id="bookmark29" href="javascript: bookmark(27470,29);"><i class="delbookmark icon pt-wuxing fca" alt="Unbookmarked" title="收藏"></i></a><a id="myrss29" href="javascript: myrss(27470,29);"><i class="delmyrss icon pt-rss fca" alt="Unmyrssed" title="加入"></i></a></td></tr></tbody></table>
</td>
</tr></tbody></table></td><td class="rowfollow" width="40"><div class="w30"><span class="fwb">0</span><br></div></td><td class="rowfollow"><a href="comment.php?action=add&amp;pid=27470&amp;type=torrent" title="添加评论">0</a></td><td class="rowfollow nowrap"><span title="2022-05-22 18:32:10">5时<br>2分</span></td><td class="rowfollow">944.49<br>MB</td><td class="rowfollow" align="center"><b><a href="details.php?id=27470&amp;hit=1&amp;dllist=1#seeders">14</a></b></td>
<td class="rowfollow"><b><a href="details.php?id=27470&amp;hit=1&amp;dllist=1#leechers">1</a></b></td>
<td class="rowfollow"><a href="viewsnatches.php?id=27470"><b>16</b></a></td>
<td class="rowfollow">-</td><td class="rowfollow"><i>匿名</i></td>
<td class="rowfollow"></td>
</tr>
<tr>
<td class="rowfollow nowrap" valign="middle"><a class="dib" href="?cat=401"><img src="pic/dot.png" alt="Movies(电影)" title="Movies(电影)"><span class="category dib c_movies" alt="Movies(电影)" title="Movies(电影)"></span></a></td>
<td class="rowfollow" width="100%" align="left"><table class="torrentname" width="100%"><tbody><tr><td class="torrentimg"><img class="pr5" src="/public/douban/35644637.jpg" height="52" onmouseover="showmenu(this,'tid_27469','/public/douban/35644637.jpg');" onmouseout="hiddmenu(this,'tid_27469');"></td><td class="embedded"><a target="_blank" class="torrentname" title="Back To Field S06E01 2022.1080p WEB-DL H264 AAC mp4" href="details.php?id=27469&amp;hit=1"><b class="promotion free">Back To Field S06E01 2022.1080p WEB-DL H264 AAC mp4</b></a> <b>[<font class="hot">热门</font>]</b> <font class="promotion free">免费</font> <span title="2022-05-24 18:35:05">1天19时</span><br>向往的生活6 / 向往的生活渔村篇</td><td width="20" class="embedded" style="text-align: right; " valign="middle"><table><tbody><tr><td class="embedded"><div style="text-align:right;margin-right:3px;width:50px"><a class="fwb" target="_blank" href="https://movie.douban.com/subject/35644637/"><i class="icon pt-douban fcg"></i> 0.0</a><br><a class="fwb" target="_blank" href=""><i class="icon pt-imdb" style="color:#E0C035"></i> ----</a></div></td><td class="embedded"><a href="download.php?id=27469&amp;passkey=cc0f2413d63a3a7f43964154d23ac2bb"><i class="download icon pt-xiazai fcg" alt="download" title="下载本种"></i></a><br><a id="bookmark30" href="javascript: bookmark(27469,30);"><i class="delbookmark icon pt-wuxing fca" alt="Unbookmarked" title="收藏"></i></a><a id="myrss30" href="javascript: myrss(27469,30);"><i class="delmyrss icon pt-rss fca" alt="Unmyrssed" title="加入"></i></a></td></tr></tbody></table>
</td>
</tr></tbody></table></td><td class="rowfollow" width="40"><div class="w30"><span class="fwb">0</span><br></div></td><td class="rowfollow"><a href="comment.php?action=add&amp;pid=27469&amp;type=torrent" title="添加评论">0</a></td><td class="rowfollow nowrap"><span title="2022-05-22 18:31:50">5时<br>3分</span></td><td class="rowfollow">1.76<br>GB</td><td class="rowfollow" align="center"><b><a href="details.php?id=27469&amp;hit=1&amp;dllist=1#seeders">32</a></b></td>
<td class="rowfollow">0</td>
<td class="rowfollow"><a href="viewsnatches.php?id=27469"><b>47</b></a></td>
<td class="rowfollow">-</td><td class="rowfollow"><a href="userdetails.php?id=45838" class="PowerUser_Name"><b>royxing1105</b></a></td>
<td class="rowfollow"></td>
</tr>
<tr>
<td class="rowfollow nowrap" valign="middle"><a class="dib" href="?cat=403"><img src="pic/dot.png" alt="TV Shows(综艺)" title="TV Shows(综艺)"><span class="category dib c_tvshows" alt="TV Shows(综艺)" title="TV Shows(综艺)"></span></a></td>
<td class="rowfollow" width="100%" align="left"><table class="torrentname" width="100%"><tbody><tr><td class="torrentimg"><img class="pr5" src="/public/douban/35644637.jpg" height="52" onmouseover="showmenu(this,'tid_27468','/public/douban/35644637.jpg');" onmouseout="hiddmenu(this,'tid_27468');"></td><td class="embedded"><a target="_blank" class="torrentname" title="Back To Field Slow S06E03 2022 1080p WEB-DL H.264 AAC-TJUPT" href="details.php?id=27468&amp;hit=1"><b class="title">Back To Field Slow S06E03 2022 1080p WEB-DL H.264 AAC-TJUPT</b></a> <br>向往的生活6 / 向往的生活渔村篇 | 慢直播第3期：何炅刘昊然手绘超惊艳 张子枫文淇手作风铃 | TJUPT小组作品 转载请注明北洋园..</td><td width="20" class="embedded" style="text-align: right; " valign="middle"><table><tbody><tr><td class="embedded"><div style="text-align:right;margin-right:3px;width:50px"><a class="fwb" target="_blank" href="https://movie.douban.com/subject/35644637/"><i class="icon pt-douban fcg"></i> 0.0</a><br><a class="fwb" target="_blank" href=""><i class="icon pt-imdb" style="color:#E0C035"></i> ----</a></div></td><td class="embedded"><a href="download.php?id=27468&amp;passkey=cc0f2413d63a3a7f43964154d23ac2bb"><i class="download icon pt-xiazai fcg" alt="download" title="下载本种"></i></a><br><a id="bookmark31" href="javascript: bookmark(27468,31);"><i class="delbookmark icon pt-wuxing fca" alt="Unbookmarked" title="收藏"></i></a><a id="myrss31" href="javascript: myrss(27468,31);"><i class="delmyrss icon pt-rss fca" alt="Unmyrssed" title="加入"></i></a></td></tr></tbody></table>
</td>
</tr></tbody></table></td><td class="rowfollow" width="40"><div class="w30"><span class="fwb">0</span><br></div></td><td class="rowfollow"><a href="comment.php?action=add&amp;pid=27468&amp;type=torrent" title="添加评论">0</a></td><td class="rowfollow nowrap"><span title="2022-05-22 18:30:50">5时<br>4分</span></td><td class="rowfollow">530.87<br>MB</td><td class="rowfollow" align="center"><b><a href="details.php?id=27468&amp;hit=1&amp;dllist=1#seeders">7</a></b></td>
<td class="rowfollow">0</td>
<td class="rowfollow"><a href="viewsnatches.php?id=27468"><b>4</b></a></td>
<td class="rowfollow">-</td><td class="rowfollow"><i>匿名</i></td>
<td class="rowfollow"></td>
</tr>
<tr>
<td class="rowfollow nowrap" valign="middle"><a class="dib" href="?cat=403"><img src="pic/dot.png" alt="TV Shows(综艺)" title="TV Shows(综艺)"><span class="category dib c_tvshows" alt="TV Shows(综艺)" title="TV Shows(综艺)"></span></a></td>
<td class="rowfollow" width="100%" align="left"><table class="torrentname" width="100%"><tbody><tr><td class="torrentimg"><img class="pr5" src="/public/douban/35800383.jpg" height="52" onmouseover="showmenu(this,'tid_27467','/public/douban/35800383.jpg');" onmouseout="hiddmenu(this,'tid_27467');"></td><td class="embedded"><a target="_blank" class="torrentname" title="Chu Ru Zhi Chang De Wo Men S02E09 PartB 2022 1080p WEB-DL H.264 AAC-TJUPT" href="details.php?id=27467&amp;hit=1"><b class="title">Chu Ru Zhi Chang De Wo Men S02E09 PartB 2022 1080p WEB-DL H.264 AAC-TJUPT</b></a> <br>初入职场的我们 法医季 / 初入职场的我们 第二季 | 法医季09案（下）：货车密室死亡案 实习生烧脑推理鉴死因 | TJUPT小组作品..</td><td width="20" class="embedded" style="text-align: right; " valign="middle"><table><tbody><tr><td class="embedded"><div style="text-align:right;margin-right:3px;width:50px"><a class="fwb" target="_blank" href="https://movie.douban.com/subject/35800383/"><i class="icon pt-douban fcg"></i> 7.6</a><br><a class="fwb" target="_blank" href=""><i class="icon pt-imdb" style="color:#E0C035"></i> ----</a></div></td><td class="embedded"><a href="download.php?id=27467&amp;passkey=cc0f2413d63a3a7f43964154d23ac2bb"><i class="download icon pt-xiazai fcg" alt="download" title="下载本种"></i></a><br><a id="bookmark32" href="javascript: bookmark(27467,32);"><i class="delbookmark icon pt-wuxing fca" alt="Unbookmarked" title="收藏"></i></a><a id="myrss32" href="javascript: myrss(27467,32);"><i class="delmyrss icon pt-rss fca" alt="Unmyrssed" title="加入"></i></a></td></tr></tbody></table>
</td>
</tr></tbody></table></td><td class="rowfollow" width="40"><div class="w30"><span class="fwb">0</span><br></div></td><td class="rowfollow"><a href="comment.php?action=add&amp;pid=27467&amp;type=torrent" title="添加评论">0</a></td><td class="rowfollow nowrap"><span title="2022-05-22 18:29:29">5时<br>5分</span></td><td class="rowfollow">1.56<br>GB</td><td class="rowfollow" align="center"><b><a href="details.php?id=27467&amp;hit=1&amp;dllist=1#seeders">5</a></b></td>
<td class="rowfollow">0</td>
<td class="rowfollow"><a href="viewsnatches.php?id=27467"><b>9</b></a></td>
<td class="rowfollow">-</td><td class="rowfollow"><i>匿名</i></td>
<td class="rowfollow"></td>
</tr>
<tr>
<td class="rowfollow nowrap" valign="middle"><a class="dib" href="?cat=403"><img src="pic/dot.png" alt="TV Shows(综艺)" title="TV Shows(综艺)"><span class="category dib c_tvshows" alt="TV Shows(综艺)" title="TV Shows(综艺)"></span></a></td>
<td class="rowfollow" width="100%" align="left"><table class="torrentname" width="100%"><tbody><tr><td class="torrentimg"><img class="pr5" src="/public/douban/35634451.jpg" height="52" onmouseover="showmenu(this,'tid_27466','/public/douban/35634451.jpg');" onmouseout="hiddmenu(this,'tid_27466');"></td><td class="embedded"><a target="_blank" class="torrentname" title="Sheng Sheng Bu Xi S01E05 Pure 2022 1080p WEB-DL H.264 AAC-TJUPT" href="details.php?id=27466&amp;hit=1"><b class="title">Sheng Sheng Bu Xi S01E05 Pure 2022 1080p WEB-DL H.264 AAC-TJUPT</b></a> <br>聲生不息 / 声生不息 港乐季 | 舞台纯享版第五期：第二轮主题竞演“一生所爱”（下）| TJUPT小组作品 转载请注明北洋园PT 每周..</td><td width="20" class="embedded" style="text-align: right; " valign="middle"><table><tbody><tr><td class="embedded"><div style="text-align:right;margin-right:3px;width:50px"><a class="fwb" target="_blank" href="https://movie.douban.com/subject/35634451/"><i class="icon pt-douban fcg"></i> 7.6</a><br><a class="fwb" target="_blank" href=""><i class="icon pt-imdb" style="color:#E0C035"></i> ----</a></div></td><td class="embedded"><a href="download.php?id=27466&amp;passkey=cc0f2413d63a3a7f43964154d23ac2bb"><i class="download icon pt-xiazai fcg" alt="download" title="下载本种"></i></a><br><a id="bookmark33" href="javascript: bookmark(27466,33);"><i class="delbookmark icon pt-wuxing fca" alt="Unbookmarked" title="收藏"></i></a><a id="myrss33" href="javascript: myrss(27466,33);"><i class="delmyrss icon pt-rss fca" alt="Unmyrssed" title="加入"></i></a></td></tr></tbody></table>
</td>
</tr></tbody></table></td><td class="rowfollow" width="40"><div class="w30"><span class="fwb">0</span><br></div></td><td class="rowfollow"><a href="comment.php?action=add&amp;pid=27466&amp;type=torrent" title="添加评论">0</a></td><td class="rowfollow nowrap"><span title="2022-05-22 18:24:08">5时<br>10分</span></td><td class="rowfollow">1.11<br>GB</td><td class="rowfollow" align="center"><b><a href="details.php?id=27466&amp;hit=1&amp;dllist=1#seeders">10</a></b></td>
<td class="rowfollow">0</td>
<td class="rowfollow"><a href="viewsnatches.php?id=27466"><b>10</b></a></td>
<td class="rowfollow">-</td><td class="rowfollow"><i>匿名</i></td>
<td class="rowfollow"></td>
</tr>
<tr>
<td class="rowfollow nowrap" valign="middle"><a class="dib" href="?cat=403"><img src="pic/dot.png" alt="TV Shows(综艺)" title="TV Shows(综艺)"><span class="category dib c_tvshows" alt="TV Shows(综艺)" title="TV Shows(综艺)"></span></a></td>
<td class="rowfollow" width="100%" align="left"><table class="torrentname" width="100%"><tbody><tr><td class="torrentimg"><img class="pr5" src="/public/douban/35634451.jpg" height="52" onmouseover="showmenu(this,'tid_27465','/public/douban/35634451.jpg');" onmouseout="hiddmenu(this,'tid_27465');"></td><td class="embedded"><a target="_blank" class="torrentname" title="Sheng Sheng Bu Xi S01E05 2022 1080p WEB-DL H.264 AAC-TJUPT" href="details.php?id=27465&amp;hit=1"><b class="title">Sheng Sheng Bu Xi S01E05 2022 1080p WEB-DL H.264 AAC-TJUPT</b></a> <br>聲生不息 / 声生不息 港乐季 | 第五期：“一生所爱”主题竞演（下） 杨千嬅李健再度交锋 | TJUPT小组作品 转载请注明北洋园PT..</td><td width="20" class="embedded" style="text-align: right; " valign="middle"><table><tbody><tr><td class="embedded"><div style="text-align:right;margin-right:3px;width:50px"><a class="fwb" target="_blank" href="https://movie.douban.com/subject/35634451/"><i class="icon pt-douban fcg"></i> 7.6</a><br><a class="fwb" target="_blank" href=""><i class="icon pt-imdb" style="color:#E0C035"></i> ----</a></div></td><td class="embedded"><a href="download.php?id=27465&amp;passkey=cc0f2413d63a3a7f43964154d23ac2bb"><i class="download icon pt-xiazai fcg" alt="download" title="下载本种"></i></a><br><a id="bookmark34" href="javascript: bookmark(27465,34);"><i class="delbookmark icon pt-wuxing fca" alt="Unbookmarked" title="收藏"></i></a><a id="myrss34" href="javascript: myrss(27465,34);"><i class="delmyrss icon pt-rss fca" alt="Unmyrssed" title="加入"></i></a></td></tr></tbody></table>
</td>
</tr></tbody></table></td><td class="rowfollow" width="40"><div class="w30"><span class="fwb">0</span><br></div></td><td class="rowfollow"><a href="comment.php?action=add&amp;pid=27465&amp;type=torrent" title="添加评论">0</a></td><td class="rowfollow nowrap"><span title="2022-05-22 18:22:22">5时<br>12分</span></td><td class="rowfollow">2.31<br>GB</td><td class="rowfollow" align="center"><b><a href="details.php?id=27465&amp;hit=1&amp;dllist=1#seeders">8</a></b></td>
<td class="rowfollow"><b><a href="details.php?id=27465&amp;hit=1&amp;dllist=1#leechers">1</a></b></td>
<td class="rowfollow"><a href="viewsnatches.php?id=27465"><b>9</b></a></td>
<td class="rowfollow">-</td><td class="rowfollow"><i>匿名</i></td>
<td class="rowfollow"></td>
</tr>
<tr>
<td class="rowfollow nowrap" valign="middle"><a class="dib" href="?cat=403"><img src="pic/dot.png" alt="TV Shows(综艺)" title="TV Shows(综艺)"><span class="category dib c_tvshows" alt="TV Shows(综艺)" title="TV Shows(综艺)"></span></a></td>
<td class="rowfollow" width="100%" align="left"><table class="torrentname" width="100%"><tbody><tr><td class="torrentimg"><img class="pr5" src="/public/douban/35657480.jpg" height="52" onmouseover="showmenu(this,'tid_27464','/public/douban/35657480.jpg');" onmouseout="hiddmenu(this,'tid_27464');"></td><td class="embedded"><a target="_blank" class="torrentname" title="Zhong Guo Hun Li S01E05 2022 1080p WEB-DL H.264 AAC-TJUPT" href="details.php?id=27464&amp;hit=1"><b class="title">Zhong Guo Hun Li S01E05 2022 1080p WEB-DL H.264 AAC-TJUPT</b></a> <br>中国婚礼——我的女儿出嫁了 | 第5期：见证张爱马笛贾昊悦浪漫爱情 翁婿和睦铸造“父子”关系 | TJUPT小组作品 转载请注明北洋园P..</td><td width="20" class="embedded" style="text-align: right; " valign="middle"><table><tbody><tr><td class="embedded"><div style="text-align:right;margin-right:3px;width:50px"><a class="fwb" target="_blank" href="https://movie.douban.com/subject/35657480/"><i class="icon pt-douban fcg"></i> 0.0</a><br><a class="fwb" target="_blank" href=""><i class="icon pt-imdb" style="color:#E0C035"></i> ----</a></div></td><td class="embedded"><a href="download.php?id=27464&amp;passkey=cc0f2413d63a3a7f43964154d23ac2bb"><i class="download icon pt-xiazai fcg" alt="download" title="下载本种"></i></a><br><a id="bookmark35" href="javascript: bookmark(27464,35);"><i class="delbookmark icon pt-wuxing fca" alt="Unbookmarked" title="收藏"></i></a><a id="myrss35" href="javascript: myrss(27464,35);"><i class="delmyrss icon pt-rss fca" alt="Unmyrssed" title="加入"></i></a></td></tr></tbody></table>
</td>
</tr></tbody></table></td><td class="rowfollow" width="40"><div class="w30"><span class="fwb">0</span><br></div></td><td class="rowfollow"><a href="comment.php?action=add&amp;pid=27464&amp;type=torrent" title="添加评论">0</a></td><td class="rowfollow nowrap"><span title="2022-05-22 18:20:54">5时<br>14分</span></td><td class="rowfollow">1.41<br>GB</td><td class="rowfollow" align="center"><b><a href="details.php?id=27464&amp;hit=1&amp;dllist=1#seeders">7</a></b></td>
<td class="rowfollow">0</td>
<td class="rowfollow"><a href="viewsnatches.php?id=27464"><b>6</b></a></td>
<td class="rowfollow">-</td><td class="rowfollow"><i>匿名</i></td>
<td class="rowfollow"></td>
</tr>
<tr>
<td class="rowfollow nowrap" valign="middle"><a class="dib" href="?cat=403"><img src="pic/dot.png" alt="TV Shows(综艺)" title="TV Shows(综艺)"><span class="category dib c_tvshows" alt="TV Shows(综艺)" title="TV Shows(综艺)"></span></a></td>
<td class="rowfollow" width="100%" align="left"><table class="torrentname" width="100%"><tbody><tr><td class="torrentimg"><img class="pr5" src="/public/douban/35794148.jpg" height="52" onmouseover="showmenu(this,'tid_27463','/public/douban/35794148.jpg');" onmouseout="hiddmenu(this,'tid_27463');"></td><td class="embedded"><a target="_blank" class="torrentname" title="Star Chaser S02E06 2022 1080p WEB-DL H.264 AAC-TJUPT" href="details.php?id=27463&amp;hit=1"><b class="title">Star Chaser S02E06 2022 1080p WEB-DL H.264 AAC-TJUPT</b></a> <br>追星星的人2 / 追星星的人 第二季 | 第6期：好养眼→宋轶马天宇上演藏族服饰秀 | TJUPT小组作品 转载请注明北洋园PT 每周六更新</td><td width="20" class="embedded" style="text-align: right; " valign="middle"><table><tbody><tr><td class="embedded"><div style="text-align:right;margin-right:3px;width:50px"><a class="fwb" target="_blank" href="https://movie.douban.com/subject/35794148/"><i class="icon pt-douban fcg"></i> 0.0</a><br><a class="fwb" target="_blank" href=""><i class="icon pt-imdb" style="color:#E0C035"></i> ----</a></div></td><td class="embedded"><a href="download.php?id=27463&amp;passkey=cc0f2413d63a3a7f43964154d23ac2bb"><i class="download icon pt-xiazai fcg" alt="download" title="下载本种"></i></a><br><a id="bookmark36" href="javascript: bookmark(27463,36);"><i class="delbookmark icon pt-wuxing fca" alt="Unbookmarked" title="收藏"></i></a><a id="myrss36" href="javascript: myrss(27463,36);"><i class="delmyrss icon pt-rss fca" alt="Unmyrssed" title="加入"></i></a></td></tr></tbody></table>
</td>
</tr></tbody></table></td><td class="rowfollow" width="40"><div class="w30"><span class="fwb">0</span><br></div></td><td class="rowfollow"><a href="comment.php?action=add&amp;pid=27463&amp;type=torrent" title="添加评论">0</a></td><td class="rowfollow nowrap"><span title="2022-05-22 18:19:33">5时<br>15分</span></td><td class="rowfollow">2.05<br>GB</td><td class="rowfollow" align="center"><b><a href="details.php?id=27463&amp;hit=1&amp;dllist=1#seeders">4</a></b></td>
<td class="rowfollow">0</td>
<td class="rowfollow"><a href="viewsnatches.php?id=27463"><b>8</b></a></td>
<td class="rowfollow">-</td><td class="rowfollow"><i>匿名</i></td>
<td class="rowfollow"></td>
</tr>
<tr>
<td class="rowfollow nowrap" valign="middle"><a class="dib" href="?cat=490"><img src="pic/dot.png" alt="Other(其它)" title="Other(其它)"><span class="category dib c_other" alt="Other(其它)" title="Other(其它)"></span></a></td>
<td class="rowfollow" width="100%" align="left"><table class="torrentname" width="100%"><tbody><tr><td class="torrentimg"><img class="pr5" src="https://img9.doubanio.com/view/photo/l_ratio_poster/public/p2574680900.jpg" height="52" onmouseover="showmenu(this,'tid_27462','https://img9.doubanio.com/view/photo/l_ratio_poster/public/p2574680900.jpg');" onmouseout="hiddmenu(this,'tid_27462');"></td><td class="embedded"><a target="_blank" class="torrentname" title="The Invincible Tour Jay Chou Remake 20220521 1080p WEB-DL H.264 AAC-TJUPT" href="details.php?id=27462&amp;hit=1"><b class="title">The Invincible Tour Jay Chou Remake 20220521 1080p WEB-DL H.264 AAC-TJUPT</b></a> <b>[<font class="hot">热门</font>]</b> <br>周杰伦地表最强世界巡回演唱会 | 20220521 腾讯重映 | TJUPT小组作品 转载请注明北洋园PT</td><td width="20" class="embedded" style="text-align: right; " valign="middle"><table><tbody><tr><td class="embedded"></td><td class="embedded"><a href="download.php?id=27462&amp;passkey=cc0f2413d63a3a7f43964154d23ac2bb"><i class="download icon pt-xiazai fcg" alt="download" title="下载本种"></i></a><br><a id="bookmark37" href="javascript: bookmark(27462,37);"><i class="delbookmark icon pt-wuxing fca" alt="Unbookmarked" title="收藏"></i></a><a id="myrss37" href="javascript: myrss(27462,37);"><i class="delmyrss icon pt-rss fca" alt="Unmyrssed" title="加入"></i></a></td></tr></tbody></table>
</td>
</tr></tbody></table></td><td class="rowfollow" width="40"><div class="w30"><span class="fwb">0</span><br></div></td><td class="rowfollow"><a href="comment.php?action=add&amp;pid=27462&amp;type=torrent" title="添加评论">0</a></td><td class="rowfollow nowrap"><span title="2022-05-22 18:15:46">5时<br>19分</span></td><td class="rowfollow">3.44<br>GB</td><td class="rowfollow" align="center"><b><a href="details.php?id=27462&amp;hit=1&amp;dllist=1#seeders">28</a></b></td>
<td class="rowfollow">0</td>
<td class="rowfollow"><a href="viewsnatches.php?id=27462"><b>35</b></a></td>
<td class="rowfollow">-</td><td class="rowfollow"><i>匿名</i></td>
<td class="rowfollow"></td>
</tr>
<tr>
<td class="rowfollow nowrap" valign="middle"><a class="dib" href="?cat=403"><img src="pic/dot.png" alt="TV Shows(综艺)" title="TV Shows(综艺)"><span class="category dib c_tvshows" alt="TV Shows(综艺)" title="TV Shows(综艺)"></span></a></td>
<td class="rowfollow" width="100%" align="left"><table class="torrentname" width="100%"><tbody><tr><td class="torrentimg"><img class="pr5" src="/public/douban/35698677.jpg" height="52" onmouseover="showmenu(this,'tid_27460','/public/douban/35698677.jpg');" onmouseout="hiddmenu(this,'tid_27460');"></td><td class="embedded"><a target="_blank" class="torrentname" title="H!6 20220521 1080p WEB-DL H.264 AAC-TJUPT" href="details.php?id=27460&amp;hit=1"><b class="title">H!6 20220521 1080p WEB-DL H.264 AAC-TJUPT</b></a> <br>你好星期六 | 20220521期：何老师游戏现场变调解员？曲春雨秦霄贤“互相伤害”| TJUPT小组作品 转载请注明北洋园PT 每周六更新</td><td width="20" class="embedded" style="text-align: right; " valign="middle"><table><tbody><tr><td class="embedded"><div style="text-align:right;margin-right:3px;width:50px"><a class="fwb" target="_blank" href="https://movie.douban.com/subject/35698677/"><i class="icon pt-douban fcg"></i> 0.0</a><br><a class="fwb" target="_blank" href=""><i class="icon pt-imdb" style="color:#E0C035"></i> ----</a></div></td><td class="embedded"><a href="download.php?id=27460&amp;passkey=cc0f2413d63a3a7f43964154d23ac2bb"><i class="download icon pt-xiazai fcg" alt="download" title="下载本种"></i></a><br><a id="bookmark38" href="javascript: bookmark(27460,38);"><i class="delbookmark icon pt-wuxing fca" alt="Unbookmarked" title="收藏"></i></a><a id="myrss38" href="javascript: myrss(27460,38);"><i class="delmyrss icon pt-rss fca" alt="Unmyrssed" title="加入"></i></a></td></tr></tbody></table>
</td>
</tr></tbody></table></td><td class="rowfollow" width="40"><div class="w30"><span class="fwb">0</span><br></div></td><td class="rowfollow"><a href="comment.php?action=add&amp;pid=27460&amp;type=torrent" title="添加评论">0</a></td><td class="rowfollow nowrap"><span title="2022-05-22 18:14:00">5时<br>21分</span></td><td class="rowfollow">1.87<br>GB</td><td class="rowfollow" align="center"><b><a href="details.php?id=27460&amp;hit=1&amp;dllist=1#seeders">3</a></b></td>
<td class="rowfollow">0</td>
<td class="rowfollow"><a href="viewsnatches.php?id=27460"><b>6</b></a></td>
<td class="rowfollow">-</td><td class="rowfollow"><i>匿名</i></td>
<td class="rowfollow"></td>
</tr>
<tr>
<td class="rowfollow nowrap" valign="middle"><a class="dib" href="?cat=401"><img src="pic/dot.png" alt="Movies(电影)" title="Movies(电影)"><span class="category dib c_movies" alt="Movies(电影)" title="Movies(电影)"></span></a></td>
<td class="rowfollow" width="100%" align="left"><table class="torrentname" width="100%"><tbody><tr><td class="torrentimg"><img class="pr5" src="/public/douban/25909236.jpg" height="52" onmouseover="showmenu(this,'tid_27459','/public/douban/25909236.jpg');" onmouseout="hiddmenu(this,'tid_27459');"></td><td class="embedded"><a target="_blank" class="torrentname" title="Malignant 2021 UHD BluRay 2160p HEVC DTS-HD MA5.1-MTeam" href="details.php?id=27459&amp;hit=1"><b class="title">Malignant 2021 UHD BluRay 2160p HEVC DTS-HD MA5.1-MTeam</b></a> <br><span class="tags hdr">HDR(10+)</span><span class="tags sk">4K(+)</span><span class="tags zz">中字</span><span class="tags yz">英字</span><span class="tags yy">英语</span>致命感应/恶性/恶毒/恶煞(港)/疾厄(台)/肿瘤/肿瘤侠 [4K UHD原盘中字] 温子仁导演作品</td><td width="20" class="embedded" style="text-align: right; " valign="middle"><table><tbody><tr><td class="embedded"><div style="text-align:right;margin-right:3px;width:50px"><a class="fwb" target="_blank" href="https://movie.douban.com/subject/25909236/"><i class="icon pt-douban fcg"></i> 6.9</a><br><a class="fwb" target="_blank" href="https://www.imdb.com/title/tt3811906/"><i class="icon pt-imdb" style="color:#E0C035"></i> 0.0</a></div></td><td class="embedded"><a href="download.php?id=27459&amp;passkey=cc0f2413d63a3a7f43964154d23ac2bb"><i class="download icon pt-xiazai fcg" alt="download" title="下载本种"></i></a><br><a id="bookmark39" href="javascript: bookmark(27459,39);"><i class="delbookmark icon pt-wuxing fca" alt="Unbookmarked" title="收藏"></i></a><a id="myrss39" href="javascript: myrss(27459,39);"><i class="delmyrss icon pt-rss fca" alt="Unmyrssed" title="加入"></i></a></td></tr></tbody></table>
</td>
</tr></tbody></table></td><td class="rowfollow" width="40"><div class="w30"><span class="fwb">0</span><br></div></td><td class="rowfollow"><a href="comment.php?action=add&amp;pid=27459&amp;type=torrent" title="添加评论">0</a></td><td class="rowfollow nowrap"><span title="2022-05-22 18:13:11">5时<br>21分</span></td><td class="rowfollow">54.49<br>GB</td><td class="rowfollow" align="center"><b><a href="details.php?id=27459&amp;hit=1&amp;dllist=1#seeders"><font color="#550000">2</font></a></b></td>
<td class="rowfollow"><b><a href="details.php?id=27459&amp;hit=1&amp;dllist=1#leechers">8</a></b></td>
<td class="rowfollow">0</td>
<td class="rowfollow">-</td><td class="rowfollow"><i>匿名</i></td>
<td class="rowfollow"></td>
</tr>
<tr>
<td class="rowfollow nowrap" valign="middle"><a class="dib" href="?cat=403"><img src="pic/dot.png" alt="TV Shows(综艺)" title="TV Shows(综艺)"><span class="category dib c_tvshows" alt="TV Shows(综艺)" title="TV Shows(综艺)"></span></a></td>
<td class="rowfollow" width="100%" align="left"><table class="torrentname" width="100%"><tbody><tr><td class="torrentimg"><img class="pr5" src="/public/douban/35690123.jpg" height="52" onmouseover="showmenu(this,'tid_27458','/public/douban/35690123.jpg');" onmouseout="hiddmenu(this,'tid_27458');"></td><td class="embedded"><a target="_blank" class="torrentname" title="Great Dance Crew S01SP1 2022 1080p WEB-DL H.264 AAC-TJUPT" href="details.php?id=27458&amp;hit=1"><b class="title">Great Dance Crew S01SP1 2022 1080p WEB-DL H.264 AAC-TJUPT</b></a> <br>了不起！舞社 / 了不起的舞社 | 特辑 正片 | 嘉宾：苏有朋 / 王霏霏 / 程潇 | TJUPT小组作品 转载请注明北洋园PT 每..</td><td width="20" class="embedded" style="text-align: right; " valign="middle"><table><tbody><tr><td class="embedded"><div style="text-align:right;margin-right:3px;width:50px"><a class="fwb" target="_blank" href="https://movie.douban.com/subject/35690123/"><i class="icon pt-douban fcg"></i> 0.0</a><br><a class="fwb" target="_blank" href=""><i class="icon pt-imdb" style="color:#E0C035"></i> ----</a></div></td><td class="embedded"><a href="download.php?id=27458&amp;passkey=cc0f2413d63a3a7f43964154d23ac2bb"><i class="download icon pt-xiazai fcg" alt="download" title="下载本种"></i></a><br><a id="bookmark40" href="javascript: bookmark(27458,40);"><i class="delbookmark icon pt-wuxing fca" alt="Unbookmarked" title="收藏"></i></a><a id="myrss40" href="javascript: myrss(27458,40);"><i class="delmyrss icon pt-rss fca" alt="Unmyrssed" title="加入"></i></a></td></tr></tbody></table>
</td>
</tr></tbody></table></td><td class="rowfollow" width="40"><div class="w30"><span class="fwb">0</span><br></div></td><td class="rowfollow"><a href="comment.php?action=add&amp;pid=27458&amp;type=torrent" title="添加评论">0</a></td><td class="rowfollow nowrap"><span title="2022-05-22 18:06:25">5时<br>28分</span></td><td class="rowfollow">909.24<br>MB</td><td class="rowfollow" align="center"><b><a href="details.php?id=27458&amp;hit=1&amp;dllist=1#seeders">3</a></b></td>
<td class="rowfollow">0</td>
<td class="rowfollow"><a href="viewsnatches.php?id=27458"><b>4</b></a></td>
<td class="rowfollow">-</td><td class="rowfollow"><i>匿名</i></td>
<td class="rowfollow"></td>
</tr>
<tr>
<td class="rowfollow nowrap" valign="middle"><a class="dib" href="?cat=403"><img src="pic/dot.png" alt="TV Shows(综艺)" title="TV Shows(综艺)"><span class="category dib c_tvshows" alt="TV Shows(综艺)" title="TV Shows(综艺)"></span></a></td>
<td class="rowfollow" width="100%" align="left"><table class="torrentname" width="100%"><tbody><tr><td class="torrentimg"><img class="pr5" src="/public/douban/35800383.jpg" height="52" onmouseover="showmenu(this,'tid_27457','/public/douban/35800383.jpg');" onmouseout="hiddmenu(this,'tid_27457');"></td><td class="embedded"><a target="_blank" class="torrentname" title="Chu Ru Zhi Chang De Wo Men S02E09 PartA 2022 1080p WEB-DL H.264 AAC-TJUPT" href="details.php?id=27457&amp;hit=1"><b class="title">Chu Ru Zhi Chang De Wo Men S02E09 PartA 2022 1080p WEB-DL H.264 AAC-TJUPT</b></a> <br>初入职场的我们 法医季 / 初入职场的我们 第二季 | 09案（上）：羊群七窍流血离奇死亡 动物解剖难度升级 | TJUPT小组作品 转..</td><td width="20" class="embedded" style="text-align: right; " valign="middle"><table><tbody><tr><td class="embedded"><div style="text-align:right;margin-right:3px;width:50px"><a class="fwb" target="_blank" href="https://movie.douban.com/subject/35800383/"><i class="icon pt-douban fcg"></i> 7.6</a><br><a class="fwb" target="_blank" href=""><i class="icon pt-imdb" style="color:#E0C035"></i> ----</a></div></td><td class="embedded"><a href="download.php?id=27457&amp;passkey=cc0f2413d63a3a7f43964154d23ac2bb"><i class="download icon pt-xiazai fcg" alt="download" title="下载本种"></i></a><br><a id="bookmark41" href="javascript: bookmark(27457,41);"><i class="delbookmark icon pt-wuxing fca" alt="Unbookmarked" title="收藏"></i></a><a id="myrss41" href="javascript: myrss(27457,41);"><i class="delmyrss icon pt-rss fca" alt="Unmyrssed" title="加入"></i></a></td></tr></tbody></table>
</td>
</tr></tbody></table></td><td class="rowfollow" width="40"><div class="w30"><span class="fwb">0</span><br></div></td><td class="rowfollow"><a href="comment.php?action=add&amp;pid=27457&amp;type=torrent" title="添加评论">0</a></td><td class="rowfollow nowrap"><span title="2022-05-22 18:06:09">5时<br>28分</span></td><td class="rowfollow">1.56<br>GB</td><td class="rowfollow" align="center"><b><a href="details.php?id=27457&amp;hit=1&amp;dllist=1#seeders">6</a></b></td>
<td class="rowfollow">0</td>
<td class="rowfollow"><a href="viewsnatches.php?id=27457"><b>5</b></a></td>
<td class="rowfollow">-</td><td class="rowfollow"><i>匿名</i></td>
<td class="rowfollow"></td>
</tr>
<tr>
<td class="rowfollow nowrap" valign="middle"><a class="dib" href="?cat=403"><img src="pic/dot.png" alt="TV Shows(综艺)" title="TV Shows(综艺)"><span class="category dib c_tvshows" alt="TV Shows(综艺)" title="TV Shows(综艺)"></span></a></td>
<td class="rowfollow" width="100%" align="left"><table class="torrentname" width="100%"><tbody><tr><td class="torrentimg"><img class="pr5" src="/public/douban/35634451.jpg" height="52" onmouseover="showmenu(this,'tid_27456','/public/douban/35634451.jpg');" onmouseout="hiddmenu(this,'tid_27456');"></td><td class="embedded"><a target="_blank" class="torrentname" title="Sheng Sheng Bu Xi S01E05 Pre 2022 1080p WEB-DL H.264 AAC-TJUPT" href="details.php?id=27456&amp;hit=1"><b class="title">Sheng Sheng Bu Xi S01E05 Pre 2022 1080p WEB-DL H.264 AAC-TJUPT</b></a> <br>聲生不息 / 声生不息 港乐季 | 超前营业的港乐第五期：女队后台唠嗑欢乐多！毛不易“社恐”观察日记出炉 | TJUPT小组作品 转载请..</td><td width="20" class="embedded" style="text-align: right; " valign="middle"><table><tbody><tr><td class="embedded"><div style="text-align:right;margin-right:3px;width:50px"><a class="fwb" target="_blank" href="https://movie.douban.com/subject/35634451/"><i class="icon pt-douban fcg"></i> 7.6</a><br><a class="fwb" target="_blank" href=""><i class="icon pt-imdb" style="color:#E0C035"></i> ----</a></div></td><td class="embedded"><a href="download.php?id=27456&amp;passkey=cc0f2413d63a3a7f43964154d23ac2bb"><i class="download icon pt-xiazai fcg" alt="download" title="下载本种"></i></a><br><a id="bookmark42" href="javascript: bookmark(27456,42);"><i class="delbookmark icon pt-wuxing fca" alt="Unbookmarked" title="收藏"></i></a><a id="myrss42" href="javascript: myrss(27456,42);"><i class="delmyrss icon pt-rss fca" alt="Unmyrssed" title="加入"></i></a></td></tr></tbody></table>
</td>
</tr></tbody></table></td><td class="rowfollow" width="40"><div class="w30"><span class="fwb">0</span><br></div></td><td class="rowfollow"><a href="comment.php?action=add&amp;pid=27456&amp;type=torrent" title="添加评论">0</a></td><td class="rowfollow nowrap"><span title="2022-05-22 18:05:53">5时<br>29分</span></td><td class="rowfollow">589.44<br>MB</td><td class="rowfollow" align="center"><b><a href="details.php?id=27456&amp;hit=1&amp;dllist=1#seeders">6</a></b></td>
<td class="rowfollow">0</td>
<td class="rowfollow"><a href="viewsnatches.php?id=27456"><b>6</b></a></td>
<td class="rowfollow">-</td><td class="rowfollow"><i>匿名</i></td>
<td class="rowfollow"></td>
</tr>
<tr>
<td class="rowfollow nowrap" valign="middle"><a class="dib" href="?cat=403"><img src="pic/dot.png" alt="TV Shows(综艺)" title="TV Shows(综艺)"><span class="category dib c_tvshows" alt="TV Shows(综艺)" title="TV Shows(综艺)"></span></a></td>
<td class="rowfollow" width="100%" align="left"><table class="torrentname" width="100%"><tbody><tr><td class="torrentimg"><img class="pr5" src="/public/douban/35644637.jpg" height="52" onmouseover="showmenu(this,'tid_27455','/public/douban/35644637.jpg');" onmouseout="hiddmenu(this,'tid_27455');"></td><td class="embedded"><a target="_blank" class="torrentname" title="Back To Field S06E03 Plus 2022 1080p WEB-DL H.264 AAC-TJUPT" href="details.php?id=27455&amp;hit=1"><b class="promotion twoupfree">Back To Field S06E03 Plus 2022 1080p WEB-DL H.264 AAC-TJUPT</b></a> <b>[<font class="hot">热门</font>]</b> <font class="promotion twoupfree">2X免费</font> <span title="2022-05-29 18:03:09">6天18时</span><br>向往的生活6 / 向往的生活渔村篇 | 会员Plus版第3期：蘑菇屋杯篮球赛开幕 张艺兴变身代驾司机 | TJUPT小组作品 转载请注明..</td><td width="20" class="embedded" style="text-align: right; " valign="middle"><table><tbody><tr><td class="embedded"><div style="text-align:right;margin-right:3px;width:50px"><a class="fwb" target="_blank" href="https://movie.douban.com/subject/35644637/"><i class="icon pt-douban fcg"></i> 0.0</a><br><a class="fwb" target="_blank" href=""><i class="icon pt-imdb" style="color:#E0C035"></i> ----</a></div></td><td class="embedded"><a href="download.php?id=27455&amp;passkey=cc0f2413d63a3a7f43964154d23ac2bb"><i class="download icon pt-xiazai fcg" alt="download" title="下载本种"></i></a><br><a id="bookmark43" href="javascript: bookmark(27455,43);"><i class="delbookmark icon pt-wuxing fca" alt="Unbookmarked" title="收藏"></i></a><a id="myrss43" href="javascript: myrss(27455,43);"><i class="delmyrss icon pt-rss fca" alt="Unmyrssed" title="加入"></i></a></td></tr></tbody></table>
</td>
</tr></tbody></table></td><td class="rowfollow" width="40"><div class="w30"><span class="fwb">1</span><br></div></td><td class="rowfollow"><a href="comment.php?action=add&amp;pid=27455&amp;type=torrent" title="添加评论">0</a></td><td class="rowfollow nowrap"><span title="2022-05-22 18:03:09">5时<br>31分</span></td><td class="rowfollow">1.10<br>GB</td><td class="rowfollow" align="center"><b><a href="details.php?id=27455&amp;hit=1&amp;dllist=1#seeders">54</a></b></td>
<td class="rowfollow"><b><a href="details.php?id=27455&amp;hit=1&amp;dllist=1#leechers">1</a></b></td>
<td class="rowfollow"><a href="viewsnatches.php?id=27455"><b>63</b></a></td>
<td class="rowfollow">-</td><td class="rowfollow"><i>匿名</i></td>
<td class="rowfollow"></td>
</tr>
<tr>
<td class="rowfollow nowrap" valign="middle"><a class="dib" href="?cat=403"><img src="pic/dot.png" alt="TV Shows(综艺)" title="TV Shows(综艺)"><span class="category dib c_tvshows" alt="TV Shows(综艺)" title="TV Shows(综艺)"></span></a></td>
<td class="rowfollow" width="100%" align="left"><table class="torrentname" width="100%"><tbody><tr><td class="torrentimg"><img class="pr5" src="/public/douban/34809305.jpg" height="52" onmouseover="showmenu(this,'tid_27454','/public/douban/34809305.jpg');" onmouseout="hiddmenu(this,'tid_27454');"></td><td class="embedded"><a target="_blank" class="torrentname" title="Opus Jay World Tour Taipei Remake 20220520 1080p WEB-DL H.264 AAC-TJUPT" href="details.php?id=27454&amp;hit=1"><b class="title">Opus Jay World Tour Taipei Remake 20220520 1080p WEB-DL H.264 AAC-TJUPT</b></a> <br>魔天伦世界巡回演唱会 台北场 | 20220520 腾讯重映 | TJUPT小组作品 转载请注明北洋园PT</td><td width="20" class="embedded" style="text-align: right; " valign="middle"><table><tbody><tr><td class="embedded"><div style="text-align:right;margin-right:3px;width:50px"><a class="fwb" target="_blank" href="https://movie.douban.com/subject/34809305/"><i class="icon pt-douban fcg"></i> 0.0</a><br><a class="fwb" target="_blank" href=""><i class="icon pt-imdb" style="color:#E0C035"></i> ----</a></div></td><td class="embedded"><a href="download.php?id=27454&amp;passkey=cc0f2413d63a3a7f43964154d23ac2bb"><i class="download icon pt-xiazai fcg" alt="download" title="下载本种"></i></a><br><a id="bookmark44" href="javascript: bookmark(27454,44);"><i class="delbookmark icon pt-wuxing fca" alt="Unbookmarked" title="收藏"></i></a><a id="myrss44" href="javascript: myrss(27454,44);"><i class="delmyrss icon pt-rss fca" alt="Unmyrssed" title="加入"></i></a></td></tr></tbody></table>
</td>
</tr></tbody></table></td><td class="rowfollow" width="40"><div class="w30"><span class="fwb">0</span><br></div></td><td class="rowfollow"><a href="comment.php?action=add&amp;pid=27454&amp;type=torrent" title="添加评论">0</a></td><td class="rowfollow nowrap"><span title="2022-05-22 17:59:38">5时<br>35分</span></td><td class="rowfollow">3.39<br>GB</td><td class="rowfollow" align="center"><b><a href="details.php?id=27454&amp;hit=1&amp;dllist=1#seeders">13</a></b></td>
<td class="rowfollow"><b><a href="details.php?id=27454&amp;hit=1&amp;dllist=1#leechers">1</a></b></td>
<td class="rowfollow"><a href="viewsnatches.php?id=27454"><b>14</b></a></td>
<td class="rowfollow">-</td><td class="rowfollow"><i>匿名</i></td>
<td class="rowfollow"></td>
</tr>
<tr>
<td class="rowfollow nowrap" valign="middle"><a class="dib" href="?cat=401"><img src="pic/dot.png" alt="Movies(电影)" title="Movies(电影)"><span class="category dib c_movies" alt="Movies(电影)" title="Movies(电影)"></span></a></td>
<td class="rowfollow" width="100%" align="left"><table class="torrentname" width="100%"><tbody><tr><td class="torrentimg"><img class="pr5" src="/public/douban/35240920.jpg" height="52" onmouseover="showmenu(this,'tid_27453','/public/douban/35240920.jpg');" onmouseout="hiddmenu(this,'tid_27453');"></td><td class="embedded"><a target="_blank" class="torrentname" title="X 2022 BluRay 1080p DTS-HD MA 5.1 x264-MTeam" href="details.php?id=27453&amp;hit=1"><b class="title">X 2022 BluRay 1080p DTS-HD MA 5.1 x264-MTeam</b></a> <br><span class="tags yz">英字</span><span class="tags yy">英语</span>X | 类别：恐怖</td><td width="20" class="embedded" style="text-align: right; " valign="middle"><table><tbody><tr><td class="embedded"><div style="text-align:right;margin-right:3px;width:50px"><a class="fwb" target="_blank" href="https://movie.douban.com/subject/35240920/"><i class="icon pt-douban fcg"></i> 6.9</a><br><a class="fwb" target="_blank" href="https://www.imdb.com/title/tt13560574/"><i class="icon pt-imdb" style="color:#E0C035"></i> 0.0</a></div></td><td class="embedded"><a href="download.php?id=27453&amp;passkey=cc0f2413d63a3a7f43964154d23ac2bb"><i class="download icon pt-xiazai fcg" alt="download" title="下载本种"></i></a><br><a id="bookmark45" href="javascript: bookmark(27453,45);"><i class="delbookmark icon pt-wuxing fca" alt="Unbookmarked" title="收藏"></i></a><a id="myrss45" href="javascript: myrss(27453,45);"><i class="delmyrss icon pt-rss fca" alt="Unmyrssed" title="加入"></i></a></td></tr></tbody></table>
</td>
</tr></tbody></table></td><td class="rowfollow" width="40"><div class="w30"><span class="fwb">0</span><br></div></td><td class="rowfollow"><a href="comment.php?action=add&amp;pid=27453&amp;type=torrent" title="添加评论">0</a></td><td class="rowfollow nowrap"><span title="2022-05-22 16:56:00">6时<br>39分</span></td><td class="rowfollow">17.18<br>GB</td><td class="rowfollow" align="center"><b><a href="details.php?id=27453&amp;hit=1&amp;dllist=1#seeders">5</a></b></td>
<td class="rowfollow"><b><a href="details.php?id=27453&amp;hit=1&amp;dllist=1#leechers">3</a></b></td>
<td class="rowfollow">0</td>
<td class="rowfollow">-</td><td class="rowfollow"><a href="userdetails.php?id=34530" class="PowerUser_Name"><b>lzgyc</b></a></td>
<td class="rowfollow"></td>
</tr>
<tr>
<td class="rowfollow nowrap" valign="middle"><a class="dib" href="?cat=402"><img src="pic/dot.png" alt="TV Series(电视剧)" title="TV Series(电视剧)"><span class="category dib c_tvseries" alt="TV Series(电视剧)" title="TV Series(电视剧)"></span></a></td>
<td class="rowfollow" width="100%" align="left"><table class="torrentname" width="100%"><tbody><tr><td class="torrentimg"><img class="pr5" src="/public/douban/25739283.jpg" height="52" onmouseover="showmenu(this,'tid_27452','/public/douban/25739283.jpg');" onmouseout="hiddmenu(this,'tid_27452');"></td><td class="embedded"><a target="_blank" class="torrentname" title="Sleepy Hollow S02 1080p Blu-ray AVC DTS-HD MA 5.1-AmasyHD" href="details.php?id=27452&amp;hit=1"><b class="promotion free">Sleepy Hollow S02 1080p Blu-ray AVC DTS-HD MA 5.1-AmasyHD</b></a> <font class="promotion free">免费</font> <span title="2022-05-23 15:07:39">15时32分</span><br>沉睡谷 第二季 / 断头谷 / This Is War *第二季 全18集* | 类别：剧情 动作 恐怖 冒险</td><td width="20" class="embedded" style="text-align: right; " valign="middle"><table><tbody><tr><td class="embedded"><div style="text-align:right;margin-right:3px;width:50px"><a class="fwb" target="_blank" href="https://movie.douban.com/subject/25739283/"><i class="icon pt-douban fcg"></i> 7.1</a><br><a class="fwb" target="_blank" href="https://www.imdb.com/title/tt3234740/"><i class="icon pt-imdb" style="color:#E0C035"></i> 0.0</a></div></td><td class="embedded"><a href="download.php?id=27452&amp;passkey=cc0f2413d63a3a7f43964154d23ac2bb"><i class="download icon pt-xiazai fcg" alt="download" title="下载本种"></i></a><br><a id="bookmark46" href="javascript: bookmark(27452,46);"><i class="delbookmark icon pt-wuxing fca" alt="Unbookmarked" title="收藏"></i></a><a id="myrss46" href="javascript: myrss(27452,46);"><i class="delmyrss icon pt-rss fca" alt="Unmyrssed" title="加入"></i></a></td></tr></tbody></table>
</td>
</tr></tbody></table></td><td class="rowfollow" width="40"><div class="w30"><span class="fwb">0</span><br></div></td><td class="rowfollow"><a href="comment.php?action=add&amp;pid=27452&amp;type=torrent" title="添加评论">0</a></td><td class="rowfollow nowrap"><span title="2022-05-22 15:07:39">8时<br>27分</span></td><td class="rowfollow">178.00<br>GB</td><td class="rowfollow"><span class="red">0</span></td>
<td class="rowfollow"><b><a href="details.php?id=27452&amp;hit=1&amp;dllist=1#leechers">5</a></b></td>
<td class="rowfollow">0</td>
<td class="rowfollow">-</td><td class="rowfollow"><a href="userdetails.php?id=550" class="UltimateUser_Name"><b>shmt86</b></a></td>
<td class="rowfollow"></td>
</tr>
<tr>
<td class="rowfollow nowrap" valign="middle"><a class="dib" href="?cat=402"><img src="pic/dot.png" alt="TV Series(电视剧)" title="TV Series(电视剧)"><span class="category dib c_tvseries" alt="TV Series(电视剧)" title="TV Series(电视剧)"></span></a></td>
<td class="rowfollow" width="100%" align="left"><table class="torrentname" width="100%"><tbody><tr><td class="torrentimg"><img class="pr5" src="/public/douban/35359490.jpg" height="52" onmouseover="showmenu(this,'tid_27451','/public/douban/35359490.jpg');" onmouseout="hiddmenu(this,'tid_27451');"></td><td class="embedded"><a target="_blank" class="torrentname" title="Be Reborn S01 2022 1080p WEB-DL H.264 AAC-TJUPT" href="details.php?id=27451&amp;hit=1"><b class="title">Be Reborn S01 2022 1080p WEB-DL H.264 AAC-TJUPT</b></a> <b>[<font class="hot">热门</font>]</b> <br>重生之门 / 重生 | 全26集 | 主演：张译 / 王俊凯 | TJUPT小组作品 转载请注明北洋园PT</td><td width="20" class="embedded" style="text-align: right; " valign="middle"><table><tbody><tr><td class="embedded"><div style="text-align:right;margin-right:3px;width:50px"><a class="fwb" target="_blank" href="https://movie.douban.com/subject/35359490/"><i class="icon pt-douban fcg"></i> 0.0</a><br><a class="fwb" target="_blank" href=""><i class="icon pt-imdb" style="color:#E0C035"></i> ----</a></div></td><td class="embedded"><a href="download.php?id=27451&amp;passkey=cc0f2413d63a3a7f43964154d23ac2bb"><i class="download icon pt-xiazai fcg" alt="download" title="下载本种"></i></a><br><a id="bookmark47" href="javascript: bookmark(27451,47);"><i class="delbookmark icon pt-wuxing fca" alt="Unbookmarked" title="收藏"></i></a><a id="myrss47" href="javascript: myrss(27451,47);"><i class="delmyrss icon pt-rss fca" alt="Unmyrssed" title="加入"></i></a></td></tr></tbody></table>
</td>
</tr></tbody></table></td><td class="rowfollow" width="40"><div class="w30"><span class="fwb">0</span><br></div></td><td class="rowfollow"><a href="comment.php?action=add&amp;pid=27451&amp;type=torrent" title="添加评论">0</a></td><td class="rowfollow nowrap"><span title="2022-05-22 11:05:11">12时<br>29分</span></td><td class="rowfollow">9.15<br>GB</td><td class="rowfollow" align="center"><b><a href="details.php?id=27451&amp;hit=1&amp;dllist=1#seeders">18</a></b></td>
<td class="rowfollow"><b><a href="details.php?id=27451&amp;hit=1&amp;dllist=1#leechers">3</a></b></td>
<td class="rowfollow"><a href="viewsnatches.php?id=27451"><b>13</b></a></td>
<td class="rowfollow">-</td><td class="rowfollow"><i>匿名</i></td>
<td class="rowfollow"></td>
</tr>
<tr>
<td class="rowfollow nowrap" valign="middle"><a class="dib" href="?cat=402"><img src="pic/dot.png" alt="TV Series(电视剧)" title="TV Series(电视剧)"><span class="category dib c_tvseries" alt="TV Series(电视剧)" title="TV Series(电视剧)"></span></a></td>
<td class="rowfollow" width="100%" align="left"><table class="torrentname" width="100%"><tbody><tr><td class="torrentimg"><img class="pr5" src="/public/douban/1863923.jpg" height="52" onmouseover="showmenu(this,'tid_27450','/public/douban/1863923.jpg');" onmouseout="hiddmenu(this,'tid_27450');"></td><td class="embedded"><a target="_blank" class="torrentname" title="The Duke of Mount Deer 1998 1080p" href="details.php?id=27450&amp;hit=1"><b class="title">The Duke of Mount Deer 1998 1080p</b></a> <br><span class="tags hj">合集</span><span class="tags zz">中字</span><span class="tags gy">国语</span><span class="tags yue">粤语</span>鹿鼎记 / 陈小春版 / 45集全</td><td width="20" class="embedded" style="text-align: right; " valign="middle"><table><tbody><tr><td class="embedded"><div style="text-align:right;margin-right:3px;width:50px"><a class="fwb" target="_blank" href="https://movie.douban.com/subject/1863923/"><i class="icon pt-douban fcg"></i> 8.9</a><br><a class="fwb" target="_blank" href="https://www.imdb.com/title/tt0825898/"><i class="icon pt-imdb" style="color:#E0C035"></i> 0.0</a></div></td><td class="embedded"><a href="download.php?id=27450&amp;passkey=cc0f2413d63a3a7f43964154d23ac2bb"><i class="download icon pt-xiazai fcg" alt="download" title="下载本种"></i></a><br><a id="bookmark48" href="javascript: bookmark(27450,48);"><i class="delbookmark icon pt-wuxing fca" alt="Unbookmarked" title="收藏"></i></a><a id="myrss48" href="javascript: myrss(27450,48);"><i class="delmyrss icon pt-rss fca" alt="Unmyrssed" title="加入"></i></a></td></tr></tbody></table>
</td>
</tr></tbody></table></td><td class="rowfollow" width="40"><div class="w30"><span class="fwb">0</span><br></div></td><td class="rowfollow"><a href="comment.php?action=add&amp;pid=27450&amp;type=torrent" title="添加评论">0</a></td><td class="rowfollow nowrap"><span title="2022-05-22 10:29:49">13时<br>5分</span></td><td class="rowfollow">68.22<br>GB</td><td class="rowfollow" align="center"><b><a href="details.php?id=27450&amp;hit=1&amp;dllist=1#seeders">3</a></b></td>
<td class="rowfollow"><b><a href="details.php?id=27450&amp;hit=1&amp;dllist=1#leechers">2</a></b></td>
<td class="rowfollow">0</td>
<td class="rowfollow">-</td><td class="rowfollow"><a href="userdetails.php?id=47939" class="User_Name"><b>nanook</b></a></td>
<td class="rowfollow"></td>
</tr>
<tr>
<td class="rowfollow nowrap" valign="middle"><a class="dib" href="?cat=402"><img src="pic/dot.png" alt="TV Series(电视剧)" title="TV Series(电视剧)"><span class="category dib c_tvseries" alt="TV Series(电视剧)" title="TV Series(电视剧)"></span></a></td>
<td class="rowfollow" width="100%" align="left"><table class="torrentname" width="100%"><tbody><tr><td class="torrentimg"><img class="pr5" src="/public/douban/26595456.jpg" height="52" onmouseover="showmenu(this,'tid_27449','/public/douban/26595456.jpg');" onmouseout="hiddmenu(this,'tid_27449');"></td><td class="embedded"><a target="_blank" class="torrentname" title="Jia Guo En Chou Ji 2016 S01 Complete 2160p WEB-DL H.265 AAC-LeagueWEB" href="details.php?id=27449&amp;hit=1"><b class="title">Jia Guo En Chou Ji 2016 S01 Complete 2160p WEB-DL H.265 AAC-LeagueWEB</b></a> <br>家国恩仇记 全50集 |  类型:剧情  主演:李依晓/李彩桦/蒋林静  国语中字 | *4k*</td><td width="20" class="embedded" style="text-align: right; " valign="middle"><table><tbody><tr><td class="embedded"><div style="text-align:right;margin-right:3px;width:50px"><a class="fwb" target="_blank" href="https://movie.douban.com/subject/26595456/"><i class="icon pt-douban fcg"></i> 2.8</a><br><a class="fwb" target="_blank" href=""><i class="icon pt-imdb" style="color:#E0C035"></i> ----</a></div></td><td class="embedded"><a href="download.php?id=27449&amp;passkey=cc0f2413d63a3a7f43964154d23ac2bb"><i class="download icon pt-xiazai fcg" alt="download" title="下载本种"></i></a><br><a id="bookmark49" href="javascript: bookmark(27449,49);"><i class="delbookmark icon pt-wuxing fca" alt="Unbookmarked" title="收藏"></i></a><a id="myrss49" href="javascript: myrss(27449,49);"><i class="delmyrss icon pt-rss fca" alt="Unmyrssed" title="加入"></i></a></td></tr></tbody></table>
</td>
</tr></tbody></table></td><td class="rowfollow" width="40"><div class="w30"><span class="fwb">0</span><br></div></td><td class="rowfollow"><a href="comment.php?action=add&amp;pid=27449&amp;type=torrent" title="添加评论">0</a></td><td class="rowfollow nowrap"><span title="2022-05-22 10:27:39">13时<br>7分</span></td><td class="rowfollow">56.18<br>GB</td><td class="rowfollow"><span class="red">0</span></td>
<td class="rowfollow">0</td>
<td class="rowfollow">0</td>
<td class="rowfollow">-</td><td class="rowfollow"><i>匿名</i></td>
<td class="rowfollow"></td>
</tr>
</tbody></table><p align="center"><font class="gray"><b>1&nbsp;-&nbsp;50</b></font> | <a href="?inclbookmarked=0&amp;incldead=1&amp;spstate=0&amp;page=1"><b>51&nbsp;-&nbsp;100</b></a> | <a href="?inclbookmarked=0&amp;incldead=1&amp;spstate=0&amp;page=2"><b>101&nbsp;-&nbsp;150</b></a> | ... | <a href="?inclbookmarked=0&amp;incldead=1&amp;spstate=0&amp;page=321"><b>16051&nbsp;-&nbsp;16100</b></a> | <a href="?inclbookmarked=0&amp;incldead=1&amp;spstate=0&amp;page=322"><b>16101&nbsp;-&nbsp;16150</b></a> | <a href="?inclbookmarked=0&amp;incldead=1&amp;spstate=0&amp;page=323"><b>16151&nbsp;-&nbsp;16158</b></a><br><font class="gray"><b title="Alt+Pageup">&lt;&lt;&nbsp;上一页</b></font>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="?inclbookmarked=0&amp;incldead=1&amp;spstate=0&amp;page=1"><b title="Alt+Pagedown">下一页&nbsp;&gt;&gt;</b></a></p>
</td></tr></tbody></table>
</td></tr></tbody></table><div id="footer"><div style="padding:20px 0;" align="center"> (c)  <a href="https://www.pttime.org" target="_self">PT时间</a> 2019-2022 Powered by <a href="aboutnexus.php">NexusPHP</a><br><br>[page created in <b> 0.340850 </b> sec with <b>63</b> db queries, <b>30</b> reads and <b>4</b> writes of memcached and <b>2.71MB</b> ram]</div>
<div style="display: none;" id="lightbox" class="lightbox"></div><div style="display: none;" id="curtain" class="curtain"></div>
<script type="text/javascript">
//<![CDATA[
var maxpage=323;
var currentpage=0;
//]]>
</script>
</div>   

    <script type="text/javascript">
        // 一键生成脚本
        function getIntro(){//获取数据然后传送给后台，再返回数据写入文本框。
            if(document.getElementById("dburl")){
                var doubanUrl = document.getElementById("dburl").value;
                var imdbUrl = document.getElementById("imdburl").value;
            }
            if(document.getElementById("avno")){
                var avno = document.getElementById("avno").value;
            }

            var descr_box = document.getElementById("descr");
            document.getElementById("wait_tips").color="red";
            document.getElementById("wait_tips").textContent=" 请等待，可能较慢";
            var ajax = new XMLHttpRequest();
            // 使用post请求
            ajax.open("post","action.php");
            // 如果 使用post发送数据 必须 设置 如下内容
            // 修改了 发送给 服务器的 请求报文的 内容
            // 如果需要像 HTML 表单那样 POST 数据，请使用 setRequestHeader() 来添加 HTTP 头。然后在 send() 方法中规定您希望发送的数据：
            ajax.setRequestHeader("Content-type","application/x-www-form-urlencoded");
            // 发送
            // post请求 发送的数据 写在 send方法中
            // 格式 name=jack&age=18 字符串的格式
            if(document.getElementById("dburl")){
                ajax.send("douban_url="+doubanUrl+"&imdb_url="+imdbUrl);
            }else{
                ajax.send("avno="+avno);
            }
            // 注册事件
            ajax.onreadystatechange = function () {
                if (ajax.readyState==4&&ajax.status==200) {
                    var obj = JSON.parse(ajax.responseText);
                    document.getElementById("wait_tips").color="green";
                    document.getElementById("wait_tips").textContent=" 获取数据完成";
                    //影视部分
                    if(document.getElementById("dburl")){
                        if(document.getElementById("small_descr").value !=""){
                            document.getElementById("small_descr_note").style.color="red";
                            document.getElementById("small_descr_note").textContent= "提示：已有副标题，不再补充。可删除再生成。";
                        }else{
                            document.getElementById("small_descr").value = obj.other;
                        }

                        //有豆瓣链接才更换链接
                        if(obj.douban){
                            document.getElementById("imdburl").value = obj.imdb;
                            document.getElementById("dburl").value = obj.douban;
                        }
                    }
                    //9kg部分
                    if(document.getElementById("avno")){
                        if(document.getElementById("small_descr").value !=""){
                            document.getElementById("small_descr_note").style.color="red";
                            document.getElementById("small_descr_note").textContent= "提示：已有副标题，不再补充。可删除再生成。";
                        }else{
                            document.getElementById("small_descr").value = obj.other;
                        }

                        if(document.getElementById("seed_name").value !=""){
                            document.getElementById("title_note").style.color="red";
                            document.getElementById("title_note").textContent= "提示：已有标题，不再补充。可删除再生成。";
                        }else{
                            document.getElementById("seed_name").value = obj.title;
                        }
                    }

                    //封面
                    if(obj.cover){
                        if(document.getElementById("pt_img").value ==""){
                            document.getElementById("pt_img").value = obj.cover;
                        }
                    }else{
                        document.getElementById("pt_img").value = "封面缺失，请自行上传！";
                    }

                    if(document.getElementById("descr").value !=""){
                        document.getElementById("descr_note").style.color="red";
                        document.getElementById("descr_note").textContent= "提示：已有简介，不再补充。可删除再生成。";
                    }else{
                        document.getElementById("descr").value = obj.intro;
                    }

                }
            }
        }
        var getIntroBtn;
        getIntroBtn = document.getElementById("getIntro");
        getIntroBtn.onclick=getIntro;
        // 统计脚本
        //countChar(a,b)为多行文本框统计输入字符
        function countChar(textareaName,spanName){
            var maxLimit=255;
            var textArea=document.getElementById(textareaName);
            var spanCount=document.getElementById(spanName);
            if (textArea.value.length>maxLimit){
                spanCount.innerHTML="0";
                    textArea.value = textArea.value.substring(0, maxLimit);
                }else{
                    spanCount.innerHTML =maxLimit-textArea.value.length;
                }
        }
        // 复制脚本
        function copyUrl(){
            var copyText =document.getElementById("download_url").value; 
            let input = document.createElement('input') // 创建一个input
            input.value = copyText // 赋值需要复制的内容
            document.body.appendChild(input) // 插入dom
            input.select()  // 选择对象
            document.execCommand('Copy') // 执行浏览器复制命令
            input.style.display = 'none' // 隐藏
            document.body.removeChild(input) // 移除创建的input
            document.getElementById("content_tips").textContent='复制成功';
            document.getElementById('message').style.display='';   //复制后弹出
            setTimeout("document.getElementById('message').style.display='none'",1000);  //2秒后自动隐藏
        }
    </script>
    </body></html>
"""


a = DB.DB()
b = PtSites.PtSites('pttime9kg')
try:
    a.dump_table('pttime9kg')
except pymysql.err.ProgrammingError as e:
    if e.args[0] == 1146:
        table_format = b.get_table_format()
        a.createTable('pttime9kg',table_format)
cookie = 'c_secure_uid=NDcyNzI%3D; c_secure_pass=ac141922646c0bcea38a6132de5fe5aa; c_secure_ssl=eWVhaA%3D%3D; c_secure_tracker_ssl=eWVhaA%3D%3D; c_secure_login=bm9wZQ%3D%3D'
firefox_user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.9.3) Gecko/20100101 Firefox/83.0'
header = {
    'User-Agent': firefox_user_agent,
    'cookie': cookie
} 


for page in range(2):
    print(page)
    url = b.gen_search_url('',page=page)
    res = requests.get(url, headers=header)
    c = b.return_all_info(res.text,time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    time.sleep(5)
    for i in c:
        a.insertDic2DB('pttime9kg',i)
    time.sleep(15) 


