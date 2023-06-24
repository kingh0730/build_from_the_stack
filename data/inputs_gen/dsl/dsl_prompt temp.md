# Prompt

## Template

Your task is to write an input generator for a competitive programming question.
Your input generator should produce a single valid input for the question.
Your input generator can only use:
    the built-in `min`, `max`, `abs`, `pow`, `sum`, `len`, `range`,
    `sorted`, `reversed`, `enumerate` functions,
    `if`, `else`, `for`, `break`, `continue` statements,
    list comprehension,
    and the functions defined below (implementations are hidden).
    Everything else is NOT allowed!!!

```python
def record(arg: int | float | str):
    """
    Records the argument
    """


def gen_int(min_inclusive: int, max_inclusive: int):
    """
    Returns a random integer between min and max
    """


def gen_float(min_inclusive: float, max_inclusive: float):
    """
    Returns a random float between min and max
    """


def gen_pos_int(max_inclusive: int):
    """
    Returns a random integer between 1 and max
    """


def gen_neg_int(min_inclusive: int):
    """
    Returns a random integer between min and -1
    """


def enum(*args):
    """
    Returns a random element from the list of args
    """


def to_str_then_concat(args: list):
    """
    Returns a string concatenation of all elements in args
    """


def to_str_then_concat_with_space(args: list):
    """
    Returns a string concatenation using space as separator of all elements in args
    """
```

Examples of a valid input generator for a question:

Example 1:

```text
QUESTION


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

```python
INPUT_GENERATOR


