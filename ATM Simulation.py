#ATM Simulation

has_card = True
pin = 123
correct_pin = 123
balance = 57000
withdraw_amount = 8000

if has_card:
  if pin == correct_pin:
    if withdraw_amount <= balance:
      print(f"balance = {balance}")
      balance -= withdraw_amount
      print(f"remaining amount : {balance}")
      else:
      print("insufficient amount")
  else:
    print("incorrect pin")
else:
  print("insert card")
