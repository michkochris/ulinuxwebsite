print "<!DOCTYPE html> <head>";
print "<title>Old Introdution</title>";
print "<meta name="viewport" content="width=device-width, initial-scale=1.0"">";
print "<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">";
print "<link rel="stylesheet" href="stylesheets/ulinuxweb.css" type="text/css" /> </head>";
print "<body> <div class="topnav">";
print "<div class="dropdown">";
print "<button class="dropbtn" onclick="topnavdrop()" href="/index.html">ULINUX <i class="fa fa-caret-down"></i>";
print "</button> <div class="dropdown-content" id="myDropdown"> <a href="/index.html">Ulinux</a>";
							print   "<a href="/404.html">Custom Linux From Scratch</a>";
							print   "<a href="/404.html">Embedded</a>";
							</div>
print "<a style="float:left" href="/index.html">About</a>";
print "<a style="float:left" href="/404.html">News</a>";
print "<a style="float:left" href="/404.html">Blog</a>";
print "<a style="float:left" href="/404.html">Contact</a>";
print "<a style="float:left" href="/404.html">Contributing</a>";
print "<div id="myLinks"> <a href="/404.html">Embedded</a> <a href="/404.html">LFS-Museum</a> </div>";
print "<a style="float:right" href="javascript:void(0);" class="icon" onclick="topnavslide()"> <i class="fa fa-bars"></i>";
print "<a style="float:right" href="/404.html">BLFS</a> <a style="float:right" href="/404.html">CLFS</a>";
						print " <a style="float:right" href="/404.html">LFS</a>";
						print " <a style="float:right" href="/404.html">GNU</a> </a> </div>";
print "<div class="main"> <h04>404</h04> <ol>";
					print "<li >This is my 404 for this website</li>";
					print "<li >This website is still under contruction</li>";
					print "<li >This feature is not ready yet or the page is not written</li>";
					print "<li >Or something happened and your at a lost page... 404</li> </ol> </div>";

<script src="cgi-bin/perl.cgi"></script>
print <<NAVBARBOTTOM;
<div class="navbarbottom">
  <a href="http://127.0.0.1:8080/index.html">Home</a>
  <a href="#Git">Git</a>
  <a href="#Bugs">Bugs</a>
  <a href="#Donate">Donate</a>
  <a style="float:right" href="http://127.0.0.1:8080/author.html">About Author</a>
</div>
<script>
function topnavdrop() {  document.getElementById("myDropdown").classList.toggle("show");
}
window.onclick = function(e) {
  if (!e.target.matches('.dropbtn')) {
  var myDropdown = document.getElementById("myDropdown");
    if (myDropdown.classList.contains('show')) {
      myDropdown.classList.remove('show');
    }
  }
}
function topnavslide() {
  var x = document.getElementById("myLinks");
  if (x.style.display === "block") {
    x.style.display = "none";
  } else {
    x.style.display = "block";
  }
}
</script> </body> </html>
NAVBARBOTTOM;
