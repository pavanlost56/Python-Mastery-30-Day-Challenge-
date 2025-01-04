from datetime import datetime, timedelta

# Assume calculate_age function is already defined
def calculate_age(dob_str):
    dob = datetime.strptime(dob_str, "%d-%m-%Y")
    today = datetime.today()
    years = today.year - dob.year
    months = today.month - dob.month
    days = today.day - dob.day

    if days < 0:
        months -= 1
        prev_month = dob.replace(year=today.year, month=today.month - 1 if today.month > 1 else 12)
        days += (today - prev_month).days

    if months < 0:
        years -= 1
        months += 12

    return {"years": years, "months": months, "days": days}

# Test cases
def run_tests():
    # Test case 1: Less than one year old
    dob_less_than_year = (datetime.today() - timedelta(days=200)).strftime("%d-%m-%Y")
    result_less_than_year = calculate_age(dob_less_than_year)
    print(f"Test 1 - DOB: {dob_less_than_year}")
    print(f"Expected: {{'years': 0, 'months': ~6, 'days': ~20}} (or similar, depending on exact date)")
    print(f"Actual: {result_less_than_year}\n")
    
    # Test case 2: DOB is today's date
    dob_today = datetime.today().strftime("%d-%m-%Y")
    result_today = calculate_age(dob_today)
    print(f"Test 2 - DOB: {dob_today}")
    print(f"Expected: {{'years': 0, 'months': 0, 'days': 0}}")
    print(f"Actual: {result_today}\n")
    
    # Test case 3: Past date not within current year
    dob_past = "01-01-2010"
    result_past = calculate_age(dob_past)
    today = datetime.today()
    expected_years = today.year - 2010 - (1 if (today.month, today.day) < (1, 1) else 0)
    if today.month == 1 and today.day < 1:
        expected_months = 0
        expected_days = today.day
    else:
        if today.month == 1:
            expected_months = 12 - 1
        else:
            expected_months = today.month - 1
        expected_days = today.day
    print(f"Test 3 - DOB: {dob_past}")
    print(f"Expected: {{'years': {expected_years}, 'months': {expected_months}, 'days': {expected_days}}}")
    print(f"Actual: {result_past}\n")

# Run the tests
run_tests()
