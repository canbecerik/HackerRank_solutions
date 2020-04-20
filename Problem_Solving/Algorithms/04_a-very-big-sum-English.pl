# Complete the aVeryBigSum function below.
sub aVeryBigSum {
# initialize value
my $array_sum=0;
# store reference
my $array_ref=$_[0];
# create iterator
my @iterator= (0..(scalar @$array_ref)-1);
# add each array value
foreach my $i (@iterator)
{
    $array_sum+=$$array_ref[$i];
}
return $array_sum;

}