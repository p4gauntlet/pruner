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
    @name("tmp_14") bit<16> tmp;
    @name("tmp_15") bit<32> tmp_0;
    @name("tmp_16") bit<16> tmp_1;
    @name("tmp_17") bit<16> tmp_2;
    @name("tmp_18") bit<16> tmp_3;
    @name("IArlRL.xQNzSP") bit<32> IArlRL_xQNzSP;
    @name("IArlRL.SYsGZI") bit<128> IArlRL_SYsGZI;
    @name("IArlRL.tmp_10") bit<32> IArlRL_tmp;
    @name("IArlRL.tmp_11") bit<32> IArlRL_tmp_0;
    @name("IArlRL.tmp_12") bit<32> IArlRL_tmp_1;
    @name("IArlRL.tmp_13") bit<32> IArlRL_tmp_2;
    apply {
        tmp = h.eth_hdr.eth_type;
        {
            @name("hasReturned") bool hasReturned = false;
            @name("retval") bit<32> retval;
            @name("sGPTcR") bit<64> sGPTcR_0;
            @name("LRpMbf") bit<32> LRpMbf_0;
            sGPTcR_0 = 64w8331771506825847071;
            sGPTcR_0 = sGPTcR_0;
            LRpMbf_0 = 32w37657 |-| (bit<32>)sGPTcR_0;
            hasReturned = true;
            retval = LRpMbf_0;
            tmp_0 = retval;
        }
        tmp_1 = tmp | (bit<16>)tmp_0;
        tmp_2 = tmp_1 | 16w58652;
        tmp_3 = tmp_2 + 16w30345;
        {
            @name("hasReturned_0") bool hasReturned_0 = false;
            @name("retval_0") Vnytmj retval_0;
            @name("tmp") bool tmp_4;
            @name("tmp_0") bit<32> tmp_5;
            @name("tmp_1") bit<16> tmp_6;
            @name("tmp_2") bool tmp_7;
            @name("tmp_3") bit<9> tmp_8;
            @name("tmp_4") bit<32> tmp_9;
            @name("tmp_5") bit<9> tmp_14;
            @name("tmp_6") bit<32> tmp_15;
            @name("tmp_7") bool tmp_16;
            @name("tmp_8") bool tmp_17;
            @name("tmp_9") bit<128> tmp_18;
            @name("kXmlrB") bit<8> kXmlrB_0;
            kXmlrB_0 = ((bit<43>)64w11378255015260334646 |+| 43w1462566353592)[16:9];
            kXmlrB_0 = kXmlrB_0;
            {
                @name("hasReturned") bool hasReturned_3 = false;
                @name("retval") bit<32> retval_5;
                @name("sGPTcR") bit<64> sGPTcR_1;
                @name("LRpMbf") bit<32> LRpMbf_1;
                sGPTcR_1 = 64w8331771506825847071;
                sGPTcR_1 = sGPTcR_1;
                LRpMbf_1 = 32w37657 |-| (bit<32>)sGPTcR_1;
                hasReturned_3 = true;
                retval_5 = LRpMbf_1;
            }
            tmp_4 = false;
            tmp_5 = (bit<32>)64w11378255015260334646;
            tmp_6 = 16w14442;
            {
                @name("hasReturned") bool hasReturned_4 = false;
                @name("retval") bit<32> retval_6;
                @name("sGPTcR") bit<64> sGPTcR_2;
                @name("LRpMbf") bit<32> LRpMbf_2;
                sGPTcR_2 = 64w8331771506825847071;
                sGPTcR_2 = sGPTcR_2;
                LRpMbf_2 = 32w37657 |-| (bit<32>)sGPTcR_2;
                hasReturned_4 = true;
                retval_6 = LRpMbf_2;
                tmp_9 = retval_6;
            }
            tmp_14 = (bit<9>)tmp_9 | 9w260;
            tmp_8 = tmp_14;
            {
                @name("hasReturned") bool hasReturned_5 = false;
                @name("retval") bit<32> retval_7;
                @name("sGPTcR") bit<64> sGPTcR_3;
                @name("LRpMbf") bit<32> LRpMbf_3;
                sGPTcR_3 = 64w8331771506825847071;
                sGPTcR_3 = sGPTcR_3;
                LRpMbf_3 = 32w37657 |-| (bit<32>)sGPTcR_3;
                hasReturned_5 = true;
                retval_7 = LRpMbf_3;
                tmp_15 = retval_7;
            }
            tmp_16 = tmp_8 != (bit<9>)tmp_15;
            if (!tmp_16) {
                tmp_17 = false;
            } else {
                tmp_17 = 51w1444364813109517 == (bit<51>)16w59162;
            }
            tmp_7 = tmp_17;
            tmp_18 = 128w127537729978999984111170865926198740152;
            hasReturned_0 = true;
            retval_0 = (Vnytmj){PZdb = tmp_4,xjKr = tmp_5,pBFG = tmp_6,VYDJ = tmp_7,GXQs = tmp_18};
        }
        IArlRL_xQNzSP = 32w1305108261;
        IArlRL_SYsGZI = 128w18672238;
        IArlRL_tmp = IArlRL_xQNzSP;
        {
            @name("hasReturned") bool hasReturned_6 = false;
            @name("retval") bit<32> retval_8;
            @name("sGPTcR") bit<64> sGPTcR_4;
            @name("LRpMbf") bit<32> LRpMbf_4;
            sGPTcR_4 = 64w8331771506825847071;
            sGPTcR_4 = sGPTcR_4;
            LRpMbf_4 = 32w37657 |-| (bit<32>)sGPTcR_4;
            hasReturned_6 = true;
            retval_8 = LRpMbf_4;
            IArlRL_tmp_0 = retval_8;
        }
        IArlRL_tmp_1 = IArlRL_tmp + IArlRL_tmp_0;
        IArlRL_tmp_2 = IArlRL_tmp_1 |-| 32w2827375294;
        IArlRL_xQNzSP = IArlRL_tmp_2;
        {
            @name("hasReturned") bool hasReturned_7 = false;
            @name("retval") bit<32> retval_9;
            @name("sGPTcR") bit<64> sGPTcR_5;
            @name("LRpMbf") bit<32> LRpMbf_5;
            sGPTcR_5 = 64w8331771506825847071;
            sGPTcR_5 = sGPTcR_5;
            LRpMbf_5 = 32w37657 |-| (bit<32>)sGPTcR_5;
            hasReturned_7 = true;
            retval_9 = LRpMbf_5;
        }
        IArlRL_SYsGZI = IArlRL_SYsGZI;
        {
            @name("hasReturned_0") bool hasReturned_8 = false;
            @name("retval_0") Vnytmj retval_10;
            @name("tmp") bool tmp_31;
            @name("tmp_0") bit<32> tmp_32;
            @name("tmp_1") bit<16> tmp_33;
            @name("tmp_2") bool tmp_34;
            @name("tmp_3") bit<9> tmp_35;
            @name("tmp_4") bit<32> tmp_36;
            @name("tmp_5") bit<9> tmp_37;
            @name("tmp_6") bit<32> tmp_38;
            @name("tmp_7") bool tmp_39;
            @name("tmp_8") bool tmp_40;
            @name("tmp_9") bit<128> tmp_41;
            @name("kXmlrB") bit<8> kXmlrB_1;
            kXmlrB_1 = ((bit<43>)64w9569382937354443357 |+| 43w1462566353592)[16:9];
            kXmlrB_1 = kXmlrB_1;
            {
                @name("hasReturned") bool hasReturned_9 = false;
                @name("retval") bit<32> retval_11;
                @name("sGPTcR") bit<64> sGPTcR_6;
                @name("LRpMbf") bit<32> LRpMbf_6;
                sGPTcR_6 = 64w8331771506825847071;
                sGPTcR_6 = sGPTcR_6;
                LRpMbf_6 = 32w37657 |-| (bit<32>)sGPTcR_6;
                hasReturned_9 = true;
                retval_11 = LRpMbf_6;
            }
            tmp_31 = false;
            tmp_32 = (bit<32>)64w9569382937354443357;
            tmp_33 = 16w14442;
            {
                @name("hasReturned") bool hasReturned_10 = false;
                @name("retval") bit<32> retval_12;
                @name("sGPTcR") bit<64> sGPTcR_7;
                @name("LRpMbf") bit<32> LRpMbf_7;
                sGPTcR_7 = 64w8331771506825847071;
                sGPTcR_7 = sGPTcR_7;
                LRpMbf_7 = 32w37657 |-| (bit<32>)sGPTcR_7;
                hasReturned_10 = true;
                retval_12 = LRpMbf_7;
                tmp_36 = retval_12;
            }
            tmp_37 = (bit<9>)tmp_36 | 9w260;
            tmp_35 = tmp_37;
            {
                @name("hasReturned") bool hasReturned_11 = false;
                @name("retval") bit<32> retval_13;
                @name("sGPTcR") bit<64> sGPTcR_8;
                @name("LRpMbf") bit<32> LRpMbf_8;
                sGPTcR_8 = 64w8331771506825847071;
                sGPTcR_8 = sGPTcR_8;
                LRpMbf_8 = 32w37657 |-| (bit<32>)sGPTcR_8;
                hasReturned_11 = true;
                retval_13 = LRpMbf_8;
                tmp_38 = retval_13;
            }
            tmp_39 = tmp_35 != (bit<9>)tmp_38;
            if (!tmp_39) {
                tmp_40 = false;
            } else {
                tmp_40 = 51w1444364813109517 == (bit<51>)16w0;
            }
            tmp_34 = tmp_40;
            tmp_41 = 128w127537729978999984111170865926198740152;
            hasReturned_8 = true;
            retval_10 = (Vnytmj){PZdb = tmp_31,xjKr = tmp_32,pBFG = tmp_33,VYDJ = tmp_34,GXQs = tmp_41};
        }
        {
            @name("hasReturned_0") bool hasReturned_12 = false;
            @name("retval_0") Vnytmj retval_14;
            @name("tmp") bool tmp_42;
            @name("tmp_0") bit<32> tmp_43;
            @name("tmp_1") bit<16> tmp_44;
            @name("tmp_2") bool tmp_45;
            @name("tmp_3") bit<9> tmp_46;
            @name("tmp_4") bit<32> tmp_47;
            @name("tmp_5") bit<9> tmp_48;
            @name("tmp_6") bit<32> tmp_49;
            @name("tmp_7") bool tmp_50;
            @name("tmp_8") bool tmp_51;
            @name("tmp_9") bit<128> tmp_52;
            @name("kXmlrB") bit<8> kXmlrB_2;
            kXmlrB_2 = ((bit<43>)64w16257984866694305357 |+| 43w1462566353592)[16:9];
            kXmlrB_2 = kXmlrB_2;
            {
                @name("hasReturned") bool hasReturned_13 = false;
                @name("retval") bit<32> retval_15;
                @name("sGPTcR") bit<64> sGPTcR_9;
                @name("LRpMbf") bit<32> LRpMbf_9;
                sGPTcR_9 = 64w8331771506825847071;
                sGPTcR_9 = sGPTcR_9;
                LRpMbf_9 = 32w37657 |-| (bit<32>)sGPTcR_9;
                hasReturned_13 = true;
                retval_15 = LRpMbf_9;
            }
            tmp_42 = false;
            tmp_43 = (bit<32>)64w16257984866694305357;
            tmp_44 = 16w14442;
            {
                @name("hasReturned") bool hasReturned_14 = false;
                @name("retval") bit<32> retval_16;
                @name("sGPTcR") bit<64> sGPTcR_10;
                @name("LRpMbf") bit<32> LRpMbf_10;
                sGPTcR_10 = 64w8331771506825847071;
                sGPTcR_10 = sGPTcR_10;
                LRpMbf_10 = 32w37657 |-| (bit<32>)sGPTcR_10;
                hasReturned_14 = true;
                retval_16 = LRpMbf_10;
                tmp_47 = retval_16;
            }
            tmp_48 = (bit<9>)tmp_47 | 9w260;
            tmp_46 = tmp_48;
            {
                @name("hasReturned") bool hasReturned_15 = false;
                @name("retval") bit<32> retval_17;
                @name("sGPTcR") bit<64> sGPTcR_11;
                @name("LRpMbf") bit<32> LRpMbf_11;
                sGPTcR_11 = 64w8331771506825847071;
                sGPTcR_11 = sGPTcR_11;
                LRpMbf_11 = 32w37657 |-| (bit<32>)sGPTcR_11;
                hasReturned_15 = true;
                retval_17 = LRpMbf_11;
                tmp_49 = retval_17;
            }
            tmp_50 = tmp_46 != (bit<9>)tmp_49;
            if (!tmp_50) {
                tmp_51 = false;
            } else {
                tmp_51 = 51w1444364813109517 == (bit<51>)16w65535;
            }
            tmp_45 = tmp_51;
            tmp_52 = 128w127537729978999984111170865926198740152;
            hasReturned_12 = true;
            retval_14 = (Vnytmj){PZdb = tmp_42,xjKr = tmp_43,pBFG = tmp_44,VYDJ = tmp_45,GXQs = tmp_52};
        }
        h.BqNk.iUNX = h.zkbz.mjHD;
        {
            @name("hasReturned") bool hasReturned_16 = false;
            @name("retval") bit<32> retval_18;
            @name("sGPTcR") bit<64> sGPTcR_12;
            @name("LRpMbf") bit<32> LRpMbf_12;
            sGPTcR_12 = 64w8331771506825847071;
            sGPTcR_12 = sGPTcR_12;
            LRpMbf_12 = 32w37657 |-| (bit<32>)sGPTcR_12;
            hasReturned_16 = true;
            retval_18 = LRpMbf_12;
        }
        h.BqNk.YwAD = 64w4314245641897930119;
        h.BqNk.YwAD = h.BqNk.YwAD;
    }
}

parser Parser(packet_in b, out Headers hdr);
control Ingress(inout Headers hdr);
package top(Parser p, Ingress ig);
top(p(), ingress()) main;

