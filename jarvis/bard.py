from bardapi import BardCookies

import datetime

cookie_dict ={
    "__Secure-1PSID":"aAgZ0ATndZeWnl62BPFOwTBfG45QXPjduKfVxSWzLT8L-5j6kWLHO7zTBEmEHTHNivy6wA.",
    "__Secure-1PSIDTS":"sidts-CjIBSAxbGV6QM4a2TNsNZ5ulopYcu-H4AzC-akHXX5I55gPBp5IAwDfz7JbUuAr-LgZvUBAA",
    "__Secure-1PSIDCC":"APoG2W_4yNC_7evxcoqyRQZ2m-dvM2DPE7a4nITT8WbVWM1VK9vceEozg69YLM60Jd1mf1QKdQ",
}

bard = BardCookies(cookie_dict=cookie_dict)

while True:
    Query = input("Enter Your Query :")
    Reply = bard.get_answer(Query)['content']
    print(Reply)


