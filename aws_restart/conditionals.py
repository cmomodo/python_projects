def numberOf(limit):
    # Checking if the limit is greater than or equal to 5.
    if limit == 0:
        print("i have no bananas")
    elif limit <= 4:
        print('i have a small bunch of bananas')
    else:
        print("i have a bunch of bananas")
        
numberOf(1)

def Counter():
    counter = 0
    while(counter <= 5):
        counter += 1;
        print(counter)

Counter()