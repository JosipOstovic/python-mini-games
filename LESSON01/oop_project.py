from bank_accounts import *

Josip = BankAccount(1000, "Josip")
Mislav = BankAccount(2500, "Mislav")
Patrik = BankAccount(3000, "Patrik")

Josip.getBalance()
Mislav.getBalance()
Patrik.getBalance()

Josip.deposit(450)
Mislav.withdraw(15000)
Mislav.withdraw(10)

Josip.transfer(500, Patrik)

Netko_Netkic = InterestRewardsAccount(1500, "Netko Netkic")
Netko_Netkic.getBalance()
Netko_Netkic.deposit(300)
Netko_Netkic.transfer(200, Mislav)

Miro = SavingsAccount(750, "Miro")
Miro.getBalance()
Miro.deposit(100)
Miro.transfer(10000, Mislav)
Miro.transfer(100, Mislav)