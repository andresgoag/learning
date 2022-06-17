<?php

session_start();
$_SESSION['logged'] = false;

$msg="";
$email="";

if(isset($_POST['email']) && isset($_POST['password'])) {

  $email = strip_tags($_POST['email']);
  $password= strip_tags($_POST['password']);

  if ($email == "andres" && $password == "1234") {

    //cargo datos del usuario en variables de sesión
    $_SESSION['user'] = $email;

    $msg .= "Exito!!!";
    $_SESSION['logged'] = true;

    echo '<meta http-equiv="refresh" content="2; url=dashboard.php">';
  } else {
    $msg .= "Acceso denegado!!!";
    $_SESSION['logged'] = false;
  }

}

?>



<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <title>Prueba login</title>
  <meta name="description" content="Admin, Dashboard, Bootstrap, Bootstrap 4, Angular, AngularJS" />
  <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, minimal-ui" />
</head>

<body>

  <form method="post" target="login.php" name="form">

    <div class="md-form-group">
      <input name="email" type="email" value="<?php echo $email; ?>" required>
      <label>Email</label>
    </div>

    <div class="md-form-group">
      <input name="password" type="password" required>
      <label>Password</label>
    </div>

    <button type="submit">Login</button>

  </form>

  <br><br>

  <div style="color:red" class="">
    <?php echo $msg ?>
  </div>
  
</body>
</html>
