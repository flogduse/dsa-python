"""Behavioural tests for every script in the repo.

Plain `pytest` from the repo root:
    python -m pytest tests/ -q
"""
from __future__ import annotations

import pytest

from conftest import load


# ---------------------------------------------------------------- arrays
def test_reverse_array_in_place_and_slicing():
    m = load("arrays/reverse_array.py")
    assert m.reverse_array([1, 2, 3, 4]) == [4, 3, 2, 1]
    assert m.reverse_array_slicing([]) == []
    assert m.reverse_array_slicing([1]) == [1]


def test_rotate_array_both_directions():
    m = load("arrays/rotate_array.py")
    arr = [1, 2, 3, 4, 5]
    assert m.rotate_left(arr, 2) == [3, 4, 5, 1, 2]
    assert m.rotate_right(arr, 2) == [4, 5, 1, 2, 3]
    assert m.rotate_left(arr, 0) == arr
    assert m.rotate_left(arr, 5) == arr  # full rotation


def test_remove_duplicates_sorted_returns_new_length():
    m = load("arrays/remove_duplicates.py")
    arr = [1, 1, 2, 2, 3, 4, 4, 5]
    k = m.remove_duplicates_sorted(arr)
    assert k == 5
    assert arr[:k] == [1, 2, 3, 4, 5]
    assert m.remove_duplicates_sorted([]) == 0


def test_two_sum_finds_indices():
    m = load("arrays/two_sum.py")
    assert m.two_sum_brute([2, 7, 11, 15], 9) == [0, 1]
    assert m.two_sum_hash([2, 7, 11, 15], 9) == [0, 1]
    assert m.two_sum_hash([1, 2], 99) == []
    # Same element used twice is not allowed.
    assert m.two_sum_hash([3], 6) == []


# --------------------------------------------------------------- hashing
def test_first_duplicate():
    m = load("hashing/first_duplicate.py")
    assert m.first_duplicate([2, 5, 1, 2, 3, 5]) == 2
    assert m.first_duplicate([1, 2, 3]) is None
    assert m.first_duplicate([]) is None


def test_frequency_count():
    m = load("hashing/frequency_count.py")
    assert m.frequency_count([1, 2, 2, 3, 3, 3]) == {1: 1, 2: 2, 3: 3}
    assert m.frequency_count([]) == {}


# ----------------------------------------------------------- linked lists
def test_singly_linked_list_append_prepend_delete():
    m = load("linked-lists/singly_linked_list.py")
    ll = m.LinkedList()
    for v in [2, 3]:
        ll.append(v)
    ll.prepend(1)
    ll.delete(2)
    values = []
    node = ll.head
    while node:
        values.append(node.data)
        node = node.next
    assert values == [1, 3]


def test_reverse_linked_list():
    m = load("linked-lists/reverse_linked_list.py")
    ll = m.LinkedList()
    for v in [1, 2, 3]:
        ll.append(v)
    ll.head = m.reverse(ll.head)
    values, node = [], ll.head
    while node:
        values.append(node.data)
        node = node.next
    assert values == [3, 2, 1]
    assert m.reverse(None) is None


def test_detect_cycle():
    m = load("linked-lists/detect_cycle.py")
    ll = m.LinkedList()
    for v in [1, 2, 3]:
        ll.append(v)
    assert m.has_cycle(ll.head) is False
    ll.head.next.next.next = ll.head
    assert m.has_cycle(ll.head) is True
    assert m.has_cycle(None) is False


# ------------------------------------------------------------- recursion
def test_factorial():
    m = load("recursion/factorial.py")
    assert m.factorial(0) == 1
    assert m.factorial(5) == 120


def test_fibonacci_both_implementations_agree():
    m = load("recursion/fibonacci.py")
    expected = [0, 1, 1, 2, 3, 5, 8, 13]
    assert [m.fibonacci_iterative(n) for n in range(8)] == expected
    assert [m.fibonacci_recursive(n) for n in range(8)] == expected


