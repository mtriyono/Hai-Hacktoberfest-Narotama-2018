i=a=b=c=0
nama=[]
npm=[]
kls=[]
jur=[]
ang=[]
while True:
    print 'Masukkan data ke - ',i+1
    nama.append(raw_input('Nama Anda : '))
    npm.append(raw_input('NPM Anda : '))
    if len(npm[i])!=8:
        print 'NPM Salah'
        print
        nama.pop(i)
        npm.pop(i)
        continue
    kls.append(raw_input('Kelas Anda : '))
    if len(kls[i])!=5:
        print 'Kelas Salah'
        print
        nama.pop(i)
        npm.pop(i)
        kls.pop(i)
        continue
    jur.append(kls[i][1:3])
    ang.append(npm[i][3:5])
    if jur[i]=='IA':
        jur[i]='Teknik Informatika'
        a+=1
    elif jur[i]=='IB':
        jur[i]='Teknik Industri'
        b+=1
    elif jur[i]=='IC':
        jur[i]='Teknik Mesin'
        c+=1
    else:
        print 'Kelas Salah'
        print
        continue
    lagi=''
    while lagi!='y' and lagi!='t':
        lagi=raw_input('INPUT LAGI [Y/T] : ')
    i+=1
    if lagi=='t':
        break
print '                        Daftar Mahasiswa'
print '========================================================================'
print 'No.  Nama     NPM     Kelas  Angkatan  Jurusan'
print '========================================================================'
for n in range(i):
    print n+1,'  ',nama[n],'   ',npm[n],' ',kls[n],'  ',ang[n],'        ',jur[n],''
print 'TOTAL JURUSAN MANAGEMEN = ',a,'orang\n'
print 'TOTAL JURUSAN BAHASA = ',b,'orang\n'
print 'TOTAL JURUSAN POLITEKNIK  = ',c,'orang\n'
ing=''
while ing!='y' and ing!='t':
    ing=raw_input('Ingin melihat hasil [Y/T]? ')
if ing=='y':
    cari=raw_input('Cari berdasarkan NPM : ')
    for n in range(i):
        if cari==npm[n]:
            print
            print 'Nama :',nama[n]
            print 'Kelas :',kls[n]
            print 'Angkatan :',ang[n]
            print 'Jurusan :',jur[n]
            break
        else:
            print 'NPM TIDAK ADA'
            break

Output :


# Fungsi Rekursif faktorial
def faktorial(n):
    if n <= 1:
        return 1
    else:
        return n*faktorial(n-1)

#Program utama
for n in range(11):
   print "%d! = %d" % (n, faktorial(n))
while True:
    try:
        n=input('Nilai n! : ')
        print 'Faktorial %d! = %d'%(n,faktorial(n))
    except:
        continue
    break

# Fungsi Fibonacci
def fibonacci(n):
    if n < 0:
        print "Tidak ada bilangan yang bernilai negatif"
    elif n == 0 or n == 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Program utama
for n in range(11):
   print "Fibonacci(%d) = %d" % (n, fibonacci(n))
while True:
    try:
        n=input("Masukkan sebuah bilangan : ")
        print "Fibonacci(%d) = %d"%(n,fibonacci(n))
    except:
        continue
    break

Output :


nm=raw_input('Nama : ')
pwd=raw_input('Password : ')
hobby=[]
other={}
i=0
while True:
    hobby.append(raw_input('Hobby Anda : '))
    lagi=''
    while lagi!='y' and lagi!='t':
        lagi=raw_input('Masih ada lagi [Y/T] : ')
    if lagi=='t':
        break
    i+=1
other['Sex']=raw_input('Jenis Kelamin : ')
other['TTL']=raw_input('Tempat/Tanggal lahir : ')
other['Umur']=raw_input('Umur : ')
def guest(name, password, *hobby, **other):
    print "Your name    :",name
    print "Your password:",password
    print "Hobby Anda   :"
    for n in range(i+1):
        print hobby[n]
    print "Lain-lain    :"
    print other['Sex']
    print other['TTL']
    print other['Umur']
guest(nm,pwd,*hobby,**other)

Output :


while True:
    nama=raw_input('Masukkan nama : ')
    npm=raw_input('Masukkan npm : ')
    if len(npm)!=8:
        print 'NPM tidak sesuai\n'
        continue
    ang=npm[3:5]
    jur=npm[0]
    if npm[3]=='9':
        ang='19'+ang
    elif npm[3]=='0':
        ang='20'+ang
    else:
        print 'NPM Salah\n'
        continue
    if jur=='1':
        jur='D3-TI'
    elif jur=='2':
        jur='S1-SI'
    elif jur=='3':
        jur='S1-SK'
    elif jur=='4':
        jur='S1-TI'
    elif jur=='5':
        jur='D3-SI'
    elif jur=='6':
        jur='D3-SK'
    elif jur=='7':
        jur='S1-TK'
    elif jur=='8':
        jur='S1-TM'
    elif jur=='9':
        jur='S1-IK'
    else:
        print 'NPM Salah\n'
        continue
    print '-------------------------------------------------------'
    print nama
    print 'Mahasiswa jurusan %s dan angkatan tahun %s'%(jur,ang)
    lagi=''
    while lagi!='y' and lagi!='t':
        lagi=raw_input('Coba lagi [y/t]? ')
    if lagi=='t':
        break