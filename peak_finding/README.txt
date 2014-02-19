Peak Finding Code for PSET #1
=============================

## Summary

* `algorithms.py` contains the three referenced implementations in the PSET for peak finding.
* `algorithm1D.py` contains the binary search implementation for a 1D problem.
* `generate.py` creates random problems.
* `main.py` runs each algorithm against a problem.

## Usage

Run `python generate.py` to generate a random problem and save it to disk.

    $ python generate.py
    Generated a matrix with 10 row and 10 columns.
    Enter a file name to save to (default: problem.py):
    The file problem.py already exists.
    Overwrite (o), enter another name (f), or cancel (c)? o

    $ cat problem.py
    problemMatrix = [[99, 16, 187, 17, 171, 48, 165, 100, 192, 126],
     [33, 67, 13, 27, 180, 175, 200, 87, 107, 51],
     [2, 31, 118, 44, 153, 177, 141, 87, 21, 6],
     [27, 137, 31, 177, 147, 24, 102, 172, 83, 135],
     [132, 29, 137, 191, 152, 127, 0, 103, 37, 108],
     [111, 94, 126, 104, 122, 62, 69, 95, 164, 188],
     [165, 78, 130, 185, 55, 26, 34, 144, 141, 103],
     [32, 88, 136, 103, 5, 47, 80, 56, 67, 123],
     [45, 184, 67, 177, 113, 91, 129, 129, 198, 105],
     [67, 16, 72, 115, 77, 66, 160, 81, 6, 44]]

Run `python main.py` to run each algorithm against the problem.

    $ python main.py
    Enter a file name to load from (default: problem.py):
    Algorithm 3 : (2, 5) => is a peak
    Algorithm 4 : (2, 5) => is a peak
    Algorithm 5 : (5, 9) => is a peak

You may edit `problem.py` by hand to try out any counterexample.
