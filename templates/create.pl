#!/usr/bin/env perl

use strict;
use warnings;
use Template;
 
my $tt = Template->new({
    INCLUDE_PATH => './',
    INTERPOLATE  => 1,
}) or die "$Template::ERROR\n";
 
my %data = (
    title      => 'This is your title',
    languages  => ['English', 'Spanish', 'Hungarian', 'Hebrew'],
    people     => [
        { name => 'Foo', email => 'foo@perlmaven.com' },
        { name => 'Zorg' },
        { name => 'Bar', email => 'Bar@perlmaven.com' },
    ],
);
 
my $report;
$tt->process('report.tt', \%data, \$report) or die $tt->error(), "\n";
print $report;
