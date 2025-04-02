# Laboratory work 2 

## Description

This project implements a doubly linked list, along with an alternative implementation based on built-in arrays/lists. It demonstrates fundamental list operations, including addition, deletion, search, and cloning. The code is covered with unit tests, and CI ensures the correctness of all tests on each commit.

## Variant

My number on the group list - 17.

17 % 4 = 1

**Initial implementation of the list** – doubly linked list.

**Second implementation of the list** – list based on built-in arrays/lists.

## Instructions

Clone the repository and navigate to its directory:

```sh
git clone https://github.com/ypapish/MTSD_lab2
cd /path/to/MTSD_lab2
```

Ensure that Python is installed:

```sh
python --version
```

Run the program:

```sh
python demo.py
```

Run the tests:

```sh
python -m unittest discover -s . -p "*_test.py"
```

## Failed test

Link to the commit, where tests failed: https://github.com/ypapish/MTSD_lab2/commit/c7bf62ed07a9e6d0219a871336c0d2b639b25cda

## Conclusion

Unit tests helped identify bugs in the implementation and simplified code refactoring. Additionally, CI made it easier to track broken functionality. In my opinion, this is not a waste of time but an essential stage of development.
