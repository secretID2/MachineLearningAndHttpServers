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
	document.cookie="{{User}}=;"//expires='Wed 01 Jan 1970'";
	window.location="/";
}
</script>