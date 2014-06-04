# Tom Hogans, Big Data CS491
# Problem Set #2, Question 1

import matplotlib.pyplot as plt

family = (0.2, 0.5, 0.6, 0.25)
n = 80
possibilities = []
for i in range(1, n + 1):
    x = n // i
    if n % i == 0:
        possibilities.append((x, i))
print("%d possible combinations of rows and bands" % len(possibilities))

# Construct F' using the AND-construction on F
# Then F'' using the OR-construction on F'
# for each possible configuration of bands and rows
results = []
for r, b in possibilities:
    f_p = (family[0], family[1], family[2] ** r, family[3] ** r)
    f_pp = (f_p[0], f_p[1], 1 - ((1 - f_p[2]) ** b), 1 - ((1 - f_p[3]) ** b))
    results.append({
        'r': r,
        'b': b,
        'd1': f_pp[0],
        'd2': f_pp[1],
        'p1': f_pp[2],
        'p2': f_pp[3]})
    print("For r=%d, b=%d: F = %s, F' = %s, F'' = %s" % (r, b, family, f_p, f_pp))

b_values = [i['b'] for i in results]
p1_values = [i['p1'] for i in results]
p2_values = [i['p2'] for i in results]
plt.plot(p1_values, b_values, 'r', label='p1')
plt.plot(p2_values, b_values, 'b', label='p2')
plt.ylabel('# of bands')
plt.xlabel('probabilities')
plt.show()
# We see r=4, b=20 maximizes the difference between p1 and p2
