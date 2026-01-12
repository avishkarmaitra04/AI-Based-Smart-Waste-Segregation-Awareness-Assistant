def waste_segregation(item):
    wet_waste = [
        "food", "leftover", "vegetable", "fruit", "peel", "tea", "coffee",
        "eggshell", "bread", "rice", "banana"
    ]

    dry_waste = [
        "plastic", "paper", "newspaper", "cardboard", "glass", "metal",
        "tin", "aluminum", "wrapper", "packet", "bottle"
    ]

    e_waste = [
        "battery", "mobile", "phone", "charger", "laptop", "earphone",
        "headphone", "keyboard", "mouse", "remote", "power bank",
        "circuit"
    ]

    item = item.lower()

    wet_score = sum(word in item for word in wet_waste)
    dry_score = sum(word in item for word in dry_waste)
    e_score = sum(word in item for word in e_waste)

    if wet_score > dry_score and wet_score > e_score:
        category = "Wet Waste"
        reason = "Organic and biodegradable waste."
        tip = "Compost or dispose in wet waste bins."
        confidence = wet_score / len(wet_waste) * 100

    elif dry_score > wet_score and dry_score > e_score:
        category = "Dry Waste"
        reason = "Recyclable non-biodegradable material."
        tip = "Dispose in dry waste or recycling bins."
        confidence = dry_score / len(dry_waste) * 100

    elif e_score > wet_score and e_score > dry_score:
        category = "E-Waste"
        reason = "Contains electronic components and harmful chemicals."
        tip = "Dispose at authorized e-waste collection centers."
        confidence = e_score / len(e_waste) * 100

    else:
        category = "Unknown"
        reason = "Insufficient information to classify."
        tip = "Check local waste management guidelines."
        confidence = 0

    return category, reason, tip, round(confidence, 2)


# Main Program Loop
print("AI-Based Smart Waste Segregation Assistant")
print("----------------------------------------")

while True:
    user_item = input("\nEnter waste item (or type 'exit' to quit): ")

    if user_item.lower() == "exit":
        print("Thank you for using the Waste Segregation Assistant!")
        break

    category, reason, tip, confidence = waste_segregation(user_item)

    print("\nResult:")
    print(f"Category      : {category}")
    print(f"Reason        : {reason}")
    print(f"Disposal Tip  : {tip}")
    print(f"Confidence    : {confidence}%")
