vowello = ["a", "e", "i", "o", "u", 'y', "w"]
vowelup = ["A", "E", "I", "O", "U", 'Y', "W"]

def main():
    vowel_count = 0
    inp = input("enter ")
    inp_List = list(inp)
    for i in range(0, len(inp_List)):
        for j in range(0, len(vowello)):
            if inp_List[i] == vowello[j]:
                vowel_count += 1
    for a in range(0, len(inp_List)):
        for b in range(0, len(vowelup)):
            if inp_List[a] == vowelup[b]:
                vowel_count += 1
    return vowel_count

if __name__ == "__main__":
    print(main())