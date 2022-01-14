import matplotlib.pyplot as plt
subject=["tamil","English","Computer","Maths","chemistry"]
mark=[85,80,86,90,86]
plt.bar(subject,mark)
plt.title("Subject & its mark")
plt.xlabel("subject name")
plt.ylabel("Marks")
#plt.xticks(subject,subject)
plt.show()
      
