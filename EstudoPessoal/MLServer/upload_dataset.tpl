<h1>Hi {{user_name}}</h1>
<text style="cursor:pointer; color:blue; text-decoration:underline" onclick="logout()">Log Out</text><br><br>
<form action="/upload" method="post" enctype="multipart/form-data">
  Split Character: <input type="text" name="split" value="," />
  Select a file: <input type="file" name="upload" />
  url:      <input type="text" name="url" />
  <input type="submit" value="Start upload" />
</form>
<script>
function logout(){
    //Remove all cookies
    DeleteAllCookies();
    window.location='/';
    
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