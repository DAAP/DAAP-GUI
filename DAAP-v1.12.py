# This is DAAP-v1.12.py,
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import font
import re
import os
from pathlib import Path
from DAAPDefs import *
from operator import itemgetter
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

Dics = []
os.chdir('./DicStore')
DicFiles = []
BigDic = {}
WDic = []
DicsN = 0
WDicsN = 0
ERRORS = 0
Speakers = {}
UseDics = []
Vars = []
ECIter = 0
DicFiles0 = os.listdir('.')
DicFiles0 = sorted(DicFiles0)
TxtCorr = 0
for dic in DicFiles0:
    if re.search('^\.', dic) is None:
        if re.search('\w+\.', dic) is None:
            Dics.append(dic)
        elif re.search('\w+\.Wt$', dic) is not None:
            Dics.append(dic)
rDics1 = []
for dic in Dics:
    if re.search(r'\.', dic) is None:
        rDics1.append(dic)
    else:
        Split = re.split(r'\.', dic)
        rDics1.append(Split[0])


def VarStates(*args):
    for i in range(len(rDics1)):
        Val = Var[i].get()
        Vars.append(Val)

root = Tk()
root.geometry('750x400+10+20')
titlefont = font.Font(family='Verdana', size=36)
root.title('THE DISCOURSE ATTRIBUTES ANALYSIS PROGRAM (DAAP)')
content = ttk.Frame(root)
frame = ttk.Frame(content, borderwidth=1, width=1000, height=1000, padding='3 3 12 12')
TxtFont = font.Font(family='Helvetica', size=14)
TopFont = font.Font(family='Helvetica', size=20)
content.grid(column=0, row=0)
labl0 = ttk.Label(content, text='WELCOME TO DAAP', font=TopFont).grid(column=5, columnspan=5, row=0)
labl1 = ttk.Label(content, text='Version 1.12', font=TxtFont).grid(column=5, columnspan = 5, row=1)

txt = Text(root, width=60, height=15, font=TxtFont, wrap='word')
Txt1 = '\n\nStep 1. A finder window should have opened. Please navigate to the folder containing your file(s) to be' \
       ' processed, click on that folder, and then click on the button marked "Choose". \n\nBefore proceeding, you' \
       ' should ensure that you have copies of these files in another folder, as some changes may need to be made.'
txt.insert('1.0', Txt1)
txt.grid(column=0, row=2, columnspan=15, rowspan=18)
dirname = filedialog.askdirectory()
Pdirname = Path(dirname)

Directory = Pdirname.name
os.chdir('..')
os.chdir(Directory)
Files = os.listdir('.')
if 'GRAPHS' not in Files:
    os.mkdir('GRAPHS')
if 'DATA' not in Files:
    os.mkdir('DATA')

MTTFile = 'DATA/' + Directory + '.MTTFile.txt'
open(MTTFile, 'w')
SMTAG0File = 'DATA/' + Directory + '.SMT.AG0.csv'
open(SMTAG0File, 'w')
SMTAG01File =  'DATA/' + Directory + '.SMT.AG01.csv'
open(SMTAG01File, 'w')
SMTAG02File = 'DATA/' + Directory + '.SMT.AG02.csv'
open(SMTAG02File, 'w')
WRDAG0File = 'DATA/' + Directory + '.WRD.AG0.csv'
open(WRDAG0File, 'w')
WRDAG1File = 'DATA/' + Directory + '.WRD.AG1.csv'
open(WRDAG1File, 'w')
SMTAG1File = 'DATA/' + Directory + '.SMT.AG1.csv'
open(SMTAG1File, 'w')
WRDAG2File = 'DATA/' + Directory + '.WRD.AG2.csv'
open(WRDAG2File, 'w')
SMTAG2File = 'DATA/' + Directory + '.SMT.AG2.csv'
open(SMTAG2File, 'w')
TTGFile = 'DATA/' + Directory + '.TTG.txt'
open(TTGFile, 'w')
WRDTRNFile = 'DATA/' + Directory + '.WRD.TRN.csv'
open(WRDTRNFile, 'w')
SMTTRNFile = 'DATA/' + Directory + '.SMT.TRN.csv'
open(SMTTRNFile, 'w')

TxtFiles = []
SMTFiles = []
WRDFiles = []
TTRFiles = []
MTTFiles = []
ECFiles = []
PLTFiles = []
Files0 = os.listdir('.')
Files0 = sorted(Files0)
TxtFiles1 = []
TxtFilesA = []
DotErrorN = 0
CATS = {}
TTGList = []
GLnDAT = []
CATUses = {}
ACATS = []
DCATS = []
OCATS = []
Var = []
for v in range(len(Files0)):
    SplitFile = re.split('\.', Files0[v])
    if len(SplitFile) > 2:
        if SplitFile[1] != 'A' and SplitFile[1] != 't':
            print('ERROR 7: File name contains too many periods (dots)', SplitFile)
            DotError = 'ERROR 7: File name', SplitFile, ' contains too many periods (dots)'
            DotErrorN = 1
        continue
    elif len(SplitFile) == 2:
        if SplitFile[1] == 'txt' or SplitFile[1] == 'TXT':
            TxtFiles.append(Files0[v])
            NewFile = SplitFile[0] + '.A.txt'
            if NewFile not in TxtFilesA:
                TxtFilesA.append(NewFile)
for fil in TxtFiles:
    SplitFile = re.split('\.', fil)
    TxtFiles1.append(SplitFile[0])
    ECFile = SplitFile[0] + 'EC.rtf'
    ECFiles.append(ECFile)

CATL = []


