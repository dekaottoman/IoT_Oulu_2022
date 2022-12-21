import os
import pathlib
import hashlib
import datetime

def read_folder(folder_path:str):
    folder = []
    
    for  root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".txt"):
                #file_path = folder_path + "/" + file_name
                folder.append(file)
    return folder

def read_file(file_path:str):
    f = open(file_path,mode="r",encoding="utf-8")
    file = f.read()
    f.close()
    return file

def write_file(file:str,file_path:str):
    f = open(file_path, "w")
    f.write(file)
    f.close()

def create_node(data,folder_len:int,folder_path:str):
    if folder_len > 0:
        previous = read_file( folder_path + "/" + ("node_" + str(folder_len - 2) + ".txt")) #NEEDS UPDATE
        prev_hash = hashlib.sha256(previous.encode("utf-8")).hexdigest()
    else:
        prev_hash = "NULL"
    #data = input("Enter node data >>")
    time_stamp = str(datetime.datetime.now())
    full_node  = prev_hash + "<S>" + data + "<S>" + time_stamp

    return full_node

def display_node(node:str):
    node = node.split("<S>")
    print("Node data\t>> ",node[1])
    print("Timestamp\t>> ",node[2])
    print("Previous Hash\t>> ",node[0])

def add_node(data,folder_path:str):
    folder = read_folder(folder_path)
    
    node = create_node(data,len(folder),folder_path)

    stop, i = False, 0
    while not stop:
        check_path = "node_"+ str(i) +".txt"
        check = pathlib.Path( folder_path + "/" + check_path)
        if not check.exists():
            write_file(node, folder_path + "/" + check_path)
            stop = True
        i += 1

    folder = read_folder(folder_path)
    full_chain = ""
    for f in folder:
        if f != "chain_hash.txt":
            f_path =  folder_path + "/" + f
            current = read_file(f_path)
            full_chain += current
    
    chain_hash = hashlib.sha256(full_chain.encode("utf-8")).hexdigest()
    write_file(chain_hash, folder_path + "/" + "chain_hash.txt")

if __name__ == "__main__":
    folder_path = input("Enter the path to the folder containing the blockchain\t>>")
    folder = read_folder(folder_path)
    print(folder)
    
    data = input("Enter node data >>")
    """node = create_node(data,len(folder), folder_path)
    stop, i = False, 0
    while not stop:
        check_path = "node_"+ str(i) +".txt"
        check = pathlib.Path( folder_path + "\\" + check_path)
        if not check.exists():
            write_file(node, folder_path + "\\" + check_path)
            stop = True
        i += 1
    folder = read_folder(folder_path)
    display_node(node)
    
    full_chain = ""
    for f in folder:
        f_path =  folder_path + "\\" + f
        current = read_file(f_path)
        full_chain += current
    
    chain_hash = hashlib.sha256(full_chain.encode("utf-8")).hexdigest()
    print("Chain Hash\t>> ", chain_hash)
    write_file(chain_hash, folder_path + "\\" + "chain_hash.txt")"""

    add_node(data,folder_path)
