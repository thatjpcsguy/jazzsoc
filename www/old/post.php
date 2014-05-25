<?php include 'nav.php'; ?>


<div id='fb-root'></div>
    <script src='http://connect.facebook.net/en_US/all.js'></script>

						<?php 
						$query = "SELECT id, title, body, DATE_FORMAT(time, '%d.%m.%y') as time FROM blog WHERE id = '".mysql_real_escape_string($_GET['id'])."' ORDER BY time DESC";
						$result = mysql_query($query);

						if (mysql_num_rows($result))
						{
							while ($row = mysql_fetch_array($result))
							{

							?>

							<div class="tent tent-small">
								<h3><?php echo $row['time']; ?></h3>
								<h2><?php echo $row['title']; ?></h2>
								<div class="content">
									<?php echo $row['body']; ?>
								</div>
								<div class="share">
									<a onclick="postToFeed(<?php echo '\''.$row['id'].'\', \''.$row['title'].'\', \''.$row['body'].'\''; ?>); return false;">
										<button class="btn btn-inverse">Share on Facebook</button>
									</a>
									<a href="https://twitter.com/share?url=http://nomadpercussion.com/post?id=<?php echo $row['id']; ?>" target="_blank">
										<button class="btn btn-inverse">Share on Twitter</button>
									</a>
								</div>
							</div>

							<?php
							}


						}
						else 
						{
						?>
							<div class="tent">
								<h2>Oops, Thats a 404</h2>
								<p>An error was encountered when trying to find the content you were looking for. It may be missing or the link you clicked might be out of date.</p>
							</div>
						<?php
						}
						?>



						 <script> 
      FB.init({appId: "380755745369186", status: true, cookie: true});

      function postToFeed(post_id, title, content) {

        // calling the API ...
        var obj = {
          method: 'feed',
          link: 'http://nomadpercussion.com/post?id='+post_id,
          picture: 'http://nomadpercussion.com/img/logo_med.jpg',
          name: title,
          caption: 'Nomad Percussion',
          description: content
        };

        function callback(response) {
          document.getElementById('msg').innerHTML = "Post ID: " + response['post_id'];
        }

        FB.ui(obj, callback);
      }
    
    </script>
		

					

<?php include 'footer.php'; ?>