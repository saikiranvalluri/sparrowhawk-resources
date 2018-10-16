#!/usr/bin/env perl

# Nagendra Kumar Goel

# This takes two arguments:
# 1) Pocolm training output folder
# 2) rnnlm weights file name (for output)

if (@ARGV != 2) {
  die "Usage: get_data_weights.pl <pocolm-folder> <output-file>\n";
}

$pdir = shift @ARGV;
$out = shift @ARGV;

open(P, "<$pdir/metaparameters") || die "Could not open $pdir/metaparameters";
open(N, "<$pdir/names") || die "Could not open $pdir/names"  ;
open(O, ">$out")  || die "Could not open $out for writing" ;

while(<N>) {
    @n = split(/\s/,$_);
    $name = $n[1];
    $w = <P>;
    @w = split(/\s/,$w);
    $weight = $w[1];
    print O "$name\t1\t$weight\n";
}
