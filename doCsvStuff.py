# read data in from json file; print list of locations to terminal

#import json python package
import json

# main executable/entry function
def main():
    print("do stuff")
    
    with open("./data/stuff.json","r+") as filedata:
        print(filedata) #practicing print from CLI
        objectdata=json.load(filedata)
        print(objectdata)
        print(type(objectdata))
        objectdata["jim"]="morton"
        objectdata["john"]="eliot"
        print(objectdata)
    
    with open("./data/stuff.json","w") as filedata:
        json.dump(objectdata,filedata)         

if __name__=="__main__":
    main()