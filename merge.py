contact1={
    "anu":"9876543210",
    "tina":"8765432109"
}
contact2={
    "john":"7654321098",
    "priya":"6543210987"
}
print("contact1:",contact1)
print("contact2:",contact2)
merged_contact=contact1.copy()
merged_contact.update(contact2)
print("merged contacts",merged_contact)