import re

def read_input(filename):
    input = open(filename, 'r')
    return input

def split_input(inputfile):
    
    id_doc_list = inputfile.split('\n\n')
    
    return id_doc_list

def part1(id_doc_list):
    number_of_valid_ids = 0
    for i in id_doc_list:
        #print(i)
        r = re.findall('(byr|iyr|eyr|hgt|hcl|ecl|pid):', i)
        length = len(r)
        if length == 7:
            number_of_valid_ids += 1
    return number_of_valid_ids

def part2(id_doc_list):
    
    
    
    
    
    
    return 0

if __name__ == "__main__":
    batchfile = read_input("input.txt")
    #batchfile = read_input("input.txt")
    inputfile = batchfile.read()
    id_doc_list = split_input(inputfile)
    part1_number_of_valid_ids = part1(id_doc_list)
    print("part 1:", part1_number_of_valid_ids)
    part2_number_of_valid_ids = part2(id_doc_list)
    print("part 2:", part2_number_of_valid_ids)
