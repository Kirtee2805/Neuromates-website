import os

home_orig = r'D:\Neuromates(website)\Neuro Mates _ Connected neurological care.html'
prod_orig = r'D:\Neuromates(website)\Products _ Neuro Mates.html'

print("Home original exists:", os.path.exists(home_orig), "size:", os.path.getsize(home_orig))
print("Products original exists:", os.path.exists(prod_orig), "size:", os.path.getsize(prod_orig))

