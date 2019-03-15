class CocaCola:
    formula = ['caffeine','sugar','water','soda']
    def drink(self):
        print('formula')

CocaCola().drink()
print(CocaCola().formula[2])
coke = CocaCola()
coke.drink()
print(coke.formula[0])#直接引用 和 实例化引用
#测试获得成功