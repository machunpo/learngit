# 生成10000以内素数表(eratosthenes算法）
def primeFilter(n):
    return lambda x: x % n > 0


def createSmallPrimeNum():
    num = iter(range(3, 10000, 2))
    prime = [2]
    while True:
        try:
            n = next(num)
            prime.append(n)
            num = filter(primeFilter(n), num)
        except StopIteration:
            return prime


def createLargePrimeNum(x):
    flag = False
    smallPrimeNum = createSmallPrimeNum()

    while (not flag):
        flag = True
        n = createRandomNum(x)
        if not n % 2:
            n += 1

        # 10000内素数检验
        for i in smallPrimeNum:
            if n % i == 0:
                flag = False
                break
        if not flag:
            continue

        # 10次Miller-Rabin素性检测
        for i in range(0, 20):
            if not Miller_Rabin(n):
                flag = False
                break
    return n


m = createLargePrimeNum(10)

print(m)
