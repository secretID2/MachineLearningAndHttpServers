<!DOCTYPE html>
<html>
<head>
  <title>Upload Files Server</title>
  <script src="http://cdnjs.cloudflare.com/ajax/libs/processing.js/1.4.8/processing.min.js"></script>
</head>
<body>
<h2>Welcome to the website</h2>
<a href="SignUp"><h3>Sign Up</h3> </a>
<h3>Please enter the username and pass to get access to Sign In</h3>
<form action="/login" method="post">
            Username: <input name="username" type="text"  />
            Password: <input name="password" type="password"  />
            <input value="Login" type="submit" />
</form>  
</body>
</html>
