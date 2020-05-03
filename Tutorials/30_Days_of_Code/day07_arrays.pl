#!/usr/bin/perl

use strict;
use warnings;



my $n = <>;
$n =~ s/\s+$//;

my $arr = <>;
$arr =~ s/\s+$//;
my @arr = split /\s+/, $arr;
chomp @arr;
my @output= reverse @arr;
my $first=1;

foreach (@output)
{
    unless ($first == 1) {print " "};
    print "$_";
    $first=0;

}
