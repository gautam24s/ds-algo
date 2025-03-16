package main

import "fmt"

func isOdd(n int) bool {
	return n&1 == 1
}

func multiplyByTwo(n int) int {
	return n << 1
}

func divideByTwo(n int) int {
	return n >> 1
}

func setBit(n, position int) int {
	return n | (1 << position)
}

func clearBit(n, position int) int {
	mask := (1 << position)
	invertedMask := ^mask
	return n & invertedMask
}

func toggleBits(n, position int) int {
	return n ^ (1 << position)
}

func isBitSet(n, position int) bool {
	return n&(1<<position) != 0
}

func rightmostSetBit(n int) int {
	return n & -n
}

func main() {
	fmt.Println("Is 3 odd? ", isOdd(3))
	fmt.Println("Multiply 4 by 2: ", multiplyByTwo(4))
	fmt.Println("Divide 4 by 2: ", divideByTwo(4))
	fmt.Println("Set 1 at position 2: ", setBit(8, 2))
	fmt.Println("Clear bit at position 0: ", clearBit(5, 0)) // Example usage of clearBit
	fmt.Println("Toggle bit at position 1: ", toggleBits(5, 1))
	fmt.Println("Is bit at position 2 set: ", isBitSet(5, 2))
	fmt.Println("Rightmost set bit in 12: ", rightmostSetBit(12))
}
