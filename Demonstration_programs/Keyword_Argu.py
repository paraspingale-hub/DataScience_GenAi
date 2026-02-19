def Empl(Name ,Age ,Salary ,city):
    print("name:" , Name)
    print("Age:",Age)
    print("Salary:",Salary)
    print("City:",city)
    print("-" * 29)

def main():
    #Posiitonal call 
    Empl("Rahul" , 22 , 2600.467 , "Pune") # correct call
    Empl(22 , "Rahul" , "pune" , 2000.5)   # Wrong call 

    #Keyword call
    Empl(Name= "Rahul", Age=45, Salary=3434.44, city= "Pune" )

if __name__ == "__main__":
    main()

