"""Utility functions."""


def check_cpf(cpf):
    """
    Check whether or not a CPF number is valid.

    Args:
        cpf (str): Unmasked string representation of CPF to check validity for.

    Returns:
        bool: Whether or not the passed CPF number is valid.
    """
    # If a CPF is made out of a single repeating number, it isn't valid, even
    # though it would pass the following mathematical check.
    if len(set(cpf)) == 1:
        return False

    try:
        # The first verification digit is obtained by multiplying the first 9
        # digits of the CPF by the decreasing sequence of numbers from 10 to 2,
        # adding the results together, multiplying the obtained number by 10
        # and then obtaining the remainder when dividing it by 11. If the
        # resulting digit is either 10 or 11, then 0 is used instead. This
        # digit must match the 10th digit of the CPF.
        first_verification_digit = (
            (sum([int(cpf[i]) * (10-i) for i in range(9)]) * 10) % 11)
        if first_verification_digit in [10, 11]:
            first_verification_digit = 0
        assert first_verification_digit == int(cpf[9])

        # Obtaining the second verification digit works much like the first
        # one, except this time the first 10 digits of the CPF are used and the
        # sequence of numbers starts in 11. This digit must match the 11th
        # digit of the CPF.
        second_verification_digit = (
            (sum([int(cpf[i]) * (11-i) for i in range(10)]) * 10) % 11)
        if second_verification_digit in [10, 11]:
            second_verification_digit = 0
        assert second_verification_digit == int(cpf[10])

        return True
    except AssertionError:
        return False
