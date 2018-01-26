%#template to generate a HTML table from a list of tuples (or list of lists, or tuple of tuples or ...)
<h1>{{User}} Uploaded Files: </h1>
<h2>You still don't have files uploaded</h2>
<form action="/upload" method="post" enctype="multipart/form-data">
  Select a file: <input type="file" name="upload" />
  <input type="submit" value="Start upload" />
</form>
<a href="/">Return</button></a>		