def test_tower_of_hanoi_move_count(capsys):
    m = load("recursion/tower_of_hanoi.py")
    m.tower_of_hanoi(3, "A", "B", "C")
    lines = capsys.readouterr().out.strip().splitlines()
    assert len(lines) == 2**3 - 1  # n disks always need 2^n - 1 moves


# -------------------------------------------------------------- searching
def test_linear_search():
    m = load("searching/linear_search.py")
    assert m.linear_search([4, 2, 9], 9) == 2
    assert m.linear_search([4, 2, 9], 7) == -1


def test_binary_search_recursive_and_iterative():
    m = load("searching/binary_search.py")
    arr = [10, 20, 30, 40, 50]
    for target, want in [(10, 0), (30, 2), (50, 4), (99, -1)]:
        assert m.binary_search_iterative(arr, target) == want
        assert m.binary_search_recursive(arr, target, 0, len(arr) - 1) == want


# --------------------------------------------------------------- sorting
SORTERS = [
    ("sorting/bubble_sort.py", "bubble_sort"),
    ("sorting/selection_sort.py", "selection_sort"),
    ("sorting/insertion_sort.py", "insertion_sort"),
    ("sorting/merge_sort.py", "merge_sort"),
    ("sorting/quick_sort.py", "quick_sort"),
]


@pytest.mark.parametrize("relpath,func_name", SORTERS)
@pytest.mark.parametrize(
    "arr",
    [
        [],
        [1],
        [2, 1],
        [5, 1, 4, 2, 8],
        [3, 3, 1, 2, 2],
        [-4, 0, -1, 7],
    ],
)
def test_every_sort_matches_sorted(relpath, func_name, arr):
    m = load(relpath)
    sort = getattr(m, func_name)
    assert sort(list(arr)) == sorted(arr)


# --------------------------------------------------------- stacks/queues
def test_balanced_parentheses():
    m = load("stacks-queues/balanced_parentheses.py")
    for good in ["", "()", "()[]{}", "{[]}", "a(b[c]{d})"]:
        assert m.is_balanced(good) is True
    for bad in ["(]", "([)]", "(", ")", "}{"]:
        assert m.is_balanced(bad) is False


def test_stack_operations():
    m = load("stacks-queues/stack.py")
    s = m.Stack()
    assert s.is_empty() and s.pop() is None and s.peek() is None
    s.push(1)
    s.push(2)
    assert s.peek() == 2 and s.size() == 2
    assert s.pop() == 2 and s.pop() == 1


def test_queue_operations():
    m = load("stacks-queues/queue.py")
    q = m.Queue()
    assert q.is_empty() and q.dequeue() is None and q.front() is None
    q.enqueue(1)
    q.enqueue(2)
    assert q.front() == 1 and q.size() == 2
    assert q.dequeue() == 1 and q.dequeue() == 2


# --------------------------------------------------------------- strings
def test_palindrome_both_implementations():
    m = load("strings/palindrome.py")
    for s in ["racecar", "A man a plan a canal Panama", ""]:
        assert m.is_palindrome(s) is True
        assert m.is_palindrome_two_pointer(s) is True
    assert m.is_palindrome("hello") is False
    assert m.is_palindrome_two_pointer("hello") is False


def test_anagram_both_implementations():
    m = load("strings/anagram.py")
    assert m.is_anagram("listen", "silent") is True
    assert m.is_anagram_count("Debit Card", "Bad Credit") is True
    assert m.is_anagram("hello", "world") is False
    assert m.is_anagram_count("aab", "abb") is False


def test_count_vowels_and_consonants():
    m = load("strings/count_vowels.py")
    assert m.count_vowels("Hello World!") == 3
    assert m.count_consonants("Hello World!") == 7
    assert m.count_vowels("") == 0


def test_reverse_string_variants():
    m = load("strings/reverse_string.py")
    assert m.reverse_string("abc") == "cba"
    assert m.reverse_string_loop("abc") == "cba"
    assert m.reverse_words("  hello   world ") == "world hello"
