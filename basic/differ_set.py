s1={2,3,4,5,6}
s2={12,23,2,5,3,}
print(s1.difference(s2))
print(s1-s2)
print(s1)
print(s2)
s1.difference_update(s2)
print(s1)
print(s2)


#o/p:
#{4, 6}
#{2, 3, 4, 5, 6}
#{2, 3, 5, 23, 12}
#{4, 6}
#{2, 3, 5, 23, 12}
