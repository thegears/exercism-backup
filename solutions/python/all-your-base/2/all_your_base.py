def rebase(input_base, digits, output_base):
    if input_base < 2:
        raise ValueError("input base must be >= 2")

    if any(e < 0 or e >= input_base for e in digits):
        raise ValueError("all digits must satisfy 0 <= d < input base")

    if output_base < 2:
        raise ValueError("output base must be >= 2")

    digits = reversed(digits)

    number = 0

    for i, e in enumerate(digits):
        number += e * input_base**i

    output_digits = []

    while number / output_base != 0:
        output_digits.append(number % output_base)
        number //= output_base

    if len(output_digits) == 0:
        output_digits.append(0)

    return list(reversed(output_digits))
