from functools import reduce
import concurrent.futures as future
import numpy as np

def A5(zip_exam): ##Exercise A5
    def femma(obj):
        if obj[1] == 5:
            return True
        return False
    res = filter(femma,zip_exam)
    return list(res)
    pass
def generate_list(n):
    a = np.random.randint(0,9)
    b = np.random.randint(10, 19)
    return np.random.uniform(a,b,n)
def Estimation(lst): ##Exercise A6
    n = len(lst)
    n_p = 10
    reshaped = lst.reshape(n_p, -1)
    with future.ProcessPoolExecutor() as ex:
        mini = ex.map(min, reshaped)
        maxi = ex.map(max, reshaped)
        mini = list(mini)
        maxi = list(maxi)
    total_min = min(mini)
    total_max = max(maxi)

    return n/(n-1)*total_min - 1/(n-1)*(total_max), n/(n-1)*total_max - 1/(n-1)*(total_min)
    pass
def main():

    print("Test A5:")
    names = ["Anna", "Anton", "Jakob",
    "Ludwig", "Nils", "Oliver",
    "Rafael", "Tim"]
    grades = [3,4,5,5,4,3,5,5]
    #for l, f in zip(names, grades):
       # print(f'{l} receives {f}')
    print(A5(zip(names, grades)))
    print("Test A6:")
    n = 10**6
    lst = generate_list(n)
    print(Estimation(lst))
if __name__ == '__main__':
    main()