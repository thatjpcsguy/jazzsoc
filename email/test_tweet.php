<?php


ini_set('display_errors', 1);

	$consumerKey = "e71uBOQhANnR2Nv4JJN9A";
	$consumerSecret = "v8v27h7sT8NP6Wx4SBgVBB6kIoJWV0prUV5CKgJKsE";
	$accessToken = "2361063104-72SA1878QPbfj5FTgzUVPjFdD986vt1CzQMD9S4";
	$accessTokenSecret = "UwtwRJYhs6lWSAE6ZWwUiDiUsy7EasAnt2nS9EJFWxFHj";

	$tosend = 'Join us in welcoming James, member number 3, to @jazzsocusyd! #jazzsoc #oweek #usuoweek #usyd';
	

	require_once('TwitterAPIExchange.php');

	/** Set access tokens here - see: https://dev.twitter.com/apps/ **/
	$settings = array(
	    'oauth_access_token' => $accessToken,
	    'oauth_access_token_secret' => $accessTokenSecret,
	    'consumer_key' => $consumerKey,
	    'consumer_secret' => $consumerSecret
	);


	/** URL for REST request, see: https://dev.twitter.com/docs/api/1.1/ **/
	$url = 'http://api.twitter.com/1.1/statuses/update.json';
	$requestMethod = 'POST';

	/** POST fields required by the URL above. See relevant docs as above **/
	$postfields = array(
	    'status' => $tosend
	);

	/** Perform a POST request and echo the response **/
	$twitter = new TwitterAPIExchange($settings);
	$twitter->buildOauth($url, $requestMethod)
	             ->setPostfields($postfields)
	             ->performRequest();

	var_dump($twitter);
?>
