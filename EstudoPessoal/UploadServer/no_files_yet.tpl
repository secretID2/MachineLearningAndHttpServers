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
	document.cookie="{{User}}=;"//expires='Wed 01 Jan 1970'";
	window.location="/";
}
</script>		
