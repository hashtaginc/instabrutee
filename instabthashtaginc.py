import base64 # Base85 için de bu modül gerek
import zlib
import marshal
import sys

# Orijinal betiğin kodlanmış (Base85) ve sıkıştırılmış bytecode'u
encoded_bytecode = 'c$}41TTmO<89pnmRzgBTfDjlPdkq*@PK&r>VG|c)2pCJYwa~_vCYnWBEo)1=%Gs42)O3cB&Okbym^SIuZza>t#C|H7>4Q7dnYyvt>EmM2K-To3lc&59$V10{>A$-Y(1J7R?(Baq|K*(XU%s<npnZ?M)b7++5c(xz5JOBLY_<d@ptVd`E?cmLHs`F^YP2LKp|wufE>oB)@$A^nkl4Z4a0Np(BJ7M?qJDJXX-2)J9<GcN(Z<6h7<=5|L5w3_0kopq7WXuxcx5kP^1laPxsR(DC#>ZSBF1%{z|~A8jB4W6XxpK7-HeB+3R$o(UI!K__<W4F*JAR^HfdDmGS!E2{UvVAK`yS})vb-!dr-H9@f~7;jCLHlzq)-g_Gs5(GVvP5A0lvLyfNB;kYDyK=vUXGF&FIUSlkO*$M!6T-3YmKiN@%;Z?eD>f%-4?ZX`fxjufkKijd`?Z%;}Y33I7Jdw;02qc7Ca-P1cTG&IJ`6McoV;qXY$Yd^Ttcdh?Mw&%*5GdvC@BCikM>I`en-cYC~)X@>@>P`~-)}-LG!nbo7>1i0-WkfB9x`~L9<q;%^B}VOyy2&X>%n&3jj{;=m#jzPh$;ku3Ae$4~6)wZ^n9a6Jm=8`%$_sx`=ET$`DVfi5qH-ZQ!zu|OH3(<4rG*S92T09<xi|BitjHRflVnA!0KJ4F-R4B_gDDT<q#>@KiT>ILlxH&>7U*e(o@Fzv`1F(Z+^pu-7fYl{t6?w5K`4;i3}g;%l9dbL`LOEi`2CR;mwN8{TJ(l`{ia$IQ<Hp=oY~P2i1mua4j}mkAZ-fwmNGaJ8G5=x-xvuS^b*kj@~*S&-M<pw#=BGd5;bNk&+pTs4k#HhDQlHmk(eSN1#dymGG&Q64r)bR2j>_|S^qnwnH0F^|IoJ{(1%loM-V!W7&7KA%N=eJvdLC1*A7Co#;SJZt@{cnV-^sPPNJB%EMZ4%5Y9@*YIpZSy>u0OtZvsbS+=Za@7^jW09HkEhz$P*m3nC+jRvhJP?`uhA{x<NAlq-{c%V6vhXO6-m1e=yg_a?a<}j8pEhUqA48=;{oq-gkb684pvMh)^U9b$$0heZxWX+bGNeNgZGXi9|T~4y1F%;P>r#T>L<-3A1qmfdM6OFXhDn{N)aydniM9r4N0<3D46&$c>9#G_xiiBqqITmy(^ukCOb_oG{bX|gz^|Ye(2kQ>js!O{{>?-3{nAaUCKSXA6Pzz)8V~cOBk;gW@z7M0ny7`Nn%hnGPMenJ(@h{x|MPkEMd9UxizIzwmyKuj6-POG6YF=hPPJfjCSo%m>Nw2pJ7TX55ETsDyvC+`{+e;6IemDAX^ugJcRI&A(T7Q0t-1IixPkrWX*{(pI`hR`xM82jSM1cIJw@z(1_h{%(qkkBEboO!A)8yYyK1n}*UG+!Sy;q-kul{?>s>{8Q^`iXqtF0GLTRuJQ9HwobcD4>5wLLj%gMNT2Gz4Wh9m{h;E}PE)qNai!!AryA;X>=nI6)?fIZl*kBt<Tqc&XGdgbK5TQ-=v$6Ou|Eb8>L9gnxy$ZxkCBWrh6~a$yJ=C-NLl?$2&L;SIQ1L<ZdKLJ>niahHk<fB|kd5yh-!?jF=I)+xP2$ZqRiG46w;UHCbyv;c^xeTCXnF4TZM@})j4cuxa#)<bVn%4OIro#I6OrT_A4A&t2Ky5QB*a;!z30T<BYk>PgD#_Iv#yN#!K0g~K?S^e0@!3@@KB8}8<M$IN?I4&0;uny?vWnkvFJ1ONwB_Zas(;SxZD=>FP7wI>1+g-ENxx~GnSR^(b?w|2$LvV$7Agf&$RsZng9~M2~HAiIAQF+h#Q|D6m`&HXE<Y~gypj)UMYhlJFhh8%`>VU9`DHfX-lB5@<eoI%6N0`YW`eJlya)che8XX?Vw}A4MCx2AZaPnyZ)3@^(<CaQ3{e)&yKzIR)dLUl|auff<8=&!N{owi^7A!<5Eao{Sa2)GDdsx40upU&+k(*5me1-#9Fc3rGaMt*7FkM!m%wUd90TAIzT}MY|6I-mJbXOx%SVwn!!kAGqynzUstBeo=XZlfdn~NmU63()U<|+;Ki_r*>W)s9*UeTO+nZpUAk9Fs3)TFTit=0@n!i<r*D+nbV3oiRzK+?!tk{~`rhTqMoI?iXMR6fJKiicpRhg)s|3Q#~0&r!v5RP_(k1oSy_86EEyh1`R46&p_foPC=l2!VhZn|tBP{FQejbHoPaS;)?3Re#q?Xyp}kkWnXNDic@Zit5X+-kDVkKPujNd)4=Lk^1qRb(?e&*NE*#dzEF*we7PK4O^9{s(#(m`pnb1{Klg*tDccL*H;uGsCW3q+xJfuDS8c^{2bZd;Z@Jc<=!F{SVL$2>8|;Czk2lhk53hA$BORpIj1S%ZC)N&{;ui?uGAN)&>9-pK;(jR-nrQM6F2O-o?iF2J@dCc$gcX&tEhGZ)vlu>tLVrYI=Vxlnx?t&&&j$a;WLu{$_m3R2O@mys9_Z~{2etKPW%t+n%e*'

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