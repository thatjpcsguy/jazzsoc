<?php 

define('SQL_SERVER', 'localhost');
define('SQL_USERNAME', 'root');
define('SQL_PASSWORD', 'des1gn');
define('SQL_DB', 'clubcurator');


ini_set('display_errors', 1);


$con = mysql_connect(SQL_SERVER, SQL_USERNAME, SQL_PASSWORD);
if (!$con){die('Could not connect: ' . mysql_error());}
mysql_select_db(SQL_DB, $con);


$access_id = "9000000" . $_POST["access_card"];
$club_id = "556883";
$first_name = $_POST["first_name"];
$last_name = $_POST["last_name"];
$email = $_POST["email"];
$phone = $_POST["phone"];
$degree = $_POST["degree"];


function transaction($amount, $description, $access_id, $club, $first_name, $last_name, $email)
{
	mysql_query("INSERT INTO transactions (value, description, user_id, club_id, time) VALUES ('$amount', '$description', '$access_id', '$club', NOW())");

	echo exec('./transaction.py "' . $first_name . '" "' . $last_name . '" "' . $email . '" "' . $access_id . '" "' . mysql_insert_id() . '" "' . $description. '" "' . $amount .'"');
}


function welcome($first_name, $last_name, $club_id, $access_id, $email)
{
	mysql_query("INSERT INTO clubs_members (society, user, join_date) VALUES ('$club_id', '$access_id', NOW())");

	echo exec('./welcome.py "' . $first_name . '" "' . $last_name . '" "' . $email . '" "' . $access_id . '"');
}


mysql_query("REPLACE INTO members SET access = '$access_id', first_name = '$first_name', last_name = '$last_name', email = '$email', degree= '$degree', phone = '$phone', join_date = NOW()");


// MEMBERSHIP
if (isset($_POST["membership"]) && $_POST["membership"] == true)
{
	welcome($first_name, $last_name, $club_id, $access_id, $email);
	transaction(10, 'JazzSoc Membership 2014', $access_id, $club_id, $first_name, $last_name, $email);
	// $id = mysql_fetch_assoc(mysql_query("SELECT COUNT(*) AS num FROM clubcurator.clubs_members WHERE join_date > DATE('2014-01-01');"));
}

// AUDITION FEES
if (isset($_POST["audition"]) && $_POST["audition"] == true){
	transaction(5, 'JazzSoc SOUL Audition 2014', $access_id, $club_id, $first_name, $last_name, $email);
}
// OLD SHIRT
if (isset($_POST["old_shirt"]) && $_POST["old_shirt"] == true){
	transaction(10, 'JazzSoc 2013 T-Shirt', $access_id, $club_id, $first_name, $last_name, $email);
}

// NEW SHIRT
if (isset($_POST["new_shirt"]) && $_POST["new_shirt"] == true){
	transaction(10, 'JazzSoc 2014 T-Shirt', $access_id, $club_id, $first_name, $last_name, $email);
}

header("Location: /");



?>