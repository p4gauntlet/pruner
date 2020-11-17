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
    bit<16> tmp_14;
    bit<32> tmp_15;
    bit<16> tmp_16;
    bit<16> tmp_17;
    bit<16> tmp_18;
    @name("IArlRL.xQNzSP") bit<32> IArlRL_xQNzSP;
    @name("IArlRL.SYsGZI") bit<128> IArlRL_SYsGZI;
    @name("IArlRL.tmp_10") bit<32> IArlRL_tmp;
    @name("IArlRL.tmp_11") bit<32> IArlRL_tmp_0;
    @name("IArlRL.tmp_12") bit<32> IArlRL_tmp_1;
    @name("IArlRL.tmp_13") bit<32> IArlRL_tmp_2;
    apply {
        tmp_14 = h.eth_hdr.eth_type;
        {
            bool hasReturned = false;
            bit<32> retval;
            @name("sGPTcR") bit<64> sGPTcR_0;
            @name("LRpMbf") bit<32> LRpMbf_0;
            sGPTcR_0 = 64w8331771506825847071;
            sGPTcR_0 = sGPTcR_0;
            LRpMbf_0 = 32w37657 |-| (bit<32>)sGPTcR_0;
            {
                hasReturned = true;
                retval = LRpMbf_0;
            }
            tmp_15 = retval;
        }
        tmp_16 = tmp_14 | (bit<16>)tmp_15;
        tmp_17 = tmp_16 | 16w58652;
        tmp_18 = tmp_17 + 16w30345;
        {
            bool hasReturned_0 = false;
            Vnytmj retval_0;
            bool tmp;
            bit<32> tmp_0;
            bit<16> tmp_1;
            bool tmp_2;
            bit<9> tmp_3;
            bit<32> tmp_4;
            bit<9> tmp_5;
            bit<32> tmp_6;
            bool tmp_7;
            bool tmp_8;
            bit<128> tmp_9;
            @name("kXmlrB") bit<8> kXmlrB_0;
            kXmlrB_0 = ((bit<43>)64w11378255015260334646 |+| 43w1462566353592)[16:9];
            kXmlrB_0 = kXmlrB_0;
            {
                bool hasReturned = false;
                bit<32> retval;
                @name("sGPTcR") bit<64> sGPTcR_0;
                @name("LRpMbf") bit<32> LRpMbf_0;
                sGPTcR_0 = 64w8331771506825847071;
                sGPTcR_0 = sGPTcR_0;
                LRpMbf_0 = 32w37657 |-| (bit<32>)sGPTcR_0;
                {
                    hasReturned = true;
                    retval = LRpMbf_0;
                }
            }
            tmp = false;
            tmp_0 = (bit<32>)64w11378255015260334646;
            tmp_1 = 16w14442;
            {
                bool hasReturned = false;
                bit<32> retval;
                @name("sGPTcR") bit<64> sGPTcR_0;
                @name("LRpMbf") bit<32> LRpMbf_0;
                sGPTcR_0 = 64w8331771506825847071;
                sGPTcR_0 = sGPTcR_0;
                LRpMbf_0 = 32w37657 |-| (bit<32>)sGPTcR_0;
                {
                    hasReturned = true;
                    retval = LRpMbf_0;
                }
                tmp_4 = retval;
            }
            tmp_5 = (bit<9>)tmp_4 | 9w260;
            tmp_3 = tmp_5;
            {
                bool hasReturned = false;
                bit<32> retval;
                @name("sGPTcR") bit<64> sGPTcR_0;
                @name("LRpMbf") bit<32> LRpMbf_0;
                sGPTcR_0 = 64w8331771506825847071;
                sGPTcR_0 = sGPTcR_0;
                LRpMbf_0 = 32w37657 |-| (bit<32>)sGPTcR_0;
                {
                    hasReturned = true;
                    retval = LRpMbf_0;
                }
                tmp_6 = retval;
            }
            tmp_7 = tmp_3 != (bit<9>)tmp_6;
            if (!tmp_7) {
                tmp_8 = false;
            } else {
                tmp_8 = 51w1444364813109517 == (bit<51>)16w59162;
            }
            tmp_2 = tmp_8;
            tmp_9 = 128w127537729978999984111170865926198740152;
            {
                hasReturned_0 = true;
                retval_0 = (Vnytmj){PZdb = tmp,xjKr = tmp_0,pBFG = tmp_1,VYDJ = tmp_2,GXQs = tmp_9};
            }
        }
        {
            IArlRL_xQNzSP = 32w1305108261;
            IArlRL_SYsGZI = 128w18672238;
            IArlRL_tmp = IArlRL_xQNzSP;
            {
                bool hasReturned = false;
                bit<32> retval;
                @name("sGPTcR") bit<64> sGPTcR_0;
                @name("LRpMbf") bit<32> LRpMbf_0;
                sGPTcR_0 = 64w8331771506825847071;
                sGPTcR_0 = sGPTcR_0;
                LRpMbf_0 = 32w37657 |-| (bit<32>)sGPTcR_0;
                {
                    hasReturned = true;
                    retval = LRpMbf_0;
                }
                IArlRL_tmp_0 = retval;
            }
            IArlRL_tmp_1 = IArlRL_tmp + IArlRL_tmp_0;
            IArlRL_tmp_2 = IArlRL_tmp_1 |-| 32w2827375294;
            IArlRL_xQNzSP = IArlRL_tmp_2;
            {
                bool hasReturned = false;
                bit<32> retval;
                @name("sGPTcR") bit<64> sGPTcR_0;
                @name("LRpMbf") bit<32> LRpMbf_0;
                sGPTcR_0 = 64w8331771506825847071;
                sGPTcR_0 = sGPTcR_0;
                LRpMbf_0 = 32w37657 |-| (bit<32>)sGPTcR_0;
                {
                    hasReturned = true;
                    retval = LRpMbf_0;
                }
            }
            IArlRL_SYsGZI = IArlRL_SYsGZI;
            {
                bool hasReturned_0 = false;
                Vnytmj retval_0;
                bool tmp;
                bit<32> tmp_0;
                bit<16> tmp_1;
                bool tmp_2;
                bit<9> tmp_3;
                bit<32> tmp_4;
                bit<9> tmp_5;
                bit<32> tmp_6;
                bool tmp_7;
                bool tmp_8;
                bit<128> tmp_9;
                @name("kXmlrB") bit<8> kXmlrB_0;
                kXmlrB_0 = ((bit<43>)64w9569382937354443357 |+| 43w1462566353592)[16:9];
                kXmlrB_0 = kXmlrB_0;
                {
                    bool hasReturned = false;
                    bit<32> retval;
                    @name("sGPTcR") bit<64> sGPTcR_0;
                    @name("LRpMbf") bit<32> LRpMbf_0;
                    sGPTcR_0 = 64w8331771506825847071;
                    sGPTcR_0 = sGPTcR_0;
                    LRpMbf_0 = 32w37657 |-| (bit<32>)sGPTcR_0;
                    {
                        hasReturned = true;
                        retval = LRpMbf_0;
                    }
                }
                tmp = false;
                tmp_0 = (bit<32>)64w9569382937354443357;
                tmp_1 = 16w14442;
                {
                    bool hasReturned = false;
                    bit<32> retval;
                    @name("sGPTcR") bit<64> sGPTcR_0;
                    @name("LRpMbf") bit<32> LRpMbf_0;
                    sGPTcR_0 = 64w8331771506825847071;
                    sGPTcR_0 = sGPTcR_0;
                    LRpMbf_0 = 32w37657 |-| (bit<32>)sGPTcR_0;
                    {
                        hasReturned = true;
                        retval = LRpMbf_0;
                    }
                    tmp_4 = retval;
                }
                tmp_5 = (bit<9>)tmp_4 | 9w260;
                tmp_3 = tmp_5;
                {
                    bool hasReturned = false;
                    bit<32> retval;
                    @name("sGPTcR") bit<64> sGPTcR_0;
                    @name("LRpMbf") bit<32> LRpMbf_0;
                    sGPTcR_0 = 64w8331771506825847071;
                    sGPTcR_0 = sGPTcR_0;
                    LRpMbf_0 = 32w37657 |-| (bit<32>)sGPTcR_0;
                    {
                        hasReturned = true;
                        retval = LRpMbf_0;
                    }
                    tmp_6 = retval;
                }
                tmp_7 = tmp_3 != (bit<9>)tmp_6;
                if (!tmp_7) {
                    tmp_8 = false;
                } else {
                    tmp_8 = 51w1444364813109517 == (bit<51>)16w0;
                }
                tmp_2 = tmp_8;
                tmp_9 = 128w127537729978999984111170865926198740152;
                {
                    hasReturned_0 = true;
                    retval_0 = (Vnytmj){PZdb = tmp,xjKr = tmp_0,pBFG = tmp_1,VYDJ = tmp_2,GXQs = tmp_9};
                }
            }
        }
        {
            bool hasReturned_0 = false;
            Vnytmj retval_0;
            bool tmp;
            bit<32> tmp_0;
            bit<16> tmp_1;
            bool tmp_2;
            bit<9> tmp_3;
            bit<32> tmp_4;
            bit<9> tmp_5;
            bit<32> tmp_6;
            bool tmp_7;
            bool tmp_8;
            bit<128> tmp_9;
            @name("kXmlrB") bit<8> kXmlrB_0;
            kXmlrB_0 = ((bit<43>)64w16257984866694305357 |+| 43w1462566353592)[16:9];
            kXmlrB_0 = kXmlrB_0;
            {
                bool hasReturned = false;
                bit<32> retval;
                @name("sGPTcR") bit<64> sGPTcR_0;
                @name("LRpMbf") bit<32> LRpMbf_0;
                sGPTcR_0 = 64w8331771506825847071;
                sGPTcR_0 = sGPTcR_0;
                LRpMbf_0 = 32w37657 |-| (bit<32>)sGPTcR_0;
                {
                    hasReturned = true;
                    retval = LRpMbf_0;
                }
            }
            tmp = false;
            tmp_0 = (bit<32>)64w16257984866694305357;
            tmp_1 = 16w14442;
            {
                bool hasReturned = false;
                bit<32> retval;
                @name("sGPTcR") bit<64> sGPTcR_0;
                @name("LRpMbf") bit<32> LRpMbf_0;
                sGPTcR_0 = 64w8331771506825847071;
                sGPTcR_0 = sGPTcR_0;
                LRpMbf_0 = 32w37657 |-| (bit<32>)sGPTcR_0;
                {
                    hasReturned = true;
                    retval = LRpMbf_0;
                }
                tmp_4 = retval;
            }
            tmp_5 = (bit<9>)tmp_4 | 9w260;
            tmp_3 = tmp_5;
            {
                bool hasReturned = false;
                bit<32> retval;
                @name("sGPTcR") bit<64> sGPTcR_0;
                @name("LRpMbf") bit<32> LRpMbf_0;
                sGPTcR_0 = 64w8331771506825847071;
                sGPTcR_0 = sGPTcR_0;
                LRpMbf_0 = 32w37657 |-| (bit<32>)sGPTcR_0;
                {
                    hasReturned = true;
                    retval = LRpMbf_0;
                }
                tmp_6 = retval;
            }
            tmp_7 = tmp_3 != (bit<9>)tmp_6;
            if (!tmp_7) {
                tmp_8 = false;
            } else {
                tmp_8 = 51w1444364813109517 == (bit<51>)16w65535;
            }
            tmp_2 = tmp_8;
            tmp_9 = 128w127537729978999984111170865926198740152;
            {
                hasReturned_0 = true;
                retval_0 = (Vnytmj){PZdb = tmp,xjKr = tmp_0,pBFG = tmp_1,VYDJ = tmp_2,GXQs = tmp_9};
            }
        }
        h.BqNk.iUNX = h.zkbz.mjHD;
        {
            bool hasReturned = false;
            bit<32> retval;
            @name("sGPTcR") bit<64> sGPTcR_0;
            @name("LRpMbf") bit<32> LRpMbf_0;
            sGPTcR_0 = 64w8331771506825847071;
            sGPTcR_0 = sGPTcR_0;
            LRpMbf_0 = 32w37657 |-| (bit<32>)sGPTcR_0;
            {
                hasReturned = true;
                retval = LRpMbf_0;
            }
        }
        h.BqNk.YwAD = 64w4314245641897930119;
        h.BqNk.YwAD = h.BqNk.YwAD;
    }
}

parser Parser(packet_in b, out Headers hdr);
control Ingress(inout Headers hdr);
package top(Parser p, Ingress ig);
top(p(), ingress()) main;

