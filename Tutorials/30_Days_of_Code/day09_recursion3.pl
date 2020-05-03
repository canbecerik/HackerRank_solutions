#!/usr/bin/perl

use strict;
use warnings;

# Complete the factorial function below.
sub factorial {
    my $n=$_[0];
    my $total=1;
    if ($n==1)
    {
        return $total;
    }
    else
    {
        $total=$n*(factorial($n-1))
    };
    return $total;

}

my $n = <>;
chomp $n;

my $result = factorial ($n);

print "$result\n";
