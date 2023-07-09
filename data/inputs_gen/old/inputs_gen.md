# Inputs Generation

## Examples

### Question

```text
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
```

### Solution

```python
for _ in range(int(input())):
    n = int(input())
    mass = []
                    need -= 1
                i += 1
            print(*ans)
        else:
            print((oz - zo) // 2)
            ans = []
            need = (oz - zo) // 2
            i = 0
            while need:
                zzz = mass[ozs[i] - 1][len(mass[ozs[i] - 1]) - 1:: -1]
                if zzz not in zoss:
                    ans.append(ozs[i])
                    need -= 1
                i += 1
            print(*ans)
```

### Input Generator

```python
import random

def generate_inputs(t_max, n_max):
    t = random.randint(1, t_max)
    inputs = [str(t)]

    for _ in range(t):
        n = random.randint(1, n_max)
        inputs.append(str(n))

        words = set()
        while len(words) < n:
            word_length = random.randint(1, min(10, (4 * 10**6) // n))
            word = ''.join(random.choices('01', k=word_length))
            words.add(word)

        inputs.extend(words)

    return '\n'.join(inputs)


# Example usage
t_max = 4
n_max = 5
inputs = generate_inputs(t_max, n_max)
print(inputs)
```

---

### Question

```text
< PREVIOUS KATA
NEXT KATA >

## Task:

You have to write a function `pattern` which returns the following Pattern(See Examples) upto desired number of rows.

* Note:```Returning``` the pattern is not the same as ```Printing``` the pattern.

### Parameters:

    pattern(        n        ,        x        ,        y        );
                    ^                 ^                 ^
                    |                 |                 |
             Term upto which   Number of times   Number of times
              Basic Pattern     Basic Pattern     Basic Pattern
                should be         should be         should be
                 created          repeated           repeated
                                horizontally        vertically

* Note: `Basic Pattern` means what we created in Complete The Pattern #12

## Rules/Note:

* The pattern should be created using only unit digits.
* If `n < 1` then it should return "" i.e. empty string.
* If `x <= 1` then the basic pattern should not be repeated horizontally.
* If `y <= 1` then the basic pattern should not be repeated vertically.
* `The length of each line is same`, and is equal to the length of longest line in the pattern.
* Range of Parameters (for the sake of CW Compiler) :
  + `n ∈ (-∞,25]`
  + `x ∈ (-∞,10]`
  + `y ∈ (-∞,10]`
* If only two arguments are passed then the function `pattern` should run as if `y <= 1`.
* If only one argument is passed then the function `pattern` should run as if `x <= 1` & `y <= 1`.
* The function `pattern` should work when extra arguments are passed, by ignoring the extra arguments.


## Examples:

* Having Three Arguments-

 + pattern(4,3,2):

        1     1     1     1
         2   2 2   2 2   2
          3 3   3 3   3 3
           4     4     4
          3 3   3 3   3 3
         2   2 2   2 2   2
        1     1     1     1
         2   2 2   2 2   2
          3 3   3 3   3 3
           4     4     4
          3 3   3 3   3 3
         2   2 2   2 2   2
        1     1     1     1

* Having Two Arguments-

  + pattern(10,2):

        1                 1                 1
         2               2 2               2
          3             3   3             3
           4           4     4           4
            5         5       5         5
             6       6         6       6
              7     7           7     7
               8   8             8   8
                9 9               9 9
                 0                 0
                9 9               9 9
               8   8             8   8
              7     7           7     7
             6       6         6       6
            5         5       5         5
           4           4     4           4
          3             3   3             3
         2               2 2               2
        1                 1                 1

* Having Only One Argument-

  + pattern(25):

        1                                               1
         2                                             2
          3                                           3
           4                                         4
            5                                       5
             6                                     6
              7                                   7
               8                                 8
                9                               9
                 0                             0
                  1                           1
                   2                         2
                    3                       3
                     4                     4
                      5                   5
                       6                 6
                        7               7
                         8             8
                          9           9
                           0         0
                            1       1
                             2     2
                              3   3
                               4 4
                                5
                               4 4
                              3   3
                             2     2
                            1       1
                           0         0
                          9           9
                         8             8
                        7               7
                       6                 6
                      5                   5
                     4                     4
                    3                       3
                   2                         2
                  1                           1
                 0                             0
                9                               9
               8                                 8
              7                                   7
             6                                     6
            5                                       5
           4                                         4
          3                                           3
         2                                             2
        1                                               1

>>>LIST OF ALL MY KATAS<<<
```
