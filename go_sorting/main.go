package main

import "fmt"

func main() {
	arr := []int{5, 3, 8, 4, 2}
	sortedArr := ShellSort(arr)
	fmt.Println(sortedArr)
}
