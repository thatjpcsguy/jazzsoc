<?php

define('SQL_SERVER', 'localhost');
define('SQL_USERNAME', 'root');
define('SQL_PASSWORD', 'des1gn');
define('SQL_DB', 'clubcurator');


ini_set('display_errors', 1);


$template = 'foundry';


$con = mysql_connect(SQL_SERVER, SQL_USERNAME, SQL_PASSWORD);
if (!$con){die('Could not connect: ' . mysql_error());}
mysql_select_db(SQL_DB, $con);


$q = mysql_query("SELECT email, first_name, last_name FROM members WHERE email <> ''");
//$q = mysql_query("SELECT email, first_name, last_name FROM members WHERE email = 'thatguy@jpcs.me'");

while ($row = mysql_fetch_assoc($q))
{
	echo $row['first_name'] . ' ' . $row['last_name'] . ': ' . $row['email'] . PHP_EOL;
	exec('python ' . $template . '.py "'. $row['email'] .'" "'. $row['first_name'] .'" "'. $row['last_name'] .'" ');

}