def errorcycle(ERRCT):
    for fil in TxtFiles:
        open(fil)
        split1 = re.split('\.', fil)
        filA = split1[0] + '.A.txt'
        open(filA, 'w')

        for line in open(fil, errors='ignore'):
            line = line.replace('\\', '>')
            line = line.replace('  ', ' ')
            line = line.replace('>st', '>s')
            line = line.replace('>sc', '>s')
            line = line.replace("o'clock", "oclock")
            line = line.replace("o-clock", "oclock")
            line = line.replace("o_clock", "oclock")
            line = line.replace('wella', 'well')
            line = line.replace('wellc', 'well')
            line = line.replace('welld', 'well')
            line = line.replace('wellw', 'well')
            line = line.replace('likec', 'like')
            line = line.replace('likev', 'like')
            line = line.replace('kindf', 'kind')
            line = line.replace('meanf', 'mean')
            line = line.replace('knowd', 'know')
            line = line.replace("'em", 'them (em)')
            line = line.replace('gonna', 'going to (gonna)')
            line = line.replace('hafta', 'have to (hafta)')
            line = line.replace('wanna', 'want to (wanna)')
            line = line.replace('gotta', 'got to (gotta)')
            line = line.replace('woulda', 'would have (woulda)')
            line = line.replace('coulda', 'could have (coulda)')
            line = line.replace('shoulda', 'should have (shoulda)')
            line = line.replace('kinda', 'kind of (kinda)')
            line = line.replace('outta', 'out of (outta)')
            line = line.replace('sorta', 'sort of (sorta)')
            line = line.replace('lotta', 'lot of (lotta)')
            line = line.replace('lotsa', 'lots of (lotsa)')
            line = line.replace('dunno', "don't know (dunno)")
            line = line.replace('uh huh', 'uhhuh')
            line = line.replace('_', '-')
            line = line.replace("'cause", 'because')
            line = line.replace("'til", 'until')
            line = line.replace(' ya', ' you (ya)')
            line = line.replace('#', '(Number sign)')
            print(line, file=open(filA, 'a'))

    LOGList = []
    if DotErrorN > 0:
        LOGList.append(DotError)
    TErrorsN = 0
    ERRFiles = []
    for v in range(len(TxtFilesA)):  # Make EC Files
        Speakers[v] = []
        open(ECFiles[v], 'w')
        print('{\\rtfl\\ansi\\deff0 {\\fonttbl {\\f0 Times New Roman;}}', file=open(ECFiles[v], 'a'))
        print('{\\colortbl', file=open(ECFiles[v], 'a'))
        print(';', file=open(ECFiles[v], 'a'))  # color cf0 = default
        print('\\red255\\green0\\blue0;', file=open(ECFiles[v], 'a'))  # color cf1 = red
        print('\\red0\\green0\\blue255;', file=open(ECFiles[v], 'a'))  # color cf2 =blue
        print('\\red0\\green255\\blue0;', file=open(ECFiles[v], 'a'))  # color cf3 = green
        print('\\red0\\green0\\blue0;', file=open(ECFiles[v], 'a'))  # color cf4 = black
        print('}', file=open(ECFiles[v], 'a'))
        StartSwitch = 0
        CAT0 = []
        TempCATS = {}
        ERRORS1 = 0
        Spkr = 0
        tSwitch = 0
        c9Check = 0
        LnDAT = []
        for line in open(TxtFilesA[v], errors='ignore'):
            if re.match(r'>c9', line) is not None:
                c9Check += 1
                LineProp = ['L', '\c9']
                LnDAT.append(LineProp)
                break
            if re.match(r'^\[.*\]$', line) is not None:
                continue
            if re.search(r'\S+.*>.*', line) is not None:
                ERRORS1 += 1
                LOGList.append(TxtFilesA[v] + ': control character (\\ or >) not at beginning of line')
                Words = re.split('\s', line)
                if Words[0] == '>s' or Words[0] == '>t' or Words[0] == '>op' or Words[0] == '>ox' or Words[0] == '>os':
                    NewLine = Words[0]
                else:
                    if re.search('>', Words[0]) is None:
                        NewLine = Words[0]
                    else:
                        NewLine = '{cf1 ' + Words[0] + '}'
                for i  in range(1, len(Words)):
                    if re.search('>', Words[i]) is None:
                        NewLine = NewLine + ' ' + Words[i]
                    else:
                        NewLine = NewLine + ' '  + '{\cf1 ' + Words[i] + '}'
                line = NewLine
            elif re.match(r'\s?>t(.*)$', line) is not None:
                tSwitch = 1
                Cat = ''
                Inst = ''
                Match = re.match(r'\s?>t(.*)', line)
                Remain = Match.group(1)
                if re.search(r'\s?(\w+)\s?:\s?(\w+)', Remain) is not None:
                    TentCat = re.search(r'\s?(\w+)\s?:\s?(\w+)', Remain)
                    Cat = TentCat.group(1)
                    Inst = TentCat.group(2)
                    if v == 0 and StartSwitch == 0:
                        if Cat in CATS:
                            LOGList.append(TxtFilesA[v] + 'ERROR 11: Same category, ' + Cat + ' appears twice at'
                                                                                              ' beginning of file')
                            ERRORS1 += 1
                            line = '\\line {\\cf1 ' + line + '}'
                        else:
                            CATL.append(Cat)
                            CATS[Cat] = Inst
                            LineProp = ['T', Cat, Inst]
                            LnDAT.append(LineProp)

                    elif v > 0 and StartSwitch == 0:
                        if Cat in TempCATS:
                            LOGList.append(TxtFilesA[v] + ' ERROR 11: Same category ' + Cat + 'appears twice at'
                                                                                              ' beginning of file,')
                            ERRORS1 += 1
                            line = '\\line {\\cf1 ' + line + '}'
                        else:
                            TempCATS[Cat] = Inst
                            LineProp = ['T', Cat, Inst]
                            LnDAT.append(LineProp)
                    elif StartSwitch > 0:
                        if Cat not in CATL:
                            LOGList.append(TxtFilesA[v] + ' ERROR 10: category ' + Cat +' not listed at top of '
                                                                                        'first file ')
                            line = '\\line {\\cf1 ' + line + '}'
                            ERRORS1 += 1
                        else:
                            CATS[Cat] = Inst
                            LineProp = ['T', Cat, Inst]
                            LnDAT.append(LineProp)
                    else:
                        print(TxtFiles[v] +' ERROR 8: Improper >t line:')
                        ERRORS1 += 1
                        line = '\\line {\\cf1 ' + line + '}'
            else:
                line = line.lower()
                if re.search(r'\s?>\s?op', line) is not None:
                    TentSpkr = int(re.match(r'^\s?>\s?op\s?(\d)(.*)', line).group(1))
                    Words = re.match(r'^\s?>\s?op\s?(\d)(.*)', line).group(2)
                    if TentSpkr == Spkr and tSwitch == 0:
                        line = '\\line {\\cf1 ' + line + '}'
                        ERRORS1 += 1
                        LOGList.append(TxtFilesA[v] + ' ERROR 9: SAME SPEAKER in line', line)
                    else:
                        Spkr = TentSpkr
                    if Spkr not in Speakers[v]:
                        Speakers[v].append(Spkr)

                    Split1 = wordcount(line)
                    if Split1[0] > 0:
                        for k in range(1, len(Split1)):
                            LOGList.append(str(TxtFilesA[v]) + ' ' + str(Split1[k]) + ': '  + line)
                            line = '\\line {\\cf1 ' + line + '}'
                            ERRORS1 += 1
                    LineProp = ['P', Spkr, Words]
                    LnDAT.append(LineProp)
                    StartSwitch += 1
                    tSwitch = 0

                elif re.search(r'\s?>\s?ox', line) is not None:  # \x with override
                    TentSpkr = int(re.match(r'^\s?>\s?ox\s?(\d)(.*)', line).group(1))
                    Words = re.match(r'^\s?>\s?ox\s?(\d)(.*)', line).group(2)
                    if TentSpkr == Spkr and tSwitch == 0:
                        line = '\\line {\\cf1 ' + line + '}'
                        ERRORS1 += 1
                        LOGList.append(TxtFilesA[v] + ' ERROR 9: SAME SPEAKER in line ' + line)
                    else:
                        Spkr = TentSpkr
                    if Spkr not in Speakers[v]:
                        Speakers[v].append(Spkr)

                    Split2 = wordcount(line)
                    if Split2[0] > 0:
                        for k in range(1, len(Split2)):
                            LOGList.append(str(TxtFilesA[v]) + ' ' + str(Split2[k]) + ': ' + line)
                            line = '\\line {\\cf1 ' + line + '}'
                            ERRORS1 += 1
                    LineProp = ['X', Spkr, Words]
                    LnDAT.append(LineProp)
                    StartSwitch += 1
                    tSwitch = 0
                elif re.search(r'\s?>\s?os', line) is not None:  # \s with override
                    TentSpkr = int(re.match(r'^\s?>\s?os\s?(\d)(.*)', line).group(1))
                    Words = re.match(r'^\s?>\s?os\s?(\d)(.*)', line).group(2)
                    if TentSpkr == Spkr and tSwitch == 0:
                        line = '\\line {\\cf1 ' + line + '}'
                        ERRORS1 += 1
                        LOGList.append(TxtFilesA[v] + ' ERROR 9: SAME SPEAKER in line ' + line)
                    else:
                        Spkr = TentSpkr
                    if Spkr not in Speakers[v]:
                        Speakers[v].append(Spkr)

                    split2 = wordcount(line)
                    if split2[0] > 0:
                        for k in range(1, len(split2)):
                            LOGList.append(str(TxtFilesA[v]) + ' ' + str(split2[k]) + ': ' + line)
                            line = '\\line {\\cf1 ' + line + '}'
                            ERRORS1 += 1
                    LineProp = ['O', Spkr, Words]
                    LnDAT.append(LineProp)
                    StartSwitch += 1
                    tSwitch = 0
                elif re.match(r'^\s?>\s?s(.*)$', line) is not None:
                    if re.match(r'^\s?>\s?s\s?\d.*', line) is not None:
                        TentSpkr = int(re.match(r'^\s?>\s?s\s?(\d)(.*)', line).group(1))
                        Words = re.match(r'^\s?>\s?s\s?(\d)(.*)', line).group(2)
                        if TentSpkr == Spkr and tSwitch == 0:
                            line = '\\line {\\cf1 ' + line + '}'
                            ERRORS1 += 1
                            LOGList.append(TxtFilesA[v] + ' ERROR 9: SAME SPEAKER in line ' + line)
                        else:
                            Spkr = TentSpkr
                        if Spkr not in Speakers[v]:
                            Speakers[v].append(Spkr)
                        split3 = wordcount(Words)
                        if split3[0] > 0:
                            for k in range(1, len(split3)):
                                LOGList.append(str(TxtFilesA[v]) + ' ' + str(split3[k]) + ': ' + line)
                                line = '\\line {\\cf1 ' + line + '}'
                                ERRORS1 += 1
                        else:
                            LineProp = ['S', Spkr, Words]
                            LnDAT.append(LineProp)
                            StartSwitch += 1
                            tSwitch = 0
                else:
                    if StartSwitch == 0:
                        LineProp = ['F', line]
                        LnDAT.append(LineProp)
                    else:
                        Balance = re.search(r'^(.+)$', line)
                        if Balance is not None:  # Line contains something
                            Content = Balance.group(1)
                            split4 = wordcount(Content)
                            if split4[0] > 0:
                                for k in range(1, len(split4)):
                                    LOGList.append(str(TxtFilesA[v]) + ' ' + str(split4[k]) + ': ' + line)
                                    line = '\\line {\\cf1 ' + line + '}'
                                    ERRORS1 += 1
                            else:
                                if split4[1] > 0:
                                    if tSwitch == 0:
                                        LineProp = ['C', Spkr, line.rstrip()]
                                        LnDAT.append(LineProp)
                                    elif tSwitch > 0:
                                        LineProp = ['S', Spkr, line.rstrip()]
                                        print('line,', line)
                                        LnDAT.append(LineProp)

                        elif Balance is None:  # No backslash and no content
                            LineProp = ['Z', line]
                            LnDAT.append(LineProp)
            print('\\line', line, end='\n', file=open(ECFiles[v], 'a'))
        print('}', file=open(ECFiles[v], 'a'))
        print('}', file=open(ECFiles[v], 'a'))
        GLnDAT.append(LnDAT)
        Speakers[v] = sorted(Speakers[v])
        for i in range(len(Speakers[v])):
            if Speakers[v][i] != i + 1:
                print('ERROR 5. The list of Speakers for TextFilesA ', v, 'has impermissable gaps\n',
                      'Speakers[v] = ', Speakers[v])
                LOGList.append(TxtFilesA[v] + ': ERROR 5. The list of Speakers has impermissable gaps\n'
                               + 'Speakers[v] = ' + Speakers[v])
                ERRORS1 += 1
        if ERRORS1 > 0:
            ERRFiles.append(v)
    TErrorsN += len(LOGList)
    return [TErrorsN, LOGList, ERRFiles, CATL]
