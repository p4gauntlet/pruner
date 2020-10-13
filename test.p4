#include <core.p4>

header ethernet_t {
    bit<48> dst_addr;
    bit<48> src_addr;
    bit<16> eth_type;
}

header HdsdGk {
    bit<4>   yRei;
    bit<128> OIfL;
}

header EJdyYz {
    bit<16>  HzMS;
    bit<64>  bLIA;
    bit<128> SMeu;
}

header hLmako {
    bit<16> CSRe;
    bit<8>  PrEX;
    bit<16> ZLsW;
    bit<16> RyoC;
    bit<8>  ZGZw;
}

header agWogS {
    bit<64>  wGtf;
    bit<128> NeVe;
    bit<32>  BiBW;
    bit<8>   VxOr;
}

struct loRgQn {
    bit<4>  mDvL;
    bit<32> hmNK;
    bit<32> kgWA;
    bit<4>  lXTk;
    bit<4>  Ueqr;
}

struct nBbPlc {
    bit<32>  wPIz;
    bit<128> Cclc;
}

struct dhMzYt {
    HdsdGk[1] OkAM;
}

struct Headers {
    ethernet_t eth_hdr;
    HdsdGk     TJHL;
}

parser p(packet_in pkt, out Headers hdr) {
    state start {
        transition parse_hdrs;
    }
    state parse_hdrs {
        transition accept;
    }
}

control ingress(inout Headers h) {
    nBbPlc HkOGuD = { 32w3423150469 & (bit<32>)h.eth_hdr.src_addr, 39w251050016615 ++ -(89w52972909472855994380936831 | 89w499164479328554570676260522) };
    HdsdGk dOaWAx = { 4w8, 128w294363269627660987683727172780004270544 |-| (128w210697525707981783467134328439773787483 ^ 128w118827640629988842965570143448685595268 % 128w96058991468477114244119746032229669749) };
    bit<128> ymGsqY = 606212367 ^ 1538303545 ^ (dOaWAx.OIfL | 18407642 - -951944168);
    bit<32> LDLifD = (!!!true ? (bit<32>)32w233620073 : 32w1904567272);
    action cnemH() {
        h.TJHL.OIfL = ~ymGsqY;
    }
    action NkYaT(inout bit<32> TBHn, bit<64> vHgY) {
        cnemH();
        bit<4> dusxjZ = 4w8 % 4w11;
    }
    table ZgQEag {
        key = {
            128w41734176219872743096347939643578477133: exact @name("MiraYB") ;
            LDLifD                                    : exact @name("DLXxJx") ;
            32w1939671254                             : exact @name("aYKLnY") ;
        }
        actions = {
        }
    }
    table jMZKWi {
        key = {
            h.eth_hdr.eth_type: exact @name("qOAzqi") ;
            48w99514929141513 : exact @name("TxowFE") ;
        }
        actions = {
            cnemH();
        }
    }
    table voROHp {
        key = {
            32w3103292882: exact @name("bqmTyi") ;
        }
        actions = {
        }
    }
    table wHPpkB {
        key = {
            (false ? ymGsqY : 128w78430254674801476827918592984531593100)                                                                   : exact @name("BaJNeq") ;
            (!!!!(((bit<110>)h.TJHL.yRei)[105:11] != (bit<95>)h.eth_hdr.eth_type) ? ((bit<37>)ymGsqY)[34:3] : 32w2790639234 / 32w4243961830): exact @name("CRsJFk") ;
            4w0                                                                                                                             : exact @name("BusOCl") ;
        }
        actions = {
            cnemH();
        }
    }
    apply {
        NkYaT(h.TJHL.OIfL[104:73], (64w5243861221667015507 |+| -64w12445722161637052267 - 64w11380158807642795511) * 64w5027264468238816501);
        bit<4> FWAbfY = (20w1046872 % 20w905728 != (bit<20>)h.TJHL.OIfL ? (!false ? (!true ? 4w8 : 4w11) : 4w2) : 4w4);
        bool YgSLNz = false;
    }
}

parser Parser(packet_in b, out Headers hdr);
control Ingress(inout Headers hdr);
package top(Parser p, Ingress ig);
top(p(), ingress()) main;


