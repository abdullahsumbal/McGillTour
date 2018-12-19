<!--  http://localhost/webmap101/php_test.php?lat=19.87&long=293.43&alt=24 -->

<?php
    $header="Welcome to MY PHP Page";
    $space=" ";
    $myString1="yolo".$space."yolo";
    $myString2="yolo{$space}yolo";
    $animal = ["Cat", "Dog", "Chicken"];
    $animal[] = "Bear";
    $animal [6] = "Ferret";
    sort($animal);

    if (isset($_GET['lat'])){
      $lat = $_GET['lat'];
    }else{
      $lat = "N/A";
    }
    if (isset($_GET['long'])){
      $long = $_GET['long'];
    }else{
      $long = "N/A";
    }
    if (isset($_GET['alt'])){
      $alt = $_GET['alt'];
    }else{
      $alt = "N/A";
    }
 ?>

 <!DOCTYPE html>
 <html lang="en">
 <head>
   <meta charset="UTF-8" />
   <title>PHP Test</title>

 </head>
 <body>
   <h1>yolo</h1>
   <h1><?php echo $header; ?></h1>
   <h4><?php echo $myString1; ?></h4>
   <hr />
   <h4><?php echo $animal[0]?></h4>
    <h4><?php echo $animal[1]?></h4>
     <h4><?php echo $animal[2]?></h4>
      <h4><?php echo $animal[3]?></h4>
 <h4><?php echo $animal[4]?></h4>
 <hr />
 <h4>Latitude: <?php echo $lat;?></h4>
 <h4>Longitude: <?php echo $long;?></h4>
 <h4>Altitude: <?php echo $alt;?></h4>
<hr />
 <?php
  foreach ($_GET as $key => $value) {
    echo "Key:{$key} Value: {$value}<br>" ;
  }

 ?>
<hr />
   <?php
   $txt1 = "Learn PHP";
   $txt2 = "W3Schools.com";
   $x = 5;
   $y = 4;

   echo "<h2>" . $txt1 . "</h2>";
   echo "Study PHP at " . $txt2 . "<br>";
   echo $x + $y;
   ?>

 </body>
 </html>
