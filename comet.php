<?php
	session_start();
	$servername = "localhost";
	$username = "root";
	$password = "";
	$dbname = "webtech";

	$conn =mysqli_connect($servername, $username, $password, $dbname);
	if (!$conn) {
	    die("Connection failed: " . mysqli_connect_error());
	} 

	ob_start();
	
	$c = 1;
	date_default_timezone_set("Asia/Kolkata");
	$sql = "SELECT UPDATE_TIME FROM information_schema.tables WHERE TABLE_SCHEMA='webtech' AND TABLE_NAME='cars'";
	$sql1 = "SELECT * FROM cars";
	$date_now = date("d/M/Y H:i:s");

	while(true)
	{
		clearstatcache();
		$result = $conn->query($sql);
		if ($result->num_rows > 0) 
		{
		    while($row = $result->fetch_assoc()) 
		    {
		        $datev = strtotime($row["UPDATE_TIME"]); 
		        if($date_now < date('d/M/Y H:i:s', $datev))
		        {
		        	//echo "<tr><td>File changed at:</td><td>".date("d/M/Y H:i:s",$date_now)."  ".date('d/M/Y H:i:s', $datev)."</td></tr>";
		        	
		        	$result1 = $conn->query($sql1);
		        	$s = "<thead class='thead-dark'><tr><th>Comapny</th><th>Model</th><th>Fuel</th><th>Distance Covered</th><th>Gear</th></tr></thead>";
		        	while ($row1 = $result1->fetch_assoc())
		        	{
		        		$s = $s."<tr><td>".$row1["brand"]."</td><td>".$row1["model"]."</td><td>".$row1["fuel"]."</td><td>".$row1["km"]."</td><td>".$row1["gear"]."</td></tr>";
		        	}
		        	echo $s;
		        	ob_flush();
					flush();
					$date_now = date('d/M/Y H:i:s', $datev);
		    	}
		    	else if($c == 1)
		    	{
		    		//echo "<tr><td>File changed at:</td><td>".$date_now."KKK".date('d/M/Y H:i:s', $datev)."</td></tr>";
		        	$result1 = $conn->query($sql1);
		        	$s = "<thead class='thead-dark'><tr><th>Comapny</th><th>Model</th><th>Fuel</th><th>Distance Covered</th><th>Gear</th></tr></thead>";
		        	while ($row1 = $result1->fetch_assoc())
		        	{
		        		$s = $s."<tr><td>".$row1["brand"]."</td><td>".$row1["model"]."</td><td>".$row1["fuel"]."</td><td>".$row1["km"]."</td><td>".$row1["gear"]."</td></tr>";
		        	}
		        	echo $s;
		    		ob_flush();
					flush();
					$c = 0;
		    	}
	    	}
		}
		else 
		{
	    	echo "<tr><td>0 results</td></tr>";
		}
		sleep(2);
	}

	$conn->close();
?>