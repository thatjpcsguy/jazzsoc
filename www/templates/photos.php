<?php 

$albums = glob("img/photos/*");
// var_dump($albums);

foreach (array_reverse($albums) as $key => $album) {

	if (!file_exists($album . '/soul.txt') && !is_jazzsoc())
	{
		continue;
	}

	$contents = file_get_contents($album . "/title.txt");


	echo '<div class="row">
			<div class="col-md-12">
				<h3 class="soul-heading half">'. mysql_real_escape_string(strip_tags($contents)) .'</h3>
				<br />
			</div>
		</div>';
	
	$thum = $album . "/thumbnails/*";
	// var_dump($thum);
	$photos = glob($thum);
	// var_dump($photos);
	$count = 0;
	foreach ($photos as $key => $thumbnail) {

		$main = explode('/', $thumbnail);
		$main = $main[sizeof($main) - 1];

		if ($count % 6 == 0)
		{

			echo '<div class="row">';
		}
		echo '<div class="col-md-2 col-sm-6 col-xs-12"><a class="fancybox" rel="group" href="http://jazzsoc.org/'. $album .'/fullres/'.$main .'"><div style="background-image: url(\'http://jazzsoc.org/'.$thumbnail.'\'); background-size: cover; height: 120px; margin-bottom: 16px;"></div></a></div>';
		
		
		if ($count % 6 == 5)
		{
			
			echo '</div>';
		}
		$count ++;
	}
	if ($count % 6 != 0)
	{
		echo '</div>';
	}


}
					

?>