problem = errorcycle(0)
Errors = problem[0]
if Errors > 0:
    Inst = ''
    Txt2 = '\n\Scroll down to read.\n Step 2: DAAP has read your files. Some of them do not follow the DAAP' \
           ' transcriptions rules. DAAP has made duplicates of these files in the project folder. If the original ' \
           ' file is named "Data1.txt", the duplicate file is named "Data1.EC.rtf." In this file, the places wheren ' \
           'changes in the transcriptions need to be made are reproduced in red.\n\nNOTE: DAAP uses both the' \
           ' backslash (\\) and the right angle bracket (>) as control characters. USE ONLY THE RIGHT ANGLE BRACKET ' \
           'TO INDICATE CHANGE IN SPEAKER IN THE EC FILE; DO NOT USE THE BACKSLASH IN THE EC FILE. \nPlease correct ' \
           'the indicated problems, and save and close each of the files you correct. Then type "y" in the "ERRORS " \
           "CORRECTED" box and click on the "CONTINUE" button. You will need to rerun DAAP after this process. DAAP ' \
           'will overwrite your original file with these corrections.' \
           '\n\n CAUTION: Error correcting is sometimes an ' \
           'iterative process, and you may need to repeat this procedure of error correcting.'

    txt.insert('4.0', Txt2)

    for line in problem[1]:
        Inst = Inst + '\n ' + str(line)
    txt.insert('15.0', Inst)

    EClabl = ttk.Label(root, text='Have you finished correcting the texts (y/n)').grid(column=0, columnspan=6, row=20)
    answer = StringVar()
    answer.set('n')
    ECC = ttk.Entry(root, textvariable=answer).grid(column=1, row=20, sticky='w')
    Finish = ttk.Button(root, text='CONTINUE', command=root.destroy).grid(column=1, row=21, sticky='w')
    root.mainloop()
    Cont = answer.get()

