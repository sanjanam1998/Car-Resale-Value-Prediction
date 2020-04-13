<?php
session_start();
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "webtech";

// Create connection
$conn =mysqli_connect($servername, $username, $password, $dbname);
// Check connection
if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
} 

$data = json_decode(file_get_contents("php://input"));

$search = $data->searchText;

$sql = "SELECT brand FROM brands WHERE brand LIKE '%".$search."%' LIMIT 6";
$sel = mysqli_query($conn,$sql);
$data = array();

while ($row = mysqli_fetch_array($sel)) {
  $data[] = array("brand"=>$row['brand']);
}

echo json_encode($data);

?>


