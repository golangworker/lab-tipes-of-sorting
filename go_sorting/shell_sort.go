package main

import "fmt"

func ShellSort(arr []int) []int {
	fmt.Println("Shell sorting")
	for gap := len(arr) / 2; gap > 0; gap /= 2 {
		for i := gap; i < len(arr); i++ {
			temp := arr[i]
			hole := i
			for hole >= gap && arr[hole-gap] > temp {
				arr[hole] = arr[hole-gap]
				hole -= gap
			}
			arr[hole] = temp
		}
	}
	return arr
}
