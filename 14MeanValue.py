# Estimates=[129,423,412,424,343,523,6432,237,3874,5234,5256,2325,6256]
# Estimates.sort()
# # print(Estimates)
# tv= int(0.1*len(Estimates))
# Estimates=Estimates[tv:]
# for i in range(len(Estimates)):
#     print(Estimates[i])


# Find the mean value:

from statistics import mean
Estimates=[129,423,412,424,343,523,6432,237,3874,5234,5256,2325,6256]
Estimates.sort()
tv= int(0.1*len(Estimates))
Estimates=Estimates[tv:]
Estimates=Estimates[:len(Estimates)-tv]
print(mean(Estimates))
