
<div class="row space">
	<div class="col-md-12">
		<h3 class="soul-heading">Upcoming Gigs</h3>
		<br />
		<?php 
		if (!is_jazzsoc())
		{
			$query = "SELECT * FROM events WHERE soul = 1 AND NOW() < time ORDER BY time ASC LIMIT 4";
		}
		else {
			$query = "SELECT * FROM events WHERE NOW() < time ORDER BY time ASC LIMIT 4";
		}
		$result = mysql_query($query);

		$counter = 1;
		$num_rows = mysql_num_rows($result);
		while ($row = mysql_fetch_array($result)){
			?>
		<a href="/events"><h5><?php echo $row['title']; ?></h5></a>
		<hr />
		<?php } ?>
		<a href="/events"><h5> . . . </h5></a>
	</div>
</div>

<div class="row space">
	<div class="col-md-12">
		<h3 class="soul-heading">Social</h3>
		<br />
		<a href="http://facebook.com/soundsofuniversitylife"><div class="jpcs-social facebook"></div></a>
		<a href="http://twitter.com/jazzsocusyd"><div class="jpcs-social twitter"></div></a>
		<a href="https://www.youtube.com/channel/UCAv8fmF62FZHNixRWhWTigg"><div class="jpcs-social youtube"></div></a>
		<!-- <a href="http://youtube.com"><div class="jpcs-social flickr"></div></a> -->
		<!-- <a href="http://youtube.com"><div class="jpcs-social soundcloud"></div></a> -->
		<a href="mailto:contact@jazzsoc.org"><div class="jpcs-social email"></div></a>
	</div>
</div>

<div class="row space">
	<div class="col-md-12">
		<h3 class="soul-heading">Tracks</h3>
		<br />
		<iframe width="100%" height="300" scrolling="no" frameborder="no" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/users/3256984&amp;auto_play=false&amp;hide_related=false&amp;visual=true"></iframe>
	</div>
</div>