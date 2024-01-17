Determine whether an integer is a palindrome. Do this without extra space.
A palindrome integer is an integer x for which reverse(x) = x where reverse(x) is x with its digit
reversed. Negative numbers are not palindromic.
Example :
Input : 12121
Output : 1

Input : 123
Output : 0
The isPalindrome function takes an integer x as input and checks if it is a palindrome.

It handles special cases where negative numbers and multiples of 10 are not palindromes.

It reverses the second half of the integer and compares it with the first half.

If the reversed and original halves match, or if there is a single middle digit left, the number is a palindrome.

The function returns True if the integer is a palindrome and False otherwise.

The example demonstrates the usage of the code with two test cases.
