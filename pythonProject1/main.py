# download the CPTAC-CCRCC manifest file

import requests

# download manifest file from CPTAC-CCRCC page
manifest = requests.get("https://wiki.cancerimagingarchive.net/download/attachments/33948213/TCIA-CPTAC-CCRCC-batch8-Sep2019.tcia?version=2&amp;modificationDate=1569606470298&amp;api=v2")
with open('CPTAC-CCRCC.tcia', 'wb') as f:
    f.write(manifest.content)

# Run this cell to edit the manifest file to download only the first three scans.

with open('CPTAC-CCRCC.tcia','r') as firstfile, open('CPTAC-CCRCC-Sample.tcia','a') as secondfile:
    count = 0
    for line in firstfile:
        # append content to second file
        secondfile.write(line)
        # Stop after header and first 3 series UIDs
        count += 1;
        if count == 9:
            break

# imports
import requests
import pandas as pd

# download tcia_utils
tcia_utils_text = requests.get("https://github.com/kirbyju/TCIA_Notebooks/raw/main/tcia_utils.py")
with open('tcia_utils.py', 'wb') as f:
    f.write(tcia_utils_text.content)