import re

fileName = input('Enter file absolute address')
y = open(fileName, "r")
fileContentAsList = y.read().split('\n\n')
y.close

outputAsList = []
nameAndVersionList = []
nameList = []
versionList = []

for package in fileContentAsList:
    nameAndVersion = re.search(r'[a-z,\-,\.]+@[\^]?[0-9]+\.[0-9]+\.[0-9]+', package)
    name = re.search(r'[a-z,\-,\.]+', package).group(0)
    version = package.split('\n')[1][11:-1]
    print("Name : "+name)
    print(version)
    if ('-pre4' in version) or ('-dev-harmony' in version) or ('-alpha.' in version) or ('-rc.' in version) or ('beta' in version):
        outputAsList.append(package)
        continue
    version = [int(m) for m in version.split('.')]
    print("Current version", version)
    flag = 0
    if (nameAndVersion and package[0] != '"'):
        nameAndVersion = nameAndVersion.group(0)
        if (nameList and name == nameList[-1]):
            print(name + " has been encountered previously")
            if version[0] == versionList[-1][0]:
                flag = 1
                if version[1] > versionList[-1][1]:
                    prevString = outputAsList.pop()
                    prevStringName = prevString.split('\n')[0]
                    package = package.split('\n')
                    v = package[0][:-1]+', '+ prevStringName
                    package[0] = v
                    outputAsList.append('\n'.join(package))
                elif version[1] < versionList[-1][1]:
                    prevString = outputAsList.pop()
                    prevStringList = prevString.split('\n')
                    prevStringList[0] = prevStringList[0][:-1]+', '+nameAndVersion+":"
                    outputAsList.append('\n'.join(prevStringList))
                else:
                    if version[2] > versionList[-1][2]:
                        prevString = outputAsList.pop()
                        prevStringName = prevString.split('\n')[0]
                        package = package.split('\n')
                        v = package[0][:-1]+', '+ prevStringName
                        package[0] = v
                        outputAsList.append('\n'.join(package))
                    elif version[2] < versionList[-1][2]:
                        prevString = outputAsList.pop()
                        prevStringList = prevString.split('\n')
                        prevStringList[0] = prevStringList[0][:-1]+', '+nameAndVersion+":"
                        outputAsList.append('\n'.join(prevStringList))
            else:
                print("Keep this yo")
        nameList.append(name)
        versionList.append(version)
        nameAndVersionList.append(nameAndVersion)
        if flag == 0:
            outputAsList.append(package)
    else:
        outputAsList.append(package)

print
print
output = "\n\n".join(outputAsList)
print(output)

text_file = open(fileName, "w")
text_file.write(output)
text_file.close()