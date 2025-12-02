import matplotlib.pyplot as plt

cat = ["iphone", "samsung", "xiaomi", "oppo", "vivo"]
price = [999, 799, 499, 699, 599]

plt.bar(cat, price)
plt.xlabel("Type de smartphone")
plt.ylabel("Prix en euros")
plt.title("Prix des smartphones")
plt.show()
