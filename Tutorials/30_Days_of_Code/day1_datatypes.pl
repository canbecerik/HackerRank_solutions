
# Declare second integer, double, and String variables.
my $new_i, $new_d, $new_str;
# Read and save an integer, double, and String to your variables.
my @input=<STDIN>;
$new_i=$input[0];
$new_d=$input[1];
$new_str=$input[2];
# Print the sum of both integer variables on a new line.
my $sum_i=$i+$new_i;
print "$sum_i\n";
# Print the sum of the double variables on a new line.
my $sum_d=$d+$new_d;
printf ("%0.1f\n","$sum_d");
# Concatenate and print the String variables on a new line
print "$s"."$new_str";
# The 's' variable above should be printed first.

