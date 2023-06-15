implementation for minimizing Boolean expressions using Karnaugh Maps (K-Maps). simplification of Boolean functions by deleting unnecessary terms from the expanded function, thus reducing the literal count.

Problem Statement

Given a Boolean function with 0s, 1s, and x's for each input combination, the task is to minimize the sum of product terms. The minimization process involves deleting terms that are fully contained within other terms or regions. The resulting set of terms should cover all the cells with '1'.

Features
_K-Map Generation:_ The repository includes code to generate K-Maps based on the number of input variables. This helps visualize the Boolean function and aids in the minimization process.

_Function Parsing:_ The provided code parses the given Boolean function and converts it into a suitable format for further processing.

_Term Extraction_: The implementation extracts the terms from the expanded function, considering the 0s, 1s, and x's for each input combination.

_Term Minimization:_ The algorithm identifies and removes terms that are fully contained within other terms or regions. This step reduces the number of terms in the Boolean expression.

_Sum of Products Generation:_ The code generates the minimized sum of product terms based on the remaining terms after minimization.
