<p>Add a new task to the ToDo list:</p>
<form action="/new" method="GET">
  <input type="text" size="100" maxlength="100" name="task" value="Write task here">
  <select name="status">
	<option value="Open">Open</option>
	<option value="Close">Close</option>	
  </select>
  <!--<input id="status" type="number" max="1" min="0" style="visibility:hidden">-->
  <input type="submit" name="save" value="save">
</form>
<!--<script>
function send_status(){
	status.document.getElemntByName("status").value;
	if(value.localCompare("Open")==0)
		document.getElemntById("status").value=1;
	else
		document.getElemntById("status").value=0;
}
</script>-->