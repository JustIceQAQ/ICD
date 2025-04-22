from helpers.icd.v11 import anti_confuse


def test_anti_confuse():
    value = "l\u0080QoiNjpVpQZ\\a\u0081P8UpPzPuY<jJP=Prw_]JQ@5l\u0080Q|`t`pVqL:UK\\~U\u0081P<TKjzPt];jJP=T[j7U[H:Uq\\~U\u0080~ph_U\u0081PqvphOY7jOT=S\u0080@w`9Yo`9Usj:U{`^<oa9]{a^<7Sukvi\u0080<wiuXpSJQok^XpVszphOY7jOT=S\u0080@w`9Yo`9Usj:U{`^<oa9]{a^<7Sukvi\u0080<wiuX}jt]\u0081i:]\u0080`9]\u0081Pp~ph^Ur`_IwPs7zPtUzh^]|kM@waJP=PqMp`\u0081orVKYrS[sp`[`{UKj<VJ7;V[`\u0080S^`8UqIoVKT7U9`<`]@pT^\\7U[H~`p7\u0080VNT9S[X<UtT{V^\\8ap8qaqP\u007FT[]pT[krT\u0081TpSJQ\u0081`9@~aZP=^\u0080Qw`9YojNsm`^Uqa_U\u0081Ps8@5s[MTQ:@horti`Y>kLTlON4>_l{={yx7X\u0080Y7y\u0081RjU;q9^=pImW@pjSMYk]]@{ip\\W@`JqlWu`}HRfP{^_upmWm=lq7T\u007Fut=tP~}QuUU<}Ly]SRo\u0080^8]q[a9H:Q4_\u007FV\\z>~l{Pmk=ZqSrks@la@[`mhs|9Rs`T;7j8I>|tY4J{oZTx\u0080S=qW}h<`NRqi\u007F{M[lm9S7=r\u0081\\<\u0080sL\\ijo_mruTnjH@<9Iq]qrP:X~U@N=P:zohH]YwV|<JWPTL4;|Q>sLWVt\u007Fn;~]i\u0081p]\\u8I<Uizr;@pNfJ\\Stp<U\u007Fn{RyKanz?:_Zw\u0081;:{\u0081p}q~arpZ?J}OhjwXj<RZx_N\\44Jj=Xa;4i`n"
    result = anti_confuse(value)
    return result
