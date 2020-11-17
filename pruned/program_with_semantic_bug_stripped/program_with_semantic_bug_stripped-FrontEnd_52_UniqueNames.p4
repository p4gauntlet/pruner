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

parser p(packet_in pkt, out Headers hdr) {
    state start {
        pkt.extract<ethernet_t>(hdr.eth_hdr);
        pkt.extract<jCFTwO>(hdr.BqNk);
        pkt.extract<kTchlw>(hdr.zkbz);
        transition accept;
    }
}

control ingress(inout Headers h) {
    @name("IArlRL.xQNzSP") bit<32> IArlRL_xQNzSP_0;
    @name("IArlRL.SYsGZI") bit<128> IArlRL_SYsGZI_0;
    apply {
        {
            @name("hasReturned_0") bool hasReturned_1 = false;
            @name("retval_0") Vnytmj retval_1;
            @name("kXmlrB") bit<8> kXmlrB;
            kXmlrB = 8w10;
            kXmlrB = kXmlrB;
            {
                @name("hasReturned") bool hasReturned_2 = false;
                @name("retval") bit<32> retval_2;
                @name("sGPTcR") bit<64> sGPTcR;
                @name("LRpMbf") bit<32> LRpMbf;
                sGPTcR = 64w10;
                LRpMbf = 32w10;
                hasReturned_2 = true;
                retval_2 = LRpMbf;
            }
            hasReturned_1 = true;
            retval_1 = (Vnytmj){PZdb = false,xjKr = (bit<32>)64w11378255015260334646,pBFG = 16w14442,VYDJ = false,GXQs = 128w127537729978999984111170865926198740152};
        }
        IArlRL_SYsGZI_0 = 128w10;
        IArlRL_xQNzSP_0 = 32w0;
        {
            @name("hasReturned") bool hasReturned_2 = false;
            @name("retval") bit<32> retval_2;
            @name("sGPTcR") bit<64> sGPTcR;
            @name("LRpMbf") bit<32> LRpMbf;
            sGPTcR = 64w10;
            LRpMbf = 32w10;
            hasReturned_2 = true;
            retval_2 = LRpMbf;
        }
        {
            @name("hasReturned_0") bool hasReturned_1 = false;
            @name("retval_0") Vnytmj retval_3;
            @name("kXmlrB") bit<8> kXmlrB;
            kXmlrB = 8w10;
            kXmlrB = kXmlrB;
            {
                @name("hasReturned") bool hasReturned_2 = false;
                @name("retval") bit<32> retval_2;
                @name("sGPTcR") bit<64> sGPTcR;
                @name("LRpMbf") bit<32> LRpMbf;
                sGPTcR = 64w10;
                LRpMbf = 32w10;
                hasReturned_2 = true;
                retval_2 = LRpMbf;
            }
            hasReturned_1 = true;
            retval_3 = (Vnytmj){PZdb = false,xjKr = (bit<32>)64w10,pBFG = 16w14442,VYDJ = false,GXQs = 128w127537729978999984111170865926198740152};
        }
        {
            @name("hasReturned_0") bool hasReturned_1 = false;
            @name("retval_0") Vnytmj retval_4;
            @name("kXmlrB") bit<8> kXmlrB;
            kXmlrB = 8w10;
            kXmlrB = kXmlrB;
            {
                @name("hasReturned") bool hasReturned_2 = false;
                @name("retval") bit<32> retval_2;
                @name("sGPTcR") bit<64> sGPTcR;
                @name("LRpMbf") bit<32> LRpMbf;
                sGPTcR = 64w10;
                LRpMbf = 32w10;
                hasReturned_2 = true;
                retval_2 = LRpMbf;
            }
            hasReturned_1 = true;
            retval_4 = (Vnytmj){PZdb = false,xjKr = (bit<32>)64w10,pBFG = 16w14442,VYDJ = false,GXQs = 128w127537729978999984111170865926198740152};
        }
        h.BqNk.iUNX = h.zkbz.mjHD;
        {
            @name("hasReturned") bool hasReturned_2 = false;
            @name("retval") bit<32> retval_2;
            @name("sGPTcR") bit<64> sGPTcR;
            @name("LRpMbf") bit<32> LRpMbf;
            sGPTcR = 64w10;
            LRpMbf = 32w10;
            hasReturned_2 = true;
            retval_2 = LRpMbf;
        }
        h.BqNk.YwAD = 64w10;
        h.BqNk.YwAD = h.BqNk.YwAD;
    }
}

parser Parser(packet_in b, out Headers hdr);
control Ingress(inout Headers hdr);
package top(Parser p, Ingress ig);
top(p(), ingress()) main;

