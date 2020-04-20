#!/usr/bin/perl

use strict;
use warnings;

# Complete the compareTriplets function below.
sub compareTriplets {

    # init score values
    my $bob_score=0;
    my $alice_score=0;

    # Store array references
    my $a_ref=$_[0];
    my $b_ref=$_[1];

    # check if arrays have same length, give error if not
    unless (scalar @$a_ref == scalar @$b_ref)
    {
        print "Invalid input, arrays must have same number of elements.\n";
        return "error";
    }

    # compare for each value

    my @input_iterator = (0..((scalar @$a_ref)-1)); # to iterate from 0 to index-1

    foreach my $i (@input_iterator)
    {
        if ($$a_ref[$i]>$$b_ref[$i])
        {
            $alice_score++;
        }
        elsif ($$a_ref[$i]<$$b_ref[$i])
        {
            $bob_score++;
        }
    }

return ($alice_score, $bob_score);

}

open(my $fptr, '>', $ENV{'OUTPUT_PATH'});

my $a = rtrim(my $a_temp = <STDIN>);

my @a = split /\s+/, $a;

my $b = rtrim(my $b_temp = <STDIN>);

my @b = split /\s+/, $b;

my @result = compareTriplets (\@a, \@b);

print $fptr join " ", @result;
print $fptr "\n";

close $fptr;

sub ltrim {
    my $str = shift;

    $str =~ s/^\s+//;

    return $str;
}

sub rtrim {
    my $str = shift;

    $str =~ s/\s+$//;

    return $str;
}
