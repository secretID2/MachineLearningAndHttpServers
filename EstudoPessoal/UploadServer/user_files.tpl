%#template to generate a HTML table from a list of tuples (or list of lists, or tuple of tuples or ...)
<h1>{{User}} Uploaded Files: </h1>
<form action="/upload" method="post" enctype="multipart/form-data">
  Select a file: <input type="file" name="upload" />
  <input type="submit" value="Start upload" />
</form>
<text style="cursor:pointer; color:blue; text-decoration:underline" onclick="logout(this)">Log Out</text>		<a href="delete">Delete</a>	

<table border="1">
%for row in rows:
  <tr  onmouseover="on(this)" onmouseout="off(this)" onclick="download('{{row}}')">
  
    <td>{{row}}</td>
  
  </tr>
%end
</table>
<p id="download_text" style="visibility:hidden;"><font color="red">Click on row to download File</font></p>	
<script>
var TableBackgroundNormalColor = "#ffffff";
var TableBackgroundMouseoverColor = "#9999ff";
function on(row){
	row.style.backgroundColor = TableBackgroundMouseoverColor;
	document.getElementById("download_text").style.visibility="visible";
}
function off(row){
	row.style.backgroundColor = TableBackgroundNormalColor;
	document.getElementById("download_text").style.visibility="hidden";
}
function download(file){
window.location=file;

}
function logout(text){
	//document.cookie="{{User}}=;expires=Thu, 01 Jan 1970 00:00:01 GMT;path=/;";
    DeleteAllCookies();
	window.location="/";
}
 function DeleteAllCookies()
{
			Cookie=document.cookie;
            console.log(Cookie.localeCompare('')!=-1);
			//if  not empty
			if(Cookie.localeCompare('')!=-1){
				cookies=Cookie.split(';');
                console.log(cookies);
				var cookies_names=[];
				cookies.forEach(function(cookie){cookies_names.push(cookie.split('=')[0]);}); 
				//deleting cookies
                console.log(cookies_names);
				cookies_names.forEach(function(name){document.cookie=name + '=;expires=Thu, 01 Jan 1970 00:00:01 GMT;path=/;';});
				//cookies_names.forEach(function(name){$.cookie(name, null, { path: '/' });});
			}
}
</script>