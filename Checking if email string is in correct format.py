# Import the regular expression module
import re


def is_valid_email(emails):
    """Create a function to search for a regular expression to determine if it is an email or not"""
    pattern = re.compile(
        r'^[\w!#$%&\'*+/=?^_`{|}~-]+(?:\.[\w!#$%&\'*+/=?^_`{|}~-]+)*@(?:[\w-]+\.)+\w+(?:\.[a-zA-Z]{2,})?$')
    # Checking to see if there is any matches in the pattern
    if re.match(pattern, emails):
        # Output true if there is a pattern
        return True
    else:
        # Return false if no patter in found
        return False


# Testing data that contains email addresses to be tested
test_data = [
    "Test.user@example.com",
    "claireclarke@belfastmet.ac.uk",
    "Barbie@Ken@gmail.com"
]

# Creates a loop through all emails in the test data
for email in test_data:
    # Call the function to check each email and store the result
    result = is_valid_email(email)
    # Print the output if it is a valid email or not
    print(f"Email: {email} - Valid: {result}")
