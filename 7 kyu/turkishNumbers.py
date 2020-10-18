def turkish_number(num):

    units = {
        0 : "sıfır",
        1 : "bir",
        2 : "iki",
        3 : "üç",
        4 : "dört",
        5 : "beş",
        6 : "altı",
        7 : "yedi",
        8 : "sekiz",
        9 : "dokuz"
    }

    tens = {
        0 : "",
        1 : "on",
        2 : "yirmi",
        3 : "otuz",
        4 : "kırk",
        5 : "elli",
        6 : "altmış",
        7 : "yetmiş",
        8 : "seksen",
        9 : "doksan"
    }
        
    return (tens[num//10] + ((num>9) and (num%10>0)) * " " + (not(num//10>0) or (num%10>0)) * units[num%10])

print(turkish_number(99))