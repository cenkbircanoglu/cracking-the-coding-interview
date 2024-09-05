def count_ways(expression, result):
    # Memoization dictionary to store results of subproblems
    memo = {}

    def count_ways_helper(expr, result):
        # If this subproblem has already been solved, return the result
        if (expr, result) in memo:
            return memo[(expr, result)]

        # Base case: if the expression is a single character, evaluate it directly
        if len(expr) == 1:
            if result:
                return 1 if expr == 'T' else 0
            else:
                return 1 if expr == 'F' else 0

        # Initialize count of ways to 0
        ways = 0

        # Recursively evaluate each operator in the expression
        for i in range(1, len(expr), 2):  # Operators are at odd indices
            operator = expr[i]
            left_expr = expr[:i]
            right_expr = expr[i + 1:]

            # Recursively count the ways for the left and right parts of the expression
            left_true = count_ways_helper(left_expr, True)
            left_false = count_ways_helper(left_expr, False)
            right_true = count_ways_helper(right_expr, True)
            right_false = count_ways_helper(right_expr, False)

            total_ways = (left_true + left_false) * (right_true + right_false)

            # Calculate the number of ways the current operator can yield the result
            if operator == '&':
                if result:
                    ways += left_true * right_true
                else:
                    ways += total_ways - (left_true * right_true)
            elif operator == '|':
                if result:
                    ways += left_true * right_true + left_true * right_false + left_false * right_true
                else:
                    ways += left_false * right_false
            elif operator == '^':
                if result:
                    ways += left_true * right_false + left_false * right_true
                else:
                    ways += left_true * right_true + left_false * right_false

        # Store the computed result in the memoization dictionary
        memo[(expr, result)] = ways
        return ways

    return count_ways_helper(expression, result)


# Example usage
expression = "T|F&T^T"
desired_result = True
print(f"Number of ways to parenthesize the expression to get {desired_result}: {count_ways(expression, desired_result)}")
