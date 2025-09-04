# Project Euler

Problems are taken from https://projecteuler.net/, the Project Euler. [Problems are licensed under CC BY-NC-SA 4.0](https://projecteuler.net/copyright).

Project Euler is a series of challenging mathematical/computer programming problems that require more than just mathematical
insights to solve. Project Euler is ideal for mathematicians who are learning to code.

The solutions will be checked by our [automated testing on GitHub Actions](https://github.com/TheAlgorithms/Python/actions) with the help of [this script](https://github.com/TheAlgorithms/Python/blob/master/scripts/validate_solutions.py). The efficiency of your code is also checked. You can view the top 10 slowest solutions on GitHub Actions logs (under `slowest 10 durations`) and open a pull request to improve those solutions.


### Solution Template

You can use the below template as your starting point but please read the [Coding Style](https://github.com/TheAlgorithms/Python/blob/master/project_euler/README.md#coding-style) first to understand how the template works.

Please change the name of the helper functions accordingly, change the parameter names with a descriptive one, replace the content within `[square brackets]` (including the brackets) with the appropriate content.

```python
"""
Project Euler Problem [problem number]: [link to the original problem]

... [Entire problem statement] ...

... [Solution explanation - Optional] ...

References [Optional]:
- [Wikipedia link to the topic]
- [Stackoverflow link]
...

"""
import module1
import module2
...

def helper1(arg1: [type hint], arg2: [type hint], ...) -> [Return type hint]:
    """
    A brief statement explaining what the function is about.

    ... A more elaborate description ... [Optional]

    ...
    [Doctest]
    ...

    """
    ...
    # calculations
    ...

    return


# You can have multiple helper functions but the solution function should be
# after all the helper functions ...


def solution(arg1: [type hint], arg2: [type hint], ...) -> [Return type hint]:
    """
    A brief statement mentioning what the function is about.

    You can have a detailed explanation about the solution in the
    module-level docstring.

    ...
    [Doctest as mentioned above]
    ...

    """

    ...
    # calculations
    ...

    return answer


if __name__ == "__main__":
    print(f"{solution() = }")
```
