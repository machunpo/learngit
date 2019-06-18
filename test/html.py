def quchu_heml(text_all):
        m=0
        n=0

        while 1 :

                m=text_all.find('<',n)
                n=text_all.find('>',m)
                
                if m==-1:
                        break
                try:
                        text_all=text_all[:m]+text_all[(n+1):]
                except:
                        pass
    
        return text_all

if __name__ == '__main__':
    print(quchu_heml('this is < a > test!<A>'))




