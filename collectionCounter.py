from collections import Counter

my_str = 'dfdefdgf'
my_str = sorted(my_str)
cnt = Counter(my_str)
cnt = cnt.most_common()
collect = []
for i in range(0, len(cnt)):
    if cnt[i][1] is cnt[0][1]:
        collect.append(cnt[i][0])
print(''.join(collect))
