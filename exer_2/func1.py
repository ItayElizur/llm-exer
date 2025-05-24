def calculate_compound_interest(principal: float, rate: float, time: int,
                                compounds_per_year: int = 1) -> float:
    """
    Calculate compound interest using the standard formula.

    Args:
        principal: Initial amount of money
        rate: Annual interest rate (as decimal, e.g., 0.05 for 5%)
        time: Number of years
        compounds_per_year: How many times interest compounds per year

    Returns:
        Final amount after compound interest

    Raises:
        ValueError: If any parameter is negative
    """
    if principal < 0 or rate < 0 or time < 0 or compounds_per_year <= 0:
        raise ValueError("Invalid input parameters")

    return principal * (1 + rate / compounds_per_year) ** (compounds_per_year * time)
