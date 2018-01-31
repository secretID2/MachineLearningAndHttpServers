%#template to generate a HTML table from a list of tuples (or list of lists, or tuple of tuples or ...)

<style>
  span {
         cursor:pointer;
         color:blue;
         text-decoration:underline;
    }
</style>
<h1>{{User}} Uploaded Files: </h1>
<h2>You still don't have files uploaded</h2>
<form action="/upload" method="post" enctype="multipart/form-data">
  Select a file: <input type="file" name="upload" />
  <input type="submit" value="Start upload" />
</form>
<text style="cursor:pointer; color:blue; text-decoration:underline" onclick="logout(this)">Log Out</text>
<script>
function logout(text){
	//document.cookie="{{User}}=;"//expires='Wed 01 Jan 1970'";
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
