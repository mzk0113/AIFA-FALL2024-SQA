Windows PowerShell
Copyright (C) Microsoft Corporation. All rights reserved.

Install the latest PowerShell for new features and improvements! https://aka.ms/PSWindows

PS C:\Users\snube> cd OneDrive
PS C:\Users\snube\OneDrive> cd Desktop
PS C:\Users\snube\OneDrive\Desktop> cd "Auburn University"
PS C:\Users\snube\OneDrive\Desktop\Auburn University> cd "COMP 5710 Software Quality Assurance"
cd : Cannot find path 'C:\Users\snube\OneDrive\Desktop\Auburn University\COMP 5710 Software Quality Assurance' because it does not exist.
At line:1 char:1
+ cd "COMP 5710 Software Quality Assurance"
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : ObjectNotFound: (C:\Users\snube\...ality Assurance:String) [Set-Location], ItemNotFoundException
    + FullyQualifiedErrorId : PathNotFound,Microsoft.PowerShell.Commands.SetLocationCommand

PS C:\Users\snube\OneDrive\Desktop\Auburn University> cd "Fall 2024"
PS C:\Users\snube\OneDrive\Desktop\Auburn University\Fall 2024> cd "COMP 5710 Software Quality Assurance"
PS C:\Users\snube\OneDrive\Desktop\Auburn University\Fall 2024\COMP 5710 Software Quality Assurance> cd PRoject
PS C:\Users\snube\OneDrive\Desktop\Auburn University\Fall 2024\COMP 5710 Software Quality Assurance\PRoject> ls


    Directory: C:\Users\snube\OneDrive\Desktop\Auburn University\Fall 2024\COMP 5710 Software Quality Assurance\PRoject


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----        11/29/2024  12:56 PM                MLForensics-farzana
-a----         12/2/2024  12:46 PM           1517 fuzz.py


