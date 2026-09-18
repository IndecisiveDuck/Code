#A bank account is opened with $1000 dollars over the year the customer makes $300 in deposites
#and $200 in withdrawls. at the end of the year, the bank gives the  the customer 2.3 precent interest
#to thank the customer for their business/ What is the final balance of the account

account_balance = 1000
desposits = 300
withdrawls = 200
interest_rate_precent = 2.3

account_balance =+ desposits
account_balance =- withdrawls

account_balance = account_balance * (interest_rate_precent/100)