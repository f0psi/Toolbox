import sys

decode = " "


if len(sys.argv) == 2:
    filename = sys.argv[1]
    print("reading File [" + filename +"]")
    with open(filename) as file:
        for line in file:
            if 'Setup Write to' in line:
                print('.')
            else:
                decode = decode + line[23:24]
                print(line[23:24])
            #print(line.rstrip())
    
    file.close
    print(decode)
else:
    print("Filename needed..")