elif Errors == 0:
    CCRec = 0
    Var = []
    for file in ECFiles:
        os.remove(file)
    for i in range(len(rDics1)):
        DicV = IntVar()
        Check = ttk.Checkbutton(content, text=rDics1[i], variable=DicV, onvalue=1, offvalue=0)
        Check.grid(column=i, row=3, sticky='w')
        Var.append(DicV)

    labl5 = ttk.Label(content, text='Usage of Categories').grid(column=0, row=4)
    CATSUse = []
    for i in range(len(CATL)):
        CAT = CATL[i]
        ttk.Label(content, text=CAT).grid(column=0, row=5 + i)
        CATUtil = StringVar()
        CATUtil.set('O')
        D = ttk.Radiobutton(content, text='D', variable=CATUtil, value='D').grid(column=1, row=5 + i)
        A = ttk.Radiobutton(content, text='A', variable=CATUtil, value='A').grid(column=2, row=5 + i)
        O = ttk.Radiobutton(content, text='O', variable=CATUtil, value='O').grid(column=3, row=5 + i)
        CATSUse.append(CATUtil)
    Txt3 = '\n\nStep 2: DAAP has read your files, found no transcription errors and is ready to proceed.' \
           '\n\nStep 3: There is a list above of available dictionaries. Please click on the dictionaries you wish' \
           ' DAAP to use for processing your files.\n\n Step 4 (Only if you use categories): Each of the categories' \
           ' used in your texts is listed above, along with three buttons: "A" for aggregate, "D" for density, and' \
           ' "O" for ordinary. Please click on exactly one of these buttons for each category.' \
           '\n\nStep 5 (Final step): Click on the button marked "DICTIONARIES", and then click on the button marked' \
           ' "CONTINUE".'
    txt.insert('7.0', Txt3)
    finish = ttk.Button(root, text='DICTIONARIES', command=VarStates).grid(column=0, row=20, sticky='w')
    Finish = ttk.Button(root, text='CONTINUE', command=root.destroy).grid(column=1, row=20, sticky='w')
    root.mainloop()
    for fil in TxtFiles:
        SplitFile = re.split('\.', fil)
        WRDFile = 'DATA/' + SplitFile[0] + '.WRD.csv'
        WRDFiles.append(WRDFile)
        SMTFile = 'DATA/' + SplitFile[0] + '.SMT.csv'
        SMTFiles.append(SMTFile)
        TTRFile = 'DATA/' + SplitFile[0] + '.TTR.txt'
        TTRFiles.append(TTRFile)
        MTTFil = 'DATA/' + SplitFile[0] + '.MTT.txt'
        MTTFiles.append(MTTFil)
        PLTFile = 'GRAPHS/' + SplitFile[0] + 'PLT.png'
        PLTFiles.append(PLTFile)
    for i in range(len(Dics)):
        if Vars[i] == 1:
            UseDics.append(Dics[i])
    DFDic = -1
    for v in range(len(UseDics)):
        if re.search('\.Wt', UseDics[v]) is not None:
            WDic.append(UseDics[v])
            WDicsN += 1
        if UseDics[v] == 'DF':
            DFDic = v
    os.chdir('../DicStore')
    for v in range(len(UseDics) - WDicsN):
        for line in open(UseDics[v]):
            NewLine = re.split('\s', line)
            if len(NewLine) == 2:
                if NewLine[0] not in BigDic:
                    if v == 0:
                        BigDic[NewLine[0]] = [1]
                    elif v > 0:
                        List = []
                        for k in range(v):
                            List.append(0)
                        List.append(1)
                        BigDic[NewLine[0]] = List
                elif NewLine[0] in BigDic:
                    List = BigDic[NewLine[0]]
                    if len(List) < v:
                        for k in range(v - len(List)):
                            List.append(0)
                    List.append(1)
                    BigDic[NewLine[0]] = List

    for v in range(len(UseDics) - WDicsN, len(UseDics)):
        for line in open(UseDics[v]):
            NewLine = re.split('\s', line)
            if NewLine[0] not in BigDic:
                if v == 0:
                    BigDic[NewLine[0]] = [NewLine[1]]
                elif v > 0:
                    List = []
                    for k in range(v):
                        List.append(0)
                    List.append(NewLine[1])
                    BigDic[NewLine[0]] = List
            elif NewLine[0] in BigDic:
                List = BigDic[NewLine[0]]
                if len(List) < v:
                    for k in range(v - len(List)):
                        List.append(0)
                    List.append(NewLine[1])
                else:
                    List.append(NewLine[1])
                BigDic[NewLine[0]] = List

    if len(UseDics) > 1:
        for word in BigDic:
            if len(BigDic[word]) < len(UseDics):
                for j in range(len(UseDics) - len(BigDic[word])):
                    BigDic[word].append(0)

    if WDicsN > 0:
        for word in BigDic:
            for j in range(len(UseDics) - WDicsN, len(UseDics)):
                BigDic[word][j] = .5 * (float(BigDic[word][j]) + 1)

    NewList = []
    for word in BigDic:
        ListItem = (word, BigDic[word])
        NewList.append(ListItem)
    NewL1 = sorted(NewList, key=itemgetter(0))

    DCATSDic = []
    os.chdir('..')
    os.chdir(dirname)
    if len(CATS) > 0:
        for cat in CATL:
            CATUses[cat] = CATUtil.get()
            if CATUses[cat] == 'A':
                ACATS.append(cat)
                OCATS.append(cat)
            elif CATUses[cat] == 'D':
                DCATS.append(cat)
            elif CATUses[cat] == 'O':
                OCATS.append(cat)
            for cat in DCATS:
                DCATSDic[cat] = {}
                for dline in open(cat):
                    Weight = re.split('\s', dline)
                    DCATSDic[cat][Weight[0]] = float(Weight[1])
        OCATS = sorted(OCATS)

    for i in range(len(DicFiles)):
        NewDic = re.split('\.', DicFiles[i])
        if len(NewDic) > 1 and NewDic[1] == 'Wt':
            DicFiles[i] = NewDic[0]
    if len(DCATS) > 0:
        TDics = DCATS + UseDics
    else:
        TDics = UseDics
    rDics = []
    rWtDics = []
    for dic in TDics:
        if re.search(r'\.', dic) is None:
            rDics.append(dic)
        else:
            Split3 = re.split('\.', dic)
            rDics.append(Split3[0])
            rWtDics.append(Split3[0])
    SMTAG0Columns1 = []
    SMTAG0Columns2 = []
    print('File,Speaker,Words,Turns,TurnLMIN,TurnL1Q,TurnLMed,TurnL3Q,TurnLMAX,TurnLMean,TurnLSD', end=',',
          file=open(WRDAG0File, 'a'))
    print('File, Speaker', end=',', file=open(WRDAG1File, 'a'))
    print('File, Speaker', end=',', file=open(WRDAG2File, 'a'))
    print('File, Turn,Speaker, Words', end=',', file=open(WRDTRNFile, 'a'))
    print('File, Speaker, Words, Turns', end=',', file=open(SMTAG0File, 'a'))
    SMTAG0Columns1.append('Words')
    SMTAG0Columns2.append('Words')
    SMTAG0Columns2.append('Turns')
    print('File,Words,Turns', end=',', file=open(SMTAG01File, 'a'))
    print('File,Words,Turns', end=',', file=open(SMTAG02File, 'a'))
    print('File,Speaker', end=',', file=open(SMTAG1File, 'a'))
    print('File,Speaker', end=',', file=open(SMTAG2File, 'a'))
    print('File,Turn,Speaker,Words', end=',', file=open(SMTTRNFile, 'a'))
    for cat in OCATS:
        print(cat, end=',', file=open(WRDAG1File, 'a'))
        print(cat, end=',', file=open(WRDAG2File, 'a'))
        print(cat, end=',', file=open(WRDTRNFile, 'a'))
        print(cat, end=',', file=open(SMTAG1File, 'a'))
        print(cat, end=',', file=open(SMTAG2File, 'a'))
        print(cat, end=',', file=open(SMTTRNFile, 'a'))
    print('Words, Turns', end=',', file=open(WRDAG1File, 'a'))
    print('Words, Turns', end=',', file=open(WRDAG2File, 'a'))
    print('Words, Turns', end=',', file=open(SMTAG1File, 'a'))
    print('Words, Turns', end=',', file=open(SMTAG2File, 'a'))
    for i in range(len(TDics)):
        item1 = rDics[i] + ' Mean'
        item2 = rDics[i] + ' SD'
        if rDics[i] not in rWtDics:
            SMTAG0Columns1.append(item1)
            SMTAG0Columns2.append(item1)
            print(item1, sep=',', end=',', file=open(SMTAG0File, 'a'))
            print(item1, sep=',', end=',', file=open(SMTAG01File, 'a'))
            print(item1, sep=',', end=',', file=open(SMTAG02File, 'a'))
            print(item1, sep=',', end=',', file=open(SMTAG1File, 'a'))
            print(item1, sep=',', end=',', file=open(SMTAG2File, 'a'))
            print(item1, item2, sep=',', end=',', file=open(SMTTRNFile, 'a'))
    for i in range(len(UseDics)):
        if UseDics[i] not in WDic:
            item0 = rDics[i] + ' Match'
            item1 = rDics[i] + ' Coverage'
            item2 = rDics[i] + ' ODDS'
            print(item0, item1, item2, sep=',', end=',', file=open(WRDAG0File, 'a'))
            print(item0, item1, item2, sep=',', end=',', file=open(WRDAG1File, 'a'))
            print(item0, item1, item2, sep=',', end=',', file=open(WRDAG2File, 'a'))
            print(item0, item1, item2, sep=',', end=',', file=open(WRDTRNFile, 'a'))

        elif UseDics[i] in WDic:
            item0 = rDics[i] + ' Match'
            item01 = rDics[i] + ' Cover'
            item1 = rDics[i] + ' Pos Match'
            item2 = rDics[i] + ' Pos Prop'
            print(item0, item01, item1, item2, sep=',', end=',', file=open(WRDAG0File, 'a'))
            print(item0, item01, item1, item2, sep=',', end=',', file=open(WRDAG1File, 'a'))
            print(item0, item01, item1, item2, sep=',', end=',', file=open(WRDAG2File, 'a'))
            print(item0, item01, item1, item2, sep=',', end=',', file=open(WRDTRNFile, 'a'))
        if TDics[i] in WDic:
            item0 = rDics[i] + ' Mean'
            item1 = rDics[i] + ' MHigh'
            item2 = rDics[i] + ' HProp'
            item3 = rDics[i] + 'SD'
            SMTAG0Columns1.append(item0)
            SMTAG0Columns1.append(item1)
            SMTAG0Columns1.append(item2)
            SMTAG0Columns2.append(item0)
            SMTAG0Columns2.append(item1)
            SMTAG0Columns2.append(item2)
            print(item0, item1, item2, sep=',', end=',', file=open(SMTAG0File, 'a'))
            print(item0, item1, item2, sep=',', end=',', file=open(SMTAG01File, 'a'))
            print(item0, item1, item2, sep=',', end=',', file=open(SMTAG02File, 'a'))
            print(item0, item1, item2, sep=',', end=',', file=open(SMTAG1File, 'a'))
            print(item0, item1, item2, sep=',', end=',', file=open(SMTAG2File, 'a'))
            print(item0, item3, item1, item2, sep=',', end=',', file=open(SMTTRNFile, 'a'))
    for i in range(len(TDics)):
        for j in range(i + 1, len(TDics)):
            item = rDics[i] + '_' + rDics[j]
            SMTAG0Columns1.append(item)
            SMTAG0Columns2.append(item)
            print(item, end=',', file=open(SMTAG0File, 'a'))
            print(item, end=',', file=open(SMTAG01File, 'a'))
            print(item, end=',', file=open(SMTAG02File, 'a'))
            print(item, end=',', file=open(SMTAG1File, 'a'))
            print(item, end=',', file=open(SMTAG2File, 'a'))
            print(item, end=',', file=open(SMTTRNFile, 'a'))
    print('', file=open(WRDAG0File, 'a'))
    print('', file=open(WRDAG1File, 'a'))
    print('', file=open(WRDAG2File, 'a'))
    print('', file=open(WRDTRNFile, 'a'))
    print('', file=open(SMTAG01File, 'a'))
    print('', file=open(SMTAG02File, 'a'))
    print('', file=open(SMTAG0File, 'a'))
    print('', file=open(SMTAG1File, 'a'))
    print('', file=open(SMTAG2File, 'a'))
    print('', file=open(SMTTRNFile, 'a'))

    for v in range(len(TxtFilesA)):
        dCheck = 0
        tCheck = 0
        CurrDCATWt = {}
        CurrOCAT = {}
        open(MTTFiles[v], 'w')
        open(WRDFiles[v], 'w')
        open(SMTFiles[v], 'w')
        open(TTRFiles[v], 'w')
        open(PLTFiles[v], 'w')
        print('Word,Turn,Speaker', end=',', file=open(WRDFiles[v], 'a'))
        for cat in DCATS:
            print(cat, end=',', file=open(WRDFiles[v], 'a'))
        for cat in OCATS:
            print(cat, end=',', file=open(WRDFiles[v], 'a'))
        for i in range(len(TDics)):
            if TDics[i] in UseDics:
                print(rDics[i], end=',', file=open(WRDFiles[v], 'a'))
        print('', file=open(WRDFiles[v], 'a'))
        print('Word', end=',', file=open(SMTFiles[v], 'a'))
        for idx in Speakers[v]:
            for j in range(len(rDics)):
                Head = rDics[j] + ' S' + str(idx)
                print(Head, end=',', file=open(SMTFiles[v], 'a'))
        print('', file=open(SMTFiles[v], 'a'))
        cat = ''
        inst = ''
        LDAT = GLnDAT[v]
        PDAT = []
        for i in range(len(LDAT)):  # Step 1 correct for 'categories into densities'
            if LDAT[i][0] == 'T':
                cat = LDAT[i][1]
                inst = LDAT[i][2]
                if cat in DCATS:
                    LDAT[i][0] = 'D'
                    Wt = DCATSDic[cat][inst]
                    LDAT[i].append(Wt)
        TurnN = 0
        Spkr = 0
        for i in range(len(LDAT)):  # Step 2 change C to S or H; change S to H
            if LDAT[i][0] == 'T':
                tCheck += 1
            elif LDAT[i][0] == 'D':
                dCheck += 1
            elif LDAT[i][0] == 'O':
                Spkr = LDAT[i][2]
                TurnN += 1
            elif LDAT[i][0] == 'S' and LDAT[i][1] != Spkr:
                Spkr = LDAT[i][1]
                tCheck = 0
                dCheck = 0
                TurnN += 1
            elif LDAT[i][0] == 'S' and TurnN == 0:
                TurnN += 1
            elif LDAT[i][0] == 'S' and LDAT[i][1] == Spkr and TurnN > 0:
                if dCheck > 0 and tCheck > 0:
                    dCheck = 0
                    tCheck = 0
                elif dCheck == 0 and tCheck > 0:
                    tCheck = 0
                elif dCheck == 0 and tCheck == 0:
                    print('Unaccountable error1, Same Spkr:', 'file ', TxtFiles1[v], ': ', LDAT[i])
                elif dCheck > 0 and tCheck == 0:
                    LDAT[i][0] = 'H'
                    dCheck = 0
                TurnN += 1
            elif LDAT[i][0] == 'C' and LDAT[i][1] == Spkr:
                if dCheck > 0 and tCheck > 0:
                    LDAT[i][0] = 'S'
                    dCheck = 0
                    tCheck = 0
                elif dCheck == 0 and tCheck > 0:
                    LDAT[i][0] = 'S'
                    tCheck = 0
                elif dCheck > 0 and tCheck == 0:
                    LDAT[i][0] = 'H'
                    dCheck = 0
        TurnN = 0
        Spkr = 0
        for i in range(len(LDAT)):
            # Step 3 where appropriate, look forward, add words and change forward to Y; change S to P or X
            if LDAT[i][0] == 'S' and LDAT[i][1] != Spkr:
                Spkr = LDAT[i][1]
                Words = LDAT[i][2]
                for j in range(i + 1, len(LDAT)):
                    if LDAT[j][0] == 'T' or LDAT[j][0] == 'D' or LDAT[j][0] == 'O':
                        break
                    elif LDAT[j][0] == 'S' and LDAT[j][1] != Spkr:
                        break
                    elif LDAT[j][0] == 'C' and LDAT[j][1] == Spkr:
                        Words = Words + ' ' + str(LDAT[j][2])
                        LDAT[j][0] = 'Y'
                    elif LDAT[j][0] == 'S' and LDAT[j][1] == Spkr:
                        Words = Words + ' ' + str(LDAT[j][2])

                        LDAT[j][0] = 'Y'
                LDAT[i][2] = Words
            elif LDAT[i][0] == 'H' and LDAT[i][1] != Spkr:
                Spkr = LDAT[i][1]
                Words = LDAT[i][2]
                for j in range(i + 1, len(LDAT)):
                    if LDAT[j][0] == 'T' or LDAT[j][0] == 'D' or LDAT[j][0] == 'O':
                        break
                    elif LDAT[j][1] != Spkr:
                        break
                    elif LDAT[j][0] == 'C' and LDAT[j][1] == Spkr:
                        Words = Words + ' ' + str(LDAT[j][2])
                        LDAT[j][0] = 'Y'
                    elif LDAT[j][0] == 'S' and LDAT[j][1] == Spkr:
                        Words = Words + ' ' + str(LDAT[j][2])
                        LDAT[j][0] = 'Y'
                LDAT[i][2] = Words
            elif LDAT[i][0] == 'O':
                for j in range(i + 1, len(LDAT)):
                    if LDAT[j][0] == 'T' or LDAT[j][0] == 'D' or LDAT[j][0] == 'O':
                        break
                    elif LDAT[j][1] != Spkr:
                        break
                    elif LDAT[j][0] == 'C' and LDAT[j][1] == Spkr:
                        Words = Words + ' ' + str(LDAT[j][2])
                        LDAT[j][0] = 'Y'
                    elif LDAT[j][0] == 'S' and LDAT[j][1] == Spkr:
                        Words = Words + ' ' + str(LDAT[j][2])
                        LDAT[j][0] = 'Y'
                LDAT[i][2] = Words
            elif LDAT[i][0] == 'P' or LDAT[i][0] == 'X':
                for j in range(i + 1, len(LDAT)):
                    if LDAT[j][0] == 'T' or LDAT[j][0] == 'D' or LDAT[j][0] == 'O':
                        break
                    elif LDAT[j][1] != Spkr:
                        break
                    elif LDAT[j][0] == 'C' and LDAT[j][1] == Spkr:
                        Words = Words + ' ' + str(LDAT[j][2])
                        LDAT[j][0] = 'Y'
                    elif LDAT[j][0] == 'S' and LDAT[j][1] == Spkr:
                        Words = Words + ' ' + str(LDAT[j][2])
                        LDAT[j][0] = 'Y'
                LDAT[i][2] = Words

        for i in range(len(LDAT)):  # Step 4

            if LDAT[i][0] == 'S':
                Spkr = LDAT[i][1]
                DCheck = 0
                for j in range(i + 1, len(LDAT)):
                    if LDAT[j][0] == 'T' or LDAT[j][0] == 'S' or LDAT[j][0] == 'O':
                        break
                    elif LDAT[j][0] == 'D':
                        DCheck += 1
                if DCheck == 0:
                    Count = wordcount(LDAT[i][2])
                    if Count[0] > 0:
                        print('Unaccountable error2 at: \n', 'file', TxtFiles1[v], ': ', LDAT[i][2])
                    elif Count[0] == 0:
                        if Count[1] <= 2:
                            small = smallturns(Count[1], Count[2])
                            if small == 'P':
                                LDAT[i][0] = 'P'
                            elif small == 'X':
                                LDAT[i][0] = 'X'
        WordN = 0
        sx = {}
        sp = {}
        CurrentSpkr = 0
        CurrentTurn = 0
        TurnStor = ''
        TurnSw = 0
        GWordN = 0
        for i in range(len(LDAT)):  # step 5
            if LDAT[i][0] == 'S' or LDAT[i][0] == 'H':
                Spkr = LDAT[i][1]
                Words = LDAT[i][2]
                for j in range(i + 1, len(LDAT)):
                    if LDAT[j][0] == 'T' or LDAT[j][0] == 'O':
                        break
                    elif LDAT[j][0] == 'S' and LDAT[j][1] != Spkr:
                        break
                    elif LDAT[j][0] == 'H':
                        break
                    elif LDAT[j][0] == 'D':
                        break
                    elif LDAT[j][0] == 'X':
                        Words = Words + ' (' + str(LDAT[j][0]) + ' ' + str(LDAT[j][2]) + ')'
                        if LDAT[j][1] in sx:
                            sx[LDAT[j][1]] += 1
                        else:
                            sx[LDAT[j][1]] = 1
                    elif LDAT[j][0] == 'P':
                        Words = Words + ' (' + str(LDAT[j][0]) + ' ' + str(LDAT[j][2]) + ')'
                        if LDAT[j][1] in sp:
                            sp[LDAT[j][1]] += 1
                        else:
                            sp[LDAT[j][1]] = 1
                    elif LDAT[j][0] == 'S' and LDAT[j][1] == Spkr:
                        Words = Words + ' ' + LDAT[j][2]
                        LDAT[j][0] = 'Y'
                    elif LDAT[j][0] == 'C' and LDAT[j][1] == Spkr:
                        Words = Words + ' ' + LDAT[j][2]
                        LDAT[j][0] = 'Y'
                LDAT[i][2] = Words
        for i in range(len(LDAT)):
            if LDAT[i][0] == 'D' or LDAT[i][0] == 'T':
                PDAT.append(LDAT[i])
            elif LDAT[i][0] == 'S' or LDAT[i][0] == 'H':
                PWords = LDAT[i][2]
                for j in range(i + 1, len(LDAT)):
                    if LDAT[j][0] == 'T' or LDAT[j][0] == 'L':
                        break
                    elif LDAT[j][0] == 'Y' and LDAT[j][1] == LDAT[i][1]:
                        PWords = PWords + ' ' + LDAT[j][2]
                    elif LDAT[j][0] == 'W':
                        continue
                    else:
                        break
                PDAT.append(LDAT[i])
        WordCt = 0
        TurnN = 0
        FWords = 0
        for i in range(len(LDAT)):
            if LDAT[i][0] == 'F' and LDAT[i][1] != '\n':
                if FWords == 0:
                    print('\n', LDAT[i][1], file=open(MTTFile, 'a'))
                    print('\n', LDAT[i][1], file=open(MTTFiles[v], 'a'))
                    FWords += 1
                else:
                    print(LDAT[i][1], file=open(MTTFile, 'a'))
                    print(LDAT[i][1], file=open(MTTFiles[v], 'a'))
            elif LDAT[i][0] == 'T':
                print('\n\\T ', LDAT[i][1], ':', LDAT[i][2], file=open(MTTFile, 'a'))
                print('\n\\T ', LDAT[i][1], ':', LDAT[i][2], file=open(MTTFiles[v], 'a'))
            elif LDAT[i][0] == 'D' and TurnN == 0:
                print('\n\\D ' + str(LDAT[i][1]) + ':' + str(LDAT[i][2]) + ':' + str(LDAT[i][3]),
                      file=open(MTTFile, 'a'))
                print('\n\\D ' + str(LDAT[i][1]) + ':' + str(LDAT[i][2]) + ':' + str(LDAT[i][3]),
                      file=open(MTTFiles[v], 'a'))
                print(LDAT[i], file=open(MTTFiles[v], 'a'))
            elif LDAT[i][0] == 'D' and TurnN > 0:
                print('(' + str(LDAT[i][1]) + ':' + str(LDAT[i][2]) + ':' + str(LDAT[i][3]) + ')', end=',',
                      file=open(MTTFile, 'a'))
                print('(' + str(LDAT[i][1]) + ':' + str(LDAT[i][2]) + ':' + str(LDAT[i][3]) + ')', end=',',
                      file=open(MTTFiles[v], 'a'))
            elif LDAT[i][0] == 'S':
                TurnN += 1
                Old = [LDAT[i][2], WordCt]
                New = mttwords(Old)
                WordCt = New[2]
                TurnMark = '[Turn ' + str(TurnN) + ']'
                LDAT[i].append(TurnN)
                print('\n\n>s ', LDAT[i][1], TurnMark, New[1], end=' ', file=open(MTTFile, 'a'))
                print('\n\n>s ', LDAT[i][1], TurnMark, New[1], end=' ', file=open(MTTFiles[v], 'a'))
            elif LDAT[i][0] == 'C':
                print('Strange Error: Files = ', TxtFilesA[v], ' LDAT[i] = ', LDAT[i])
            elif LDAT[i][0] == 'H':
                Old = [LDAT[i][2], WordCt]
                New = mttwords(Old)
                WordCt = New[2]
                LDAT[i].append(TurnN)
                print(New[1], end=' ', file=open(MTTFile, 'a'))
                print(New[1], end=' ', file=open(MTTFiles[v], 'a'))
            elif LDAT[i][0] == 'L':
                print('\n>c9', file=open(MTTFile, 'a'))
                print('\n>c9', file=open(MTTFiles[v], 'a'))
        print('\n\nThe total number of words in file', TxtFiles1[v], 'is', WordCt, file=open(MTTFile, 'a'))
        print('\n\nThe total number of words in file', TxtFiles1[v], 'is', WordCt, file=open(MTTFiles[v], 'a'))
        for Spkr in sp:
            print('\nThe number of positive NTVs by Speaker', Spkr, 'is', sp[Spkr], file=open(MTTFile, 'a'))
            print('\nThe number of positive NTVs by Speaker', Spkr, 'is', sp[Spkr], file=open(MTTFiles[v], 'a'))
        for Spkr in sx:
            print('\nThe number of neutral NTVs by Speaker', Spkr, 'is', sx[Spkr], file=open(MTTFile, 'a'))
            print('\nThe number of neutral NTVs by Speaker', Spkr, 'is', sx[Spkr], file=open(MTTFiles[v], 'a'))

        for i in range(len(PDAT)):  # Close up blank lines and 'C' lines; fix 'Y' lines, and apply wordcound
            if PDAT[i][0] == 'S' or PDAT[i][0] == 'O' or PDAT[i][0] == 'H':
                PWords = wordcount(PDAT[i][2])
                if PWords[0] > 0:
                    print('Unaccountable Error in Processing Text: ', 'file ', TxtFiles1[v], ': ', PDAT[i])
                else:
                    PDAT[i].append(PWords[1])
                    PDAT[i].append(PWords[2])
        TDATA = []
        CompWord = []
        TTList = []
        for i in range(1, len(Speakers[v]) + 1):
            STTList = {}
            LSTTList = []
            for j in range(len(PDAT)):
                if PDAT[j][0] == 'S' or PDAT[j][0] == 'H' or PDAT[j][0] == 'O' and PDAT[j][1] == i:
                    Words = re.split('\s', PDAT[j][5])
                    for word in Words:
                        if word in STTList:
                            STTList[word] += 1
                        else:
                            STTList[word] = 1
            print('\nSpeaker = ', i, '\n', file=open(TTRFiles[v], 'a'))
            for word in STTList:
                ListItem = (word, STTList[word])
                LSTTList.append(ListItem)
            LSTTList = sorted(LSTTList, key=itemgetter(0))
            TTList.append(LSTTList)
            Types = len(LSTTList)
            Tokens = 0
            TTR = 0
            for j in range(len(LSTTList)):
                print(LSTTList[j][0], ',', LSTTList[j][1], file=open(TTRFiles[v], 'a'))
                Tokens += LSTTList[j][1]
            if Tokens > 0:
                TTR = Types / Tokens
            print('Types = ', Types, '; ', 'Tokens = ', Tokens, '; Ratio = ', TTR, file=open(TTRFiles[v], 'a'))
            if len(TTGList) < i:
                TTGList.append(LSTTList)
            else:
                TTGList[i - 1] = TTGList[i - 1] + LSTTList
        CurrDCATWts = {}
        for i in range(len(PDAT)):  # Here we make the TDATA (TurnDATA) file
            if PDAT[i][0] == 'T':
                CurrOCAT[PDAT[i][1]] = PDAT[i][2]
            elif PDAT[i][0] == 'D':
                CurrDCATWts[PDAT[i][1]] = PDAT[i][3]

            elif PDAT[i][0] == 'S' or PDAT[i][0] == 'H' or PDAT[i][0] == 'O':
                preTT = []
                WordN = PDAT[i][4]
                CurrSpkr = PDAT[i][1]
                CurrTurn = PDAT[i][3]
                PreWdBank = PDAT[i][5]
                TurnWords = re.split('\s', PreWdBank)

                for j in range(len(TurnWords)):
                    WdFileData = [TurnWords[j], CurrTurn, CurrSpkr]
                    for k in range(len(DCATS)):
                        WdFileData.append(CurrDCATWts[DCATS[k]])
                    for cat in OCATS:
                        WdFileData.append(CurrOCAT[cat])
                    TDATA.append(WdFileData)

            elif PDAT[i][0] == 'L':
                break
        CompWord.append('zero')
        for q in range(len(TDATA)):
            CompWord.append(TDATA[q][0])
        for i in range(len(TDATA)):
            DicWts = []
            CWord = CompWord[i] + '$'
            if re.match(CWord, TDATA[i][0]) is None:
                if TDATA[i][0] in BigDic:
                    DicWts = BigDic[TDATA[i][0]]
                else:
                    for j in range(len(UseDics) - WDicsN):
                        DicWts.append(0)
                    for j in range(len(UseDics) - WDicsN, len(UseDics)):
                        DicWts.append(.5)
            else:
                if TDATA[i][0] in BigDic and len(BigDic[TDATA[i][0]]) > 1:
                    for j in range(len(UseDics)):
                        if j == DFDic:
                            DicWts.append(1)
                        elif j != DFDic:
                            DicWts.append(BigDic[TDATA[i][0]][j])
                elif TDATA[i][0] in BigDic and len(BigDic[TDATA[i][0]]) == 1:
                    if DFDic == 0:
                        DicWts.append(1)
                    else:
                        DicWts = BigDic[TDATA[i][0]]
                elif TDATA[i][0] not in BigDic:
                    for j in range(len(UseDics) - WDicsN):
                        if j != DFDic:
                            DicWts.append(0)
                        else:
                            DicWts.append(1)
                    for j in range(WDicsN):
                        DicWts.append(.5)
            if re.search('\w+-$', TDATA[i][0]) is not None:
                Weights = []
                if DFDic > -1:
                    for j in range(len(UseDics) - WDicsN):
                        if j != DFDic:
                            Weights.append(0)
                        else:
                            Weights.append(1)
                    for j in range(len(UseDics) - WDicsN, len(UseDics)):
                        Weights.append(.5)
                else:
                    for j in range(len(UseDics) - WDicsN):
                        Weights.append(0)
                    for j in range(len(UseDics) - WDicsN, len(UseDics)):
                        Weights.append(.5)
                DicWts = Weights
            for j in range(len(DicWts)):
                TDATA[i].append(DicWts[j])
        for i in range(len(TDATA)):
            for j in range(len(TDATA[i])):
                print(TDATA[i][j], end=',', file=open(WRDFiles[v], 'a'))
            print('', file=open(WRDFiles[v], 'a'))
        ODicsN = len(rDics) - len(rWtDics)
        AG1Dems = []
        AG12Rows = []
        AG2Dems = []
        TD = pd.read_csv(WRDFiles[v])
        Turns = TD.loc[:, 'Turn']
        npTurns = np.array(Turns)
        TurnMax = np.max(Turns)
        WordN = len(Turns)
        TurnL = []
        WdCt = []
        SpkrTurns = []
        for k in range(1, int(TurnMax) + 1):
            AG1Dem = []  # [Spkr, Cats]
            AG2Dem = []
            AG12Row = []  # [Words, DFMat, WRADMat, WRADPosM, WRADTot, WRADTotH, WRRLMat, ...
            T0TD = TD['Turn']
            T1TD = T0TD == k
            T2TD = TD[T1TD]
            WC = sum(T1TD)
            WdCt.append(WC)
            Spkr = T2TD.iloc[0, 2]
            AG1Dem.append(Spkr)
            AG2Dem.append(Spkr)
            SpkrTurns.append(Spkr)
            print(TxtFiles1[v], k, Spkr, WC, sep=',', end=',', file=open(WRDTRNFile, 'a'))
            for cat in OCATS:
                List = T2TD.loc[:, cat]
                print(List.iloc[0], end=',', file=open(WRDTRNFile, 'a'))
                if cat in ACATS:
                    AG1Dem.append(List.iloc[0])
                    AG2Dem.append(',')
                else:
                    AG2Dem.append(List.iloc[0])
                    AG1Dem.append(List.iloc[0])
            AG12Row.append(WC)
            for dic in rDics:
                TDdic = T2TD.loc[:, dic]
                npdic = np.array(TDdic)
                Match = 0
                Cover = 0
                Odds = 0

                if dic not in rWtDics:
                    npTDdic = np.array(TDdic)
                    Match = np.sum(npTDdic)
                    if WC > 0:
                        Cover = Match / WC
                    if WC - Match > 0:
                        Odds = Match / (WC - Match)
                    print(Match, Cover, Odds, sep=',', end=',', file=open(WRDTRNFile, 'a'))
                    Addition = [Match]
                    AG12Row = AG12Row + Addition
                else:
                    Mat = TDdic != .5
                    npMat = np.array(TDdic[Mat])
                    Match = len(npMat)
                    if WC > 0:
                        Cover = float(Match) / float(WC)
                    PMat = TDdic > .5
                    PMatL = np.array(TDdic[PMat])
                    PMatch = len(PMatL)
                    PosP = 0
                    if Match > 0:
                        PosP = PMatch / Match
                    print(Match, Cover, PMatch, PosP, sep=',', end=',', file=open(WRDTRNFile, 'a'))
                    Addit = [Match, PMatch]
                    AG12Row = AG12Row + Addit
            print('', file=open(WRDTRNFile, 'a'))
            AG12Rows.append(AG12Row)
            AG1Dems.append(AG1Dem)
            AG2Dems.append(AG2Dem)
        for k in range(1, max(SpkrTurns) + 1):
            TurnWords = []
            S0TD = TD['Speaker']
            S1TD = S0TD == k
            S2TD = TD[S1TD]
            Words = sum(S1TD)
            for m in range(len(SpkrTurns)):
                if SpkrTurns[m] == k:
                    TurnWords.append(WdCt[m])
            SWC = sum(S1TD)
            print(TxtFiles1[v], k, sum(S1TD), len(TurnWords), sep=',', end=',', file=open(WRDAG0File, 'a'))
            Fstq = firstquartile(TurnWords)
            if len(TurnWords) > 3:
                Med = statistics.median(TurnWords)
            else:
                Med = 'NA'
            Thrdq = thirdquartile(TurnWords)
            SD = statistics.pstdev(TurnWords)
            print(min(TurnWords), Fstq, Med, Thrdq, max(TurnWords), statistics.mean(TurnWords), SD, sep=',', end=',',
                  file=open(WRDAG0File, 'a'))

            for dic in rDics:
                STDdic = S2TD.loc[:, dic]
                npdic = np.array(STDdic)
                Match = 0
                Cover = 0
                Odds = 0
                PosP = 0
                if dic not in rWtDics:
                    Match = np.sum(npdic)
                    if SWC > 0:
                        Cover = Match / SWC
                    if SWC - Match > 0:
                        Odds = Match / (SWC - Match)
                    print(Match, Cover, Odds, sep=',', end=',', file=open(WRDAG0File, 'a'))
                else:
                    Mat = STDdic != .5
                    npMat = np.array(STDdic[Mat])
                    Match = len(npMat)
                    if SWC > 0:
                        Cover = Match / SWC
                    PMat = STDdic > .5
                    npPMat = np.array(STDdic[PMat])
                    PMatch = len(npPMat)
                    if Match > 0:
                        PosP = PMatch / Match
                    print(Match, Cover, PMatch, PosP, sep=',', end=',', file=open(WRDAG0File, 'a'))
            print('', file=open(WRDAG0File, 'a'))
        Used = []
        for k in range(len(AG12Rows)):
            if k not in Used:
                Dem = AG1Dems[k]
                Dat = np.array(AG12Rows[k])
                Words = Dat[0]
                Turns = 1
                for m in range(k + 1, len(AG12Rows)):
                    if m not in Used:
                        if AG1Dems[m] == AG1Dems[k]:
                            Turns += 1
                            Dat = Dat + np.array(AG12Rows[m])
                            Words = Dat[0]
                            Used.append(m)
                Used.append(k)
                print(TxtFiles1[v], Dem[0], sep=',', end=',', file=open(WRDAG1File, 'a'))
                for r in range(len(OCATS)):
                    print(Dem[1 + r], sep=',', end=',', file=open(WRDAG1File, 'a'))
                print(Words, Turns, sep=',', end=',', file=open(WRDAG1File, 'a'))
                for r in range(len(rDics)):
                    if rDics[r] not in rWtDics:
                        Mat = Dat[1 + r]
                        if Dat[0] > 0:
                            Cover = Mat / Dat[0]
                        else:
                            Cover = 0
                        if Dat[0] - Mat > 0:
                            Odds = Mat / (Dat[0] - Mat)
                        else:
                            Odds = 0
                        print(Mat, Cover, Odds, sep=',', end=',', file=open(WRDAG1File, 'a'))
                    else:
                        Mat = Dat[1 + ODicsN + (2 * (r - ODicsN))]
                        if Dat[0] > 0:
                            Cover = Mat / Dat[0]
                        else:
                            Cover = 0
                        PosMat = Dat[2 + ODicsN + (2 * (r - ODicsN))]
                        if Mat > 0:
                            PosP = PosMat / Mat
                        else:
                            PosP = 0
                        print(Mat, Cover, PosMat, PosP, sep=',', end=',', file=open(WRDAG1File, 'a'))
                print('', file=open(WRDAG1File, 'a'))
        Used = []
        for k in range(len(AG12Rows)):
            if k not in Used:
                Dem = AG2Dems[k]
                Dat = np.array(AG12Rows[k])
                Words = Dat[0]
                Turns = 1
                for m in range(k + 1, len(AG12Rows)):
                    if m not in Used:
                        if AG2Dems[m] == AG2Dems[k]:
                            Turns += 1
                            Dat = Dat + np.array(AG12Rows[m])
                            Words = Dat[0]
                            Used.append(m)
                Used.append(k)
                print(TxtFiles1[v], Dem[0], sep=',', end=',', file=open(WRDAG2File, 'a'))
                for r in range(len(OCATS)):
                    print(Dem[1 + r], sep=',', end=',', file=open(WRDAG2File, 'a'))
                print(Words, Turns, sep=',', end=',', file=open(WRDAG2File, 'a'))
                for r in range(len(rDics)):
                    if rDics[r] not in rWtDics:
                        Mat = Dat[1 + r]
                        if Dat[0] > 0:
                            Cover = Mat / Dat[0]
                        else:
                            Cover = 0
                        if Dat[0] - Mat > 0:
                            Odds = Mat / (Dat[0] - Mat)
                        else:
                            Odds = 0
                        print(Mat, Cover, Odds, sep=',', end=',', file=open(WRDAG2File, 'a'))
                    else:
                        Mat = Dat[1 + ODicsN + (2 * (r - ODicsN))]
                        if Dat[0] > 0:
                            Cover = Mat / Dat[0]
                        else:
                            Cover = 0
                        PosMat = Dat[2 + ODicsN + (2 * (r - ODicsN))]
                        if Mat > 0:
                            PosP = PosMat / Mat
                        else:
                            PosP = 0
                        print(Mat, Cover, PosMat, PosP, sep=',', end=',', file=open(WRDAG2File, 'a'))
                print('', file=open(WRDAG2File, 'a'))
        SMTDems1 = {}
        SMTDems2 = {}
        SMTVals = {}
        SMTVals2 = []
        T0TD = TD['Turn']
        for k in range(1, TurnN + 1):
            SMT2 = []
            SMTVals[k] = []
            SDicV = []
            T1TD = T0TD == k
            T2TD = TD[T1TD]
            L = len(T2TD.index)
            Spkr = T2TD.iloc[0, 2]
            GSDicV = [Spkr]
            SMTDems1[k] = [Spkr]
            SMTDems2[k] = [Spkr]
            print(TxtFiles1[v], k, Spkr, L, sep=',', end=',', file=open(SMTTRNFile, 'a'))
            for m in range(len(OCATS)):
                print(T2TD.iloc[0, 3 + m], end=',', file=open(SMTTRNFile, 'a'))
                GSDicV.append(T2TD.iloc[0, 3 + m])
                SMTDems1[k].append(T2TD.iloc[0, 3 + m])
                if OCATS[m] in ACATS:
                    SMTDems2[k].append(',')
                else:
                    SMTDems2[k].append(T2TD.iloc[0, 3 + m])
            for rDic in rDics:
                TRNVals = []
                T3TD = T2TD.loc[:, rDic]
                npT3D = np.array(T3TD)
                TnpT3D = npT3D.transpose()
                STnpT3D = smth(TnpT3D)
                TRNVals.append(STnpT3D)
                SMTVals[k].append(STnpT3D)
                SMT2.append(STnpT3D)
                SDicV.append(STnpT3D)
                GSDicV.append(STnpT3D)
                npSDicV = np.array(SDicV)
                if rDic not in rWtDics:
                    print(statistics.mean(STnpT3D), statistics.pstdev(STnpT3D), sep=',', end=',',
                          file=open(SMTTRNFile, 'a'))
                else:
                    print(np.mean(STnpT3D), statistics.pstdev(STnpT3D), sep=',', end=',', file=open(SMTTRNFile, 'a'))
                    TotHigh = 0
                    HighN = 0
                    Tot = 0
                    MHigh = 0
                    HighP = 0
                    for t in range(len(STnpT3D)):
                        Tot += STnpT3D[t]
                        if STnpT3D[t] > .5:
                            HighN += 1
                            TotHigh += STnpT3D[t]
                    if len(STnpT3D) > 0:
                        HighP = HighN / len(STnpT3D)
                    if HighN > 0:
                        MHigh = (TotHigh - (.5 * HighN)) / HighN
                    print(MHigh, HighP, sep=',', end=',', file=open(SMTTRNFile, 'a'))
            TnpSDicV = npSDicV.transpose()
            SMTVals[k] = SDicV
            SMTVals2.append(SMT2)
            for m in range(L):
                Word = T2TD.iloc[m, 0]
                print(Word, end=',', file=open(SMTFiles[v], 'a'))
                if Spkr > 1:
                    for r in range((Spkr - 1) * len(rDics)):
                        print(',', end='', file=open(SMTFiles[v], 'a'))
                for q in range(len(TnpSDicV[m])):
                    print(TnpSDicV[m][q], end=',', file=open(SMTFiles[v], 'a'))
                print('', file=open(SMTFiles[v], 'a'))

            for m in range(len(npSDicV)):
                for r in range(m + 1, len(npSDicV)):
                    print(covar(npSDicV[m], npSDicV[r]), end=',', file=open(SMTTRNFile, 'a'))
            print('', file=open(SMTTRNFile, 'a'))
        SMTVals0 = {}
        for k in range(1, max(SpkrTurns) + 1):
            LinDic = {}
            Words = 0
            Turns = 0
            SMTVals0[k] = []
            print(TxtFiles1[v], k, sep=',', end=',', file=open(SMTAG0File, 'a'))
            if k == 1:
                print(TxtFiles1[v], end=',', file=open(SMTAG01File, 'a'))
            elif k == 2:
                print(TxtFiles1[v], end=',', file=open(SMTAG02File, 'a'))
            for m in range(1, TurnN + 1):
                if SMTDems1[m][0] == k:
                    Turns += 1
                    Words += len(SMTVals[m][0])
                    if len(SMTVals0[k]) > 0:
                        for r in range(len(rDics)):
                            SMTVals0[k][r] = SMTVals0[k][r] + SMTVals[m][r]
                    else:
                        for r in range(len(rDics)):
                            SMTVals0[k].append(SMTVals[m][r])
            print(Words, Turns, sep=',', end=',', file=open(SMTAG0File, 'a'))
            if k == 1:
                print(Words, Turns, sep=',', end=',', file=open(SMTAG01File, 'a'))
            elif k == 2:
                print(Words, Turns, sep=',', end=',', file=open(SMTAG02File, 'a'))
            if len(SMTVals0[k]) > 0:
                for r in range(len(rDics)):
                    Mean = statistics.mean(SMTVals0[k][r])
                    if rDics[r] not in rWtDics:
                        print(Mean, end=',', file=open(SMTAG0File, 'a'))
                        if k == 1:
                            print(Mean, end=',', file=open(SMTAG01File, 'a'))
                        elif k == 2:
                            print(Mean, end=',', file=open(SMTAG02File, 'a'))
                    else:
                        Vals = SMTVals0[k][r]
                        TotHigh = 0
                        HighN = 0
                        Tot = 0
                        MHigh = 0
                        HighP = 0
                        for t in range(len(Vals)):
                            Tot += Vals[t]
                            if Vals[t] > .5:
                                HighN += 1
                                TotHigh += Vals[t]
                        if len(Vals) > 0:
                            HighP = HighN / len(Vals)
                        if HighN > 0:
                            MHigh = (TotHigh - (.5 * HighN)) / HighN
                        print(Mean, MHigh, HighP, sep=',', end=',', file=open(SMTAG0File, 'a'))
                        if k == 1:
                            print(Mean, MHigh, HighP, sep=',', end=',', file=open(SMTAG01File, 'a'))
                        elif k == 2:
                            print(Mean, MHigh, HighP, sep=',', end=',', file=open(SMTAG02File, 'a'))
                for p in range(len(SMTVals0[k])):
                    for q in range(p + 1, len(SMTVals0[k])):
                        print(covar(SMTVals0[k][p], SMTVals0[k][q]), end=',', file=open(SMTAG0File, 'a'))
                        if k == 1:
                            print(covar(SMTVals0[k][p], SMTVals0[k][q]), end=',', file=open(SMTAG01File, 'a'))
                        elif k == 2:
                            print(covar(SMTVals0[k][p], SMTVals0[k][q]), end=',', file=open(SMTAG02File, 'a'))
            print('', file=open(SMTAG0File, 'a'))
            if k == 1:
                print('', file=open(SMTAG01File, 'a'))
            elif k == 2:
                print('', file=open(SMTAG02File, 'a'))

        Used1 = []
        DEM = []
        DAT1 = []
        SMTVals1 = SMTVals
        for k in range(1, TurnN + 1):
            if k not in Used1:
                DEM = SMTDems1[k]
                DAT1 = SMTVals1[k]
                WordN = 0
                TurnNo = 1
                for m in range(k + 1, TurnN + 1):
                    if m not in Used1 and SMTDems1[m] == SMTDems1[k]:
                        Used1.append(m)
                        TurnNo += 1
                        for r in range(len(rDics)):
                            DAT1[r] = DAT1[r] + SMTVals1[m][r]
                Used1.append(k)
                WordN = len(DAT1[0])
                print(TxtFiles1[v], DEM[0], sep=',', end=',', file=open(SMTAG1File, 'a'))
                for q in range(len(OCATS)):
                    print(DEM[1 + q], end=',', file=open(SMTAG1File, 'a'))
                print(WordN, TurnNo, sep=',', end=',', file=open(SMTAG1File, 'a'))
                for r in range(len(rDics)):
                    print(statistics.mean(DAT1[r]), end=',', file=open(SMTAG1File, 'a'))
                    if rDics[r] in rWtDics:
                        TotHigh = 0
                        HighN = 0
                        Tot = 0
                        MHigh = 0
                        HighP = 0
                        for t in range(len(DAT1[r])):
                            Tot += DAT1[r][t]
                            if DAT1[r][t] > .5:
                                HighN += 1
                                TotHigh += DAT1[r][t]
                        if len(DAT1[r]) > 0:
                            HighP = HighN / len(DAT1[r])
                        if HighN > 0:
                            MHigh = (TotHigh - (.5 * HighN)) / HighN
                        print(MHigh, HighP, sep=',', end=',', file=open(SMTAG1File, 'a'))
                for r in range(len(rDics)):
                    for q in range(r + 1, len(rDics)):
                        print(covar(DAT1[r], DAT1[q]), end=',', file=open(SMTAG1File, 'a'))
                print('', file=open(SMTAG1File, 'a'))
        Used2 = []
        DEM = []
        for k in range(1, TurnN + 1):
            if k not in Used2:
                DEM = SMTDems2[k]
                DAT2 = SMTVals2[k - 1]
                WordN = 0
                TurnNo = 1
                for m in range(k + 1, TurnN + 1):
                    if m not in Used2 and SMTDems2[m] == SMTDems2[k]:
                        Used2.append(m)
                        TurnNo += 1
                        for r in range(len(rDics)):
                            DAT2[r] = DAT2[r] + SMTVals2[m - 1][r]
                Used2.append(k)
                WordN = len(DAT2[0])
                print(TxtFiles1[v], DEM[0], sep=',', end=',', file=open(SMTAG2File, 'a'))
                for q in range(len(OCATS)):
                    print(DEM[1 + q], end=',', file=open(SMTAG2File, 'a'))
                print(WordN, TurnNo, sep=',', end=',', file=open(SMTAG2File, 'a'))
                for r in range(len(rDics)):
                    print(statistics.mean(DAT2[r]), end=',', file=open(SMTAG2File, 'a'))
                    if rDics[r] in rWtDics:
                        TotHigh = 0
                        HighN = 0
                        Tot = 0
                        MHigh = 0
                        HighP = 0
                        for t in range(len(DAT2[r])):
                            Tot += DAT2[r][t]
                            if DAT2[r][t] > .5:
                                HighN += 1
                                TotHigh += DAT2[r][t]
                        if len(DAT2[r]) > 0:
                            HighP = HighN / len(DAT2[r])
                        if HighN > 0:
                            MHigh = (TotHigh - (.5 * HighN)) / HighN
                        print(MHigh, HighP, sep=',', end=',', file=open(SMTAG2File, 'a'))
                for r in range(len(rDics)):
                    for q in range(r + 1, len(rDics)):
                        print(covar(DAT2[r], DAT2[q]), end=',', file=open(SMTAG2File, 'a'))
                print('', file=open(SMTAG2File, 'a'))

        STD = pd.read_csv(SMTFiles[v])
        colors = []
        NameFiles1 = []
        NameFiles2 = []
        for dic in rDics:
            if dic == 'DF':
                color = 'grey'
                colors.append(color)
            elif dic == 'WRAD':
                color = 'green'
                colors.append(color)
            elif dic == 'WRRL':
                color = 'blue'
                colors.append(color)
            elif dic == 'SenS':
                color = 'red'
                colors.append(color)
            elif dic == 'NEG':
                color = 'black'
                colors.append(color)
            else:
                if 'magenta' not in colors:
                    color = 'magenta'
                    colors.append(color)
                elif 'magenta' in colors and 'cyan' not in colors:
                    color = 'cyan'
                    colors.append(color)
                else:
                    color = 'yellow'
                    colors.append(color)
            NameFile1 = dic + ' S1'
            if len(Speakers[v]) > 1:
                NameFile2 = dic + ' S2'
            NameFiles1.append(NameFile1)
            if len(Speakers[v]) > 1:
                NameFiles2.append(NameFile2)
        plt.title(TxtFiles1[v])
        for k in range(len(NameFiles1)):

            plt.subplot(len(NameFiles1), 1, k + 1)
            plt.plot(STD.loc[:, NameFiles1[k]], c=colors[k], alpha=1, lw=1.5, label=NameFiles1[k])
            if len(Speakers[v]) > 1:
                plt.plot(STD.loc[:, NameFiles2[k]], c=colors[k], alpha=.4, lw=1.5, label=NameFiles2[k])
            plt.ylabel(rDics[k])
            plt.grid(True)

        plt.savefig(fname=PLTFiles[v])
        plt.clf()

    for v in TxtFilesA:
        os.remove(v)
    AG00 = pd.read_csv(SMTAG0File, index_col=0)
    AG01 = pd.read_csv(SMTAG01File)
    AG02 = pd.read_csv(SMTAG02File)
    for i in range(len(TTGList)):
        TypeList = {}
        for pair in TTGList[i]:
            if pair[0] in TypeList:
                TypeList[pair[0]] += pair[1]
            else:
                TypeList[pair[0]] = pair[1]
        PairList = []
        for pair in TypeList:
            NewPair = (pair, TypeList[pair])
            PairList.append(NewPair)
        PairList = sorted(PairList, key=itemgetter(0))
        Toks = 0
        for type in TypeList:
            Toks += TypeList[type]
        Types = len(TypeList)
        print('These are the types and tokens for speaker ', i + 1, ' for the folder: ', Directory, '.', sep='',
              file=open(TTGFile, 'a'))
        print('The number of types is: ', Types, sep='', file=open(TTGFile, 'a'))
        print('The number of tokens is: ', Toks, sep='', file=open(TTGFile, 'a'))
        Rat = 0
        if Toks > 0:
            Rat = Types / Toks
        print('The Type-Token ratio is: ', Rat, sep='', file=open(TTGFile, 'a'))
        for pair in PairList:
            print(pair[0], pair[1], sep=' ', file=open(TTGFile, 'a'))
        if len(TxtFiles1) > 2:
            tick_val = []
            tick_lab = []
            for i in range(len(TxtFiles1)):
                tick_val.append(i)
                tick_lab.append(TxtFiles1[i])
            GSpkrs = 0
            for v in range(1, len(TxtFiles1)):
                if len(Speakers[v]) > GSpkrs:
                    GSpkrs = len(Speakers[v])
            GC = []
            for i in range(len(SMTAG0Columns1)):
                if SMTAG0Columns1[i] == 'Words':
                    GC.append('blue')
                elif SMTAG0Columns1[i] == 'DF Mean':
                    GC.append('grey')
                elif SMTAG0Columns1[i] == 'WRAD Mean':
                    GC.append('green')
                elif SMTAG0Columns1[i] == 'WRAD MHgh':
                    GC.append('green')
                elif SMTAG0Columns1[i] == 'WRAD HProp':
                    GC.append('green')
                elif SMTAG0Columns1[i] == 'WRRL Mean':
                    GC.append('magenta')
                elif SMTAG0Columns1[i] == 'WRRL MHgh':
                    GC.append('magenta')
                elif SMTAG0Columns1[i] == 'WRRL HProp':
                    GC.append('magenta')
                else:
                    GC.append('red')
            if GSpkrs == 1:
                for i in range(len(SMTAG0Columns1)):
                    Filename = 'GRAPHS/' + Directory + '.' + SMTAG0Columns1[i] + '.png'
                    open(Filename, 'w')
                    plt.plot(tick_val, AG01.loc[:, SMTAG0Columns1[i]], alpha=1, lw=1.5, color=GC[i],
                             label=SMTAG0Columns1[i])
                    plt.title(SMTAG0Columns1[i])
                    plt.xticks(tick_val, tick_lab)
                    plt.grid(axis='x', which='major')
                    plt.savefig(fname=Filename)
                    plt.clf()
            elif GSpkrs > 1:
                FileTurns = 'GRAPHS/' + Directory + '.Turns.png'
                open(FileTurns, 'w')
                plt.plot(AG01.loc[:, 'Turns'], alpha=1, lw=1.5, color='black', label='Turns')
                plt.title('Turns')
                plt.xticks(tick_val, tick_lab)
                plt.grid(axis='x', which='major')
                plt.savefig(fname=FileTurns)
                plt.clf()
                for i in range(len(SMTAG0Columns1)):
                    Filename = 'GRAPHS/' + Directory + '.' + SMTAG0Columns1[i] + '.png'
                    open(Filename, 'w')
                    plt.plot(AG01.loc[:, SMTAG0Columns1[i]], color=GC[i], alpha=1, lw=1.5, label=SMTAG0Columns1[i])
                    plt.plot(AG02.loc[:, SMTAG0Columns1[i]], color=GC[i], alpha=.4, lw=1.5, ls='dashed',
                             label=SMTAG0Columns1[i])
                    plt.title(SMTAG0Columns1[i])
                    plt.xticks(tick_val, tick_lab)
                    plt.grid(axis='x', which='major')
                    plt.savefig(fname=Filename)
                    plt.clf()
