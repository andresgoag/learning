<?php
session_start();
$logged = $_SESSION['logged'];

if(!$logged){
  echo "Ingreso no autorizado";
  die();
}

$usuario = $_SESSION['user'];

?>



<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hola</title>
</head>
<body>
    <div>
        <h3>Dashboard</h3>
        <p>Hola</p>
        <p><?php echo $usuario; ?></p>
    </div>
</body>
</html>
