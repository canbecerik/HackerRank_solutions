#!/usr/bin/perl

use strict;
use warnings;

my $binary;
my $s;
my $t;
my $n = <>;
$n =~ s/\s+$//;

while ($n>0)
{
    my $rem;
    $rem=$n%2;
    $n/=2;
    if ($rem == 1)
    {
        $s++;
        if ($s>$t)
        {
            $t=$s;
        }
    }
    else
    {
        $s=0;
    }
}

print $t;
