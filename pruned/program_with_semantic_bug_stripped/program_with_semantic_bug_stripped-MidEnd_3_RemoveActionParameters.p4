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
    @name("ingress.IArlRL.xQNzSP") bit<32> IArlRL_xQNzSP;
    @name("ingress.IArlRL.SYsGZI") bit<128> IArlRL_SYsGZI;
    @name("ingress.hasReturned_0") bool hasReturned;
    @name("ingress.retval_0") Vnytmj retval;
    @name("ingress.kXmlrB") bit<8> kXmlrB_0;
    @name("ingress.hasReturned") bool hasReturned_0;
    @name("ingress.retval") bit<32> retval_0;
    @name("ingress.sGPTcR") bit<64> sGPTcR_0;
    @name("ingress.LRpMbf") bit<32> LRpMbf_0;
    @name("ingress.hasReturned") bool hasReturned_3;
    @name("ingress.retval") bit<32> retval_5;
    @name("ingress.sGPTcR") bit<64> sGPTcR_1;
    @name("ingress.LRpMbf") bit<32> LRpMbf_1;
    @name("ingress.hasReturned_0") bool hasReturned_4;
    @name("ingress.retval_0") Vnytmj retval_6;
    @name("ingress.kXmlrB") bit<8> kXmlrB_1;
    @name("ingress.hasReturned") bool hasReturned_5;
    @name("ingress.retval") bit<32> retval_7;
    @name("ingress.sGPTcR") bit<64> sGPTcR_2;
    @name("ingress.LRpMbf") bit<32> LRpMbf_2;
    @name("ingress.hasReturned_0") bool hasReturned_6;
    @name("ingress.retval_0") Vnytmj retval_8;
    @name("ingress.kXmlrB") bit<8> kXmlrB_2;
    @name("ingress.hasReturned") bool hasReturned_7;
    @name("ingress.retval") bit<32> retval_9;
    @name("ingress.sGPTcR") bit<64> sGPTcR_3;
    @name("ingress.LRpMbf") bit<32> LRpMbf_3;
    @name("ingress.hasReturned") bool hasReturned_8;
    @name("ingress.retval") bit<32> retval_10;
    @name("ingress.sGPTcR") bit<64> sGPTcR_4;
    @name("ingress.LRpMbf") bit<32> LRpMbf_4;
    apply {
        {
            hasReturned = false;
            kXmlrB_0 = 8w10;
            kXmlrB_0 = kXmlrB_0;
            {
                hasReturned_0 = false;
                sGPTcR_0 = 64w10;
                LRpMbf_0 = 32w10;
                hasReturned_0 = true;
                retval_0 = LRpMbf_0;
            }
            hasReturned = true;
            retval = (Vnytmj){PZdb = false,xjKr = (bit<32>)64w11378255015260334646,pBFG = 16w14442,VYDJ = false,GXQs = 128w127537729978999984111170865926198740152};
        }
        IArlRL_SYsGZI = 128w10;
        IArlRL_xQNzSP = 32w0;
        {
            hasReturned_3 = false;
            sGPTcR_1 = 64w10;
            LRpMbf_1 = 32w10;
            hasReturned_3 = true;
            retval_5 = LRpMbf_1;
        }
        {
            hasReturned_4 = false;
            kXmlrB_1 = 8w10;
            kXmlrB_1 = kXmlrB_1;
            {
                hasReturned_5 = false;
                sGPTcR_2 = 64w10;
                LRpMbf_2 = 32w10;
                hasReturned_5 = true;
                retval_7 = LRpMbf_2;
            }
            hasReturned_4 = true;
            retval_6 = (Vnytmj){PZdb = false,xjKr = (bit<32>)64w10,pBFG = 16w14442,VYDJ = false,GXQs = 128w127537729978999984111170865926198740152};
        }
        {
            hasReturned_6 = false;
            kXmlrB_2 = 8w10;
            kXmlrB_2 = kXmlrB_2;
            {
                hasReturned_7 = false;
                sGPTcR_3 = 64w10;
                LRpMbf_3 = 32w10;
                hasReturned_7 = true;
                retval_9 = LRpMbf_3;
            }
            hasReturned_6 = true;
            retval_8 = (Vnytmj){PZdb = false,xjKr = (bit<32>)64w10,pBFG = 16w14442,VYDJ = false,GXQs = 128w127537729978999984111170865926198740152};
        }
        h.BqNk.iUNX = h.zkbz.mjHD;
        {
            hasReturned_8 = false;
            sGPTcR_4 = 64w10;
            LRpMbf_4 = 32w10;
            hasReturned_8 = true;
            retval_10 = LRpMbf_4;
        }
        h.BqNk.YwAD = 64w10;
        h.BqNk.YwAD = h.BqNk.YwAD;
    }
}

parser Parser(packet_in b, out Headers hdr);
control Ingress(inout Headers hdr);
package top(Parser p, Ingress ig);
top(p(), ingress()) main;

