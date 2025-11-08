def check_phone_number(number):
    area_codes = {
        # Landlines
        "01": ("Zagreb area", "landline", None),
        "020": ("Dubrovnik area", "landline", None),
        "021": ("Split area", "landline", None),
        "022": ("Šibenik area", "landline", None),
        "023": ("Zadar area", "landline", None),
        "031": ("Osijek area", "landline", None),
        "032": ("Vukovar area", "landline", None),
        "035": ("Slavonski Brod area", "landline", None),
        "052": ("Istria area", "landline", None),
        "051": ("Rijeka area", "landline", None),
        "053": ("Lika area", "landline", None),

        # Mobile
        "091": (None, "mobile", "A1"),
        "092": (None, "mobile", "Tomato"),
        "095": (None, "mobile", "Telemach"),
        "097": (None, "mobile", "bonbon"),
        "098": (None, "mobile", "HT"),
        "099": (None, "mobile", "HT"),

        # Special services
        "0800": (None, "special", None),
        "060": (None, "special", None),
        "061": (None, "special", None),
        "064": (None, "special", None),
        "065": (None, "special", None),
        "069": (None, "special", None),
        "072": (None, "special", None),
    }

    # Clean input
    number = number.replace(" ", "").replace("-", "").replace("(", "").replace(")", "").replace("/", "").strip()

    # Normalize prefix (handle +385, 00385, 385, (385))
    if number.startswith("+385"):
        number = number[4:]
        if not number.startswith("0"):
            number = "0" + number
    elif number.startswith("00385"):
        number = number[5:]
        if not number.startswith("0"):
            number = "0" + number
    elif number.startswith("385"):
        number = number[3:]
        if not number.startswith("0"):
            number = "0" + number
    elif number.startswith("0"):
        pass
    else:
        # In case number starts with something else
        print("\nInvalid number format.\n")
        return

    code = None
    for c in sorted(area_codes.keys(), key=lambda x: -len(x)):
        if number.startswith(c):
            code = c
            break

    if not code:
        print("\nInvalid number. Area code not recognized.\n")
        return {
            "area_code": None,
            "subscriber_number": number,
            "type": None,
            "region": None,
            "operator": None,
            "valid": False
        }

    region, number_type, operator = area_codes[code]
    rest = number[len(code):]
    length = len(rest)
    valid = False

    if number_type == "landline" and length in (6, 7):
        valid = True
    elif number_type == "mobile" and length in (6, 7):
        valid = True
    elif number_type == "special" and length == 6:
        valid = True

    result = {
        "area_code": code,
        "subscriber_number": rest,
        "type": number_type,
        "region": region,
        "operator": operator,
        "valid": valid
    }

    print("\nResult:")
    for key, value in result.items():
        print(f"{key}: {value}")
    print()

    return result


while True:
    user_input = input("Enter a phone number (or 'exit' to quit): ").strip()
    if user_input.lower() == "exit":
        print("Program ended.")
        break
    check_phone_number(user_input)
