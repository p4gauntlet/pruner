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
        bit<64> sGPTcR = 64w10;
        {
            const bit<16> oZMmrS = 16w37657;
            sGPTcR = sGPTcR;
            bit<32> LRpMbf = 32w10;
            sGPTcR = 64w152762851772443914;
            return LRpMbf;
        }
        sGPTcR = sGPTcR;
        bit<64> noVnDj = 64w10;
        noVnDj = 64w10;
        noVnDj = 64w859692371;
        sGPTcR = 64w0;
        sGPTcR = 64w10240 + noVnDj;
        const int yZIceN = 838390161;
        return 32w10;
    }
    bit<128> AfXLZG = 128w2144402680;
    AfXLZG = 128w10;
    AfXLZG = AfXLZG;
    AfXLZG = AfXLZG;
    AfXLZG = 128w10;
    AfXLZG = AfXLZG;
    {
        AfXLZG = 128w10;
        AfXLZG = 128w119851796932508784808775619006417521460;
        AfXLZG = 128w10;
        AfXLZG = AfXLZG;
        const bit<64> pQiUqJ = 64w15318551338288664749;
        const bit<8> rPqZzN = 8w211;
        AfXLZG = 128w10;
        AfXLZG = 128w10;
        AfXLZG = AfXLZG;
        return 32w10;
    }
    return 32w10;
}
Vnytmj IBaXWsK(bit<64> yQJV, bit<16> gOEI) {
    bit<8> kXmlrB = 8w10;
    {
        kXmlrB = kXmlrB;
        kXmlrB = kXmlrB;
        const int YXRheT = 77175706;
        ZqTDGWH();
        kXmlrB = 8w174;
        return (Vnytmj){PZdb = false,xjKr = (bit<32>)yQJV,pBFG = 16w14442,VYDJ = false,GXQs = 128w127537729978999984111170865926198740152};
    }
    const jCFTwO wUxkGX = (jCFTwO){iUNX = 4w11,YwAD = 64w16737022111367307944,PamX = 32w10};
    kXmlrB = 8w10;
    kXmlrB = kXmlrB;
    ZqTDGWH();
    return (Vnytmj){PZdb = true,xjKr = 32w1354969928,pBFG = 16w10,VYDJ = true,GXQs = 128w10};
}
control PFizfTj(out bit<16> lcNR, bit<128> SZxu) {
    bool oHvtbH = false;
    bit<64> nYJwrn = 64w10;
    bool htHGwZ = oHvtbH;
    bit<32> xQNzSP = 32w10;
    bit<128> SYsGZI = 128w10;
    bool NdjDFo = true;
    action woqMg(inout bit<4> OcIW, out Vnytmj ILUP, bit<128> YFnT) {
        OcIW = 4w15;
        {
            OcIW = 4w1;
            nYJwrn = 64w10;
            ILUP.GXQs = SZxu;
            nYJwrn = nYJwrn;
            xQNzSP = 32w10;
            ILUP.GXQs[56:41] = ILUP.pBFG;
            lcNR = 16w10;
            bit<32> xtBTEG = 32w10;
            ILUP.pBFG = 16w23124;
            ILUP.xjKr[8:5] = OcIW;
        }
        OcIW = 4w10;
        ILUP.GXQs[36:5] = 32w1728758457;
        IBaXWsK(64w10, 16w10);
        nYJwrn[6:3] = 4w10;
        return;
        IBaXWsK(64w6235384825236171976, 16w10);
    }
    action CBiEr(in bit<8> DgGZ, KGAUpM MevJ, bit<8> PHeC) {
        pQcOkh UitBTw = (pQcOkh){wBCb = 32w1531371326,fwsC = xQNzSP,XbXc = 8w10,RNQF = 64w10};
        SYsGZI = 128w216323781136148277345578055083500959293;
        UitBTw.wBCb = 32w2554680596;
        UitBTw.XbXc = 8w10;
        ZqTDGWH();
        SYsGZI = SZxu;
        SYsGZI = 128w340282366920938463463374607431768211446;
        SYsGZI = -(SYsGZI |-| 128w294999660554044817754265939658325384524 >> 8w10);
        bit<32> GSuYjJ = ~UitBTw.wBCb;
        UitBTw.XbXc = 8w10;
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
            128w10                 : exact @name("vdbGnq") ;
            32w10                  : exact @name("TWbDDS") ;
            64w17488452717387411170: exact @name("RXlgBk") ;
        }
        actions = {
            @defaultonly NoAction();
        }
        default_action = NoAction();
    }
    table YSvMfd {
        key = {
            128w0: exact @name("iZjain") ;
        }
        actions = {
            @defaultonly NoAction();
        }
        default_action = NoAction();
    }
    apply {
        xQNzSP = 32w0;
        ZqTDGWH();
        SYsGZI = SYsGZI;
        xQNzSP = xQNzSP;
        IBaXWsK(64w10, 16w0);
        SYsGZI = 128w10;
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
    bit<8> TCVSkL = 8w10;
    PFizfTj() IArlRL;
    action dpTJp() {
        IBaXWsK(64w6943846788549823044, 16w10);
        IArlRL.apply(h.eth_hdr.eth_type, 128w10);
        return;
        h.eth_hdr.src_addr = 48w281474897995198;
        const bit<32> QlaOEA = 32w10;
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
        h.zkbz.WNfX = 16w58664;
        IBaXWsK(64w11378255015260334646, 16w59162);
        IArlRL.apply(h.zkbz.WNfX, 128w10);
        IBaXWsK(64w10, 16w10);
        h.BqNk.iUNX = h.zkbz.mjHD;
        ZqTDGWH();
        h.BqNk.YwAD = 64w10;
        h.BqNk.YwAD = h.BqNk.YwAD;
        const bit<16> oOqmbD = 16w10;
    }
}

parser Parser(packet_in b, out Headers hdr);
control Ingress(inout Headers hdr);
package top(Parser p, Ingress ig);
top(p(), ingress()) main;

