import matplotlib.pyplot as plt
batsmen = ["Dhoni","fafduplessi","Samcurran","Jadeja","watson","Rayudu"]
scores = [200,449,186,232,299,359]

plt.bar(batsmen,scores)
#plt.xticks(batsmen,batsmen)
plt.xlabel("CSK Players' name")
plt.ylabel("scores in IPL2020")
plt.title("CSK Batsmen scores in IPL2020")
plt.show()

