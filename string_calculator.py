import re

class StringCalculator:
    def add(self, numbers: str) -> int:
        if not numbers:
            return 0
        # Support commas and newlines as delimiters
        nums = map(int, re.split(',|\n', numbers))
        return sum(nums)