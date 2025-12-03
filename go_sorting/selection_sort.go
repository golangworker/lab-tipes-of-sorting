package main

import "fmt"

func SelectionSort(arr []int) []int {
	fmt.Println("selection sorting")
	for i := range arr {
		currVal := arr[i]
		minIndx := i
		for j := i; j < len(arr); j++ {
			if arr[minIndx] > arr[j] {
				minIndx = j
			}
		}
		arr[i] = arr[minIndx]
		arr[minIndx] = currVal
	}
	return arr
}
