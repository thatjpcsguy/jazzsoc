<?php ini_set('display_errors', 1); error_reporting(-1); ?>

<?php include 'includes/includes.php'; ?>

<!DOCTYPE html>
<html lang="en">
	<head>
		<meta charset="utf-8">
		<title><?php echo $title; ?></title>

		<!-- HTML5 shim, for IE6-8 support of HTML5 elements -->
		<!--[if lt IE 9]>
			<script src="http://html5shim.googlecode.com/svn/trunk/html5.js"></script>
		<![endif]-->

		<!-- CSS -->
		<?php echo autoload_css(); ?>
		<link rel="stylesheet" href='http://fonts.googleapis.com/css?family=Roboto+Condensed' />
		<link rel="stylesheet" href="/js/fancybox/jquery.fancybox.css?v=2.1.4" />
		<link rel="stylesheet" href="/css/soul.css" />
		<?php if(is_jazzsoc()) { ?>
		<link rel="stylesheet" href="/css/jazzsoc.css" />
		<?php } ?>
		<!-- JS -->
		<?php echo autoload_js(); ?>
		<script src="/js/jquery.min.js" type="text/javascript"></script>
		<script src="/js/bootstrap.min.js" type="text/javascript"></script>
		<script src="/js/fancybox/jquery.fancybox.pack.js?v=2.1.4" type="text/javascript"></script>

		<?php include 'templates/extrajs.php'; ?>

		<!-- Facebook Meta Tags -->
		<meta property="og:type"   content="Website" /> 
		<meta property="og:site_name"   content="<?php echo DEFAULT_TITLE; ?>" />
		<meta property="og:description"   content="<?php echo DESCRIPTION; ?>" />
		<meta property="og:url"    content="<?php if (is_jazzsoc()) echo 'http://jazzsoc.org'; else echo 'http://soundsofuniversitylife.com'; ?>" /> 
		<meta property="og:title"  content="<?php echo $title; ?>" />

		<!-- Twitter Meta Tags -->
		<meta property="twitter:card" content="" />
		<meta property="twitter:title"  content="<?php echo $title; ?>" />
		<meta property="twitter:url" content="<?php if (is_jazzsoc()) echo 'http://jazzsoc.org'; else echo 'http://soundsofuniversitylife.com'; ?>" />
		<meta property="twitter:description" content="<?php echo DESCRIPTION; ?>" />
		<meta property="twitter:image" content="" />
		<meta property="twitter:site" content="" />

		<!-- Additional Meta Tags -->
		<meta name="description" content="<?php echo DESCRIPTION; ?>">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">


		<script>
		  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
		  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
		  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
		  })(window,document,'script','//www.google-analytics.com/analytics.js','ga');

		  <?php if (is_jazzsoc()){ ?>
		  	ga('create', 'UA-48344739-1', 'jazzsoc.org');
		  	<?php } else { ?>
	ga('create', 'UA-48344739-2', 'soundsofuniversitylife.com');
			<?php   } ?>
		  
		  ga('send', 'pageview');

		</script>
	</head>
	<body>
		<!-- <div class="top-line"></div> -->
		<!-- Begin The Navgiation Bar -->
		<nav class="navbar navbar-fixed-top navbar-default nav-largestate" role="navigation" style="margin-bottom: 0px;">
			<div class="container">
				<!-- Brand and toggle get grouped for better mobile display -->
				<div class="navbar-header">
					<button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">
						<span class="sr-only">Toggle navigation</span>
						<span class="icon-bar"></span>
						<span class="icon-bar"></span>
						<span class="icon-bar"></span>
					</button>
					<a class="navbar-brand" href="/"></a>
				</div>
				<!-- Collect the nav links, forms, and other content for toggling -->
				<div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
					<ul class="nav navbar-nav navbar-right">
						<li><a href="/">Home</a></li>
						<li><a href="/about">About</a></li>
						<li><a href="/events">Events</a></li>
						<li><a href="/photos">Photos</a></li>
						<li><a href="/videos">Videos</a></li>
						<?php if (is_jazzsoc()) { ?>
						<li><a href="http://soundsofuniversitylife.com">SOUL</a></li>
						<!-- <li><a href="/bands">The Funk Chefs</a></li> -->
						<?php } else { ?>
						<li><a href="http://jazzsoc.org">JazzSoc</a></li>
						<?php } ?>
					</ul>
				</div>
			</div>
		</nav>

		<?php if (is_page('home')){ ?>
		<!-- Begin Homepage Carousel -->
		<div id="carousel-example-generic" class="carousel slide" data-ride="carousel">
			<!-- Wrapper for slides -->
			<div class="carousel-inner">
		    	<?php if (is_jazzsoc()){ ?>
			    	<div class="item active" style="background-image: url('/img/gigs/foundry_banner.jpg');">
			    		<div class="carousel-caption">
			        		<a href="/events"><h3 class="soul-heading half">Jazzsoc Attends Foundry 616</h3></a>
			    		</div>
			    	</div>
		    	<? } ?>
		    	<div class="item <?php if (!is_jazzsoc()) { echo 'active'; } ?>" style="height: 450px; background: url('/img/gigs/caberet.jpg'); background-size: cover; background-position: center; background-repeat: no-repeat;">
		    		<div class="carousel-caption">
		        		<a href="/photos"><h3 class="soul-heading half">MUSE and SOUL Presents Caberet 2013</h3></a>
		    		</div>
		    	</div>
		    	<div class="item" style="height: 450px; background: url('/img/gigs/verge.jpg'); background-size: cover; background-position: center; background-repeat: no-repeat;">
		    		<div class="carousel-caption">
		    			<a href="/photos"><h3 class="soul-heading half">ConVerge Festival 2013</h3></a>
		    		</div>
				</div>
			</div>
			<!-- Controls -->
			<a class="left carousel-control" href="#carousel-example-generic" data-slide="prev">
				<span class="glyphicon glyphicon-chevron-left"></span>
			</a>
			<a class="right carousel-control" href="#carousel-example-generic" data-slide="next">
				<span class="glyphicon glyphicon-chevron-right"></span>
			</a>
		</div>
		<?php } ?>

		<!-- Main Page Content -->
		<div class="container">
			<div class="row space"></div>
			<div class="row">
				<?php if (is_page('home')) { ?>

				<div class="col-md-8">
					<?php include 'templates/' . $template . '.php'; ?>
				</div>
				<div class="col-md-4">
					<?php include 'templates/sidebar.php'; ?>
				</div>

				<?php } else { ?>

				<div class="col-md-12">
					<?php include 'templates/' . $template . '.php'; ?>
				</div>

				<?php } ?>
			</div>
			<!-- Begin Footer -->
			<?php include 'templates/footer.php'; ?>
		</div>
