#!/usr/bin/perl

use strict;
use warnings;



my $n = <>;
$n =~ s/\s+$//;
my @ten=(1..10);

foreach my $current (@ten)
{
    my $result=$n*$current;
    print $n." x ".$current." = ".$result."\n";
}
