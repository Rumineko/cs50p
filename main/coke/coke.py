# We set owed amount here
amnt = 50

# Make a while loop for as long as amnt is more than 0
while amnt > 0:
    # We print the amount due with said amount
    print("Amount Due: " + str(amnt))
    # Ask user to insert coin
    coin = int(input("Insert Coin: ").strip())
    if coin == 50 or coin == 25 or coin == 10 or coin == 5:
        amnt = amnt - coin

# Then once the loop above breaks, we print out the Change
if amnt <= 0:
    print("Change Owed: " + str(-amnt))