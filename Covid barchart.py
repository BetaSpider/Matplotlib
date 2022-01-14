import matplotlib.pyplot as plt
district=["Madurai","chennai","thrichy","Dindigul"]
cases=[250,300,200,178]
plt.bar(district,cases)
plt.title("Corona cases in districts")

plt.xlabel("Name of the district")
plt.ylabel("CoVID Cases")

plt.show()

        
