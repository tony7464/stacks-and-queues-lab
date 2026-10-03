# Lab: Stacks and Queues  
**Lab GitHub Repo**: [Stacks and Queues](https://github.com/learn-co-curriculum/stacks-and-queues-lab)

---

## How to Run

Requires Python 3.8 or newer. No external packages are needed.

```bash
git clone https://github.com/tony7464/stacks-and-queues-lab.git
cd stacks-and-queues-lab
python test_structures.py
```

A successful test run ends with `Ran 5 tests` and `OK`.

Run the demos to see both structures:

```bash
python custom_stack.py
python custom_queue.py
```

---

## Overview
In this lab, you’ll apply **stacks** and **queues** to solve two real-world challenges. First, you’ll implement a **parentheses validator** using a stack—a feature commonly used in compilers or formatting tools. Then, you'll simulate a **customer raffle system** using a queue, where entries are processed in the order received and a winner is selected.

By focusing on **LIFO** (last-in, first-out) and **FIFO** (first-in, first-out) behavior, you’ll develop a stronger understanding of foundational data structures used in systems like parsers, schedulers, and task processors.

---

## Task 1: Define the Problem

1. Implement a function that validates **balanced parentheses** using a stack.
2. Create a **queue** that stores customer entries and:
   - **Selects a random winner**.
   - **Dequeues up to and including** the winner.
3. Display the result of both operations clearly in your output.

**The Challenge**: Demonstrate your understanding of stack and queue behavior in common technical workflows.

---

## Task 2: Determine the Design

### Stack Functionality

- **File**: `custom_stack.py`
- **Function**:  
  - `is_valid_parentheses(s: str) -> bool`  
  - Returns `True` if the parentheses in the string are balanced.

### Queue Class Design

- **File**: `custom_queue.py`
- **Class**: `Queue`
- **Methods**:
  - `enqueue(item)`  
  - `dequeue()`  
  - `peek()`  
  - `is_empty()`  
  - `select_and_announce_winner()` → Randomly selects a winner and dequeues everyone up to and including that customer.

---

## Task 3: Develop, Test, and Refine the Code

### Set Up

#### Fork and Clone
1. Go to the provided **GitHub repository link**.  
2. Fork the repository to your GitHub account.  
3. Clone the forked repository to your local machine.

#### Open and Run
1. Open the project in your Python-friendly IDE (VSCode, PyCharm, etc.).  

### Implementation Details

1. **Starter code uses `pass`**:
   - You’ll see `pass` in method bodies—this is a Python placeholder.
   - Replace it with your actual code to make each method work.

2. **Build each file**:
   - Implement `Queue` methods as described above.
   - Write the stack validator function for balanced parentheses.

3. **Run Tests**:
   - Execute the provided test file with:
     ```bash
     python test_structures.py
     ```
   - Ensure all tests pass before submission.

4. **Push and Merge**:
   - Commit your work regularly.
   - Push to your feature branch.
   - Open a Pull Request (PR).
   - Merge to `main` after review.

---

## Task 4: Document and Maintain

### Best Practice Documentation Steps

- **Comment your logic**: Especially around recursive or loop-based behavior.
- **Explain your thinking** in your function definitions.
- **README**: Make sure your repo’s README includes how to run the project.
- **Clean Up**:
  - Remove debug prints.
  - Ensure your `.gitignore` ignores `.pyc`, `__pycache__`, etc.

---

## Solution Approach

### Parentheses validator (`custom_stack.py`)

`is_valid_parentheses` uses a Python list as an explicit stack (LIFO) and a dict that maps each closing bracket to its opener: `{')': '(', ']': '[', '}': '{'}`. Opening brackets are pushed. A closing bracket is valid only when the stack is not empty and the popped top is the matching opener, because the most recent unmatched opener must close first. Characters that are not brackets are ignored. At the end, `len(stack) == 0` is True only when every opener was closed. An empty stack on a closer, a mismatched closer, or leftover openers all return False. The scan is O(n) time and O(n) space.

### Customer raffle queue (`custom_queue.py`)

`Queue` keeps customers in a Python list and follows FIFO: `enqueue` appends to the back, and `dequeue` removes index 0 with `pop(0)`. `peek` returns the front item, or None when the queue is empty. `dequeue` on an empty queue raises `IndexError("dequeue from empty queue")`. `is_empty` returns `len(self.items) == 0`.

`select_and_announce_winner` returns None when the queue is empty. Otherwise it picks a winner index with `random.randrange(len(self.items))`, then calls `dequeue` in a loop from the front up to and including that winner so the FIFO order is explicit. It prints one announcement line and returns the winner string. Customers behind the winner stay in `self.items`. Selecting and removing the winner is O(n) because each `pop(0)` shifts the remaining list.

---

## Submission
Once your lab is complete and all tests are passing:

- Push your code to GitHub.
- Submit the link to your repo through **Canvas using CodeGrade**.
