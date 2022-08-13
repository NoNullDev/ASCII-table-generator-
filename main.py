from openpyxl import Workbook, load_workbook
import re
from openpyxl.cell.cell import ILLEGAL_CHARACTERS_RE

wb = load_workbook('table.xlsx')
ws = wb.active


#wb.save("table.xlsx")

def charToBin(char):
    numbers = 8 - len(str("{0:b}".format((ord(char)))))

    new_text = ""
    for i in range(numbers):
        new_text += ("0")

    new_text += "{0:b}".format((ord(char)))
    return new_text

ws.append(["Sequência","Bit 0", "Bit 1", "Bit 2", "Bit 3", "Bit 4", "Bit 5", "Bit 6", "Bit 7", "Char", "Obs"])
for linha in range(0,128):
    array_list = [str(linha)]
    array_list.extend(list(str(charToBin(chr(linha)))))
    lol = chr(linha)
    lol = ILLEGAL_CHARACTERS_RE.sub(r'', lol)
    array_list.append(lol)
    print(array_list)
    ws.append(array_list)
        

wb.save("table.xlsx")

print(chr(0))
print(charToBin(chr(0)))