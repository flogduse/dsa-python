# DSA Python — Beginner Reference Implementations

Small, self-contained Data Structures and Algorithms programs in Python, each
runnable on its own and each covered by a test. Written while working through
the patterns in `patterns/`, so the emphasis is on readable implementations
rather than interview-optimised tricks.

> **Scope:** this is a learning repo, not a library. Every file in the topic
> folders below is implemented and tested. `ROADMAP.md`, `tracker.md` and
> `patterns/` are the study plan and notes that drove it — they list problems
> and topics, not code that ships here.

## What is implemented

| Folder | Files | What it shows |
|---|---|---|
| `arrays/` | `reverse_array.py`, `rotate_array.py`, `remove_duplicates.py`, `two_sum.py` | in-place reversal, left/right rotation, in-place dedupe of a sorted array, brute force vs hash-map two sum |
| `hashing/` | `frequency_count.py`, `first_duplicate.py` | counting with a dict, first repeated value with a set |
| `linked-lists/` | `singly_linked_list.py`, `reverse_linked_list.py`, `detect_cycle.py` | append/prepend/delete, iterative reversal, Floyd's cycle detection |
| `stacks-queues/` | `stack.py`, `queue.py`, `balanced_parentheses.py` | list-backed stack, `deque`-backed queue, bracket matching |
| `recursion/` | `factorial.py`, `fibonacci.py`, `tower_of_hanoi.py` | base cases, recursive vs iterative Fibonacci, Hanoi move order |
| `sorting/` | `bubble_sort.py`, `selection_sort.py`, `insertion_sort.py`, `merge_sort.py`, `quick_sort.py` | five sorts with the same `list -> sorted list` contract |
| `searching/` | `linear_search.py`, `binary_search.py` | linear search, binary search iterative and recursive |
| `strings/` | `palindrome.py`, `anagram.py`, `count_vowels.py`, `reverse_string.py` | two-pointer vs slice checks, `Counter` comparison, character counting, word reversal |

`patterns/` contains written notes for eight topic areas (arrays/hashing,
two pointers, linked lists, trees, graphs, DP, sorting/searching, system
design). They are reading material, not runnable code.

## How to run

Every script has a `__main__` block with example input:

```bash
python arrays/two_sum.py
python sorting/merge_sort.py
```

## Tests

```bash
pip install pytest
python -m pytest tests/ -q
```

The suite imports each script by file path (the folders are not packages) and
checks behaviour, including edge cases: empty input, single elements, full
rotations, duplicate values, unbalanced brackets and a linked-list cycle.

## License

MIT — see [LICENSE](LICENSE).
