
def insertion_sort(lst):
	for i in range(1, len(lst)):
		n = lst[i]
		j = i - 1
		while j >= 0 and n < lst[j]:
			lst[j+1] = lst[j]
			j -= 1
			lst[j+1] = n
	return lst

lst = [16, 3, 5, 25, 43, 18]

print('Unsorted: ', lst)
print('Sorted: ', insertion_sort(lst))

