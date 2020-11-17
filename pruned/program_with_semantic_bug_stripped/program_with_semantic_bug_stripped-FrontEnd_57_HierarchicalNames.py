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
        ControlDeclaration(P4Parser(
            name="p",
            type_params=[],
            params=[
                P4Parameter("none", "pkt", "packet_in", None),
                P4Parameter("out", "hdr", "Headers", None),],
            const_params=[],
            local_decls=[],
            body=ParserTree([
                ParserState(name="start", select="accept",
                components=[
                MethodCallStmt(MethodCallExpr(P4Member("pkt", "extract"), ["ethernet_t", ], P4Member("hdr", "eth_hdr"), )),
                MethodCallStmt(MethodCallExpr(P4Member("pkt", "extract"), ["jCFTwO", ], P4Member("hdr", "BqNk"), )),
                MethodCallStmt(MethodCallExpr(P4Member("pkt", "extract"), ["kTchlw", ], P4Member("hdr", "zkbz"), )),                ]),
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
                BlockStatement([
                    ValueDeclaration("hasReturned", P4Initializer(z3.BoolVal(False), z3.BoolSort()), z3_type=z3.BoolSort()),
                    ValueDeclaration("retval", None, z3_type="Vnytmj"),
                    ValueDeclaration("kXmlrB_0", None, z3_type=z3.BitVecSort(8)),
                    AssignmentStatement("kXmlrB_0", z3.BitVecVal(10, 8)),
                    AssignmentStatement("kXmlrB_0", "kXmlrB_0"),
                    BlockStatement([
                        ValueDeclaration("hasReturned_0", P4Initializer(z3.BoolVal(False), z3.BoolSort()), z3_type=z3.BoolSort()),
                        ValueDeclaration("retval_0", None, z3_type=z3.BitVecSort(32)),
                        ValueDeclaration("sGPTcR_0", None, z3_type=z3.BitVecSort(64)),
                        ValueDeclaration("LRpMbf_0", None, z3_type=z3.BitVecSort(32)),
                        AssignmentStatement("sGPTcR_0", z3.BitVecVal(10, 64)),
                        AssignmentStatement("LRpMbf_0", z3.BitVecVal(10, 32)),
                        AssignmentStatement("hasReturned_0", z3.BoolVal(True)),
                        AssignmentStatement("retval_0", "LRpMbf_0"),]
                    ),
                    AssignmentStatement("hasReturned", z3.BoolVal(True)),
                    AssignmentStatement("retval", P4Cast(P4Initializer([z3.BoolVal(False), P4Cast(z3.BitVecVal(11378255015260334646, 64), z3.BitVecSort(32)), z3.BitVecVal(14442, 16), z3.BoolVal(False), z3.BitVecVal(127537729978999984111170865926198740152, 128), ], ), "Vnytmj")),]
                ),
                AssignmentStatement("IArlRL_SYsGZI", z3.BitVecVal(10, 128)),
                AssignmentStatement("IArlRL_xQNzSP", z3.BitVecVal(0, 32)),
                BlockStatement([
                    ValueDeclaration("hasReturned_3", P4Initializer(z3.BoolVal(False), z3.BoolSort()), z3_type=z3.BoolSort()),
                    ValueDeclaration("retval_5", None, z3_type=z3.BitVecSort(32)),
                    ValueDeclaration("sGPTcR_1", None, z3_type=z3.BitVecSort(64)),
                    ValueDeclaration("LRpMbf_1", None, z3_type=z3.BitVecSort(32)),
                    AssignmentStatement("sGPTcR_1", z3.BitVecVal(10, 64)),
                    AssignmentStatement("LRpMbf_1", z3.BitVecVal(10, 32)),
                    AssignmentStatement("hasReturned_3", z3.BoolVal(True)),
                    AssignmentStatement("retval_5", "LRpMbf_1"),]
                ),
                BlockStatement([
                    ValueDeclaration("hasReturned_4", P4Initializer(z3.BoolVal(False), z3.BoolSort()), z3_type=z3.BoolSort()),
                    ValueDeclaration("retval_6", None, z3_type="Vnytmj"),
                    ValueDeclaration("kXmlrB_1", None, z3_type=z3.BitVecSort(8)),
                    AssignmentStatement("kXmlrB_1", z3.BitVecVal(10, 8)),
                    AssignmentStatement("kXmlrB_1", "kXmlrB_1"),
                    BlockStatement([
                        ValueDeclaration("hasReturned_5", P4Initializer(z3.BoolVal(False), z3.BoolSort()), z3_type=z3.BoolSort()),
                        ValueDeclaration("retval_7", None, z3_type=z3.BitVecSort(32)),
                        ValueDeclaration("sGPTcR_2", None, z3_type=z3.BitVecSort(64)),
                        ValueDeclaration("LRpMbf_2", None, z3_type=z3.BitVecSort(32)),
                        AssignmentStatement("sGPTcR_2", z3.BitVecVal(10, 64)),
                        AssignmentStatement("LRpMbf_2", z3.BitVecVal(10, 32)),
                        AssignmentStatement("hasReturned_5", z3.BoolVal(True)),
                        AssignmentStatement("retval_7", "LRpMbf_2"),]
                    ),
                    AssignmentStatement("hasReturned_4", z3.BoolVal(True)),
                    AssignmentStatement("retval_6", P4Cast(P4Initializer([z3.BoolVal(False), P4Cast(z3.BitVecVal(10, 64), z3.BitVecSort(32)), z3.BitVecVal(14442, 16), z3.BoolVal(False), z3.BitVecVal(127537729978999984111170865926198740152, 128), ], ), "Vnytmj")),]
                ),
                BlockStatement([
                    ValueDeclaration("hasReturned_6", P4Initializer(z3.BoolVal(False), z3.BoolSort()), z3_type=z3.BoolSort()),
                    ValueDeclaration("retval_8", None, z3_type="Vnytmj"),
                    ValueDeclaration("kXmlrB_2", None, z3_type=z3.BitVecSort(8)),
                    AssignmentStatement("kXmlrB_2", z3.BitVecVal(10, 8)),
                    AssignmentStatement("kXmlrB_2", "kXmlrB_2"),
                    BlockStatement([
                        ValueDeclaration("hasReturned_7", P4Initializer(z3.BoolVal(False), z3.BoolSort()), z3_type=z3.BoolSort()),
                        ValueDeclaration("retval_9", None, z3_type=z3.BitVecSort(32)),
                        ValueDeclaration("sGPTcR_3", None, z3_type=z3.BitVecSort(64)),
                        ValueDeclaration("LRpMbf_3", None, z3_type=z3.BitVecSort(32)),
                        AssignmentStatement("sGPTcR_3", z3.BitVecVal(10, 64)),
                        AssignmentStatement("LRpMbf_3", z3.BitVecVal(10, 32)),
                        AssignmentStatement("hasReturned_7", z3.BoolVal(True)),
                        AssignmentStatement("retval_9", "LRpMbf_3"),]
                    ),
                    AssignmentStatement("hasReturned_6", z3.BoolVal(True)),
                    AssignmentStatement("retval_8", P4Cast(P4Initializer([z3.BoolVal(False), P4Cast(z3.BitVecVal(10, 64), z3.BitVecSort(32)), z3.BitVecVal(14442, 16), z3.BoolVal(False), z3.BitVecVal(127537729978999984111170865926198740152, 128), ], ), "Vnytmj")),]
                ),
                AssignmentStatement(P4Member(P4Member("h", "BqNk"), "iUNX"), P4Member(P4Member("h", "zkbz"), "mjHD")),
                BlockStatement([
                    ValueDeclaration("hasReturned_8", P4Initializer(z3.BoolVal(False), z3.BoolSort()), z3_type=z3.BoolSort()),
                    ValueDeclaration("retval_10", None, z3_type=z3.BitVecSort(32)),
                    ValueDeclaration("sGPTcR_4", None, z3_type=z3.BitVecSort(64)),
                    ValueDeclaration("LRpMbf_4", None, z3_type=z3.BitVecSort(32)),
                    AssignmentStatement("sGPTcR_4", z3.BitVecVal(10, 64)),
                    AssignmentStatement("LRpMbf_4", z3.BitVecVal(10, 32)),
                    AssignmentStatement("hasReturned_8", z3.BoolVal(True)),
                    AssignmentStatement("retval_10", "LRpMbf_4"),]
                ),
                AssignmentStatement(P4Member(P4Member("h", "BqNk"), "YwAD"), z3.BitVecVal(10, 64)),
                AssignmentStatement(P4Member(P4Member("h", "BqNk"), "YwAD"), P4Member(P4Member("h", "BqNk"), "YwAD")),]
            ),
            local_decls=[
ValueDeclaration("IArlRL_xQNzSP", None, z3_type=z3.BitVecSort(32)), 
ValueDeclaration("IArlRL_SYsGZI", None, z3_type=z3.BitVecSort(128)), ]
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
