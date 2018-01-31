<!DOCTYPE html>
<html>
<head>
  <title>Upload Files Server</title>
  <script src="http://cdnjs.cloudflare.com/ajax/libs/processing.js/1.4.8/processing.min.js"></script>
</head>
<body>
<h2>Welcome to the website</h2>
<a href="/"><h3>Return to Initial Page</h3> </a>
<h3>Please choose a username and password to Sign Up!</h3>
<form action="/SignUp/form" method="post">
            Username: <input name="username" type="text"/><br>
            Password: <input name="password" type="password"/><br>
			Confirm Password: <input name="cpassword" type="password"/>
            <input value="Sign Up" type="submit" />
</form>  
<h3 style="visibility:{{different_pass_error}};"><font color="red">Error "confirm password" different from "password"</font></h3>    
<h3 style="visibility:{{username_error}};"><font color="red">Your username already exists. Choose other one.</font></h3>    
</body>
</html>
