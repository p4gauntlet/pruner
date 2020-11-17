from p4z3 import *



def p4_program(z3_reg):
    z3_reg.declare_global(
        Enum( "error", ["NoError", "PacketTooShort", "NoMatch", "StackOutOfBounds", "HeaderTooShort", "ParserTimeout", "ParserInvalidArgument", ])
    )
    z3_reg.declare_global(
        P4Extern("packet_in", type_params=[], methods=[P4Declaration("extract", P4Method("extract", type_params=(None, [
            "T",]), params=[
            P4Parameter("out", "hdr", "T", None),])), P4Declaration("extract", P4Method("extract", type_params=(None, [
            "T",]), params=[
            P4Parameter("out", "variableSizeHeader", "T", None),
            P4Parameter("in", "variableFieldSizeInBits", z3.BitVecSort(32), None),])), P4Declaration("lookahead", P4Method("lookahead", type_params=("T", [
            "T",]), params=[])), P4Declaration("advance", P4Method("advance", type_params=(None, []), params=[
            P4Parameter("in", "sizeInBits", z3.BitVecSort(32), None),])), P4Declaration("length", P4Method("length", type_params=(z3.BitVecSort(32), []), params=[])), ])
    )
    z3_reg.declare_global(
        P4Extern("packet_out", type_params=[], methods=[P4Declaration("emit", P4Method("emit", type_params=(None, [
            "T",]), params=[
            P4Parameter("in", "hdr", "T", None),])), ])
    )
    z3_reg.declare_global(
        P4Declaration("verify", P4Method("verify", type_params=(None, []), params=[
            P4Parameter("in", "check", z3.BoolSort(), None),
            P4Parameter("in", "toSignal", "error", None),]))
    )
    z3_reg.declare_global(
        P4Declaration("NoAction", P4Action("NoAction", params=[],         body=BlockStatement([]
        )        ))
    )
    z3_reg.declare_global(
        P4Declaration("match_kind", ["exact", "ternary", "lpm", ])
    )
    z3_reg.declare_global(
        HeaderType("ethernet_t", z3_reg, z3_args=[("dst_addr", z3.BitVecSort(48)), ("src_addr", z3.BitVecSort(48)), ("eth_type", z3.BitVecSort(16)), ])
    )
    z3_reg.declare_global(
        StructType("FddaxM", z3_reg, z3_args=[("tFfR", z3.BitVecSort(8)), ("JIfb", z3.BoolSort()), ("sNYh", z3_reg.stack("ethernet_t", 8)), ("cIrx", z3.BitVecSort(4)), ("Govt", z3.BitVecSort(8)), ])
    )
    z3_reg.declare_global(
        HeaderType("jCFTwO", z3_reg, z3_args=[("iUNX", z3.BitVecSort(4)), ("YwAD", z3.BitVecSort(64)), ("PamX", z3.BitVecSort(32)), ])
    )
    z3_reg.declare_global(
        HeaderType("qTdOho", z3_reg, z3_args=[("fZMq", z3.BitVecSort(4)), ("RhAV", z3.BitVecSort(16)), ])
    )
    z3_reg.declare_global(
        HeaderType("pQcOkh", z3_reg, z3_args=[("wBCb", z3.BitVecSort(32)), ("fwsC", z3.BitVecSort(32)), ("XbXc", z3.BitVecSort(8)), ("RNQF", z3.BitVecSort(64)), ])
    )
    z3_reg.declare_global(
        StructType("Vnytmj", z3_reg, z3_args=[("PZdb", z3.BoolSort()), ("xjKr", z3.BitVecSort(32)), ("pBFG", z3.BitVecSort(16)), ("VYDJ", z3.BoolSort()), ("GXQs", z3.BitVecSort(128)), ])
    )
    z3_reg.declare_global(
        StructType("KGAUpM", z3_reg, z3_args=[("RiWG", z3.BitVecSort(128)), ])
    )
    z3_reg.declare_global(
        StructType("VJczUg", z3_reg, z3_args=[("Laoh", z3.BoolSort()), ("daEM", z3.BitVecSort(8)), ("sfPX", z3.BitVecSort(128)), ("nVIm", z3.BitVecSort(16)), ])
    )
    z3_reg.declare_global(
        HeaderType("kTchlw", z3_reg, z3_args=[("WNfX", z3.BitVecSort(16)), ("mjHD", z3.BitVecSort(4)), ("SzNw", z3.BitVecSort(8)), ])
    )
    z3_reg.declare_global(
        StructType("Headers", z3_reg, z3_args=[("eth_hdr", "ethernet_t"), ("BqNk", "jCFTwO"), ("zkbz", "kTchlw"), ])
    )
    z3_reg.declare_global(
        P4Declaration("ZqTDGWH", P4Function("ZqTDGWH", return_type=z3.BitVecSort(32), params=[],         body=BlockStatement([
            BlockStatement([
                ValueDeclaration("sGPTcR", P4Initializer(z3.BitVecVal(10, 64), z3.BitVecSort(64)), z3_type=z3.BitVecSort(64)),
                BlockStatement([
                    ValueDeclaration("oZMmrS", z3.BitVecVal(37657, 16), z3_type=z3.BitVecSort(16)),
                    AssignmentStatement("sGPTcR", "sGPTcR"),
                    ValueDeclaration("LRpMbf", P4Initializer(P4Cast(z3.BitVecVal(10, 32), z3.BitVecSort(32)), z3.BitVecSort(32)), z3_type=z3.BitVecSort(32)),
                    AssignmentStatement("sGPTcR", z3.BitVecVal(152762851772443914, 64)),
                    P4Return("LRpMbf"),]
                ),
                AssignmentStatement("sGPTcR", "sGPTcR"),
                ValueDeclaration("noVnDj", P4Initializer(z3.BitVecVal(10, 64), z3.BitVecSort(64)), z3_type=z3.BitVecSort(64)),
                AssignmentStatement("noVnDj", z3.BitVecVal(10, 64)),
                AssignmentStatement("noVnDj", P4Cast(z3.BitVecVal(859692371, 64), z3.BitVecSort(64))),
                AssignmentStatement("sGPTcR", z3.BitVecVal(0, 64)),
                AssignmentStatement("sGPTcR", P4add(P4lshift(z3.BitVecVal(10, 64), z3.BitVecVal(10, 8)), "noVnDj")),
                ValueDeclaration("yZIceN", 838390161, z3_type=z3.IntSort()),
                P4Return(z3.BitVecVal(10, 32)),]
            ),
            ValueDeclaration("AfXLZG", P4Initializer(P4Cast(z3.BitVecVal(2144402680, 128), z3.BitVecSort(128)), z3.BitVecSort(128)), z3_type=z3.BitVecSort(128)),
            AssignmentStatement("AfXLZG", z3.BitVecVal(10, 128)),
            AssignmentStatement("AfXLZG", "AfXLZG"),
            AssignmentStatement("AfXLZG", "AfXLZG"),
            AssignmentStatement("AfXLZG", z3.BitVecVal(10, 128)),
            AssignmentStatement("AfXLZG", "AfXLZG"),
            BlockStatement([
                AssignmentStatement("AfXLZG", z3.BitVecVal(10, 128)),
                AssignmentStatement("AfXLZG", z3.BitVecVal(119851796932508784808775619006417521460, 128)),
                AssignmentStatement("AfXLZG", z3.BitVecVal(10, 128)),
                AssignmentStatement("AfXLZG", "AfXLZG"),
                ValueDeclaration("pQiUqJ", z3.BitVecVal(15318551338288664749, 64), z3_type=z3.BitVecSort(64)),
                ValueDeclaration("rPqZzN", z3.BitVecVal(211, 8), z3_type=z3.BitVecSort(8)),
                AssignmentStatement("AfXLZG", z3.BitVecVal(10, 128)),
                AssignmentStatement("AfXLZG", z3.BitVecVal(10, 128)),
                AssignmentStatement("AfXLZG", "AfXLZG"),
                P4Return(z3.BitVecVal(10, 32)),]
            ),
            P4Return(P4Cast(z3.BitVecVal(10, 32), z3.BitVecSort(32))),]
        )        )        )
    )
    z3_reg.declare_global(
        P4Declaration("IBaXWsK", P4Function("IBaXWsK", return_type="Vnytmj", params=[
            P4Parameter("none", "yQJV", z3.BitVecSort(64), None),
            P4Parameter("none", "gOEI", z3.BitVecSort(16), None),],         body=BlockStatement([
            ValueDeclaration("kXmlrB", P4Initializer(z3.BitVecVal(10, 8), z3.BitVecSort(8)), z3_type=z3.BitVecSort(8)),
            BlockStatement([
                BlockStatement([
                    AssignmentStatement("kXmlrB", "kXmlrB"),]
                ),
                AssignmentStatement("kXmlrB", "kXmlrB"),
                ValueDeclaration("YXRheT", 77175706, z3_type=z3.IntSort()),
                MethodCallStmt(MethodCallExpr("ZqTDGWH", [], )),
                AssignmentStatement("kXmlrB", z3.BitVecVal(174, 8)),
                P4Return(P4Cast(P4Initializer([z3.BoolVal(False), P4Cast("yQJV", z3.BitVecSort(32)), z3.BitVecVal(14442, 16), P4not(P4not(P4land(P4ne(z3.BitVecVal(10, 9), z3.BitVecVal(10, 9)), P4not(P4not(P4not(P4not(P4eq(z3.BitVecVal(10, 51), z3.BitVecVal(10, 51))))))))), z3.BitVecVal(127537729978999984111170865926198740152, 128), ], ), "Vnytmj")),]
            ),
            ValueDeclaration("wUxkGX", P4Cast(P4Initializer([z3.BitVecVal(11, 4), z3.BitVecVal(16737022111367307944, 64), z3.BitVecVal(10, 32), ], ), "jCFTwO"), z3_type="jCFTwO"),
            AssignmentStatement("kXmlrB", z3.BitVecVal(10, 8)),
            AssignmentStatement("kXmlrB", "kXmlrB"),
            MethodCallStmt(MethodCallExpr("ZqTDGWH", [], )),
            P4Return(P4Cast(P4Initializer([z3.BoolVal(True), z3.BitVecVal(1354969928, 32), z3.BitVecVal(10, 16), z3.BoolVal(True), z3.BitVecVal(10, 128), ], ), "Vnytmj")),]
        )        )        )
    )
    z3_reg.declare_global(
        ControlDeclaration(P4Control(
            name="PFizfTj",
            type_params=[],
            params=[
                P4Parameter("out", "lcNR", z3.BitVecSort(16), None),
                P4Parameter("none", "SZxu", z3.BitVecSort(128), None),],
            const_params=[],
            body=BlockStatement([
                AssignmentStatement("xQNzSP", P4subsat(z3.BitVecVal(10, 32), z3.BitVecVal(10, 32))),
                MethodCallStmt(MethodCallExpr("ZqTDGWH", [], )),
                AssignmentStatement("SYsGZI", "SYsGZI"),
                AssignmentStatement("xQNzSP", "xQNzSP"),
                MethodCallStmt(MethodCallExpr("IBaXWsK", [], z3.BitVecVal(10, 64), z3.BitVecVal(0, 16), )),
                AssignmentStatement("SYsGZI", z3.BitVecVal(10, 128)),]
            ),
            local_decls=[
ValueDeclaration("oHvtbH", P4Initializer(P4not(P4lor(P4not(P4eq(z3.BitVecVal(10, 57), z3.BitVecVal(10, 57))), z3.BoolVal(True))), z3.BoolSort()), z3_type=z3.BoolSort()), 
ValueDeclaration("nYJwrn", P4Initializer(z3.BitVecVal(10, 64), z3.BitVecSort(64)), z3_type=z3.BitVecSort(64)), 
ValueDeclaration("htHGwZ", P4Initializer(P4not(P4not("oHvtbH")), z3.BoolSort()), z3_type=z3.BoolSort()), 
ValueDeclaration("xQNzSP", P4Initializer(z3.BitVecVal(10, 32), z3.BitVecSort(32)), z3_type=z3.BitVecSort(32)), 
ValueDeclaration("SYsGZI", P4Initializer(P4Cast(z3.BitVecVal(10, 128), z3.BitVecSort(128)), z3.BitVecSort(128)), z3_type=z3.BitVecSort(128)), 
ValueDeclaration("NdjDFo", P4Initializer(P4lor(P4ne(P4Slice(z3.BitVecVal(10, 113), 62, 9), z3.BitVecVal(10, 54)), z3.BoolVal(True)), z3.BoolSort()), z3_type=z3.BoolSort()), 
P4Declaration("woqMg", P4Action("woqMg", params=[
                    P4Parameter("inout", "OcIW", z3.BitVecSort(4), None),
                    P4Parameter("out", "ILUP", "Vnytmj", None),
                    P4Parameter("none", "YFnT", z3.BitVecSort(128), None),],                 body=BlockStatement([
                    AssignmentStatement("OcIW", z3.BitVecVal(15, 4)),
                    BlockStatement([
                        AssignmentStatement("OcIW", z3.BitVecVal(1, 4)),
                        AssignmentStatement("nYJwrn", z3.BitVecVal(10, 64)),
                        AssignmentStatement(P4Member("ILUP", "GXQs"), "SZxu"),
                        AssignmentStatement("nYJwrn", "nYJwrn"),
                        AssignmentStatement("xQNzSP", z3.BitVecVal(10, 32)),
                        AssignmentStatement(P4Slice(P4Member("ILUP", "GXQs"), 56, 41), P4Member("ILUP", "pBFG")),
                        AssignmentStatement("lcNR", z3.BitVecVal(10, 16)),
                        ValueDeclaration("xtBTEG", P4Initializer(z3.BitVecVal(10, 32), z3.BitVecSort(32)), z3_type=z3.BitVecSort(32)),
                        AssignmentStatement(P4Member("ILUP", "pBFG"), z3.BitVecVal(23124, 16)),
                        AssignmentStatement(P4Slice(P4Member("ILUP", "xjKr"), 8, 5), "OcIW"),]
                    ),
                    AssignmentStatement("OcIW", z3.BitVecVal(10, 4)),
                    AssignmentStatement(P4Slice(P4Member("ILUP", "GXQs"), 36, 5), z3.BitVecVal(1728758457, 32)),
                    MethodCallStmt(MethodCallExpr("IBaXWsK", [], z3.BitVecVal(10, 64), z3.BitVecVal(10, 16), )),
                    AssignmentStatement(P4Slice("nYJwrn", 6, 3), z3.BitVecVal(10, 4)),
                    P4Return(None),
                    MethodCallStmt(MethodCallExpr("IBaXWsK", [], z3.BitVecVal(6235384825236171976, 64), z3.BitVecVal(10, 16), )),]
                )                )), 
P4Declaration("CBiEr", P4Action("CBiEr", params=[
                    P4Parameter("in", "DgGZ", z3.BitVecSort(8), None),
                    P4Parameter("none", "MevJ", "KGAUpM", None),
                    P4Parameter("none", "PHeC", z3.BitVecSort(8), None),],                 body=BlockStatement([
                    ValueDeclaration("UitBTw", P4Initializer(P4Cast(P4Initializer([z3.BitVecVal(1531371326, 32), "xQNzSP", z3.BitVecVal(10, 8), z3.BitVecVal(10, 64), ], ), "pQcOkh"), "pQcOkh"), z3_type="pQcOkh"),
                    AssignmentStatement("SYsGZI", z3.BitVecVal(216323781136148277345578055083500959293, 128)),
                    AssignmentStatement(P4Member("UitBTw", "wBCb"), z3.BitVecVal(2554680596, 32)),
                    AssignmentStatement(P4Member("UitBTw", "XbXc"), z3.BitVecVal(10, 8)),
                    MethodCallStmt(MethodCallExpr("ZqTDGWH", [], )),
                    AssignmentStatement("SYsGZI", "SZxu"),
                    AssignmentStatement("SYsGZI", P4neg(z3.BitVecVal(10, 128))),
                    AssignmentStatement("SYsGZI", P4neg(P4rshift(P4subsat("SYsGZI", z3.BitVecVal(294999660554044817754265939658325384524, 128)), z3.BitVecVal(10, 8)))),
                    ValueDeclaration("GSuYjJ", P4Initializer(P4inv(P4Member("UitBTw", "wBCb")), z3.BitVecSort(32)), z3_type=z3.BitVecSort(32)),
                    AssignmentStatement(P4Member("UitBTw", "XbXc"), z3.BitVecVal(10, 8)),
                    MethodCallStmt(MethodCallExpr("ZqTDGWH", [], )),]
                )                )), 
P4Declaration("TNAYJq", P4Table("TNAYJq", key=[("SYsGZI", "exact"), ], actions=[], default_action=MethodCallExpr("NoAction", [], ), immutable=False)), 
P4Declaration("VtgSNW", P4Table("VtgSNW", key=[(z3.BitVecVal(10, 128), "exact"), (z3.BitVecVal(10, 32), "exact"), (z3.BitVecVal(17488452717387411170, 64), "exact"), ], actions=[], default_action=MethodCallExpr("NoAction", [], ), immutable=False)), 
P4Declaration("YSvMfd", P4Table("YSvMfd", key=[(P4Slice(z3.BitVecVal(10, 213), 157, 30), "exact"), ], actions=[], default_action=MethodCallExpr("NoAction", [], ), immutable=False)), ]
        ))
    )
    z3_reg.declare_global(
        ControlDeclaration(P4Parser(
            name="p",
            type_params=[],
            params=[
                P4Parameter("none", "pkt", "packet_in", None),
                P4Parameter("out", "hdr", "Headers", None),],
            const_params=[],
            local_decls=[],
            body=ParserTree([
                ParserState(name="start", select="parse_hdrs",
                components=[                ]),
                ParserState(name="parse_hdrs", select="accept",
                components=[
                MethodCallStmt(MethodCallExpr(P4Member("pkt", "extract"), [], P4Member("hdr", "eth_hdr"), )),
                MethodCallStmt(MethodCallExpr(P4Member("pkt", "extract"), [], P4Member("hdr", "BqNk"), )),
                MethodCallStmt(MethodCallExpr(P4Member("pkt", "extract"), [], P4Member("hdr", "zkbz"), )),                ]),
                ])
))
    )
    z3_reg.declare_global(
        ControlDeclaration(P4Control(
            name="ingress",
            type_params=[],
            params=[
                P4Parameter("inout", "h", "Headers", None),],
            const_params=[],
            body=BlockStatement([
                AssignmentStatement(P4Member(P4Member("h", "zkbz"), "WNfX"), P4add(P4bor(z3.BitVecVal(10, 16), z3.BitVecVal(58652, 16)), z3.BitVecVal(10, 16))),
                MethodCallStmt(MethodCallExpr("IBaXWsK", [], z3.BitVecVal(11378255015260334646, 64), z3.BitVecVal(59162, 16), )),
                MethodCallStmt(MethodCallExpr(P4Member("IArlRL", "apply"), [], P4Member(P4Member("h", "zkbz"), "WNfX"), z3.BitVecVal(10, 128), )),
                BlockStatement([
                    MethodCallStmt(MethodCallExpr("IBaXWsK", [], z3.BitVecVal(10, 64), z3.BitVecVal(10, 16), )),]
                ),
                AssignmentStatement(P4Member(P4Member("h", "BqNk"), "iUNX"), P4Member(P4Member("h", "zkbz"), "mjHD")),
                MethodCallStmt(MethodCallExpr("ZqTDGWH", [], )),
                AssignmentStatement(P4Member(P4Member("h", "BqNk"), "YwAD"), z3.BitVecVal(10, 64)),
                AssignmentStatement(P4Member(P4Member("h", "BqNk"), "YwAD"), P4Member(P4Member("h", "BqNk"), "YwAD")),
                ValueDeclaration("oOqmbD", z3.BitVecVal(10, 16), z3_type=z3.BitVecSort(16)),]
            ),
            local_decls=[
ValueDeclaration("TCVSkL", P4Initializer(z3.BitVecVal(10, 8), z3.BitVecSort(8)), z3_type=z3.BitVecSort(8)), 
InstanceDeclaration("IArlRL", "PFizfTj", ), 
P4Declaration("dpTJp", P4Action("dpTJp", params=[],                 body=BlockStatement([
                    MethodCallStmt(MethodCallExpr("IBaXWsK", [], z3.BitVecVal(6943846788549823044, 64), z3.BitVecVal(10, 16), )),
                    MethodCallStmt(MethodCallExpr(P4Member("IArlRL", "apply"), [], P4Member(P4Member("h", "eth_hdr"), "eth_type"), z3.BitVecVal(10, 128), )),
                    P4Return(None),
                    AssignmentStatement(P4Member(P4Member("h", "eth_hdr"), "src_addr"), P4Cast(z3.BitVecVal(281474897995198, 48), z3.BitVecSort(48))),
                    ValueDeclaration("QlaOEA", z3.BitVecVal(10, 32), z3_type=z3.BitVecSort(32)),]
                )                )), 
P4Declaration("QyKFXD", P4Table("QyKFXD", key=[], actions=[MethodCallExpr("dpTJp", [], ), ], default_action=MethodCallExpr("NoAction", [], ), immutable=False)), ]
        ))
    )
    z3_reg.declare_global(
        ControlDeclaration(P4ParserType("Parser", params=[
            P4Parameter("none", "b", "packet_in", None),
            P4Parameter("out", "hdr", "Headers", None),], type_params=[]))
    )
    z3_reg.declare_global(
        ControlDeclaration(P4ControlType("Ingress", params=[
            P4Parameter("inout", "hdr", "Headers", None),], type_params=[]))
    )
    z3_reg.declare_global(
        ControlDeclaration(P4Package(z3_reg, "top", params=[
            P4Parameter("none", "p", "Parser", None),
            P4Parameter("none", "ig", "Ingress", None),],type_params=[]))
    )
    z3_reg.declare_global(
        InstanceDeclaration("main", "top", ConstCallExpr("p", ), ConstCallExpr("ingress", ), )
    )
    var = z3_reg.get_main_function()
    return var if isinstance(var, P4Package) else None
