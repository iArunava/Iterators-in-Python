def mimic_for_in(iterable):
    iterobj = iter(iterable)

    while 1:
        try:
            # Start Body of the loop
            print (next(iterobj))
            # End body of the loop

        # When the iterator raises StopIteration
        # to indicate the end of iteration
        except StopIteration:
            break

l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
mimic_for_in(l1)
