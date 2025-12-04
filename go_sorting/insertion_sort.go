package main

import "fmt"

func InsertionSort(arr []int) []int {
	fmt.Println("Insertion sorting")
	for i := 1; i < len(arr); i++ {
		tmp := arr[i]
		hole := i
		for hole > 0 && tmp < arr[hole-1] {
			arr[hole] = arr[hole-1]
			hole--
		}
		arr[hole] = tmp
	}
	return arr
}
