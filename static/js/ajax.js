function ajax(url,fnSucc,fnFaild)
{
	//创建Ajax对象
	if(window.XMLHttpRequest)     //解决IE6报错问题
	{
		var oAjax=new XMLHttpRequest();   //非IE6
	}
	else
	{
		var oAjax=new ActiveXObject("Microsoft.XMLHTTP");  //IE6
	}
	
	//连接服务器
	oAjax.open('GET',url,true);  //true为异步方式（即提交过程中可同时做别的事情）
	
	//发送请求
	oAjax.send();
	
	//接收返回
	oAjax.onreadystatechange=function()
	{
		if(oAjax.readyState==4) //0未初始化 1载入（正在发送） 2载入完成（发送完成） 3解析 4完成
		{
			if(oAjax.status==200)
			{
				fnSucc(oAjax.responseText);
			}
			else
			{
				if(fnFaild)
				{
					fnFaild(oAjax.status);
				}
			}
		};
	}
}