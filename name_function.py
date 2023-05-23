def get_formatted_name(first,  last, middle="", ):
    """Gets a username and formats it"""
    if middle:
        fullname = f"{first} {middle} {last}"
    else:
        fullname = f"{first} {last}"

    return fullname.title()