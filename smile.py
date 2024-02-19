def count_smileys(arr):
    licznik = []
    for i in range(len(arr)):
        if ((":") in arr[i]):
            
            if (")") in arr[i]:
                licznik.append(arr[i])
                print(arr[i])
            elif ('D') in arr[i]:
                licznik.append(arr[i])
                print(arr[i])
        elif (";") in arr[i]:
            if (")") in arr[i]:
                licznik.append(arr[i])
                print(arr[i])
            elif ('D') in arr[i]:
                licznik.append(arr[i])
                print(arr[i])
                
    return len(licznik)







print(count_smileys([':)',':(',':D',':O',':;']))
