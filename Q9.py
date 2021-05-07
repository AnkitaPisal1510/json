import json
a={
    "shopping_list":
    {
        "chaco":"15",
        "biscuits":"50",
        "dairy_milk":"30",
        "ice_cream":"20"
    }
}
#ise json file
#create json file
#ask to user which item kharoidana u want agar user ne chaco dala to kitna chahiye4,54 fir remove that item from json file
# add karna hai to insert
with open("q9.json","w") as f:
    json.dump(a,f,indent=2)
    user=input("which item you want")
    q=int(input("kitne item chahiye?"))
    l=[]
    l.append(a)
    print(l                                                                  )
    for i in l:
        for j in i:
            if l[i][j] in l:
                l.pop(l[i][j])
                
    INSERT=input("you want to insert any item?")
    if INSERT=="yes":
        a.update(INSERT)
        
        
