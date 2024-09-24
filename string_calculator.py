import re

class StringCalculator:
    def add(self, numbers: str) -> int:
        try:
            if not numbers:
                print("Input:- '' -> Output:- 0")
                return 0

            # Checking for custom delimiter
            delimiter = ',|\n'
            if numbers.startswith("//"):
                delimiter_spec, numbers = numbers.split("\n", 1)
                delimiter = re.escape(delimiter_spec[2:])  # Extracting the custom delimiter

            # Split the numbers based on the delimiters
            numbers_list = re.split(delimiter, numbers)

            # Convert to integers and handle negative numbers
            total = 0
            negative_numbers = []
            for num in numbers_list:
                if num:
                    number = int(num)
                    if number < 0:
                        negative_numbers.append(number)
                    total += number

            # If there are negative numbers, raise an exception
            if negative_numbers:
                raise ValueError(f"negative numbers not allowed:- {','.join(map(str, negative_numbers))}")

            print(f"Input:- '{numbers}' -> Output:- {total}")
            return total
        except ValueError as ve:
            print(f"Error:- {ve}")
            raise
        except Exception as e:
            print(f"Unexpected error:- {e}")
            raise
