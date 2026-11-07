import os

to_remove = [
    r'D:\Neuromates(website)\insights\articles.html',
    r'D:\Neuromates(website)\insights\case-studies.html'
]

for p in to_remove:
    if os.path.exists(p):
        os.remove(p)
        print("Removed:", p)

