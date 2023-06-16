# Prompts

## Template

Write an input generator in Python that satisfies the following requirements:

-----Input Requirements-----
{requirements}

-----Input Example 1-----
{example}

-----Input Example 2-----
{example}

-----Input Example N-----
{example}

## Examples

### Problem ID

0

### Question

Polycarp has $n$ different binary words. A word called binary if it contains only characters '0' and '1'. For example, these words are binary: "0001", "11", "0" and "0011100".

Polycarp wants to offer his set of $n$ binary words to play a game "words". In this game, players name words and each next word (starting from the second) must start with the last character of the previous word. The first word can be any. For example, these sequence of words can be named during the game: "0101", "1", "10", "00", "00001".

Word reversal is the operation of reversing the order of the characters. For example, the word "0111" after the reversal becomes "1110", the word "11010" after the reversal becomes "01011".

Probably, Polycarp has such a set of words that there is no way to put them in the order correspondent to the game rules. In this situation, he wants to reverse some words from his set so that:  the final set of $n$ words still contains different words (i.e. all words are unique);  there is a way to put all words of the final set of words in the order so that the final sequence of $n$ words is consistent with the game rules.

Polycarp wants to reverse minimal number of words. Please, help him.

-----Input-----

The first line of the input contains one integer $t$ ($1 \le t \le 10^4$) — the number of test cases in the input. Then $t$ test cases follow.

The first line of a test case contains one integer $n$ ($1 \le n \le 2\cdot10^5$) — the number of words in the Polycarp's set. Next $n$ lines contain these words. All of $n$ words aren't empty and contains only characters '0' and '1'. The sum of word lengths doesn't exceed $4\cdot10^6$. All words are different.

Guaranteed, that the sum of $n$ for all test cases in the input doesn't exceed $2\cdot10^5$. Also, guaranteed that the sum of word lengths for all test cases in the input doesn't exceed $4\cdot10^6$.

-----Output-----

Print answer for all of $t$ test cases in the order they appear.

If there is no answer for the test case, print -1. Otherwise, the first line of the output should contain $k$ ($0 \le k \le n$) — the minimal number of words in the set which should be reversed. The second line of the output should contain $k$ distinct integers — the indexes of the words in the set which should be reversed. Words are numerated from $1$ to $n$ in the order they appear. If $k=0$ you can skip this line (or you can print an empty line). If there are many answers you can print any of them.

-----Example-----
Input
4
4
0001
1000
0011
0111
3
010
101
0
2
00000
00001
4
01
001
0001
00001

Output
1
3
-1
0

2
1 2

### Prompt

Write an input generator in Python that satisfies the following requirements:

-----Input Requirements-----

The first line of the input contains one integer $t$ ($1 \le t \le 10^4$) — the number of test cases in the input. Then $t$ test cases follow.

The first line of a test case contains one integer $n$ ($1 \le n \le 2\cdot10^5$) — the number of words in the Polycarp's set. Next $n$ lines contain these words. All of $n$ words aren't empty and contains only characters '0' and '1'. The sum of word lengths doesn't exceed $4\cdot10^6$. All words are different.

Guaranteed, that the sum of $n$ for all test cases in the input doesn't exceed $2\cdot10^5$. Also, guaranteed that the sum of word lengths for all test cases in the input doesn't exceed $4\cdot10^6$.

-----Input Example-----
4
4
0001
1000
0011
0111
3
010
101
0
2
00000
00001
4
01
001
0001
00001

### Answer

Here's a Python code snippet that generates input satisfying the given requirements:

```python
import random

def generate_input():
    t = random.randint(1, 10**4)
    test_cases = []
    
    for _ in range(t):
        n = random.randint(1, 2*10**5)
        words = set()
        
        for _ in range(n):
            word_length = random.randint(1, (4*10**6)//n)  # Distribute word lengths among n words
            word = ''.join(random.choices(['0', '1'], k=word_length))
            words.add(word)
        
        test_cases.append((n, words))
    
    input_lines = []
    input_lines.append(str(t))
    
    for test_case in test_cases:
        input_lines.append(str(test_case[0]))
        input_lines.extend(test_case[1])
    
    return '\n'.join(input_lines)

# Generate input and print
input_data = generate_input()
print(input_data)
```

This code will generate the desired input with the number of test cases, the number of words in each test case, and the actual words themselves randomly generated within the given constraints. You can adjust the `random.randint` ranges according to your requirements if needed.

### Comments

- Very slow to execute

---

### Problem ID

300

### Question

Given a single positive integer x, we will write an expression of the form x (op1) x (op2) x (op3) x ... where each operator op1, op2, etc. is either addition, subtraction, multiplication, or division (+, -, *, or /).  For example, with x = 3, we might write 3* 3 / 3 + 3 - 3 which is a value of 3.
When writing such an expression, we adhere to the following conventions:

The division operator (/) returns rational numbers.
There are no parentheses placed anywhere.
We use the usual order of operations: multiplication and division happens before addition and subtraction.
It's not allowed to use the unary negation operator (-).  For example, "x - x" is a valid expression as it only uses subtraction, but "-x + x" is not because it uses negation.

We would like to write an expression with the least number of operators such that the expression equals the given target.  Return the least number of operators used.

Example 1:
Input: x = 3, target = 19
Output: 5
Explanation: 3 *3 + 3* 3 + 3 / 3.  The expression contains 5 operations.

Example 2:

Input: x = 5, target = 501
Output: 8
Explanation: 5 *5* 5 *5 - 5* 5 * 5 + 5 / 5.  The expression contains 8 operations.

Example 3:
Input: x = 100, target = 100000000
Output: 3
Explanation: 100 *100* 100 * 100.  The expression contains 3 operations.

Note:

2 <= x <= 100
1 <= target <= 2 * 10^8

### Prompt

Write an input generator in Python that satisfies the following requirements:

-----Input Requirements-----

2 <= x <= 100
1 <= target <= 2 * 10^8

-----Input Example 1-----
x = 3, target = 19

-----Input Example 2-----
x = 5, target = 501

-----Input Example 3-----
x = 100, target = 100000000

### Answer

Here's a Python code snippet that generates input satisfying the given requirements:

```python
import random

def generate_input():
    x = random.randint(2, 100)
    target = random.randint(1, 2 * 10**8)
    return x, target

# Example usage:
x, target = generate_input()
print(f"x = {x}, target = {target}")
```

This code defines a `generate_input` function that randomly selects values for `x` and `target` within the specified ranges. You can call this function whenever you need to generate a new set of inputs. The examples above demonstrate how to use the `generate_input` function and print the generated values.

### Comments

- Actually very hard to verify the semantic validity of inputs without implementing the solution itself

---
