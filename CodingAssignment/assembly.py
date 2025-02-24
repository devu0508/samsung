def can_arrange_students(boys, girls):
    boys.sort()
    girls.sort()
    
    start_with_boy = True
    for i in range(len(boys)):
        if boys[i] > girls[i]:
            start_with_boy = False
            break
    if start_with_boy:
        return "YES"
    
    start_with_girl = True
    for i in range(len(boys)):
        if girls[i] > boys[i + 1]:
            start_with_girl = False
            break
    if start_with_girl:
        return "YES"
    
    return "NO"


def main():
    t = int(input("Enter number of test cases: "))
    results = []
    for _ in range(t):
        n = int(input("Enter number of boys and girls: "))
        boys = list(map(int, input("Enter boys' heights: ").split()))
        girls = list(map(int, input("Enter girls' heights: ").split()))
        result = can_arrange_students(boys, girls)
        results.append(result)
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()