def can_arrange_students(boys, girls):
    boys.sort()
    girls.sort()
    
    combined1 = [None] * (len(boys) + len(girls))
    combined2 = [None] * (len(boys) + len(girls))
    
    for i in range(len(boys)):
        combined1[2 * i] = boys[i]
        combined1[2 * i + 1] = girls[i]
        
        combined2[2 * i] = girls[i]
        combined2[2 * i + 1] = boys[i]
        
    if (all(combined1[i] <= combined1[i + 1] for i in range(len(combined1) - 1)) or 
        all(combined2[i] <= combined2[i + 1] for i in range(len(combined2) - 1))):
        return "YES"
    
    return "NO"

def main():
    t = int(input("Enter the number of test cases: "))
    results = []
    
    for _ in range(t):
        n = int(input("Enter the number of boys and girls: "))
        boys = list(map(int, input("Enter the heights of the boys: ").split()))
        girls = list(map(int, input("Enter the heights of the girls: ").split()))
        
        result = can_arrange_students(boys, girls)
        results.append(result)
        
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
