#necompleta
prenume=['Mihai','George','Ana','Dan','Ion','Geta','Vio']
virsta=[14,23,15,14,12,41,39]

for i in range(0,len(prenume)):
    print(f'{prenume[1]} are  virsta de {virsta[i]} ani \n')

prenume.append('Andreea')
prenume.append('Ioan')
virsta.append('34')
virsta.append('23')

print(f'{prenume}\n')
print(f'{virsta}\n')

prenume.pop(2)
virsta.pop(2)

print(f'{prenume[:3]}\n')
print(f'{prenume[::-1]}\n')
print(f'{prenume[2]},{prenume[4]}\n')
print(f'{virsta[2]},{virsta[4]}\n')
print(f'{prenume[:5]}\n')
print(f'{virsta[:5]}\n')
