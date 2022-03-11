main()
{
    int sum = 0;
    char vowels[] = {'a','e','ı','i','o','ö','u','ü'};
    char word[100] = "Muvaffakiyetsizleştiricileştiriveremeyebileceklerimizdenmişsinizcesine"; 
    
    
    
        for (int i = 0; i < strlen(word); i++)
        {
            for(int j = 0; j < 5; j++)
            {
                if(word[i] == vowels[j]){
                    sum++;
                }
            }
        }
    printf("\n %d ", sum);
