def main():
    a = 0
    b = 0
    for i in range(0,1000,3):
        a+=i
    for i in range(0,1000,5):
        a+=i
    for i in range(0,1000,15):
        b+=2*i
    print(a-b)
if __name__ == "__main__":
    main()