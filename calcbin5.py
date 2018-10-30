
activo = int(1)

while (activo == 1):
    print()
    print('*******Calculadora Binaria*******')
    print()
    print('Elige una operación:')
    print('1)Decimal a Binario')
    print('2)Binario a Decimal')
    print('3)Decimal a Hexadecimal')
    print('4)Hexadecimal a Decimal (BETA)')
    print('5)Traductor Rosarigasino(KAPPA)')
    print("\n")
    print('ᵜᵜby MAⱿFEⱤ ᵜᵜ')
    print("\n")

    z = int(input("Elige la operacion a realizar:"))

    if z == 1:
        print("\n")
        print("** Entrando al modulo Decimal a Binario **")
        print("\n")
	
        x = int(input("Introduce un numero Decimal para convertir en Binario:"))
        c = x // 2
        d = x // 4
        e = x // 8
        f = x // 16
        g = x // 32
        ha = x // 64
        ia = x // 128
        ja = x // 256
        ka = x // 512
        la = x // 1024
        ma = x // 2048
        na = x // 4096
        oa = x // 8192
        pa = x // 16384

        if ((x % 2) == 0):
            l = 0
        else:
            l = 1

        if ((c % 2) == 0):
            m = 0
        else:
            m = 1

        if ((d % 2 == 0)):
            n = 0
        else:
            n = 1

        if ((e % 2) == 0):
            o = 0
        else:
            o = 1

        if ((f % 2) == 0):
            p = 0
        else:
            p = 1

        if ((g % 2) == 0):
            q = 0
        else:
            q = 1

        if ((ha % 2) == 0):
            r = 0
        else:
            r = 1

        if ((ia % 2) == 0):
            s = 0
        else:
            s = 1

        if ((ja % 2) == 0):
            t = 0
        else:
            t = 1
        if ((ka % 2) == 0):
            u = 0
        else:
            u = 1
        if ((la % 2) == 0):
            v = 0
        else:
            v = 1
        if ((ma % 2) == 0):
            w = 0
        else:
            w = 1
        if ((na % 2) == 0):
            z = 0
        else:
            z = 1
        if ((oa % 2) == 0):
            a1 = 0
        else:
            a1 = 1
        if ((pa % 2) == 0):
            b1 = 0
        else:
            b1 = 1
        print("\n")
        print('el numero en binario es:', b1, a1, z, w, v, u, t, s, r, q, p, o, n, m, l)
        print("\n")
    elif z == 2:
        print("\n")
        print("** Entrando al modulo Binario a Decimal **")

        x = input("Introduce un numero Binario para convertir en Decimal:")

        if len(x) == 1:
            a = x[0]

            b = 0 * 2 + int(a)

            print(b)

        elif len(x) == 2:
            a = x[0]
            b = x[1]

            c = 0 * 2 + int(a)
            d = int(c) * 2 + int(b)
            print(d)

        elif len(x) == 3:
            a = x[0]
            b = x[1]
            c = x[2]

            d = 0 * 2 + int(a)
            e = int(d) * 2 + int(b)
            f = int(e) * 2 + int(c)
            print(f)

        elif len(x) == 4:
            a = x[0]
            b = x[1]
            c = x[2]
            d = x[3]

            e = 0 * 2 + int(a)
            f = int(e) * 2 + int(b)
            g = int(f) * 2 + int(c)
            h = int(g) * 2 + int(d)
            print(h)

        elif len(x) == 5:
            a = x[0]
            b = x[1]
            c = x[2]
            d = x[3]
            e = x[4]

            f = 0 * 2 + int(a)
            g = int(f) * 2 + int(b)
            h = int(g) * 2 + int(c)
            i = int(h) * 2 + int(d)
            j = int(i) * 2 + int(e)
            print(j)

        elif len(x) == 6:
            a = x[0]
            b = x[1]
            c = x[2]
            d = x[3]
            e = x[4]
            f = x[5]

            g = 0 * 2 + int(a)
            h = int(g) * 2 + int(b)
            i = int(h) * 2 + int(c)
            j = int(i) * 2 + int(d)
            k = int(j) * 2 + int(e)
            l = int(k) * 2 + int(f)
            print(l)

        elif len(x) == 7:
            a = x[0]
            b = x[1]
            c = x[2]
            d = x[3]
            e = x[4]
            f = x[5]
            g = x[6]

            h = 0 * 2 + int(a)
            i = int(h) * 2 + int(b)
            j = int(i) * 2 + int(c)
            k = int(j) * 2 + int(d)
            l = int(k) * 2 + int(e)
            m = int(l) * 2 + int(f)
            n = int(m) * 2 + int(g)
            print(n)

        elif len(x) == 8:
            a = x[0]
            b = x[1]
            c = x[2]
            d = x[3]
            e = x[4]
            f = x[5]
            g = x[6]
            h = x[7]

            i = 0 * 2 + int(a)
            j = int(i) * 2 + int(b)
            k = int(j) * 2 + int(c)
            l = int(k) * 2 + int(d)
            m = int(l) * 2 + int(e)
            n = int(m) * 2 + int(f)
            o = int(n) * 2 + int(g)
            p = int(o) * 2 + int(h)
            print(p)

        elif len(x) == 9:
            a = x[0]
            b = x[1]
            c = x[2]
            d = x[3]
            e = x[4]
            f = x[5]
            g = x[6]
            h = x[7]
            i = x[8]

            j = 0 * 2 + int(a)
            k = int(j) * 2 + int(b)
            l = int(k) * 2 + int(c)
            m = int(l) * 2 + int(d)
            n = int(m) * 2 + int(e)
            o = int(n) * 2 + int(f)
            p = int(o) * 2 + int(g)
            q = int(p) * 2 + int(h)
            r = int(q) * 2 + int(i)
            print(r)

        elif len(x) == 10:
            a = x[0]
            b = x[1]
            c = x[2]
            d = x[3]
            e = x[4]
            f = x[5]
            g = x[6]
            h = x[7]
            i = x[8]
            j = x[9]

            k = 0 * 2 + int(a)
            l = int(k) * 2 + int(b)
            m = int(l) * 2 + int(c)
            n = int(m) * 2 + int(d)
            o = int(n) * 2 + int(e)
            p = int(o) * 2 + int(f)
            q = int(p) * 2 + int(g)
            r = int(q) * 2 + int(h)
            s = int(r) * 2 + int(i)
            t = int(s) * 2 + int(j)
            print(t)

        elif len(x) == 11:
            a = x[0]
            b = x[1]
            c = x[2]
            d = x[3]
            e = x[4]
            f = x[5]
            g = x[6]
            h = x[7]
            i = x[8]
            j = x[9]
            k = x[10]

            l = 0 * 2 + int(a)
            m = int(l) * 2 + int(b)
            n = int(m) * 2 + int(c)
            o = int(n) * 2 + int(d)
            p = int(o) * 2 + int(e)
            q = int(p) * 2 + int(f)
            r = int(q) * 2 + int(g)
            s = int(r) * 2 + int(h)
            t = int(s) * 2 + int(i)
            u = int(t) * 2 + int(j)
            v = int(u) * 2 + int(k)

            print(v)

        elif len(x) == 12:
            a = x[0]
            b = x[1]
            c = x[2]
            d = x[3]
            e = x[4]
            f = x[5]
            g = x[6]
            h = x[7]
            i = x[8]
            j = x[9]
            k = x[10]
            l = x[11]

            m = 0 * 2 + int(a)
            n = int(m) * 2 + int(b)
            o = int(n) * 2 + int(c)
            p = int(o) * 2 + int(d)
            q = int(p) * 2 + int(e)
            r = int(q) * 2 + int(f)
            s = int(r) * 2 + int(g)
            t = int(s) * 2 + int(h)
            u = int(t) * 2 + int(i)
            v = int(u) * 2 + int(j)
            w = int(v) * 2 + int(k)
            x1 = int(w) * 2 + int(l)

            print(x1)

        elif len(x) == 13:
            a = x[0]
            b = x[1]
            c = x[2]
            d = x[3]
            e = x[4]
            f = x[5]
            g = x[6]
            h = x[7]
            i = x[8]
            j = x[9]
            k = x[10]
            l = x[11]
            m = x[12]

            n = 0 * 2 + int(a)
            o = int(n) * 2 + int(b)
            p = int(o) * 2 + int(c)
            q = int(p) * 2 + int(d)
            r = int(q) * 2 + int(e)
            s = int(r) * 2 + int(f)
            t = int(s) * 2 + int(g)
            u = int(t) * 2 + int(h)
            v = int(u) * 2 + int(i)
            w = int(v) * 2 + int(j)
            x1 = int(w) * 2 + int(k)
            x2 = int(x1) * 2 + int(l)
            x3 = int(x2) * 2 + int(m)

            print(x3)

        elif len(x) == 14:
            a = x[0]
            b = x[1]
            c = x[2]
            d = x[3]
            e = x[4]
            f = x[5]
            g = x[6]
            h = x[7]
            i = x[8]
            j = x[9]
            k = x[10]
            l = x[11]
            m = x[12]
            n = x[13]

            o = 0 * 2 + int(a)
            p = int(o) * 2 + int(b)
            q = int(p) * 2 + int(c)
            r = int(q) * 2 + int(d)
            s = int(r) * 2 + int(e)
            t = int(s) * 2 + int(f)
            u = int(t) * 2 + int(g)
            v = int(u) * 2 + int(h)
            w = int(v) * 2 + int(i)
            x1 = int(w) * 2 + int(j)
            x2 = int(x1) * 2 + int(k)
            x3 = int(x2) * 2 + int(l)
            x4 = int(x3) * 2 + int(m)
            x5 = int(x4) * 2 + int(n)

            print(x5)

        elif len(x) == 15:
            a = x[0]
            b = x[1]
            c = x[2]
            d = x[3]
            e = x[4]
            f = x[5]
            g = x[6]
            h = x[7]
            i = x[8]
            j = x[9]
            k = x[10]
            l = x[11]
            m = x[12]
            n = x[13]
            o = x[14]

            p = 0 * 2 + int(a)
            q = int(p) * 2 + int(b)
            r = int(q) * 2 + int(c)
            s = int(r) * 2 + int(d)
            t = int(s) * 2 + int(e)
            u = int(t) * 2 + int(f)
            v = int(u) * 2 + int(g)
            w = int(v) * 2 + int(h)
            x1 = int(w) * 2 + int(i)
            x2 = int(x1) * 2 + int(j)
            x3 = int(x2) * 2 + int(k)
            x4 = int(x3) * 2 + int(l)
            x5 = int(x4) * 2 + int(m)
            x6 = int(x5) * 2 + int(n)
            x7 = int(x6) * 2 + int(o)

            print(x7)





    elif z == 3:
        print("\n")
        print("** Entrando al modulo Decimal a Hexadecimal **")
	
        x = int(input("introduce un numero decimal para transformar a hexadecimal:"))

        c = x // 16
        d = x // 256
        e = x // 4096
        f = x // 65536
        g = x // 1048576

        if ((x % 16) == 0):
            l = 0
        elif ((x % 16) == 1):
            l = 1
        elif ((x % 16) == 2):
            l = 2
        elif ((x % 16) == 3):
            l = 3
        elif ((x % 16) == 4):
            l = 4
        elif ((x % 16) == 5):
            l = 5
        elif ((x % 16) == 6):
            l = 6
        elif ((x % 16) == 7):
            l = 7
        elif ((x % 16) == 8):
            l = 8
        elif ((x % 16) == 9):
            l = 9
        elif ((x % 16) == 10):
            l = 'A'
        elif ((x % 16) == 11):
            l = 'B'
        elif ((x % 16) == 12):
            l = 'C'
        elif ((x % 16) == 13):
            l = 'D'
        elif ((x % 16) == 14):
            l = 'E'
        else:
            l = 'F'

        if ((c % 16) == 0):
            m = 0
        elif ((c % 16) == 1):
            m = 1
        elif ((c % 16) == 2):
            m = 2
        elif ((c % 16) == 3):
            m = 3
        elif ((c % 16) == 4):
            m = 4
        elif ((c % 16) == 5):
            m = 5
        elif ((c % 16) == 6):
            m = 6
        elif ((c % 16) == 7):
            m = 7
        elif ((c % 16) == 8):
            m = 8
        elif ((c % 16) == 9):
            m = 9
        elif ((c % 16) == 10):
            m = 'A'
        elif ((c % 16) == 11):
            m = 'B'
        elif ((c % 16) == 12):
            m = 'C'
        elif ((c % 16) == 13):
            m = 'D'
        elif ((c % 16) == 14):
            m = 'E'
        else:
            m = 'F'

        if ((d % 16 == 0)):
            n = 0
        elif ((d % 16) == 1):
            n = 1
        elif ((d % 16) == 2):
            n = 2
        elif ((d % 16) == 3):
            n = 3
        elif ((d % 16) == 4):
            n = 4
        elif ((d % 16) == 5):
            n = 5
        elif ((d % 16) == 6):
            n = 6
        elif ((d % 16) == 7):
            n = 7
        elif ((d % 16) == 8):
            n = 8
        elif ((d % 16) == 9):
            n = 9
        elif ((d % 16) == 10):
            n = 'A'
        elif ((d % 16) == 11):
            n = 'B'
        elif ((d % 16) == 12):
            n = 'C'
        elif ((d % 16) == 13):
            n = 'D'
        elif ((d % 16) == 14):
            n = 'E'
        else:
            n = 'F'

        if ((e % 16 == 0)):
            o = 0
        elif ((e % 16) == 1):
            o = 1
        elif ((e % 16) == 2):
            o = 2
        elif ((e % 16) == 3):
            o = 3
        elif ((e % 16) == 4):
            o = 4
        elif ((e % 16) == 5):
            o = 5
        elif ((e % 16) == 6):
            o = 6
        elif ((e % 16) == 7):
            o = 7
        elif ((e % 16) == 8):
            o = 8
        elif ((e % 16) == 9):
            o = 9
        elif ((e % 16) == 10):
            o = 'A'
        elif ((e % 16) == 11):
            o = 'B'
        elif ((e % 16) == 12):
            o = 'C'
        elif ((e % 16) == 13):
            o = 'D'
        elif ((e % 16) == 14):
            o = 'E'
        else:
            o = 'F'

        if ((f % 16 == 0)):
            p = 0
        elif ((f % 16) == 1):
            p = 1
        elif ((f % 16) == 2):
            p = 2
        elif ((f % 16) == 3):
            p = 3
        elif ((f % 16) == 4):
            p = 4
        elif ((f % 16) == 5):
            p = 5
        elif ((f % 16) == 6):
            p = 6
        elif ((f % 16) == 7):
            p = 7
        elif ((f % 16) == 8):
            p = 8
        elif ((f % 16) == 9):
            p = 9
        elif ((f % 16) == 10):
            p = 'A'
        elif ((f % 16) == 11):
            p = 'B'
        elif ((f % 16) == 12):
            p = 'C'
        elif ((f % 16) == 13):
            p = 'D'
        elif ((f % 16) == 14):
            p = 'E'
        else:
            p = 'F'

        if ((g % 16 == 0)):
            q = 0
        elif ((g % 16) == 1):
            q = 1
        elif ((g % 16) == 2):
            q = 2
        elif ((g % 16) == 3):
            q = 3
        elif ((g % 16) == 4):
            q = 4
        elif ((g % 16) == 5):
            q = 5
        elif ((g % 16) == 6):
            q = 6
        elif ((g % 16) == 7):
            q = 7
        elif ((g % 16) == 8):
            q = 8
        elif ((g % 16) == 9):
            q = 9
        elif ((g % 16) == 10):
            q = 'A'
        elif ((g % 16) == 11):
            q = 'B'
        elif ((g % 16) == 12):
            q = 'C'
        elif ((g % 16) == 13):
            q = 'D'
        elif ((g % 16) == 14):
            q = 'E'
        else:
            q = 'F'

        print(q, p, o, n, m, l)

    elif z == 4:
        print("\n")
        print("** Entrando al modulo Hexadecimal a Decimal (BETA)**")
        print("\n")
        print("Recuerda que tienes que ingresar 5 dígitos por separado.")
        print("En caso de ser un número con menor cantidad de dígitos ingresar ceros.")
        print("Ejemplo: para el número 2A4 ingresar 002A4")
        print()

        x1 = input("Introduce el primer dígito del numero hexadecimal: ")
        x2 = input("Introduce el segundo dígito del numero hexadecimal: ")
        x3 = input("Introduce el tercer dígito del numero hexadecimal: ")
        x4 = input("Introduce el cuarto dígito del numero hexadecimal: ")
        x5 = input("Introduce el quinto dígito del numero hexadecimal: ")

        if x1 == ("A"):
            x1 = 10

        if x1 == ("B"):
            x1 = 11

        if x1 == ("C"):
            x1 = 12

        if x1 == ("D"):
            x1 = 13

        if x1 == ("E"):
            x = 14

        if x1 == ("F"):
            x1 = 15

        #################

        if x2 == ("A"):
            x2 = 10

        if x2 == ("B"):
            x2 = 11

        if x2 == ("C"):
            x2 = 12

        if x2 == ("D"):
            x2 = 13

        if x2 == ("E"):
            x2 = 14

        if x2 == ("F"):
            x2 = 15

        #################

        if x3 == ("A"):
            x3 = 10

        if x3 == ("B"):
            x3 = 11

        if x3 == ("C"):
            x3 = 12

        if x3 == ("D"):
            x3 = 13

        if x3 == ("E"):
            x3 = 14

        if x3 == ("F"):
            x3 = 15

        #

        if x4 == ("A"):
            x4 = 10

        if x4 == ("B"):
            x4 = 11

        if x4 == ("C"):
            x4 = 12

        if x4 == ("D"):
            x4 = 13

        if x4 == ("E"):
            x4 = 14

        if x4 == ("F"):
            x4 = 15

        #################

        if x5 == ("A"):
            x5 = 10

        if x5 == ("B"):
            x5 = 11

        if x5 == ("C"):
            x5 = 12

        if x5 == ("D"):
            x5 = 13

        if x5 == ("E"):
            x5 = 14

        if x5 == ("F"):
            x5 = 15

        print(int(x1) * (16 ** 4) + int(x2) * (16 ** 3) + int(x3) * (16 ** 2) + int(x4) * (16 ** 1) + int(x5))


    elif z == 5:
        pyg = 'gas'

        original = input('Enter a Word:')

        if len(original) <= 5 and original.isalpha():
            word = original.lower()
            new_word = word[0:2] + pyg + word[1] + word[2:5]
            print(new_word)
        elif len(original) == 6 and original.isalpha():
            word = original.lower()
            new_word = word[0:4] + pyg + word[3] + word[4:6]
            print(new_word)
        elif len(original) == 7 and original.isalpha():
            word = original.lower()
            new_word = word[0:5] + pyg + word[4] + word[5:7]
            print(new_word)
        elif len(original) == 8 and original.isalpha():
            word = original.lower()
            new_word = word[0:5] + pyg + word[4] + word[5:8]
            print(new_word)
        else:
            print('that is not a word')
    print("\n")
    y = int(input("Desea continuar?\n 1) Sí\n 2) No\n"))

    if y == 1:
        activo = 1
    else:
        activo = 0
        print("Gracias por usar la calculadora by MAⱿFEⱤ")
