#include <core.p4>

header ethernet_t {
    bit<48> dst_addr;
    bit<48> src_addr;
    bit<16> eth_type;
}

struct FddaxM {
    bit<8>        tFfR;
    bool          JIfb;
    ethernet_t[8] sNYh;
    bit<4>        cIrx;
    bit<8>        Govt;
}

header jCFTwO {
    bit<4>  iUNX;
    bit<64> YwAD;
    bit<32> PamX;
}

header qTdOho {
    bit<4>  fZMq;
    bit<16> RhAV;
}

header pQcOkh {
    bit<32> wBCb;
    bit<32> fwsC;
    bit<8>  XbXc;
    bit<64> RNQF;
}

struct Vnytmj {
    bool     PZdb;
    bit<32>  xjKr;
    bit<16>  pBFG;
    bool     VYDJ;
    bit<128> GXQs;
}

struct KGAUpM {
    bit<128> RiWG;
}

struct VJczUg {
    bool     Laoh;
    bit<8>   daEM;
    bit<128> sfPX;
    bit<16>  nVIm;
}

header kTchlw {
    bit<16> WNfX;
    bit<4>  mjHD;
    bit<8>  SzNw;
}

struct Headers {
    ethernet_t eth_hdr;
    jCFTwO     BqNk;
    kTchlw     zkbz;
}

