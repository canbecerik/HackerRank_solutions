#!/usr/bin/perl

use strict;
use warnings;



my $n = <>;
$n =~ s/\s+$//;

if ($n%2!= 0 or (($n>6 and $n <21) and $n%2==0))
{
    print "Weird\n";
}

else {print "Not Weird\n"};