PS C:\Users\snube\OneDrive\Desktop\Auburn University\Fall 2024\COMP 5710 Software Quality Assurance\PRoject> python fuzz.py
Processing input: yUXf$|{K,<
Processing input: DtA>=g\I^`
Processing input: {+cHdJh/^b
Processing input: i\RtPX#v[z
Processing input: V8uQ1ArWj1
Processing input: mhc'_=&uXX
Processing input: D:N'(8.^]e
Processing input: ~xf^0h!_.(
Processing input: u H~Fs$NV,
Processing input: &)x<]V,pln
Processing input: *'w"tQ5gQR
Processing input: K(-%9Ou{//
Processing input: )P}6||K@QT
Processing input: Iv(EOCQ*G5
Processing input: .[]/*g9G|l
Processing input: p+Ug?wuq\*
Processing input: x;_PF|/Qzt
Processing input: SD>K6Kz2h_
Processing input: =m]sneHqyE
Processing input: 8qjUjd[0Ou
Processing input: Iz5"R_fB=n
Processing input: CZhVUo*Y.Y
Processing input: U))<4j4PdA
Processing input: LV_)6gHcJ-
Processing input: VNZod/>5d\
Processing input: I2`%w+.mxr
Processing input: (IDf$Ha{jJ
Processing input: wf^2{)s,3X
Processing input: DW9`ZZ2X8a
Processing input: hDz+Nj_yA-
Processing input: m:wof0:?"$
Processing input: !TUh(% =Gq
Processing input: J]@/|{aU$H
Processing input: G3_f0!}#=0
Processing input: U>"L\)tG[(
Processing input: Vo8H\=b]'g
Processing input: *NqiB?~~\?
Processing input: x%f^[<ckjT
Processing input: E(T&v2I\X6
Processing input: LFxr7t.I6W
Processing input: =V[.~V_(X-
Processing input: lW9`3Br30F
Processing input: "`VP!K|kP;
Processing input: ohxFI%YQuS
Processing input: %8Zk>]h4~q
Processing input: sYl#K%3]R!
Processing input: +7vig2@6(G
Processing input: 2!kFW|$K(r
Processing input: ,"FS;!itKd
Processing input: mZ1HFw3%L'
Processing input: ?$k\6?e.Ji
Processing input: WEiDK0(z)
Processing input: 5J(M[D4_z}
Processing input: 3#s}Sk%dWv
Processing input: XXB>v2oSN2
Processing input: acfD&g2zVO
Processing input: Xh^(b KtN4
Processing input: C^/ujB^J28
Processing input: xf"i SgXxP
Processing input: +MTNl-;=7;
Processing input: LZ"T&\P'z!
Processing input: Q8x}p?.%nI
Processing input: )CgXe}|8+x
Processing input: raJfAoS)cX
Processing input: .ZE0xR;nVb
Processing input: Hxti!h*Wkm
Processing input: $+@9iMp6K0
Processing input: A=]o5#@D~D
Processing input: NPl2J+<=AT
Processing input: a'd*n/(P(.
Processing input: ^^1>L!V0Dr
Processing input: &7Pal4[62t
Processing input: S3Pe{.rEou
Processing input: [G7s6 kWL>
Processing input: tW7H,.]w/{
Processing input: 4p?`17NU!9
Processing input: rdN}f6"v-h
Processing input: yQjTm3)(6'
Processing input: /g0E-_'o0f
Processing input: dYj*YFX'Sm
Processing input: S"6YI#e!C|
Processing input: NQ]<4|`z{W
Processing input: E;$nXoP97+
Processing input: tilZ}m#]=5
Processing input: A2:ILkKr!3
Processing input: sk%%>8rOYw
Processing input: jViv:-CeWs
Processing input: /z9Fuk!2sq
Processing input: z<#^*XY>!t
Processing input: V[v6I^pxF!
Processing input: |!fyX$UHzs
Processing input: Knwt6dgQi!
Processing input: :1,nbv'$Kz
Processing input: =j-7.ljRiV
Processing input: [s%QsVeZv}
Processing input: zPUW5-5(0?
Processing input: b\_7q5eY&7
Processing input:  :%W`~I4e,
Processing input: #k6\(mxL.]
Processing input: EtOTSc&j{]
PS C:\Users\snube\OneDrive\Desktop\Auburn University\Fall 2024\COMP 5710 Software Quality Assurance\PRoject> python fuzz.py
PS C:\Users\snube\OneDrive\Desktop\Auburn University\Fall 2024\COMP 5710 Software Quality Assurance\PRoject> python fuzz.py
Fuzzing method_one...
Fuzzing method_two...
Fuzzing method_three...
Bug found in method_three with input 'Y@HGpNXq7h': invalid literal for int() with base 10: 'Y@HGpNXq7h'
Bug found in method_three with input 'jT\Q.*J8~"': invalid literal for int() with base 10: 'jT\\Q.*J8~"'
Bug found in method_three with input 'L&AC|mF$mU': invalid literal for int() with base 10: 'L&AC|mF$mU'
Bug found in method_three with input 'uZxYd%j}#p': invalid literal for int() with base 10: 'uZxYd%j}#p'
Bug found in method_three with input '?E"Q&f$Po8': invalid literal for int() with base 10: '?E"Q&f$Po8'
Bug found in method_three with input 'PG$0&=TKog': invalid literal for int() with base 10: 'PG$0&=TKog'
Bug found in method_three with input '\2xM!qJ1xR': invalid literal for int() with base 10: '\\2xM!qJ1xR'
Bug found in method_three with input 'wQ@re0^}bI': invalid literal for int() with base 10: 'wQ@re0^}bI'
Bug found in method_three with input '?YH"PzQn?C': invalid literal for int() with base 10: '?YH"PzQn?C'
Bug found in method_three with input 'i/<UrF|gDZ': invalid literal for int() with base 10: 'i/<UrF|gDZ'
Bug found in method_three with input 'K@@Irc0b"j': invalid literal for int() with base 10: 'K@@Irc0b"j'
Bug found in method_three with input '=9*2C<)rlj': invalid literal for int() with base 10: '=9*2C<)rlj'
Bug found in method_three with input 'o+#@c]B[;Y': invalid literal for int() with base 10: 'o+#@c]B[;Y'
Bug found in method_three with input 'a!z#z_,Kc%': invalid literal for int() with base 10: 'a!z#z_,Kc%'
Bug found in method_three with input 'WJ=;_q+Ju.': invalid literal for int() with base 10: 'WJ=;_q+Ju.'
Bug found in method_three with input 'GPd,cPUd?`': invalid literal for int() with base 10: 'GPd,cPUd?`'
Bug found in method_three with input 'l#)b2kq:5l': invalid literal for int() with base 10: 'l#)b2kq:5l'
Bug found in method_three with input 'r8L{/nPC;Z': invalid literal for int() with base 10: 'r8L{/nPC;Z'
Bug found in method_three with input ':eQuBBAI@Z': invalid literal for int() with base 10: ':eQuBBAI@Z'
Bug found in method_three with input 'Pm8~|@;@@z': invalid literal for int() with base 10: 'Pm8~|@;@@z'
Bug found in method_three with input '^4FN:lG*f"': invalid literal for int() with base 10: '^4FN:lG*f"'
Bug found in method_three with input 'MK9q<,xN(:': invalid literal for int() with base 10: 'MK9q<,xN(:'
Bug found in method_three with input 'Tl&E>)W![O': invalid literal for int() with base 10: 'Tl&E>)W![O'
Bug found in method_three with input '/R0n,*50[Q': invalid literal for int() with base 10: '/R0n,*50[Q'
Bug found in method_three with input '7VM5x?'N:v': invalid literal for int() with base 10: "7VM5x?'N:v"
Bug found in method_three with input 'W7YTSC5Se1': invalid literal for int() with base 10: 'W7YTSC5Se1'
Bug found in method_three with input 'r_/O\Xq*<+': invalid literal for int() with base 10: 'r_/O\\Xq*<+'
Bug found in method_three with input 'e,5T6B@;`x': invalid literal for int() with base 10: 'e,5T6B@;`x'
Bug found in method_three with input 'lOX"W?F\SP': invalid literal for int() with base 10: 'lOX"W?F\\SP'
Bug found in method_three with input 'o?Sy8}k?sS': invalid literal for int() with base 10: 'o?Sy8}k?sS'
Bug found in method_three with input 'ak+p~J2m-4': invalid literal for int() with base 10: 'ak+p~J2m-4'
Bug found in method_three with input ']ifPtSfG=&': invalid literal for int() with base 10: ']ifPtSfG=&'
Bug found in method_three with input 'N3L#Q3<`["': invalid literal for int() with base 10: 'N3L#Q3<`["'
Bug found in method_three with input 'd8wAQ/,KOI': invalid literal for int() with base 10: 'd8wAQ/,KOI'
Bug found in method_three with input 'E}>+lW]xLp': invalid literal for int() with base 10: 'E}>+lW]xLp'
Bug found in method_three with input '<r7)kU[z;b': invalid literal for int() with base 10: '<r7)kU[z;b'
Bug found in method_three with input '9EoN`C\x[w': invalid literal for int() with base 10: '9EoN`C\\x[w'
Bug found in method_three with input 'V3>QnH_+&^': invalid literal for int() with base 10: 'V3>QnH_+&^'
Bug found in method_three with input ';+Cd1\qBa'': invalid literal for int() with base 10: ";+Cd1\\qBa'"
Bug found in method_three with input 'vlvo+)4uJN': invalid literal for int() with base 10: 'vlvo+)4uJN'
Bug found in method_three with input ';pT|l]L'I=': invalid literal for int() with base 10: ";pT|l]L'I="
Bug found in method_three with input ',Bs+Z\#5E)': invalid literal for int() with base 10: ',Bs+Z\\#5E)'
Bug found in method_three with input 'loV0dw@w`d': invalid literal for int() with base 10: 'loV0dw@w`d'
Bug found in method_three with input '}o9BD++R/T': invalid literal for int() with base 10: '}o9BD++R/T'
Bug found in method_three with input 'w[+<Mh6i_W': invalid literal for int() with base 10: 'w[+<Mh6i_W'
Bug found in method_three with input 'yR^2GjH=QR': invalid literal for int() with base 10: 'yR^2GjH=QR'
Bug found in method_three with input 'PmFjx=F&ip': invalid literal for int() with base 10: 'PmFjx=F&ip'
Bug found in method_three with input 'ms0b_N4CG\': invalid literal for int() with base 10: 'ms0b_N4CG\\'
Bug found in method_three with input '`(JYJ-ZL=?': invalid literal for int() with base 10: '`(JYJ-ZL=?'
Bug found in method_three with input 'tf>K*)'BBk': invalid literal for int() with base 10: "tf>K*)'BBk"
Bug found in method_three with input 'HSCPR.H>P.': invalid literal for int() with base 10: 'HSCPR.H>P.'
Bug found in method_three with input '}!(!*<ZZ$o': invalid literal for int() with base 10: '}!(!*<ZZ$o'
Bug found in method_three with input 'O|JP5I;>6&': invalid literal for int() with base 10: 'O|JP5I;>6&'
Bug found in method_three with input '$~d}6YpO]h': invalid literal for int() with base 10: '$~d}6YpO]h'
Bug found in method_three with input 'cjTY8p}UL\': invalid literal for int() with base 10: 'cjTY8p}UL\\'
Bug found in method_three with input 'SUk1e9)h&T': invalid literal for int() with base 10: 'SUk1e9)h&T'
Bug found in method_three with input 'cS:4!nNb$G': invalid literal for int() with base 10: 'cS:4!nNb$G'
Bug found in method_three with input '^DjD0$}qR:': invalid literal for int() with base 10: '^DjD0$}qR:'
Bug found in method_three with input 'OG<?$S'eV3': invalid literal for int() with base 10: "OG<?$S'eV3"
Bug found in method_three with input '[Z,k?]&-O(': invalid literal for int() with base 10: '[Z,k?]&-O('
Bug found in method_three with input 'Y60UuQ=1Jy': invalid literal for int() with base 10: 'Y60UuQ=1Jy'
Bug found in method_three with input 'Q)P};9?H~:': invalid literal for int() with base 10: 'Q)P};9?H~:'
Bug found in method_three with input ':xzsos]M/J': invalid literal for int() with base 10: ':xzsos]M/J'
Bug found in method_three with input 'Ct[sISZoqe': invalid literal for int() with base 10: 'Ct[sISZoqe'
Bug found in method_three with input 'b)4Uxd^g>m': invalid literal for int() with base 10: 'b)4Uxd^g>m'
Bug found in method_three with input 'lfa)SJRM,W': invalid literal for int() with base 10: 'lfa)SJRM,W'
Bug found in method_three with input 'k)vX|6Jumc': invalid literal for int() with base 10: 'k)vX|6Jumc'
Bug found in method_three with input '</I<7u/\1E': invalid literal for int() with base 10: '</I<7u/\\1E'
Bug found in method_three with input '>`drCBxTEQ': invalid literal for int() with base 10: '>`drCBxTEQ'
Bug found in method_three with input 'm_)-HJ.t"e': invalid literal for int() with base 10: 'm_)-HJ.t"e'
Bug found in method_three with input 'O4sx_)Cllt': invalid literal for int() with base 10: 'O4sx_)Cllt'
Bug found in method_three with input 'H)IN<k$/QW': invalid literal for int() with base 10: 'H)IN<k$/QW'
Bug found in method_three with input 'IB2{)7I.?=': invalid literal for int() with base 10: 'IB2{)7I.?='
Bug found in method_three with input '8Z]l2]@$&-': invalid literal for int() with base 10: '8Z]l2]@$&-'
Bug found in method_three with input '+z'?Fc.&F"': invalid literal for int() with base 10: '+z\'?Fc.&F"'
Bug found in method_three with input '^@eKaN5wl[': invalid literal for int() with base 10: '^@eKaN5wl['
Bug found in method_three with input 'p.]\1s'jDI': invalid literal for int() with base 10: "p.]\\1s'jDI"
Bug found in method_three with input '(0<GM2gq~r': invalid literal for int() with base 10: '(0<GM2gq~r'
Bug found in method_three with input '7j_)CQZ8Rn': invalid literal for int() with base 10: '7j_)CQZ8Rn'
Bug found in method_three with input '>/ve+ahI-"': invalid literal for int() with base 10: '>/ve+ahI-"'
Bug found in method_three with input '>d)eIl*twR': invalid literal for int() with base 10: '>d)eIl*twR'
Bug found in method_three with input 'q0KJb\H/$M': invalid literal for int() with base 10: 'q0KJb\\H/$M'
Bug found in method_three with input 'G8&Kb$cM~[': invalid literal for int() with base 10: 'G8&Kb$cM~['
Bug found in method_three with input 'I1.W6`@UE)': invalid literal for int() with base 10: 'I1.W6`@UE)'
Bug found in method_three with input 'oh?0\>,/dz': invalid literal for int() with base 10: 'oh?0\\>,/dz'
Bug found in method_three with input '~yxs5s'fIB': invalid literal for int() with base 10: "~yxs5s'fIB"
Bug found in method_three with input 'N9."";hac<': invalid literal for int() with base 10: 'N9."";hac<'
Bug found in method_three with input 'qG/0mx7sUm': invalid literal for int() with base 10: 'qG/0mx7sUm'
Bug found in method_three with input '4C7|,6GN]4': invalid literal for int() with base 10: '4C7|,6GN]4'
Bug found in method_three with input 'NAq);7=aZx': invalid literal for int() with base 10: 'NAq);7=aZx'
Bug found in method_three with input '58v+]"1hi1': invalid literal for int() with base 10: '58v+]"1hi1'
Bug found in method_three with input '#Y1x-T`#`)': invalid literal for int() with base 10: '#Y1x-T`#`)'
Bug found in method_three with input '[LQ6_NskEU': invalid literal for int() with base 10: '[LQ6_NskEU'
Bug found in method_three with input 'sE:1M$W.YZ': invalid literal for int() with base 10: 'sE:1M$W.YZ'
Bug found in method_three with input 'R<TK$1|Fvb': invalid literal for int() with base 10: 'R<TK$1|Fvb'
Bug found in method_three with input 'f-x(EW}C}!': invalid literal for int() with base 10: 'f-x(EW}C}!'
Bug found in method_three with input '>G&~V+AMI-': invalid literal for int() with base 10: '>G&~V+AMI-'
Bug found in method_three with input 'gS;4hVq1Su': invalid literal for int() with base 10: 'gS;4hVq1Su'
Bug found in method_three with input 'TkGD*X.vQw': invalid literal for int() with base 10: 'TkGD*X.vQw'
Bug found in method_three with input '*bnl8w-B5f': invalid literal for int() with base 10: '*bnl8w-B5f'
Fuzzing method_four...
Bug found in method_four with input '8n;U'BX"fW': Input too long
Bug found in method_four with input '3/1,zXE.XP': Input too long
Bug found in method_four with input 'w-h$P=^mz`': Input too long
Bug found in method_four with input '%js0?#l5Oi': Input too long
Bug found in method_four with input 'W/u,0%3c,%': Input too long
Bug found in method_four with input 'vY*+DR>WlT': Input too long
Bug found in method_four with input 'k|BBTm2n%(': Input too long
Bug found in method_four with input '\oT^+ZRGM]': Input too long
Bug found in method_four with input '+AByfc9;6s': Input too long
Bug found in method_four with input '2y8`[!vz&g': Input too long
Bug found in method_four with input ''8dp3.^|jV': Input too long
Bug found in method_four with input '7#i*PMj3YW': Input too long
Bug found in method_four with input '"'bG%=*nwN': Input too long
Bug found in method_four with input '7d7gI"w~e)': Input too long
Bug found in method_four with input ':OPr'F'Oaa': Input too long
Bug found in method_four with input '?="\yr"tmP': Input too long
Bug found in method_four with input 'WH{Z{*Zn|u': Input too long
Bug found in method_four with input 'as|~P#|P?9': Input too long
Bug found in method_four with input '["]p)Ghw>t': Input too long
Bug found in method_four with input '.:hrux+Q(_': Input too long
Bug found in method_four with input '8a.q<e]O*-': Input too long
Bug found in method_four with input 'yN*43fI<t*': Input too long
Bug found in method_four with input 'DQ7&O|.-dp': Input too long
Bug found in method_four with input 'AfC@Rl0)Tt': Input too long
Bug found in method_four with input 'B!}6q{PKYP': Input too long
Bug found in method_four with input '9f/@f%.Qao': Input too long
Bug found in method_four with input '6NeS&DXKM!': Input too long
Bug found in method_four with input '.M;fX-,MpA': Input too long
Bug found in method_four with input '=uMhs>b,1J': Input too long
Bug found in method_four with input 'EiBkDuGf~D': Input too long
Bug found in method_four with input 'zoX1IEHG|Z': Input too long
Bug found in method_four with input 'lgwT0Mq+>:': Input too long
Bug found in method_four with input 'jjnCw]1|lR': Input too long
Bug found in method_four with input '(x(l"Bx])'': Input too long
Bug found in method_four with input 'o9l">Vuuc_': Input too long
Bug found in method_four with input 'y<RLQp:4~K': Input too long
Bug found in method_four with input ''UNTnX?.Hj': Input too long
Bug found in method_four with input ':$tbX9|z`F': Input too long
Bug found in method_four with input 'R)^pvx,8iO': Input too long
Bug found in method_four with input 'kx<'VxnleS': Input too long
Bug found in method_four with input ':W-T^K23)r': Input too long
Bug found in method_four with input 'dT"]aNf0>`': Input too long
Bug found in method_four with input 'p\<A'tQYnK': Input too long
Bug found in method_four with input ':DJ3T2u_$N': Input too long
Bug found in method_four with input 'OD]H7xQ%DM': Input too long
Bug found in method_four with input '4SRklh6m#M': Input too long
Bug found in method_four with input 'jT*8(qhX$4': Input too long
Bug found in method_four with input '$u^:7<4lJ;': Input too long
Bug found in method_four with input 'wW@3DI/R`_': Input too long
Bug found in method_four with input '4pTiwV.ecK': Input too long
Bug found in method_four with input 'v.(NO}wXp0': Input too long
Bug found in method_four with input ']d#\nu<1s6': Input too long
Bug found in method_four with input ']4%HQrrTYk': Input too long
Bug found in method_four with input 'Nw4&98yOaU': Input too long
Bug found in method_four with input '1@{-Yfd&*X': Input too long
Bug found in method_four with input '"apsR4&N%d': Input too long
Bug found in method_four with input 'Y5*b6loD2,': Input too long
Bug found in method_four with input '=hv]KBVG_+': Input too long
Bug found in method_four with input 'Nk3mC'~#Ut': Input too long
Bug found in method_four with input '1Ba<&w&o93': Input too long
Bug found in method_four with input 'X\LFbwl?,Q': Input too long
Bug found in method_four with input '^8H>cu=2u.': Input too long
Bug found in method_four with input 'IdxwSPx?p4': Input too long
Bug found in method_four with input 'fn{[O+^<]O': Input too long
Bug found in method_four with input ')\{:%rW["\': Input too long
Bug found in method_four with input '+(S<3)+>&h': Input too long
Bug found in method_four with input 'I@JFiN%~cD': Input too long
Bug found in method_four with input 'Z2`nWiI88'': Input too long
Bug found in method_four with input 'P2L@Uhdo@B': Input too long
Bug found in method_four with input 'zu:EHM4MjJ': Input too long
Bug found in method_four with input '<1U[^gjEd+': Input too long
Bug found in method_four with input 'yp\{cOl=z\': Input too long
Bug found in method_four with input '/aJDiS(Xo_': Input too long
Bug found in method_four with input '%i*R}jL$%(': Input too long
Bug found in method_four with input '?&e=*H%L?y': Input too long
Bug found in method_four with input '=1==TS7uL*': Input too long
Bug found in method_four with input ''h&q=CT)_g': Input too long
Bug found in method_four with input 'vUXBBHS`W"': Input too long
Bug found in method_four with input '.-i<m'smOZ': Input too long
Bug found in method_four with input '/vGtRYu@ie': Input too long
Bug found in method_four with input '>kk,;XO/0}': Input too long
Bug found in method_four with input '&Dlu+[ma+S': Input too long
Bug found in method_four with input '_j%'tw{n-c': Input too long
Bug found in method_four with input 'y~=IQ/EBDy': Input too long
Bug found in method_four with input '8qB;s}7mvs': Input too long
Bug found in method_four with input 'FVpWG%7{Z0': Input too long
Bug found in method_four with input '>RoHpgO8]c': Input too long
Bug found in method_four with input '[nlg(?Ce1$': Input too long
Bug found in method_four with input 'Ho"DElM:Hh': Input too long
Bug found in method_four with input '3t8=?nF_tX': Input too long
Bug found in method_four with input 'w`nZUQIh8o': Input too long
Bug found in method_four with input 'q.q'7;M|.l': Input too long
Bug found in method_four with input 'tbS:NZU;o=': Input too long
Bug found in method_four with input 'KC]i^l>IC+': Input too long
Bug found in method_four with input 'aukG(Y=Yj*': Input too long
Bug found in method_four with input 'dmPFzHzX{O': Input too long
Bug found in method_four with input 'c7_4PuG*s3': Input too long
Bug found in method_four with input '5eMQzs+XL?': Input too long
Bug found in method_four with input 'm9MO$'2]L%': Input too long
Bug found in method_four with input ')6yVtY>%/&': Input too long
Fuzzing method_five...
PS C:\Users\snube\OneDrive\Desktop\Auburn University\Fall 2024\COMP 5710 Software Quality Assurance\PRoject> git commit -m "Initial Commit"
[main]  INFO    profile include tests: None
[main]  INFO    profile exclude tests: None
[main]  INFO    cli include tests: None
[main]  INFO    cli exclude tests: None
[main]  INFO    running on Python 3.11.9
[csv]   INFO    CSV output written to file: bandit_report.csv
No security issues found. Proceeding with commit.
On branch master
Your branch is up to date with 'origin/master'.

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        bandit_report.csv
        fuzz.py

nothing added to commit but untracked files present (use "git add" to track)
PS C:\Users\snube\OneDrive\Desktop\Auburn University\Fall 2024\COMP 5710 Software Quality Assurance\PRoject>

