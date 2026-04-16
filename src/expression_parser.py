import math
import re

class ExpressionParser:
    """
    Parses mathematical expressions into a safe, evaluable format (a callable function).

    This parser handles basic arithmetic operations, exponentiation (converting '^' to '**'),
    a predefined set of mathematical functions from the 'math' module, and the variable 'x'.
    It includes input validation to ensure safety and correct syntax, and automatically
    inserts '*' for common implicit multiplication patterns.
    """

    # Allowed functions from the 'math' module. 'abs' and 'round' are built-ins
    # but explicitly included for clarity and control in the safe evaluation scope.
    _allowed_functions = {
        'sin': math.sin, 'cos': math.cos, 'tan': math.tan,
        'sqrt': math.sqrt, 'log': math.log, 'exp': math.exp,
        'abs': abs,
        'ceil': math.ceil, 'floor': math.floor, 'round': round,
        'radians': math.radians, 'degrees': math.degrees,
        'acos': math.acos, 'asin': math.asin, 'atan': math.atan, 'atan2': math.atan2,
        'cosh': math.cosh, 'sinh': math.sinh, 'tanh': math.tanh,
        'hypot': math.hypot, 'pow': math.pow, 'fmod': math.fmod,
        'factorial': math.factorial, 'gamma': math.gamma, 'lgamma': math.lgamma,
        'erf': math.erf, 'erfc': math.erfc,
        'log10': math.log10, 'log2': math.log2, 'log1p': math.log1p, 'expm1': math.expm1,
        'gcd': math.gcd,
    }

    # Allowed constants from the 'math' module
    _allowed_constants = {
        'pi': math.pi,
        'e': math.e,
        'tau': math.tau,
        'inf': math.inf,
        'nan': math.nan,
    }

    def __init__(self):
        """Initializes the ExpressionParser.

        The allowed functions and constants are defined as class-level attributes.
        """
        pass

    def _preprocess_expression(self, expression: str) -> str:
        """
        Applies preliminary transformations to the expression string.

        - Removes all whitespace.
        - Converts `^` to `**` for exponentiation.
        - Inserts '*' for common implicit multiplication patterns like:
          - Number followed by 'x', or an identifier (e.g., '2x', '2pi', '2sin(x)')
          - 'x' followed by '(', or an identifier (e.g., 'x(x+1)', 'xpi', 'xsin(x)')
          - ')' followed by 'x', '(', or an identifier (e.g., '(x+1)x', '(x+1)(x-1)', '(x+1)sin(x)')
          - Number followed by '(' (e.g., '2(x+1)')

        Args:
            expression: The raw mathematical expression string.

        Returns:
            The preprocessed expression string.
        """
        expression = expression.replace(' ', '')  # Remove all whitespace

        # Convert `^` to `**` for exponentiation
        expression = expression.replace('^', '**')

        # Handle implicit multiplication using specific regex patterns.
        # The order of these replacements is important.

        # Pattern 1: Number (integer or float) followed by 'x', or an identifier (function/constant).
        # This regex ensures the number can be an integer or float. The `[a-zA-Z_]+` matches
        # the longest possible identifier name (e.g., 'log10' instead of just 'log').
        # E.g., '2x' -> '2*x', '2.5pi' -> '2.5*pi', '2sin(x)' -> '2*sin(x)'
        expression = re.sub(r'(\d+(?:\.\d*)?)([a-zA-Z_]+)', r'\1*\2', expression)

        # Pattern 2: 'x' followed by an identifier.
        # E.g., 'xpi' -> 'x*pi', 'xsin(x)' -> 'x*sin(x)'
        expression = re.sub(r'(x)([a-zA-Z_]+)', r'\1*\2', expression)

        # Pattern 3: 'x' followed by '('.
        # E.g., 'x(x+1)' -> 'x*(x+1)'
        expression = re.sub(r'(x)(\()', r'\1*\2', expression)

        # Pattern 4: ')' followed by 'x', or an identifier.
        # E.g., '(x+1)x' -> '(x+1)*x', '(x+1)pi' -> '(x+1)*pi', '(x+1)sin(x)' -> '(x+1)*sin(x)'
        expression = re.sub(r'(\))([a-zA-Z_]+)', r'\1*\2', expression)

        # Pattern 5: ')' followed by '('.
        # E.g., '(x+1)(x-1)' -> '(x+1)*(x-1)'
        expression = re.sub(r'(\))(\()', r'\1*\2', expression)

        # Pattern 6: Number followed by '('.
        # E.g., '2(x+1)' -> '2*(x+1)'
        expression = re.sub(r'(\d+(?:\.\d*)?)(\()', r'\1*\2', expression)

        return expression

    def _validate_expression(self, expression: str) -> None:
        """
        Validates the preprocessed expression for allowed characters, balanced parentheses,
        and known identifiers. It uses Python's `compile` and a dummy `eval` to catch
        syntax and basic runtime errors without actual execution risks.

        Args:
            expression: The preprocessed mathematical expression string.

        Raises:
            ValueError: If the expression contains invalid characters, has unbalanced
                        parentheses, or contains unknown identifiers or syntax errors.
        """
        # 1. Check for non-whitelisted characters.
        # Build a set of all characters that are part of allowed function/constant names.
        allowed_name_chars = set()
        for name in self._allowed_functions:
            allowed_name_chars.update(name)
        for name in self._allowed_constants:
            allowed_name_chars.update(name)

        # Basic allowed characters (digits, 'x', '.', operators, parentheses)
        basic_allowed_chars = r"0-9x\.\+\-*/\(\)"
        # Escape special regex characters in the collected name characters
        name_char_pattern = re.escape("".join(sorted(list(allowed_name_chars))))

        # Combined pattern to find ANY character that is NOT allowed.
        invalid_char_regex = re.compile(rf"[^{basic_allowed_chars}{name_char_pattern}]")

        if invalid_char_regex.search(expression):
            raise ValueError(f"Expression contains invalid or disallowed characters.")

        # 2. Check for balanced parentheses.
        balance = 0
        for char in expression:
            if char == '(':
                balance += 1
            elif char == ')':
                balance -= 1
            if balance < 0:
                raise ValueError("Unbalanced parentheses: ')' without matching '('")
        if balance != 0:
            raise ValueError("Unbalanced parentheses: '(' without matching ')'")

        # 3. Identify and validate all potential identifiers.
        # This regex matches sequences of letters and digits that start with a letter or underscore.
        identifier_pattern = re.compile(r'[a-zA-Z_][a-zA-Z0-9_]*')
        found_identifiers = set(identifier_pattern.findall(expression))

        # Check each found identifier against our allowed list.
        for identifier in found_identifiers:
            if identifier == 'x':
                continue
            if identifier not in self._allowed_functions and identifier not in self._allowed_constants:
                raise ValueError(f"Unknown identifier '{identifier}' in expression.")

        # 4. Use Python's built-in `compile` and a dummy `eval` to catch syntax errors
        # and other structural issues that our regex might miss, without executing harmful code.
        try:
            # Create a dummy scope that includes 'x' and all allowed functions/constants
            # to prevent NameErrors during compilation/dummy evaluation.
            dummy_scope = {'x': 0.0}
            dummy_scope.update(self._allowed_functions)
            dummy_scope.update(self._allowed_constants)

            # Compile the expression in 'eval' mode to catch syntax errors specific to expressions.
            # This step only checks the syntax tree, no code is executed.
            compile(expression, '<string>', 'eval')

            # Perform a dummy evaluation to catch errors that are only evident during execution,
            # such as calling a non-callable, or incorrect number of arguments (for functions
            # that Python's eval might allow without arguments like `sin`).
            # This is done with a controlled safe_globals dictionary.
            safe_globals_for_dummy_eval = {'__builtins__': {'abs': abs, 'round': round, 'pow': math.pow}}
            safe_globals_for_dummy_eval.update(self._allowed_functions)
            safe_globals_for_dummy_eval.update(self._allowed_constants)
            eval(expression, safe_globals_for_dummy_eval, {'x': 0.0})

        except SyntaxError as e:
            raise ValueError(f"Syntax error in expression: {e}") from e
        except NameError as e:
            # This should ideally be caught by the `found_identifiers` check, but serves as a fallback.
            raise ValueError(f"Name error in expression (unknown variable or function): {e}") from e
        except TypeError as e:
            # Catches issues like calling a function with incorrect arguments if it's evaluated.
            # E.g., `sin` (the function object itself) would raise TypeError if called directly.
            raise ValueError(f"Type error in expression (e.g., invalid function call): {e}") from e
        except Exception as e:
            # Catch any other unexpected errors during the validation process.
            raise ValueError(f"An unexpected error occurred during expression validation: {e}") from e

    def parse(self, expression_string: str):
        """
        Parses a mathematical expression string into a callable function.

        The returned function takes a single argument 'x' (the value for the
        variable 'x' in the expression) and returns the evaluated result.

        Args:
            expression_string: The mathematical expression to parse,
                               e.g., 'x^2 + 2*x - sin(pi)'.

        Returns:
            A callable function `f(x)` that evaluates the parsed expression
            when called with a numerical value for 'x'.

        Raises:
            TypeError: If `expression_string` is not a string.
            ValueError: If the expression is invalid (e.g., syntax error,
                        unknown identifier, unbalanced parentheses, disallowed characters).
        """
        if not isinstance(expression_string, str):
            raise TypeError("Expression must be a string.")

        if not expression_string.strip():
            raise ValueError("Expression cannot be empty or just whitespace.")

        preprocessed_expression = self._preprocess_expression(expression_string)
        self._validate_expression(preprocessed_expression)

        # Prepare the safe evaluation environment for the lambda function.
        # `__builtins__` is restricted to prevent access to dangerous Python built-ins.
        safe_globals = {
            '__builtins__': {
                'abs': abs,   # Allow built-in abs
                'round': round, # Allow built-in round
                'pow': math.pow, # Use math.pow explicitly for consistency/safety
            }
        }
        # Add all allowed functions and constants to the safe global scope.
        safe_globals.update(self._allowed_functions)
        safe_globals.update(self._allowed_constants)

        # Return a lambda function that evaluates the preprocessed expression.
        # The 'x' variable is provided via the `locals` dictionary when the lambda is called.
        return lambda x: eval(preprocessed_expression, safe_globals, {'x': x})