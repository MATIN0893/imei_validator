def validate_imei(imei: str) -> bool:
    """Validate a 15‑digit IMEI number.

    The IMEI must be a string consisting of exactly 15 numeric characters.
    Validation is performed using the Luhn algorithm (also known as the
    Mod‑10 checksum). The function returns ``True`` if the IMEI is valid,
    otherwise ``False``.

    Args:
        imei: The IMEI number as a string.

    Returns:
        bool: ``True`` if the IMEI is valid, ``False`` otherwise.
    """
    # Ensure the IMEI is a 15‑digit numeric string
    if not isinstance(imei, str) or len(imei) != 15 or not imei.isdigit():
        return False

    # Luhn algorithm implementation
    total = 0
    # Process digits from right to left, enumerating starting at 0
    for i, digit_char in enumerate(reversed(imei)):
        digit = int(digit_char)
        # Double every second digit (i.e., those in odd positions when counting from 0)
        if i % 2 == 1:
            digit *= 2
            # If the result is two digits, subtract 9 (equivalent to summing the digits)
            if digit > 9:
                digit -= 9
        total += digit

    # IMEI is valid if total modulo 10 equals 0
    return total % 10 == 0


if __name__ == "__main__":
    # Simple manual tests
    test_imeis = [
        "490154203237518",  # valid example
        "490154203237517",  # invalid (last digit altered)
        "123456789012345",  # invalid checksum
        "49015420323751",   # too short
        "4901542032375189", # too long
        "49015420323A518",  # non‑numeric
    ]
    for imei in test_imeis:
        print(f"{imei}: {validate_imei(imei)}")
