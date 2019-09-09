import os


dan_qian_mu_lu=os.getcwd()
print(dan_qian_mu_lu)
for i in os.walk(dan_qian_mu_lu):
    print(i)