import base64 # Base85 için de bu modül gerek
import zlib
import marshal
import sys

# Orijinal betiğin kodlanmış (Base85) ve sıkıştırılmış bytecode'u
encoded_bytecode = 'c$}41TWs6b89tOK>SoFEO>&$#p)YZ!bhCVS<iyPs$F3bmN+Q}@6A2Y)iK3WDq<Tmtjn)BbHo)#MG~Nx%+gxlwlc%}B9x`CSvL+k$NJn1nGTy_`r@p!N9)|2?=a7=^%}UXc;JN<)f6n>;|N9O<2L~Q&rQU5c0q_gJ0EU<a(5MMWpxQKRx@3YT+88rKvtE;sM74R=a*2XeWzGt%3<+(F1=<;^4M0cS6!n5bPbV0zv|wGFh_=;|V61VQ8!)!G9hLS$OWfTF;&sD>G5;;}Rok$haiFz40l+w~5wL-&L%qhhIoeaxu8VOq^+6MCj<+C-6#AMO&#=juuiB(Rb(U$UIqR*=HXfdZzCGQhxX%p+O-yqQ3uLsf=Kfj^$XKHTwPfOrj5kQYws>1~^zeMuw@AOC2~0cDj*i7WNbA_X<**9?Czfc7p8YBdJmL3!ftwLOq1jTb!YM+ILv3qP%1V$+6?;d6{e2_BzQLj4u~2B5muE+cXTsshp*OyBd*tfq_1w_qw=+BpCL(W6-0Tl)j^SW%DA?B*92iUz2iBy}XGY)dC4kc~wl@(q)pQdPBda}>Af_0#-y0<7QDO#B!t%gRMqVDvC`w))3k2A_(5rA+j)!cnSAu+CK~i3N12QM3E=tKljuVyh$qcI`gw!}Xqa`h5IoVHYHpsnQ;ABPC$h;&gnjPsS6zLWxB0m`NNSxHg@tJ7NCy27bE+~qUVdad%@`9L5_U7+uF1%PGRap&skTePfkULRP0$XI=V)$NIZSMQskyWR9_S$;%x_a$~+89%le3{Jb;sZjASZG5<p%oQ93ipmOJ{bu;Tcxj0hV}9yD*wy7j;eS6LVO+X&L2qBn58;?K#Mx0q{pPHRjoy0o<J#h6SYk9rl{?(R@8ZTj4@U9zfl=UA@}?r`sPFW=#=3}0FDEOjJc|EwJoA-vQ**PM~LQF{hqw}0D!UvfOyaWVxFpm6|ezxRx;MKw-@S_t5{<#dzQ(nWt_eHtDHczDv}{G{A*BYrHM2cH=h7$!f%UcL~oJoy_x4xnHPBk&`MruCb&@S3W+oap#*6unJhpAR{Bl`r6`?;Qj(KpLFDP8X^i$eHIpQ3mSiR+K#j}_D8sFCk`?u?$mTfBhLTpkBPbb-l=7UYr>$n6d?(4}6+sd;OCAbnRkN%>zeRH+MJ}mG@NOc{A{{#hMnbns2+)mn2~NgoMdJrz2Wt(LT_yIEVK*Abj+7q(102-i^u6h&x7NvHTb|~hM}K+ar#Dv2KTDK7CrdM*ySz)prnBz;$onJr&%b~E!N`WQbIsYg!hV$gF#VDAp|qOb=ov5fjBlGr*HvP(wevR@ABKKA^=RthnblOe`>g6aw@hw%+8?Ao^>ppnf!p`5e>y;O`z|1m{FbLhZ9V%q^v9{+Pdz^KWZ+ryuN_a*Pu^6$kqyt4=bkJ7-Zo>omof(BpI-02aLV+_DaQnD`J}&l;;7~6Q44DOt;LRjj84b$T!70JvWQVrfxf`SiJ5SK5!pPZlVa<uM2aU~sXT$=1leNutF0#?$BA-AQsm;vT2fbqq*8#K9GI(6WU=Qf#bz+YeGR!ViYh1a984Yr0LFyQNJ~Ixq&>D`2!#I%{t$Pd3s3|xb9Hu~jTrMhMiDt^-pA_!*4ksJTIfSuMIFHMP!-F5Yvc<&EO<^KcJ-mwoRrV9IXcCO_@)2+D<KWJF}mo%nLFL3b2~i~ndsFlJoYa?s6XZN2nQC(;$t62W+1+-G!kE)nnliXT;5MW%=yNBVL-r@lnSDf5DU2l4$AN~G=@KU)JT6<<8uEp_d#Nb*s{5P%&V<|RpOzn4qQ;Z6HmTdc8Aw(ku6)@eaDX+%Yz@(?^uAl9X24{V%>BXGd&l2!`P?|g-uMc(73ZCj9Yw>H_Swsxe$FJIzKl_PhE*lOcuJ3^5v(0P}1n+3j(BX6|z}YeD-nj*~c`SLIp1%+>aF+k=*S6%#G3T6h1iq2}27}3JZBo@gIlye-PsP2;!h>w*1|+z-Kwc96G5e9L(we7KY30N(ORl3UL*z!#bF}4f-*Q(jARRL3{zg6Z(jf<#p1~oK+GLIKz*c%UC3lmSB!mG-suY?@m2Hnne)v1x0fdWDX|uHav~TsX2WET9Xl$gb^cSS16R|Sm=LXkFzxLrX+}ufbMrAs<v}EDOJdFufq`P;&97ds6=c*5HEoJ1*rc!Xh-D>;M5zQZ3?)?OZH8Nw`AQR2|^&yh{d&d`QGIpL`uXa<zCF)%c<Uh)!^!D>Num$#Z)G)#uc@>uy*^dTKr!5_PcA%@0O|Wm&`k)gSblUwAt!SCFhRUOtfy-fqLJDyZgDjd*!Xir`Oz*CFhqEAgK5FrCSe9mMMB2bbJOZ@A0a;V`aEZ`Paeef4CZdGO8Z^_LGz4rs=Y4rsOarJe@0JE8kSzfmL6b3a*2(O+YR>?m3qFf9OKH_R$;Op6A}4hq*QHITbW*f~E~{WDOiy2S;})(AZv@`HXB?7Ct5EFU_dCZ39H}254Oat$zb;x)c8cAp7Wl'

try:
    # Base85'ten geri çöz
    # base64.b85decode() girdi olarak byte bekler, stringimizi byte'a çeviriyoruz.
    compressed_bytecode = base64.b85decode(encoded_bytecode.encode('ascii'))

    # Sıkıştırmayı aç
    bytecode = zlib.decompress(compressed_bytecode)

    # Bytecode'tan code object'i yükle
    code_obj = marshal.loads(bytecode)

    # Code object'i çalıştır
    exec(code_obj, {'__name__': '__main__'})

except Exception as e:
    print(f"Kodlanmış (Base85) betiği çalıştırırken bir hata oluştu: {e}")
    # sys.exit(1)