set1= {8, 16, 24, 32, 44}
set2= {7, 14, 8, 32, 21}

#set difference
diff_set = set1 - set2
print(f"Set Difference : ", diff_set)

#set union
union_set = set1 | set2
print(f"Union of Sets: ", union_set)

#set symmetric
symdiff_set = set1 ^ set2
print(f"Symmetric Difference of Sets: ", symdiff_set)

#set intersection
intersec_set = set1 & set2
print(f"Intersection of Sets: ", intersec_set)