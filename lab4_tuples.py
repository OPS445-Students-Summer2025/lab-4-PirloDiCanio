# Original tuple and list
t1 = ('Prime', 'Ix', 'Secundus', 'Caladan')
t2 = (1, 2, 3, 4, 5, 6)
list2 = ['uli101', 'ops235', 'ops335', 'ops445', 'ops535', 'ops635']

print("\n--- Accessing Values ---")
print("t1[0]:", t1[0])               # Output: Prime
print("t2[2:4]:", t2[2:4])           # Output: (3, 4)

print("\n--- Checking if Value Exists ---")
print("'Ix' in t1:", 'Ix' in t1)             # True
print("'Geidi' in t1:", 'Geidi' in t1)       # False

print("\n--- List is Mutable ---")
list2[0] = 'ica100'
print("Changed list2[0]:", list2[0])         # ica100
print("Updated list2:", list2)              # Full updated list

print("\n--- Tuple is Immutable ---")
try:
    t2[1] = 10           # This will throw an error
except TypeError as e:
    print("Error:", e)   # Show the error

print("\n--- Creating New Tuple from Slice ---")
t3 = t2[2:3]
print("New t3 (slice of t2):", t3)           # (3,)

print("\n--- Loop Through Tuple ---")
for item in t1:
    print("item:", item)