bit<32> ZqTDGWH() {
    {
        bit<64> sGPTcR = 68w53557031161070797374[64:1];
        {
            const bit<16> oZMmrS = 16w37657;
            sGPTcR = sGPTcR;
            bit<32> LRpMbf = (bit<32>)((bit<32>)oZMmrS |-| (bit<32>)sGPTcR);
            sGPTcR = 64w16398916870993737006 % 64w427530368926876134;
            return LRpMbf;
        }
        sGPTcR = sGPTcR;
        bit<64> noVnDj = 64w1172448623121743915;
        noVnDj = -64w9291219075994716466;
        noVnDj = 859692371;
        sGPTcR = (bit<64>)64w2898692507126017355 << (bit<8>)64w11981686051562272611;
        sGPTcR = (sGPTcR - 64w11817574793371717234 << (bit<8>)(34w13079922245 ++ 30w269591351)) + noVnDj;
        const int yZIceN = 838390161;
        return 32w2806012093;
    }
    bit<128> AfXLZG = 2144402680;
    AfXLZG = 128w290201655608422881013301261221431492354 & (!(!(false || (!!(true || !!false) || !true)) || true) ? (bit<128>)128w898317342468254849257934916010057547 |-| 128w7095990583075605562491329095786241671 : 78w26593309204912329688403 ++ 50w796590729582915);
    AfXLZG = AfXLZG;
    AfXLZG = (!!(false || true && 99w126521560808615075284510202349 == 99w93554252872241793680402658917) ? 128w265277269598615858768621607659578766285 : AfXLZG);
    AfXLZG = 128w306288353508935945900133283398710167980;
    AfXLZG = AfXLZG;
    {
        AfXLZG = 128w203190633050105623488232349361061266317;
        AfXLZG = 128w119851796932508784808775619006417521460;
        AfXLZG = 128w89063546262527641425054991023365647631;
        AfXLZG = AfXLZG;
        const bit<64> pQiUqJ = 64w15318551338288664749;
        const bit<8> rPqZzN = (!false ? (bit<8>)-1784394285 : 8w143 % 8w170);
        AfXLZG = 235w1767574341728031404715666999839022448308662552235129012715307495487784[229:102];
        AfXLZG = ((bit<128>)(-2108222292 - -2028710138) << (bit<8>)128w65220779906866385009446598857967736806) + 128w232550981149043971176658599253778146419;
        AfXLZG = AfXLZG;
        return (bit<32>)rPqZzN + 32w1938567588;
    }
    return (!!false ? (bit<32>)AfXLZG : (bit<32>)(839498710 | (bit<32>)AfXLZG));
}
Vnytmj IBaXWsK(bit<64> yQJV, bit<16> gOEI) {
    bit<8> kXmlrB = (!!true ? ((bit<43>)yQJV | (bit<43>)yQJV) |+| 43w1462566353592 : 43w984356912767)[16:9];
    {
        if (!(false && true) && !false) {
            kXmlrB = (true ? kXmlrB : ((bit<30>)yQJV)[26:19]);
        } else {
            kXmlrB = kXmlrB;
        }
        kXmlrB = kXmlrB;
        const int YXRheT = 77175706;
        ZqTDGWH();
        kXmlrB = 8w174;
        return { !!(false || !true), (bit<32>)yQJV, 16w14442, !!((bit<9>)ZqTDGWH() | 9w260 != (bit<9>)ZqTDGWH() && !!!!(51w1444364813109517 == (false ? (bit<51>)gOEI : (bit<51>)gOEI))), 128w127537729978999984111170865926198740152 };
    }
    const jCFTwO wUxkGX = { 4w11, 64w16737022111367307944, 32w2836164008 };
    kXmlrB = (-1656398165 ^ 1119644396 & -1299329753) & 8w14;
    kXmlrB = kXmlrB;
    ZqTDGWH();
    return { true, 32w1354969928, gOEI, true, (bit<128>)wUxkGX.iUNX & (bit<128>)wUxkGX.PamX };
}
control PFizfTj(out bit<16> lcNR, bit<128> SZxu) {
    bool oHvtbH = false || !(!((true ? ((bit<79>)(bit<79>)SZxu)[78:22] : 57w27316355257469953) |-| 57w128961855891103457 | 57w83480883236889332 == (bit<57>)lcNR) || !!(!false || true));
    bit<64> nYJwrn = 64w12914525900351020762;
    bool htHGwZ = !!oHvtbH;
    bit<32> xQNzSP = 32w1305108261;
    bit<128> SYsGZI = -69135971 ^ -84018189;
    bool NdjDFo = ((bit<113>)(bit<113>)nYJwrn |+| (bit<113>)lcNR)[62:9] != 54w5833293339867020 + 54w14324310626544480 || 124w1972002707832674242128141845115307680 & -1808553676 != 124w10100509633410923453791864725814817281;
    action woqMg(inout bit<4> OcIW, out Vnytmj ILUP, bit<128> YFnT) {
        OcIW = 4w15;
        {
            OcIW = 4w1;
            nYJwrn = --440494971;
            ILUP.GXQs = SZxu;
            nYJwrn = nYJwrn;
            xQNzSP = (bit<22>)22w3072515 ++ 10w235;
            ILUP.GXQs[56:41] = ILUP.pBFG;
            lcNR = (-2139035674 & 756808726) + -1830690600 ^ 1514111508;
            bit<32> xtBTEG = 32w4137147051;
            ILUP.pBFG = 16w23124;
            ILUP.xjKr[8:5] = OcIW;
        }
        OcIW = (bit<4>)-OcIW |+| ((bit<78>)ZqTDGWH())[73:70];
        ILUP.GXQs[36:5] = 32w1728758457;
        IBaXWsK(64w10928050462811547131, 16w55614);
        nYJwrn[6:3] = (bit<4>)ZqTDGWH();
        return;
        IBaXWsK(64w6235384825236171976, 16w36291);
    }
    action CBiEr(in bit<8> DgGZ, KGAUpM MevJ, bit<8> PHeC) {
        pQcOkh UitBTw = { 32w1531371326, xQNzSP, ~(PHeC ^ 8w221), 64w3628752390428671448 };
        SYsGZI = 128w216323781136148277345578055083500959293;
        UitBTw.wBCb = 32w2554680596;
        UitBTw.XbXc = 8w10;
        ZqTDGWH();
        SYsGZI = SZxu;
        SYsGZI = -((bit<182>)lcNR)[131:4];
        SYsGZI = -(SYsGZI |-| (128w243328255867979410922387748647889646280 ^ 128w142069344174629607110478862563052744580) >> (bit<8>)128w97451597401805586974158020750006213781);
        bit<32> GSuYjJ = ~UitBTw.wBCb;
        UitBTw.XbXc = ((bit<130>)DgGZ)[109:102];
        ZqTDGWH();
    }
    table TNAYJq {
        key = {
            SYsGZI: exact @name("RAfuHF") ;
        }
        actions = {
            @defaultonly NoAction();
        }
        default_action = NoAction();
    }
    table VtgSNW {
        key = {
            (!!false ? ((bit<185>)xQNzSP)[162:35] : 128w50421981630794248132575380387204031162): exact @name("vdbGnq") ;
            (oHvtbH ? -32w952818420 : 32w3429918406)                                           : exact @name("TWbDDS") ;
            64w17488452717387411170                                                            : exact @name("RXlgBk") ;
        }
        actions = {
            @defaultonly NoAction();
        }
        default_action = NoAction();
    }
    table YSvMfd {
        key = {
            ((bit<213>)xQNzSP)[157:30]: exact @name("iZjain") ;
        }
        actions = {
            @defaultonly NoAction();
        }
        default_action = NoAction();
    }
    apply {
        xQNzSP = xQNzSP + (bit<32>)ZqTDGWH() |-| 32w2827375294;
        ZqTDGWH();
        SYsGZI = SYsGZI;
        xQNzSP = xQNzSP;
        IBaXWsK(64w9569382937354443357, 16w47370 / 16w52726);
        SYsGZI = SYsGZI - 128w174843887977112616899567535517197106864 | SZxu;
    }
}

