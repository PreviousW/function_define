def functional_formula(x):
    y = 2*x + 10 
    return y
    
def function(domain):
    _range = []
    for i in domain:
        _range.append(functional_formula(i))
    return sorted(_range)
 

i = list(map(int, input("정의역을 입력하세요: ").split()))       
print("치역: ", function(i))
