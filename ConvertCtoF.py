def CtoFConverter():
    while True:
        cTerm=input("Please enter C term:")
        if cTerm:
            cTerm=float(cTerm)
            fterm=round(cTerm*9/5+32,1)
            print(f"{cTerm}C had been converted to {fterm}F")
            break
        else:
            print("cTerm input is empty!!!")
            continue

def main():
    CtoFConverter()
if __name__=="__main__":
    main()