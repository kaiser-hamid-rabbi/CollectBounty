from typing import List


class Solution:
    def calculate_power(self, string: str):
        # check whether a string is palindrom or not
        if string == string[::-1]:
            X = 5
        else:
            X = 1
        return len(string) // 2 + X

    def max_power_difference(self, input_strings: List[str]):
        powers = []
        for string in input_strings:
            power = self.calculate_power(string)
            powers.append(power)
        return max(powers) - min(powers)


def main():
    input_strings = ["abc", "acca", "loki"]
    solution = Solution()
    result = solution.max_power_difference(input_strings)
    print(f"Maximum difference in power: {result}")


if __name__ == "__main__":
    main()
