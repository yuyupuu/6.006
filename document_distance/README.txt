Document Distance Code for PSET #1
==================================

- `docdist.py` is a template for you to implement solutions to Part B of Problem Set 1.
- `speech1.txt` and `speech2.txt` contain short speeches you might recognize and can be used to test for correctness of your algorithm at a small scale. We found their distance to be:
  - 1.255 radians using single words
  - 1.566 radians using pairs of words
- `shakespeare.txt` and `chaucer.txt` contain the full works of their respective authors and can be used as larger test cases to run locally. Our solution compares these in ~5 seconds for both words and pairs. We found their distance to be:
  - 0.429 radians using single words
  - 0.885 radians using pairs of words

## Local Testing

You can run your implementation against the provided files to check for accuracy in the following way.

```bash
# using words
python docdist.py <file1> <file2>

# using pairs
python docdist.py --pairs <file1> <file2>
```

## Submitting

Submit your solution on alg.csail.mit.edu. Each part of your solution will be tested independently, so be sure to adhere to the spec in the prompt.
