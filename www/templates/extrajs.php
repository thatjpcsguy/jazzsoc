		<!-- Fancybox Init -->
		<script>
			$(document).ready(function() {
				$(".fancybox").fancybox({
					openEffect	: 'none',
					closeEffect	: 'none'
				});
			});
		</script>

		<!-- Nav Bar Shrink JS -->
		<script>
			$(window).scroll(function(){
				if($(document).scrollTop() > 70)
				{
					// console.log($(document).scrollTop());
				    $('.navbar-default').removeClass('nav-largestate');
				}
				else
			  	{
			    	$('.navbar-default').addClass('nav-largestate');
			  	}
			});
		</script>