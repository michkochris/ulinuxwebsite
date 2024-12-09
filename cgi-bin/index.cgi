#!/usr/bin/env perl

print "Content-type:text/html\r\n\r\n";
print "<html>\n";
print "<head>\n";
print "<title>Hello Word</title>\n";
print "<link rel='stylesheet' href='ulinuxweb.css' type='text/css'>\n";
print "</head>\n";
print "<div class='main'>\n";
print "<body\n";
print "<h1>Hello Word! This is my first CGI program</h1>\n";
print "</body>\n";
print "</html>\n";
#print "<font size=+1>Environment</font>\n";
#
#foreach (sort keys %ENV) {
#   print "<b>$_</b>: $ENV{$_}<br>\n";
#}
1;
