def remove_item(sett):

    print("\n",sett)
    print("Remove item from set:")
    sett.discard(5)
    print(sett)

set1 = {1,2,3,4,5}
remove_item(set1)