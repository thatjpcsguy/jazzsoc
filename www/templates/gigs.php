
<?php 
	if (!is_jazzsoc())
	{
		$query = "SELECT * FROM events WHERE soul = 1 AND NOW() < time ORDER BY time ASC";
	}
	else {
		$query = "SELECT * FROM events WHERE NOW() < time ORDER BY time ASC";
	}
	$result = mysql_query($query);

	$counter = 1;
	$num_rows = mysql_num_rows($result);
	while ($row = mysql_fetch_array($result)){
		$counter ++;

		echo '<div class="row space">
				<div class="col-md-12">
					<h3 class="soul-heading half">'.$row['title'].'</h3>
					<br />
					<a href="' . $row['rsvp'] .'"><img class="full-img" src="http://jazzsoc.org/img/gigs/' . $row['image'] . '" /></a>
				</div>
			</div>';

	}
					

?>