def generate_input():
    t = gen_pos_int(10**4)
    record(t)

    for _ in range(t):
        n = gen_pos_int(2 * 10**5)
        record(n)

        for _ in range(n):
            word_length = gen_pos_int(4 * 10**6 // n)
            word = to_str_then_concat(
                [enum("0", "1") for _ in range(word_length)],
            )
            record(word)
```

Example 2:

```text
QUESTION


Mikhail walks on a Cartesian plane. He starts at the point $(0, 0)$, and in one move he can go to any of eight adjacent points. For example, if Mikhail is currently at the point $(0, 0)$, he can go to any of the following points in one move:   $(1, 0)$;  $(1, 1)$;  $(0, 1)$;  $(-1, 1)$;  $(-1, 0)$;  $(-1, -1)$;  $(0, -1)$;  $(1, -1)$.

If Mikhail goes from the point $(x1, y1)$ to the point $(x2, y2)$ in one move, and $x1 \ne x2$ and $y1 \ne y2$, then such a move is called a diagonal move.

Mikhail has $q$ queries. For the $i$-th query Mikhail's target is to go to the point $(n_i, m_i)$ from the point $(0, 0)$ in exactly $k_i$ moves. Among all possible movements he want to choose one with the maximum number of diagonal moves. Your task is to find the maximum number of diagonal moves or find that it is impossible to go from the point $(0, 0)$ to the point $(n_i, m_i)$ in $k_i$ moves.

Note that Mikhail can visit any point any number of times (even the destination point!).


-----Input-----

The first line of the input contains one integer $q$ ($1 \le q \le 10^4$) — the number of queries.

Then $q$ lines follow. The $i$-th of these $q$ lines contains three integers $n_i$, $m_i$ and $k_i$ ($1 \le n_i, m_i, k_i \le 10^{18}$) — $x$-coordinate of the destination point of the query, $y$-coordinate of the destination point of the query and the number of moves in the query, correspondingly.


-----Output-----

Print $q$ integers. The $i$-th integer should be equal to -1 if Mikhail cannot go from the point $(0, 0)$ to the point $(n_i, m_i)$ in exactly $k_i$ moves described above. Otherwise the $i$-th integer should be equal to the the maximum number of diagonal moves among all possible movements.


-----Example-----
Input
3
2 2 3
4 3 7
10 1 9

Output
1
6
-1



-----Note-----

One of the possible answers to the first test case: $(0, 0) \to (1, 0) \to (1, 1) \to (2, 2)$.

One of the possible answers to the second test case: $(0, 0) \to (0, 1) \to (1, 2) \to (0, 3) \to (1, 4) \to (2, 3) \to (3, 2) \to (4, 3)$.

In the third test case Mikhail cannot reach the point $(10, 1)$ in 9 moves.
```

```python
INPUT_GENERATOR


def generate_input():
    q = gen_pos_int(10**4)
    record(q)

    for _ in range(q):
        ni = gen_pos_int(10**18)
        mi = gen_pos_int(10**18)
        ki = gen_pos_int(10**18)

        line = to_str_then_concat_with_space([ni, mi, ki])
        record(line)
```

Now, write an input generator for the following competitive programming question:

```text
QUESTION


You are given three sequences: $a_1, a_2, \ldots, a_n$; $b_1, b_2, \ldots, b_n$; $c_1, c_2, \ldots, c_n$.

For each $i$, $a_i \neq b_i$, $a_i \neq c_i$, $b_i \neq c_i$.

Find a sequence $p_1, p_2, \ldots, p_n$, that satisfy the following conditions:



 $p_i \in \{a_i, b_i, c_i\}$

 $p_i \neq p_{(i \mod n) + 1}$.

In other words, for each element, you need to choose one of the three possible values, such that no two adjacent elements (where we consider elements $i,i+1$ adjacent for $i<n$ and also elements $1$ and $n$) will have equal value.

It can be proved that in the given constraints solution always exists. You don't need to minimize/maximize anything, you need to find any proper sequence.


-----Input-----

The first line of input contains one integer $t$ ($1 \leq t \leq 100$): the number of test cases.

The first line of each test case contains one integer $n$ ($3 \leq n \leq 100$): the number of elements in the given sequences.

The second line contains $n$ integers $a_1, a_2, \ldots, a_n$ ($1 \leq a_i \leq 100$).

The third line contains $n$ integers $b_1, b_2, \ldots, b_n$ ($1 \leq b_i \leq 100$).

The fourth line contains $n$ integers $c_1, c_2, \ldots, c_n$ ($1 \leq c_i \leq 100$).

It is guaranteed that $a_i \neq b_i$, $a_i \neq c_i$, $b_i \neq c_i$ for all $i$.


-----Output-----

For each test case, print $n$ integers: $p_1, p_2, \ldots, p_n$ ($p_i \in \{a_i, b_i, c_i\}$, $p_i \neq p_{i \mod n + 1}$).

If there are several solutions, you can print any.


-----Example-----
Input
5
3
1 1 1
2 2 2
3 3 3
4
1 2 1 2
2 1 2 1
3 4 3 4
7
1 3 3 1 1 1 1
2 4 4 3 2 2 4
4 2 2 2 4 4 2
3
1 2 1
2 3 3
3 1 2
10
1 1 1 2 2 2 3 3 3 1
2 2 2 3 3 3 1 1 1 2
3 3 3 1 1 1 2 2 2 3

Output
1 2 3
1 2 1 2
1 3 4 3 2 4 2
1 3 2
1 2 3 1 2 3 1 2 3 2



-----Note-----

In the first test case $p = [1, 2, 3]$.

It is a correct answer, because:

  $p_1 = 1 = a_1$, $p_2 = 2 = b_2$, $p_3 = 3 = c_3$  $p_1 \neq p_2 $, $p_2 \neq p_3 $, $p_3 \neq p_1$

All possible correct answers to this test case are: $[1, 2, 3]$, $[1, 3, 2]$, $[2, 1, 3]$, $[2, 3, 1]$, $[3, 1, 2]$, $[3, 2, 1]$.

In the second test case $p = [1, 2, 1, 2]$.

In this sequence $p_1 = a_1$, $p_2 = a_2$, $p_3 = a_3$, $p_4 = a_4$. Also we can see, that no two adjacent elements of the sequence are equal.

In the third test case $p = [1, 3, 4, 3, 2, 4, 2]$.

In this sequence $p_1 = a_1$, $p_2 = a_2$, $p_3 = b_3$, $p_4 = b_4$, $p_5 = b_5$, $p_6 = c_6$, $p_7 = c_7$. Also we can see, that no two adjacent elements of the sequence are equal.
```
