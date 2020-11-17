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
    @name("tmp_14") bit<16> tmp_10;
    @name("tmp_15") bit<32> tmp_11;
    @name("tmp_16") bit<16> tmp_12;
    @name("tmp_17") bit<16> tmp_13;
    @name("tmp_18") bit<16> tmp_19;
    @name("IArlRL.xQNzSP") bit<32> IArlRL_xQNzSP_0;
    @name("IArlRL.SYsGZI") bit<128> IArlRL_SYsGZI_0;
    @name("IArlRL.tmp_10") bit<32> IArlRL_tmp_3;
    @name("IArlRL.tmp_11") bit<32> IArlRL_tmp_4;
    @name("IArlRL.tmp_12") bit<32> IArlRL_tmp_5;
    @name("IArlRL.tmp_13") bit<32> IArlRL_tmp_6;
    apply {
        tmp_10 = h.eth_hdr.eth_type;
        {
            @name("hasReturned") bool hasReturned_1 = false;
            @name("retval") bit<32> retval_1;
            @name("sGPTcR") bit<64> sGPTcR;
            @name("LRpMbf") bit<32> LRpMbf;
            sGPTcR = 64w8331771506825847071;
            sGPTcR = sGPTcR;
            LRpMbf = 32w37657 |-| (bit<32>)sGPTcR;
            hasReturned_1 = true;
            retval_1 = LRpMbf;
            tmp_11 = retval_1;
        }
        tmp_12 = tmp_10 | (bit<16>)tmp_11;
        tmp_13 = tmp_12 | 16w58652;
        tmp_19 = tmp_13 + 16w30345;
        {
            @name("hasReturned_0") bool hasReturned_2 = false;
            @name("retval_0") Vnytmj retval_2;
            @name("tmp") bool tmp_20;
            @name("tmp_0") bit<32> tmp_21;
            @name("tmp_1") bit<16> tmp_22;
            @name("tmp_2") bool tmp_23;
            @name("tmp_3") bit<9> tmp_24;
            @name("tmp_4") bit<32> tmp_25;
            @name("tmp_5") bit<9> tmp_26;
            @name("tmp_6") bit<32> tmp_27;
            @name("tmp_7") bool tmp_28;
            @name("tmp_8") bool tmp_29;
            @name("tmp_9") bit<128> tmp_30;
            @name("kXmlrB") bit<8> kXmlrB;
            kXmlrB = ((bit<43>)64w11378255015260334646 |+| 43w1462566353592)[16:9];
            kXmlrB = kXmlrB;
            {
                @name("hasReturned") bool hasReturned_1 = false;
                @name("retval") bit<32> retval_1;
                @name("sGPTcR") bit<64> sGPTcR;
                @name("LRpMbf") bit<32> LRpMbf;
                sGPTcR = 64w8331771506825847071;
                sGPTcR = sGPTcR;
                LRpMbf = 32w37657 |-| (bit<32>)sGPTcR;
                hasReturned_1 = true;
                retval_1 = LRpMbf;
            }
            tmp_20 = false;
            tmp_21 = (bit<32>)64w11378255015260334646;
            tmp_22 = 16w14442;
            {
                @name("hasReturned") bool hasReturned_1 = false;
                @name("retval") bit<32> retval_1;
                @name("sGPTcR") bit<64> sGPTcR;
                @name("LRpMbf") bit<32> LRpMbf;
                sGPTcR = 64w8331771506825847071;
                sGPTcR = sGPTcR;
                LRpMbf = 32w37657 |-| (bit<32>)sGPTcR;
                hasReturned_1 = true;
                retval_1 = LRpMbf;
                tmp_25 = retval_1;
            }
            tmp_26 = (bit<9>)tmp_25 | 9w260;
            tmp_24 = tmp_26;
            {
                @name("hasReturned") bool hasReturned_1 = false;
                @name("retval") bit<32> retval_1;
                @name("sGPTcR") bit<64> sGPTcR;
                @name("LRpMbf") bit<32> LRpMbf;
                sGPTcR = 64w8331771506825847071;
                sGPTcR = sGPTcR;
                LRpMbf = 32w37657 |-| (bit<32>)sGPTcR;
                hasReturned_1 = true;
                retval_1 = LRpMbf;
                tmp_27 = retval_1;
            }
            tmp_28 = tmp_24 != (bit<9>)tmp_27;
            if (!tmp_28) {
                tmp_29 = false;
            } else {
                tmp_29 = 51w1444364813109517 == (bit<51>)16w59162;
            }
            tmp_23 = tmp_29;
            tmp_30 = 128w127537729978999984111170865926198740152;
            hasReturned_2 = true;
            retval_2 = (Vnytmj){PZdb = tmp_20,xjKr = tmp_21,pBFG = tmp_22,VYDJ = tmp_23,GXQs = tmp_30};
        }
        IArlRL_xQNzSP_0 = 32w1305108261;
        IArlRL_SYsGZI_0 = 128w18672238;
        IArlRL_tmp_3 = IArlRL_xQNzSP_0;
        {
            @name("hasReturned") bool hasReturned_1 = false;
            @name("retval") bit<32> retval_1;
            @name("sGPTcR") bit<64> sGPTcR;
            @name("LRpMbf") bit<32> LRpMbf;
            sGPTcR = 64w8331771506825847071;
            sGPTcR = sGPTcR;
            LRpMbf = 32w37657 |-| (bit<32>)sGPTcR;
            hasReturned_1 = true;
            retval_1 = LRpMbf;
            IArlRL_tmp_4 = retval_1;
        }
        IArlRL_tmp_5 = IArlRL_tmp_3 + IArlRL_tmp_4;
        IArlRL_tmp_6 = IArlRL_tmp_5 |-| 32w2827375294;
        IArlRL_xQNzSP_0 = IArlRL_tmp_6;
        {
            @name("hasReturned") bool hasReturned_1 = false;
            @name("retval") bit<32> retval_1;
            @name("sGPTcR") bit<64> sGPTcR;
            @name("LRpMbf") bit<32> LRpMbf;
            sGPTcR = 64w8331771506825847071;
            sGPTcR = sGPTcR;
            LRpMbf = 32w37657 |-| (bit<32>)sGPTcR;
            hasReturned_1 = true;
            retval_1 = LRpMbf;
        }
        IArlRL_SYsGZI_0 = IArlRL_SYsGZI_0;
        {
            @name("hasReturned_0") bool hasReturned_2 = false;
            @name("retval_0") Vnytmj retval_3;
            @name("tmp") bool tmp_20;
            @name("tmp_0") bit<32> tmp_21;
            @name("tmp_1") bit<16> tmp_22;
            @name("tmp_2") bool tmp_23;
            @name("tmp_3") bit<9> tmp_24;
            @name("tmp_4") bit<32> tmp_25;
            @name("tmp_5") bit<9> tmp_26;
            @name("tmp_6") bit<32> tmp_27;
            @name("tmp_7") bool tmp_28;
            @name("tmp_8") bool tmp_29;
            @name("tmp_9") bit<128> tmp_30;
            @name("kXmlrB") bit<8> kXmlrB;
            kXmlrB = ((bit<43>)64w9569382937354443357 |+| 43w1462566353592)[16:9];
            kXmlrB = kXmlrB;
            {
                @name("hasReturned") bool hasReturned_1 = false;
                @name("retval") bit<32> retval_1;
                @name("sGPTcR") bit<64> sGPTcR;
                @name("LRpMbf") bit<32> LRpMbf;
                sGPTcR = 64w8331771506825847071;
                sGPTcR = sGPTcR;
                LRpMbf = 32w37657 |-| (bit<32>)sGPTcR;
                hasReturned_1 = true;
                retval_1 = LRpMbf;
            }
            tmp_20 = false;
            tmp_21 = (bit<32>)64w9569382937354443357;
            tmp_22 = 16w14442;
            {
                @name("hasReturned") bool hasReturned_1 = false;
                @name("retval") bit<32> retval_1;
                @name("sGPTcR") bit<64> sGPTcR;
                @name("LRpMbf") bit<32> LRpMbf;
                sGPTcR = 64w8331771506825847071;
                sGPTcR = sGPTcR;
                LRpMbf = 32w37657 |-| (bit<32>)sGPTcR;
                hasReturned_1 = true;
                retval_1 = LRpMbf;
                tmp_25 = retval_1;
            }
            tmp_26 = (bit<9>)tmp_25 | 9w260;
            tmp_24 = tmp_26;
            {
                @name("hasReturned") bool hasReturned_1 = false;
                @name("retval") bit<32> retval_1;
                @name("sGPTcR") bit<64> sGPTcR;
                @name("LRpMbf") bit<32> LRpMbf;
                sGPTcR = 64w8331771506825847071;
                sGPTcR = sGPTcR;
                LRpMbf = 32w37657 |-| (bit<32>)sGPTcR;
                hasReturned_1 = true;
                retval_1 = LRpMbf;
                tmp_27 = retval_1;
            }
            tmp_28 = tmp_24 != (bit<9>)tmp_27;
            if (!tmp_28) {
                tmp_29 = false;
            } else {
                tmp_29 = 51w1444364813109517 == (bit<51>)16w0;
            }
            tmp_23 = tmp_29;
            tmp_30 = 128w127537729978999984111170865926198740152;
            hasReturned_2 = true;
            retval_3 = (Vnytmj){PZdb = tmp_20,xjKr = tmp_21,pBFG = tmp_22,VYDJ = tmp_23,GXQs = tmp_30};
        }
        {
            @name("hasReturned_0") bool hasReturned_2 = false;
            @name("retval_0") Vnytmj retval_4;
            @name("tmp") bool tmp_20;
            @name("tmp_0") bit<32> tmp_21;
            @name("tmp_1") bit<16> tmp_22;
            @name("tmp_2") bool tmp_23;
            @name("tmp_3") bit<9> tmp_24;
            @name("tmp_4") bit<32> tmp_25;
            @name("tmp_5") bit<9> tmp_26;
            @name("tmp_6") bit<32> tmp_27;
            @name("tmp_7") bool tmp_28;
            @name("tmp_8") bool tmp_29;
            @name("tmp_9") bit<128> tmp_30;
            @name("kXmlrB") bit<8> kXmlrB;
            kXmlrB = ((bit<43>)64w16257984866694305357 |+| 43w1462566353592)[16:9];
            kXmlrB = kXmlrB;
            {
                @name("hasReturned") bool hasReturned_1 = false;
                @name("retval") bit<32> retval_1;
                @name("sGPTcR") bit<64> sGPTcR;
                @name("LRpMbf") bit<32> LRpMbf;
                sGPTcR = 64w8331771506825847071;
                sGPTcR = sGPTcR;
                LRpMbf = 32w37657 |-| (bit<32>)sGPTcR;
                hasReturned_1 = true;
                retval_1 = LRpMbf;
            }
            tmp_20 = false;
            tmp_21 = (bit<32>)64w16257984866694305357;
            tmp_22 = 16w14442;
            {
                @name("hasReturned") bool hasReturned_1 = false;
                @name("retval") bit<32> retval_1;
                @name("sGPTcR") bit<64> sGPTcR;
                @name("LRpMbf") bit<32> LRpMbf;
                sGPTcR = 64w8331771506825847071;
                sGPTcR = sGPTcR;
                LRpMbf = 32w37657 |-| (bit<32>)sGPTcR;
                hasReturned_1 = true;
                retval_1 = LRpMbf;
                tmp_25 = retval_1;
            }
            tmp_26 = (bit<9>)tmp_25 | 9w260;
            tmp_24 = tmp_26;
            {
                @name("hasReturned") bool hasReturned_1 = false;
                @name("retval") bit<32> retval_1;
                @name("sGPTcR") bit<64> sGPTcR;
                @name("LRpMbf") bit<32> LRpMbf;
                sGPTcR = 64w8331771506825847071;
                sGPTcR = sGPTcR;
                LRpMbf = 32w37657 |-| (bit<32>)sGPTcR;
                hasReturned_1 = true;
                retval_1 = LRpMbf;
                tmp_27 = retval_1;
            }
            tmp_28 = tmp_24 != (bit<9>)tmp_27;
            if (!tmp_28) {
                tmp_29 = false;
            } else {
                tmp_29 = 51w1444364813109517 == (bit<51>)16w65535;
            }
            tmp_23 = tmp_29;
            tmp_30 = 128w127537729978999984111170865926198740152;
            hasReturned_2 = true;
            retval_4 = (Vnytmj){PZdb = tmp_20,xjKr = tmp_21,pBFG = tmp_22,VYDJ = tmp_23,GXQs = tmp_30};
        }
        h.BqNk.iUNX = h.zkbz.mjHD;
        {
            @name("hasReturned") bool hasReturned_1 = false;
            @name("retval") bit<32> retval_1;
            @name("sGPTcR") bit<64> sGPTcR;
            @name("LRpMbf") bit<32> LRpMbf;
            sGPTcR = 64w8331771506825847071;
            sGPTcR = sGPTcR;
            LRpMbf = 32w37657 |-| (bit<32>)sGPTcR;
            hasReturned_1 = true;
            retval_1 = LRpMbf;
        }
        h.BqNk.YwAD = 64w4314245641897930119;
        h.BqNk.YwAD = h.BqNk.YwAD;
    }
}

parser Parser(packet_in b, out Headers hdr);
control Ingress(inout Headers hdr);
package top(Parser p, Ingress ig);
top(p(), ingress()) main;

