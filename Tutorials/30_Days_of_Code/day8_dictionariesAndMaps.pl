# Enter your code here. Read input from STDIN. Print output to STDOUT
use strict;
my %phoneBook=();
my $n=<STDIN>;
chomp $n;

for(my $i=0; $i<$n; $i++)
{
    my $input=<STDIN>;
    chomp $input;
    my ($name, $number) = split (/ /, $input);
    $phoneBook{$name}=$number;
}


while (my $query=<>)
{
    chomp $query;
    if (exists $phoneBook{$query})
    {
        print "$query=$phoneBook{$query}\n";
    }
    else
    {
        print "Not found\n";
    }
}
