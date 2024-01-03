secret_bid = {}
def auction(bidder_name, bid_amount):
    secret_bid[bidder_name] = bid_amount

end_auction = False
while end_auction == False:
    bidder_name = input("What's your name? ")
    bid_amount = int(input("What is your bid? $"))
    auction(bidder_name, bid_amount)
    new_bid = input("Are there any other bidders? Type 'yes' or 'no'. ")
    if new_bid == 'yes':
        end_auction = False
    else:
        end_auction = True
        
highest_bidder = ""
highest_bid = 0
for bid in secret_bid:
    if secret_bid[bid] > highest_bid:
        highest_bid = secret_bid[bid]
        highest_bidder = bid

print(f"The winner is {highest_bidder} with a final bid of {highest_bid}")