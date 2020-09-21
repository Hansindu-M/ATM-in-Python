while True:

    balance=10000

    print("    ATM    ")
    print("""
    1)    Balance
    2)    Withdraw
    3)    Deposit
    4)    Quit
    """)

    try:
        Option=int(input("Enter Option: "))

    except Exception as e:

        print("Error: ", e)
        print("Enter 1, 2, 3 or 4 only")

        continue

    if Option==1:

        print("Balance Rs ", balance)
        
    if Option==2:

        print("Balance Rs ", balance)

        Withdraw=float(input("Enter Withdraw amount Rs "))

    if Withdraw>0:

        forwardbalance=(balance-Withdraw)

        print("forward balance Rs " ,forwardbalance)

    elif Withdraw>balance:
        print("No funds in the account")

    else:
        print("No withdraws made")


    if Option==3:

        print("Balance Rs ", balance)

        Deposit=float(input("Enter depost amount Rs  "))

        if Deposit>0:
            forwardbalance=(balance+Deposit)

            print("Forward Balance Rs ", forwardbalance)

        else:
            print("No deposits made")

    if Option==4:
        exit()
        

    
