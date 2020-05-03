# Enter your code here. Read input from STDIN. Print output to STDOUT
use strict;
my @input=<STDIN>;
chomp @input;
my $no_of_cases=$input[0];
my @output='';
for ( my $input_index=1; $input_index < $no_of_cases+1; $input_index++)
{
    unless ($input_index==1) {print "\n"};
    my $current_case=$input[$input_index];
    my @current_case_chars=split("",$current_case);
    for (my $string_even_index = 0; $string_even_index < scalar(@current_case_chars); $string_even_index=$string_even_index+2)
    {
        print "$current_case_chars[$string_even_index]";
    }
    print " ";
    for (my $string_odd_index = 1; $string_odd_index < scalar(@current_case_chars); $string_odd_index=$string_odd_index+2)
    {
        print "$current_case_chars[$string_odd_index]";
    }
    
}
