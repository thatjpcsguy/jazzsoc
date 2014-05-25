
<?php 
	if (!is_jazzsoc())
	{
		$query = "SELECT link, title, subtitle, DATE_FORMAT(date, '%d/%m/%y') as time, info FROM videos WHERE soul = 1 ORDER BY date DESC";
	}
	else {
		$query = "SELECT link, title, subtitle, DATE_FORMAT(date, '%d/%m/%y') as time, info FROM videos ORDER BY date DESC";
	}
	$result = mysql_query($query);

	$counter = 1;
	$num_rows = mysql_num_rows($result);
	while ($row = mysql_fetch_array($result)){
		$counter ++;

		echo '<div class="row space">
				<div class="col-md-10">
					<h3 class="soul-heading half">'.$row['title'].'</h3>
					<h5 class="">' . $row['subtitle'] . ' ' . $row['time']. '</h5>
					<iframe width="100%" height="400" src="http://www.youtube.com/embed/'.$row['link'].'" frameborder="0" allowfullscreen></iframe>
				</div>
			</div>';

	}
					

?>