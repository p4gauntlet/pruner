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
    @name("ingress.tmp_8") bool tmp_17;
    @name("ingress.tmp_8") bool tmp_40;
    @name("ingress.tmp_8") bool tmp_51;
    apply {
        {
            if (!((bit<9>)(32w37657 |-| (bit<32>)64w8331771506825847071) | 9w260 != (bit<9>)(32w37657 |-| (bit<32>)64w8331771506825847071))) {
                tmp_17 = false;
            } else {
                tmp_17 = false;
            }
        }
        {
            if (!((bit<9>)(32w37657 |-| (bit<32>)64w8331771506825847071) | 9w260 != (bit<9>)(32w37657 |-| (bit<32>)64w8331771506825847071))) {
                tmp_40 = false;
            } else {
                tmp_40 = false;
            }
        }
        {
            if (!((bit<9>)(32w37657 |-| (bit<32>)64w8331771506825847071) | 9w260 != (bit<9>)(32w37657 |-| (bit<32>)64w8331771506825847071))) {
                tmp_51 = false;
            } else {
                tmp_51 = false;
            }
        }
        h.BqNk.iUNX = h.zkbz.mjHD;
        h.BqNk.YwAD = 64w4314245641897930119;
        h.BqNk.YwAD = 64w4314245641897930119;
    }
}

parser Parser(packet_in b, out Headers hdr);
control Ingress(inout Headers hdr);
package top(Parser p, Ingress ig);
top(p(), ingress()) main;

