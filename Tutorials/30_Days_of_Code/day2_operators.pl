#!/usr/bin/perl

use strict;
use warnings;

# Complete the solve function below.
sub solve {
my $tip=$_[0]*$_[1]*0.01;
my $tax=$_[0]*$_[2]*0.01;
my $total=$_[0]+$tip+$tax;
printf("%.0f\n",$total);

}

my $meal_cost = <>;
$meal_cost =~ s/\s+$//;

my $tip_percent = <>;
$tip_percent =~ s/\s+$//;

my $tax_percent = <>;
$tax_percent =~ s/\s+$//;

solve ($meal_cost, $tip_percent, $tax_percent);
