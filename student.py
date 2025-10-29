student={
    "anu":340,
    "tine":485,
    "john":300
}
asc_by_name=dict(sorted(student.items()))
print("sorted by name(Ascending):")
print(asc_by_name)

desc_by_name=dict(sorted(student.items(), reverse=True))
print("\n sorted buy name(descending):")
print(desc_by_name)