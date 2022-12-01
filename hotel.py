print("SURESH STALL")
menu=["idly","dosa","aapam","pongal"]
print("idly : 5 rs\ndosa : 10 rs\naapam : 10 rs\npongal : 30 rs")
customer_order=input("Entr order:").lower()
idly_amnt=0
dosa_amnt=0
aapam_amnt=0
pongal_amnt=0
if customer_order in menu:
    print(f"{customer_order} is available")
    if customer_order=="idly":
        idly_count=int(input("Enter idly quantity:"))
        idly_amnt=5*(idly_count)
        # print(f"Your bill amount is {idly_amnt}")
    elif customer_order=="dosa":
        dosa_count=int(input("Enter dosa quantity:"))
        dosa_amnt=10*(dosa_count)
       # print(f"Your bill amount is {dosa_amnt}")
    elif customer_order=="aapam":
        aapam_count=int(input("Enter aapam quantity:"))
        aapam_amnt=10*(aapam_count)
       # print(f"Your bill amount is {aapam_amnt}")
    elif customer_order=="pongal":
        pongal_count=int(input("Enter pongal quantity:"))
        pongal_amnt=30*(pongal_count)
       # print(f"Your bill amount is {pongal_amnt}")
    total=(idly_amnt)+(dosa_amnt)+(aapam_amnt)+(pongal_amnt)
    print(f"Your bill amount is {total}")
    if 100<=total<500:
        discount=(20/100)*total
        discount_amnt=total-discount
        print(f"Thanks for buying more than 100rs\nYour bill is {total}\nAfter discount your bill is {discount_amnt}")
    if total>=500:
        discount=(50/100)*total
        discount_amnt=total-discount
        # print("You are eligible for our discount")
        print(f"Thanks for buying more than 500rs\nYou are eligible for our discount\nYour bill is {total}\nAfter discount your bill is {discount_amnt}")   
else:
    print(f"{customer_order} is not available")
    
    