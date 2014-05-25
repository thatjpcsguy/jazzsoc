<?php
if (is_jazzsoc())
{
	define('DEFAULT_TITLE', 'Jazz Society Sydney University | JazzSoc');
	define('DESCRIPTION', 'The Sydney University Jazz Society (JazzSoc) is the club for anyone interested in any aspect of jazz-related music. We offer performance opportunities to our members, including our flagship jazz orchestra, SOUL (Sounds of University Life). We also have regular events on campus, often featuring free drinks for members. From Bebop to Funk, this is THE club for all that jazz.');
}
	
else 
{
	define('DESCRIPTION', 'SOUL (Sounds of University Life) is JazzSoc\'s flagship big band. The band is composed entirely of Sydney University students enrolled in a diverse range of degrees, and aims to provide students with opportunities to perform and promote jazz around USYD.');
	define('DEFAULT_TITLE', 'Sounds Of University Life | SOUL');
}
	

if ($_SERVER['SERVER_NAME'] == 'www.jazzsoc.org')
{
	header('Location: http://jazzsoc.org');
}

if ($_SERVER['SERVER_NAME'] == 'www.soundsofuniversitylife.com')
{
	header('Location: http://soundsofuniversitylife.com');
}

if (file_exists('/Users/james/.localhost'))
{
	define('SQL_SERVER', 'localhost');
	define('SQL_USERNAME', 'root');
	define('SQL_PASSWORD', 'root');
	define('SQL_DB', 'nomad');
}
else 
{
	define('SQL_SERVER', 'localhost');
	define('SQL_USERNAME', 'root');
	define('SQL_PASSWORD', 'des1gn');
	define('SQL_DB', 'jazzsoc');
}



function is_jazzsoc()
{
	if ($_SERVER['SERVER_NAME'] == 'jazzsoc.org' || $_SERVER['SERVER_NAME'] == 'www.jazzsoc.org')
	{
		return true;
	}

	return false;
	
}


$con = mysql_connect(SQL_SERVER, SQL_USERNAME, SQL_PASSWORD);
if (!$con){die('Could not connect: ' . mysql_error());}
mysql_select_db(SQL_DB, $con);


function is_page($name)
{
	if ($_SERVER['REQUEST_URI'] == '/' . $name)
	{
		return true;
	}
	else if ($name == 'home' && $_SERVER['REQUEST_URI'] == '/')
	{
		return true;
	}
	return false;
}

function autoload_css()
{
	$html = '';
	foreach(glob('css/auto/*.css') as $css){
      $html .= '		<link rel="stylesheet" href="/' . $css . '" />' . PHP_EOL;
    }
    return $html;
}

function autoload_js()
{
	$html = '';
	foreach(glob('js/auto/*.js') as $js){
      $html .= '		<script src="/'.$js.'" type="text/javascript"></script>' . PHP_EOL;
    }
    return $html;
}



if (is_page('home'))
{
	$template = "home";
	$title = DEFAULT_TITLE;
}
else if (is_page('about'))
{
	if (is_jazzsoc())
		$template = "about";
	else 
		$template = "about_soul";

	$title = 'About Us - ' . DEFAULT_TITLE;
}
else if (is_page('videos')) {
	$template = "videos";
	$title = 'Videos - ' . DEFAULT_TITLE;
}
else if (is_page('photos')) {
	$template = "photos";
	$title = 'Photos - ' . DEFAULT_TITLE;
}
else if (is_page('events')) {
	$template = "gigs";
	$title = 'Upcoming Events - ' . DEFAULT_TITLE;
}
else if (is_page('signup')) {
	$template = "signup";
	$title = 'Signup - ' . DEFAULT_TITLE;
}
else {
	$title = "404 Not Found - " . DEFAULT_TITLE;
	$template = "404";
}

?>