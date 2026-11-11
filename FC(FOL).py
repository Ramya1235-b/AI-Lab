
# Forward Chaining in First Order Logic (FOL)

# Step 1: Initialize Knowledge Base (KB)
facts = {
    ("American", "Robert"),
    ("Enemy", "A", "America"),
    ("Owns", "A", "T1"),
    ("Missile", "T1")
}

# Step 2: Apply Forward Chaining
new_facts = True

while new_facts:
    new_facts = False

    # Rule 1: Missiles are weapons
    for fact in list(facts):
        if fact[0] == "Missile":
            new_fact = ("Weapon", fact[1])
            if new_fact not in facts:
                facts.add(new_fact)
                new_facts = True

    # Rule 2: Enemy of America is Hostile
    for fact in list(facts):
        if fact[0] == "Enemy" and fact[2] == "America":
            new_fact = ("Hostile", fact[1])
            if new_fact not in facts:
                facts.add(new_fact)
                new_facts = True

    # Rule 3: Robert sells missiles owned by Country A to Country A
    for fact in list(facts):
        if fact[0] == "Owns":
            country, missile = fact[1], fact[2]

            if ("Missile", missile) in facts:
                new_fact = ("Sells", "Robert", missile, country)

                if new_fact not in facts:
                    facts.add(new_fact)
                    new_facts = True

    # Rule 4: An American selling weapons to a hostile country is criminal
    for fact in list(facts):
        if fact[0] == "American":
            person = fact[1]

            for weapon in list(facts):
                if weapon[0] == "Weapon":
                    item = weapon[1]

                    for sale in list(facts):
                        if sale == ("Sells", person, item, "A"):
                            if ("Hostile", "A") in facts:
                                new_fact = ("Criminal", person)

                                if new_fact not in facts:
                                    facts.add(new_fact)
                                    new_facts = True

# Step 3: Display Result
print("Knowledge Base:")
for fact in sorted(facts):
    print(fact)

# Step 4: Check the Query
if ("Criminal", "Robert") in facts:
    print("\nGoal Proved: Robert is a Criminal")
else:
    print("\nGoal Not Proved")
