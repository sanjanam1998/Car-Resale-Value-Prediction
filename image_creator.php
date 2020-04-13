<?php
    extract($_GET);
    $image_name = $image_name.".jpg";
    header("Content-Type:image/jpg");
    header("Content-Length:".filesize($image_name));
    $file = fopen($image_name, "r");
    echo fread($file, filesize($image_name));
?>
