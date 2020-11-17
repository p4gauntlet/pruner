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
    @name("sGPTcR") bit<64> sGPTcR_0;
    @name("LRpMbf") bit<32> LRpMbf_0;
    @name("noVnDj") bit<64> noVnDj_0;
    @name("AfXLZG") bit<128> AfXLZG_0;
    {
        sGPTcR_0 = 64w10;
        {
            sGPTcR_0 = sGPTcR_0;
            LRpMbf_0 = 32w10;
            sGPTcR_0 = 64w152762851772443914;
            return LRpMbf_0;
        }
        sGPTcR_0 = sGPTcR_0;
        noVnDj_0 = 64w10;
        noVnDj_0 = 64w10;
        noVnDj_0 = 64w859692371;
        sGPTcR_0 = 64w0;
        sGPTcR_0 = 64w10240 + noVnDj_0;
        return 32w10;
    }
    AfXLZG_0 = 128w2144402680;
    AfXLZG_0 = 128w10;
    AfXLZG_0 = AfXLZG_0;
    AfXLZG_0 = AfXLZG_0;
    AfXLZG_0 = 128w10;
    AfXLZG_0 = AfXLZG_0;
    {
        AfXLZG_0 = 128w10;
        AfXLZG_0 = 128w119851796932508784808775619006417521460;
        AfXLZG_0 = 128w10;
        AfXLZG_0 = AfXLZG_0;
        AfXLZG_0 = 128w10;
        AfXLZG_0 = 128w10;
        AfXLZG_0 = AfXLZG_0;
        return 32w10;
    }
    return 32w10;
}
Vnytmj IBaXWsK(bit<64> yQJV, bit<16> gOEI) {
    @name("kXmlrB") bit<8> kXmlrB_0;
    kXmlrB_0 = 8w10;
    {
        kXmlrB_0 = kXmlrB_0;
        kXmlrB_0 = kXmlrB_0;
        ZqTDGWH();
        kXmlrB_0 = 8w174;
        return (Vnytmj){PZdb = false,xjKr = (bit<32>)yQJV,pBFG = 16w14442,VYDJ = false,GXQs = 128w127537729978999984111170865926198740152};
    }
    kXmlrB_0 = 8w10;
    kXmlrB_0 = kXmlrB_0;
    ZqTDGWH();
    return (Vnytmj){PZdb = true,xjKr = 32w1354969928,pBFG = 16w10,VYDJ = true,GXQs = 128w10};
}
control PFizfTj(out bit<16> lcNR, bit<128> SZxu) {
    @name("xQNzSP") bit<32> xQNzSP_0;
    @name("SYsGZI") bit<128> SYsGZI_0;
    apply {
        xQNzSP_0 = 32w10;
        SYsGZI_0 = 128w10;
        xQNzSP_0 = 32w0;
        ZqTDGWH();
        SYsGZI_0 = SYsGZI_0;
        xQNzSP_0 = xQNzSP_0;
        IBaXWsK(64w10, 16w0);
        SYsGZI_0 = 128w10;
    }
}

parser p(packet_in pkt, out Headers hdr) {
    state start {
        pkt.extract<ethernet_t>(hdr.eth_hdr);
        pkt.extract<jCFTwO>(hdr.BqNk);
        pkt.extract<kTchlw>(hdr.zkbz);
        transition accept;
    }
}

control ingress(inout Headers h) {
    @name("IArlRL") PFizfTj() IArlRL_0;
    apply {
        h.zkbz.WNfX = 16w58664;
        IBaXWsK(64w11378255015260334646, 16w59162);
        IArlRL_0.apply(h.zkbz.WNfX, 128w10);
        IBaXWsK(64w10, 16w10);
        h.BqNk.iUNX = h.zkbz.mjHD;
        ZqTDGWH();
        h.BqNk.YwAD = 64w10;
        h.BqNk.YwAD = h.BqNk.YwAD;
    }
}

parser Parser(packet_in b, out Headers hdr);
control Ingress(inout Headers hdr);
package top(Parser p, Ingress ig);
top(p(), ingress()) main;

