import random, string
amount = int(input('Amount of nitro codes to generate: '))
value = 1
while value <= amount:
    code = "https://discord.com/billing/promotions/xbox-game-pass/redeem/" + ('').join(random.choices(string.ascii_letters + string.digits, k=24))
    f = open('Codes.txt', "a+")
    f.write(f'{code}\n')
    f.close()
    print(f'{code}')
    value += 1
