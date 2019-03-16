# read data in from json file; print list of locations to terminal

#import json python package
import json

# main executable/entry function
def main():
    print("do stuff")
    with open("./data/stuff.json") as filedata:
        print(filedata)
        objectdata=json.load(filedata)
        print(objectdata)
        print(type(objectdata))
        objectdata["jim"]="morton"
        print(objectdata)

if __name__=="__main__":
    main()