parser p(packet_in pkt, out Headers hdr) {
    state start {
        transition parse_hdrs;
    }
    state parse_hdrs {
        pkt.extract(hdr.eth_hdr);
        pkt.extract(hdr.BqNk);
        pkt.extract(hdr.zkbz);
        transition accept;
    }
}

control ingress(inout Headers h) {
    bit<8> TCVSkL = 8w41;
    PFizfTj() IArlRL;
    action dpTJp() {
        IBaXWsK(64w11781722781536468735 - -64w13608868080722905925, ~16w51927);
        IArlRL.apply(h.eth_hdr.eth_type, 128w30865149178727196209754798400394629432);
        return;
        h.eth_hdr.src_addr = -78715458;
        const bit<32> QlaOEA = (bit<32>)32w2475038456;
    }
    table QyKFXD {
        key = {
        }
        actions = {
            dpTJp();
            @defaultonly NoAction();
        }
        default_action = NoAction();
    }
    apply {
        h.zkbz.WNfX = (h.eth_hdr.eth_type | (bit<16>)ZqTDGWH() | 16w58652) + 16w30345;
        IBaXWsK(64w11378255015260334646, 16w59162);
        IArlRL.apply(h.zkbz.WNfX, 1017011646);
        if (!false) {
            IBaXWsK(64w16257984866694305357, (bit<16>)16w23685 |+| ~(!false ? 16w16709 : 16w22268));
        } else {
            switch (QyKFXD.apply().action_run) {
                dpTJp: {
                    h.zkbz.WNfX = 141w1842415444230137893288072292211188200133399[87:72];
                    h.BqNk.YwAD = 64w5755209842779639858;
                    h.BqNk.YwAD = 64w11024526164810448119;
                    if (false) {
                        TCVSkL = (bit<8>)ZqTDGWH();
                    } else {
                        h.zkbz.mjHD = h.BqNk.iUNX;
                    }
                    h.BqNk.PamX = 32w4169415496;
                    ZqTDGWH();
                    IBaXWsK(64w12301071070313056270, 16w34838 * 16w47871);
                    IBaXWsK(64w7199869912651391625, 16w11619);
                }
            }

        }
        h.BqNk.iUNX = h.zkbz.mjHD;
        ZqTDGWH();
        h.BqNk.YwAD = 64w4314245641897930119;
        h.BqNk.YwAD = h.BqNk.YwAD;
        const bit<16> oOqmbD = 16w34931;
    }
}

parser Parser(packet_in b, out Headers hdr);
control Ingress(inout Headers hdr);
package top(Parser p, Ingress ig);
top(p(), ingress()) main;

