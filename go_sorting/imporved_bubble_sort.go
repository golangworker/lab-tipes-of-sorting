package main

import "fmt"

func ImpovedBubbleSort(arr []int) []int {
	fmt.Println("Improved Bubble sorting")
	for i := range arr {
		swapped := false
		for j := 0; j < len(arr)-i-1; j++ {
			if arr[j] > arr[j+1] {
				arr[j], arr[j+1] = arr[j+1], arr[j]
				swapped = true
			}
		}
		if swapped == false {
			break
		}
	}
	return arr
}
