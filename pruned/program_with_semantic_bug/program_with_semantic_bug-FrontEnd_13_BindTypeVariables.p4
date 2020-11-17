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
        bit<64> sGPTcR = 64w8331771506825847071;
        {
            const bit<16> oZMmrS = 16w37657;
            sGPTcR = sGPTcR;
            bit<32> LRpMbf = (bit<32>)(32w37657 |-| (bit<32>)sGPTcR);
            sGPTcR = 64w152762851772443914;
            return LRpMbf;
        }
        sGPTcR = sGPTcR;
        bit<64> noVnDj = 64w1172448623121743915;
        noVnDj = 64w9155524997714835150;
        noVnDj = (bit<64>)64w859692371;
        sGPTcR = 64w0;
        sGPTcR = (sGPTcR - 64w11817574793371717234 << 8w55) + noVnDj;
        const int yZIceN = 838390161;
        return 32w2806012093;
    }
    bit<128> AfXLZG = (bit<128>)128w2144402680;
    AfXLZG = 128w23939084785281499464369578139775539458;
    AfXLZG = AfXLZG;
    AfXLZG = AfXLZG;
    AfXLZG = 128w306288353508935945900133283398710167980;
    AfXLZG = AfXLZG;
    {
        AfXLZG = 128w203190633050105623488232349361061266317;
        AfXLZG = 128w119851796932508784808775619006417521460;
        AfXLZG = 128w89063546262527641425054991023365647631;
        AfXLZG = AfXLZG;
        const bit<64> pQiUqJ = 64w15318551338288664749;
        const bit<8> rPqZzN = 8w211;
        AfXLZG = 128w8310206894313765100920948761954001695;
        AfXLZG = 128w232550981149043971176658599253778146419;
        AfXLZG = AfXLZG;
        return 32w1938567799;
    }
    return (bit<32>)(32w839498710 | (bit<32>)AfXLZG);
}
Vnytmj IBaXWsK(bit<64> yQJV, bit<16> gOEI) {
    bit<8> kXmlrB = (((bit<43>)yQJV | (bit<43>)yQJV) |+| 43w1462566353592)[16:9];
    {
        {
            kXmlrB = kXmlrB;
        }
        kXmlrB = kXmlrB;
        const int YXRheT = 77175706;
        ZqTDGWH();
        kXmlrB = 8w174;
        return (Vnytmj){PZdb = false,xjKr = (bit<32>)yQJV,pBFG = 16w14442,VYDJ = !!((bit<9>)ZqTDGWH() | 9w260 != (bit<9>)ZqTDGWH() && !!!!(51w1444364813109517 == (bit<51>)gOEI)),GXQs = 128w127537729978999984111170865926198740152};
    }
    const jCFTwO wUxkGX = (jCFTwO){iUNX = 4w11,YwAD = 64w16737022111367307944,PamX = 32w2836164008};
    kXmlrB = 8w14;
    kXmlrB = kXmlrB;
    ZqTDGWH();
    return (Vnytmj){PZdb = true,xjKr = 32w1354969928,pBFG = gOEI,VYDJ = true,GXQs = (bit<128>)wUxkGX.iUNX & (bit<128>)wUxkGX.PamX};
}
control PFizfTj(out bit<16> lcNR, bit<128> SZxu) {
    bool oHvtbH = !(!(((bit<79>)(bit<79>)SZxu)[78:22] |-| 57w128961855891103457 | 57w83480883236889332 == (bit<57>)lcNR) || true);
    bit<64> nYJwrn = 64w12914525900351020762;
    bool htHGwZ = !!oHvtbH;
    bit<32> xQNzSP = 32w1305108261;
    bit<128> SYsGZI = (bit<128>)128w18672238;
    bool NdjDFo = ((bit<113>)(bit<113>)nYJwrn |+| (bit<113>)lcNR)[62:9] != 54w2143205456929516 || true;
    action woqMg(inout bit<4> OcIW, out Vnytmj ILUP, bit<128> YFnT) {
        OcIW = 4w15;
        {
            OcIW = 4w1;
            nYJwrn = (bit<64>)64w440494971;
            ILUP.GXQs = SZxu;
            nYJwrn = nYJwrn;
            xQNzSP = 32w3146255595;
            ILUP.GXQs[56:41] = ILUP.pBFG;
            lcNR = (bit<16>)16w18122;
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
        pQcOkh UitBTw = (pQcOkh){wBCb = 32w1531371326,fwsC = xQNzSP,XbXc = ~(PHeC ^ 8w221),RNQF = 64w3628752390428671448};
        SYsGZI = 128w216323781136148277345578055083500959293;
        UitBTw.wBCb = 32w2554680596;
        UitBTw.XbXc = 8w10;
        ZqTDGWH();
        SYsGZI = SZxu;
        SYsGZI = -((bit<182>)lcNR)[131:4];
        SYsGZI = -(SYsGZI |-| 128w294999660554044817754265939658325384524 >> 8w149);
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
            128w50421981630794248132575380387204031162: exact @name("vdbGnq") ;
            (oHvtbH ? 32w3342148876 : 32w3429918406)  : exact @name("TWbDDS") ;
            64w17488452717387411170                   : exact @name("RXlgBk") ;
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
        IBaXWsK(64w9569382937354443357, 16w0);
        SYsGZI = SYsGZI - 128w174843887977112616899567535517197106864 | SZxu;
    }
}

parser p(packet_in pkt, out Headers hdr) {
    state start {
        transition parse_hdrs;
    }
    state parse_hdrs {
        pkt.extract<ethernet_t>(hdr.eth_hdr);
        pkt.extract<jCFTwO>(hdr.BqNk);
        pkt.extract<kTchlw>(hdr.zkbz);
        transition accept;
    }
}

control ingress(inout Headers h) {
    bit<8> TCVSkL = 8w41;
    PFizfTj() IArlRL;
    action dpTJp() {
        IBaXWsK(64w6943846788549823044, 16w13608);
        IArlRL.apply(h.eth_hdr.eth_type, 128w30865149178727196209754798400394629432);
        return;
        h.eth_hdr.src_addr = (bit<48>)48w281474897995198;
        const bit<32> QlaOEA = 32w2475038456;
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
        IArlRL.apply(h.zkbz.WNfX, 128w1017011646);
        {
            IBaXWsK(64w16257984866694305357, 16w65535);
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

