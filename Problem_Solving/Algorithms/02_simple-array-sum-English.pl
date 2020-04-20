#!/usr/bin/perl

use strict;
use warnings;

#
# Complete the simpleArraySum function below.
#
sub simpleArraySum {
    #
    # Write your code here.
    my $ar_ref=@_[0];
    my $arr_int_sum;
    foreach my $arr_var (@{$ar_ref})
    {
        $arr_int_sum= $arr_int_sum + $arr_var;
    }
    #


    return $arr_int_sum;

}

open(my $fptr, '>', $ENV{'OUTPUT_PATH'});

my $ar_count = <>;
$ar_count =~ s/\s+$//;

my $ar = <>;
$ar =~ s/\s+$//;
my @ar = split /\s+/, $ar;
my $result = simpleArraySum (\@ar);

print $fptr "$result\n";

close $fptr;
