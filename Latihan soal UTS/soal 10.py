#validasi expensi campuran acak
def valid(kurung):          #menggunakan stack agar kurung terakhir yang dibuka harus ditutup pertama 
    stack = []              #karena menggunakan konsep LIFO

    pasangan = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    for i in kurung:
        if i in "([{":
            stack.append (i)

        elif i in ")]}":
            if not stack or stack [-1] != pasangan[i]:      #pada bagian ini stack[-1] digunakan untuk mengecek bagian atas stack
                return "Tidak valid"
        
            stack.pop()      #setelah cocok pop ini bertugas untuk menghapus kurung pembuka pada stack

    if not stack:
        return "Valid"
    else:
        return "Tidak valid"    
    
print("{[()]} :", valid("{[()]}"))
print("{[(])} :", valid ("{[(])}"))
print("((( :", valid("((("))
