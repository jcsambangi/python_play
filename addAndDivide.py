def main():
    """Add the number 1, 2, and 3 and divides the sum by 3.

    :returns: final product after summation and division
    """
    summation = add_three(1, 2, 3)
    final = divide_three(summation)
    print('This is the output of divide_three: {}'.format(final))

def add_three(v1, v2, v3):
    """Add the inputs

    :paramv1: number one
    :paramv2: number two
    :paramv3: number three
    :returns: summation of numbers
    """
    summation = v1 + v2 + v3
    return summation

def divide_three(summation):
    """"Divide the input by 3

    :paramsummation: input number
    :returns: quotient after division by 3
    """
    final = summation/3
    return final

if __name__ == "__main__":
    main()
