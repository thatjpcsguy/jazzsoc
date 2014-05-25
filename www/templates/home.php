
<?php 






	if (!is_jazzsoc())
	{
		$query = "SELECT link, title, subtitle, DATE_FORMAT(date, '%d.%m.%y') as time, info FROM videos WHERE soul = 1 ORDER BY date DESC";
	}
	else {
		// $latest_member = mysql_fetch_assoc(mysql_query("SELECT CONCAT(m.first_name, ' ', m.last_name) AS name FROM clubcurator.members m JOIN clubcurator.clubs_members c ON m.access = c.user ORDER BY c.id DESC LIMIT 1"));
		// $num_members = mysql_fetch_assoc(mysql_query("SELECT COUNT(*) AS num FROM clubcurator.clubs_members WHERE join_date > DATE('2014-01-01');"));
		// echo '<div class="row space">
		// 	<div class="col-md-12">
		// 		<h3 class="soul-heading half">Welcome to Oweek!</h3>
		// 		<p><br />JazzSoc\'s Stall is #183 which is on the main lawns right in front of Fisher Library</p>
		// 		<p>Currently, for 2014, JazzSoc has <strong>'.$num_members["num"].'</strong> Members and the latest member to join was <strong>'.$latest_member['name'].'!</strong></p>
		// 		<p>Don\'t forget to come to <a href="http://www.facebook.com/events/500389560080646/"><strong>Jazzin\' The Wild</strong></a> this thursday night at hermans bar!</p>
		// 		<p>See you around the festival!</p>
		// 	</div>
		// </div>';
		$query = "SELECT link, title, subtitle, DATE_FORMAT(date, '%d.%m.%y') as time, info FROM videos ORDER BY date DESC";
	}
	$result = mysql_query($query);

	$counter = 1;
	$num_rows = mysql_num_rows($result);
	while ($row = mysql_fetch_array($result)){
		$counter ++;

		echo '<div class="row space">
				<div class="col-md-12">
					<h3 class="soul-heading half">'.$row['title'].'</h3>
					<h5 class="">' . $row['subtitle'] . ' ' . $row['time']. '</h5>
					<iframe width="100%" height="400" src="http://www.youtube.com/embed/'.$row['link'].'" frameborder="0" allowfullscreen></iframe>
				</div>
			</div>';

	}
					

?>