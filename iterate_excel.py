#!/bin/python

import openpyxl

wb = openpyxl.load_workbook("switches.xlsx", data_only=True)
sheet = wb["Sheet1"]

list1 = []
list2 = []

for i in range(2, 52):
    rowH = "H{0}".format(i)
    rowI = "I{0}".format(i)
    list1.append(sheet[rowH].value)
    list2.append(sheet[rowI].value)

data = ""

for i in range(len(list1)):
    data +=(
        """
- HOSTNAME: """
        + list1[i]
        + """
    VLAN_3123_SVI_IP: """
        + list2[i]
        + """ 255.255.255.0
    DEFAULT_GW: 10.0.0.1
    VLAN_LIST:
        vlan100:
        VLAN_ID: 100
        VLAN_NAME: WTS
        """
)

print(data)