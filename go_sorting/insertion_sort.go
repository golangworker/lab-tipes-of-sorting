package main

import "fmt"

func InsertionSort(arr []int) []int {
	fmt.Println("Insertion sorting")
	for i := 1; i < len(arr); i++ {
		hole := arr[i]
		indx := i
		for indx > 0 && hole < arr[indx-1] {
			arr[indx] = arr[indx-1]
			indx--
		}
		arr[indx] = hole
	}
	return arr
}
