%#template to generate a HTML table from a list of tuples (or list of lists, or tuple of tuples or ...)
<h1>{{User}} Uploaded Files: </h1>

<a href="restricted">Return</a>	

<table border="1">
%for row in rows:
  <tr  onmouseover="on(this)" onmouseout="off(this)" onclick="Delete('{{row}}')">
  
    <td>{{row}}</td>
  
  </tr>
%end
</table>
<p id="delete_text" style="visibility:hidden;"><font color="red">Click on row to Delete File</font></p>	
<script>
var TableBackgroundNormalColor = "#ffffff";
var TableBackgroundMouseoverColor = "#9999ff";
function on(row){
	row.style.backgroundColor = TableBackgroundMouseoverColor;
	document.getElementById("delete_text").style.visibility="visible";
}
function off(row){
	row.style.backgroundColor = TableBackgroundNormalColor;
	document.getElementById("delete_text").style.visibility="hidden";
}
function Delete(file){
window.location="delete/"+file;

}

</script>