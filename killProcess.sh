#! /bin/bash

IFS='\",[]'
arr=( $1 )
for i in "${arr[@]}" 
do 
    kill $i
done
