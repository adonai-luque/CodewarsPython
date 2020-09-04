def longest_repetition(s):
    if s == "":
        return ('', 0)
    else:
        carray = [s[0]]
        larray = [1]
        for c in s[1:]:
            if c == carray[-1]:
                larray[-1] += 1
            else:
                carray.append(c)
                larray.append(1)
        return (carray[larray.index(max(larray))], max(larray))

print(longest_repetition('gCL{pJD>RHYny>EJ+-RWC!mp]vbWlk#IVQ.I.c(\\CCBN:o>i}Krw`x#xuw/udZ$OKSQf;E\'VkpikLNEuy(Zka(wQtY[?S~kNtUDbC}p}^eAPE=bPx-)|%:g?mR{_-b#gcng(LgXzegQjF&[kRBsopnM{?qI:KKn$cphic.cc")K{W{>~pd"FUeO:Qa]cxwsnaBF^W\\P{>(TecW>XcJu>Ha>-w|CbwynYd\'Q}Z#UaKML&n:&!NM;#.,scy@I(lkg~s^H[+zD+Is+|Y^y#TW?cGyKrJpm[~w<=<H>JL_\\sf+$L|WqQ+Yh@F(kl\'%BCNc:^Z&^_=/HeReke+_Av?=*i[;@zsR^cIa[k*?Qcar#+l%/,s#>RH}s+{>N`,HE!WMQ&~h(rC@lURi;yt`UKor:brvJ>)nur^=,gbe=`Ss,xvLYPr|lfK%o^_)+pTl]Dd^x?O`iChRSi[}^R,@Fh"o^(PB*rF>Iyy)w>FqL@PI].L?=~GE/Z#\\~!'))