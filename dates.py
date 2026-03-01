from datetime import datetime, timedelta
import random

def generate_random_date_in_range(start_year: int, end_year: int) -> str:
    """
    Generate a random date within a specified year range.
    
    Args:
        start_year: The start year (inclusive) for the date range.
        end_year: The end year (inclusive) for the date range.
        
    Returns:
        A date string in ISO format (YYYY-MM-DD).
    """
    start_date = datetime(start_year, 1, 1)
    end_date = datetime(end_year, 12, 31)
    
    total_days_between = (end_date - start_date).days
    random_days_offset = random.randint(0, total_days_between)
    random_date = start_date + timedelta(days=random_days_offset)
    
    return random_date.strftime("%Y-%m-%d")


# Usage example
random_date = generate_random_date_in_range(2025, 2025)
print(f"Generated date: {random_date}")