word = "Muvaffakiyetsizleştiricileştiriveremeyebileceklerimizdenmişsinizcesine"

vowels = "aeıioöuü"
vowels_count= 0 


for i in word:
    if i in vowels:
        vowels_count+=1
        
print(vowels_count)
