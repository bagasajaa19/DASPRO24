#!/usr/bin/env python
# coding: utf-8

# In[4]:


name = "BAGAS"
age = 19
addreas,province = "Jl. Benteng","75645666"
scorePython = 80.5
isMarried = False

print("nama :",name)
print("umur:", age)
print("alamat:",addreas)
print("nilai pemrograman :",scorePython)
print("status menikah :", isMarried)


# In[5]:


print("Tipe data <name>",type(name))
print("Tipe data <age>",type(age))
print("Tipe data <addreas>",type(addreas))
print("Tipe data <province>",type(province))
print("Tipe data <scorePython>",type(scorePython))
print("Tipe data <isMarried>",type(isMarried))


# In[15]:


#Casting atau Konversi Tipe Data
#Konversi dari String ke (int,float,bool)
strToInt = int(province)
strToFloat = float(province)
strToBool = bool(province)
print(strToInt,strToFloat,strToBool, sep="-")
#Konversi dari int ke (str,float,bool)
intToStr = str(age)
intToFloat = float(age)
intToBool =  bool(age)
print(intToStr,intToFloat,intToBool, sep="-")
#Konversi dari float ke (str,int,bool)
floatToStr = float(scorePython)
floatToInt = float(scorePython)
floatToBool = float(scorePython)
print(floatToStr,floatToInt,floatToBool, sep="-")
#Konversi dari bool ke (int,float,str)
boolToInt = bool(isMarried)
boolToFloat = bool(isMarried)
boolToStr = bool(isMarried)
print(boolToInt,boolToFloat,boolToStr, sep="-")


# In[16]:


city = "Bandung"
lenCity = len(city) 
print(city[0])
print(city[lenCity-1])


# In[17]:


desimal = 200
hexa = 0xff
biner = 0b1010
octal = 0o377

print("Nilai Desimal:", desimal)
print("Nilai Desimal dari 0xff", hexa)
print("Nilai Desimal dari 0b1010", biner)
print("Nilai Desimal dari 0o377", octal)
print("================")
print("Nilai Biner dari :",desimal,bin(desimal))
print("Nilai Octal dari :",desimal,oct(desimal))
print("Nilai Hexa dari :",desimal,hex(desimal))


# In[40]:


#Tipe Data Collection

cities = ["Sukabumi", "Bandung", "Bogor", "Cianjur"]
print(cities)
print(cities[0])
print(cities[len(cities)-1])
cities[1] = "Semarang"
print(cities)
print(cities[len(cities)-1][0])

#Tuple
names =("Andi", "Budi" ,"Caca")
print(names)
#names[0] = "Rudi akan menyebabkan error, karena Tuple adalah Imutable"
ListStudent = {
    
}
studentData = {
    "name" : "Dedi",
    "addreass" : {
        "street" : "Cibatu",
        "number" : 21,
        "province" : "west java"
    },
    "hobbies" : ["basket","football"],
    "age" : 15,
    "isMarried" : False
}
studentData = {
    "name" : "Budi",
    "addreass" : {
        "street" : "Caringin",
        "number" : 25,
        "province" : "north java"
    },
    "hobbies" : ["basket","football"],
    "age" : 35,
    "isMarried" : True
}
print(studentData)
print(studentData["addreass"]["province"])


# In[48]:


#Casting Dictionary

list_tuple = [("name","dika"),("nilai","86")]
dictStudent = dict(list_tuple)
print(dictStudent)

list_list = [("buah","apel"),("harga","5500")]
dictBuah = dict(list_list)
print(dictBuah)

tuple_tuple = (("cindo","chatez"),("kulit","putih"))
dictCindo = dict(tuple_tuple)
print(dictCindo)

tuple_list = (["rokok","magnum filter"],["perbatang","2500"])
dictRokok = dict(tuple_list)
print(dictRokok)

keys = ("name","age","addreass")
values = ("bagas","23","Jepang")

dictData = dict(zip(keys,values))
print(dictData)

