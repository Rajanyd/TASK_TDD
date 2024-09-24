import re

class StringCalculator:
    def add(self, numbers: str) -> int:
        if not numbers:
            return 0

        # Check for custom delimiter
        delimiter = ',|\n'
        if numbers.startswith("//"):
            delimiter_spec, numbers = numbers.split("\n", 1)
            delimiter = re.escape(delimiter_spec[2:])  # Extract custom delimiter

        # Split the numbers based on the delimiter(s)
        nums = map(int, re.split(delimiter, numbers))
        return sum(nums)