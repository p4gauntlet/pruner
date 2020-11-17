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
                AssignmentStatement("tmp", P4Member(P4Member("h", "eth_hdr"), "eth_type")),
                BlockStatement([
                    AssignmentStatement("hasReturned", z3.BoolVal(False)),
                    AssignmentStatement("sGPTcR_0", z3.BitVecVal(8331771506825847071, 64)),
                    AssignmentStatement("sGPTcR_0", "sGPTcR_0"),
                    AssignmentStatement("LRpMbf_0", P4subsat(z3.BitVecVal(37657, 32), P4Cast("sGPTcR_0", z3.BitVecSort(32)))),
                    AssignmentStatement("hasReturned", z3.BoolVal(True)),
                    AssignmentStatement("retval", "LRpMbf_0"),
                    AssignmentStatement("tmp_0", "retval"),]
                ),
                AssignmentStatement("tmp_1", P4bor("tmp", P4Cast("tmp_0", z3.BitVecSort(16)))),
                AssignmentStatement("tmp_2", P4bor("tmp_1", z3.BitVecVal(58652, 16))),
                AssignmentStatement("tmp_3", P4add("tmp_2", z3.BitVecVal(30345, 16))),
                BlockStatement([
                    AssignmentStatement("hasReturned_0", z3.BoolVal(False)),
                    AssignmentStatement("kXmlrB_0", P4Slice(P4addsat(P4Cast(z3.BitVecVal(11378255015260334646, 64), z3.BitVecSort(43)), z3.BitVecVal(1462566353592, 43)), 16, 9)),
                    AssignmentStatement("kXmlrB_0", "kXmlrB_0"),
                    BlockStatement([
                        AssignmentStatement("hasReturned_3", z3.BoolVal(False)),
                        AssignmentStatement("sGPTcR_1", z3.BitVecVal(8331771506825847071, 64)),
                        AssignmentStatement("sGPTcR_1", "sGPTcR_1"),
                        AssignmentStatement("LRpMbf_1", P4subsat(z3.BitVecVal(37657, 32), P4Cast("sGPTcR_1", z3.BitVecSort(32)))),
                        AssignmentStatement("hasReturned_3", z3.BoolVal(True)),
                        AssignmentStatement("retval_5", "LRpMbf_1"),]
                    ),
                    AssignmentStatement("tmp_4", z3.BoolVal(False)),
                    AssignmentStatement("tmp_5", P4Cast(z3.BitVecVal(11378255015260334646, 64), z3.BitVecSort(32))),
                    AssignmentStatement("tmp_6", z3.BitVecVal(14442, 16)),
                    BlockStatement([
                        AssignmentStatement("hasReturned_4", z3.BoolVal(False)),
                        AssignmentStatement("sGPTcR_2", z3.BitVecVal(8331771506825847071, 64)),
                        AssignmentStatement("sGPTcR_2", "sGPTcR_2"),
                        AssignmentStatement("LRpMbf_2", P4subsat(z3.BitVecVal(37657, 32), P4Cast("sGPTcR_2", z3.BitVecSort(32)))),
                        AssignmentStatement("hasReturned_4", z3.BoolVal(True)),
                        AssignmentStatement("retval_6", "LRpMbf_2"),
                        AssignmentStatement("tmp_9", "retval_6"),]
                    ),
                    AssignmentStatement("tmp_14", P4bor(P4Cast("tmp_9", z3.BitVecSort(9)), z3.BitVecVal(260, 9))),
                    AssignmentStatement("tmp_8", "tmp_14"),
                    BlockStatement([
                        AssignmentStatement("hasReturned_5", z3.BoolVal(False)),
                        AssignmentStatement("sGPTcR_3", z3.BitVecVal(8331771506825847071, 64)),
                        AssignmentStatement("sGPTcR_3", "sGPTcR_3"),
                        AssignmentStatement("LRpMbf_3", P4subsat(z3.BitVecVal(37657, 32), P4Cast("sGPTcR_3", z3.BitVecSort(32)))),
                        AssignmentStatement("hasReturned_5", z3.BoolVal(True)),
                        AssignmentStatement("retval_7", "LRpMbf_3"),
                        AssignmentStatement("tmp_15", "retval_7"),]
                    ),
                    AssignmentStatement("tmp_16", P4ne("tmp_8", P4Cast("tmp_15", z3.BitVecSort(9)))),
                    IfStatement(P4not("tmp_16"), BlockStatement([
                        AssignmentStatement("tmp_17", z3.BoolVal(False)),]
                    ), BlockStatement([
                        AssignmentStatement("tmp_17", P4eq(z3.BitVecVal(1444364813109517, 51), P4Cast(z3.BitVecVal(59162, 16), z3.BitVecSort(51)))),]
                    )),
                    AssignmentStatement("tmp_7", "tmp_17"),
                    AssignmentStatement("tmp_18", z3.BitVecVal(127537729978999984111170865926198740152, 128)),
                    AssignmentStatement("hasReturned_0", z3.BoolVal(True)),
                    AssignmentStatement("retval_0", P4Cast(P4Initializer(["tmp_4", "tmp_5", "tmp_6", "tmp_7", "tmp_18", ], ), "Vnytmj")),]
                ),
                AssignmentStatement("IArlRL_xQNzSP", z3.BitVecVal(1305108261, 32)),
                AssignmentStatement("IArlRL_SYsGZI", z3.BitVecVal(18672238, 128)),
                AssignmentStatement("IArlRL_tmp", "IArlRL_xQNzSP"),
                BlockStatement([
                    AssignmentStatement("hasReturned_6", z3.BoolVal(False)),
                    AssignmentStatement("sGPTcR_4", z3.BitVecVal(8331771506825847071, 64)),
                    AssignmentStatement("sGPTcR_4", "sGPTcR_4"),
                    AssignmentStatement("LRpMbf_4", P4subsat(z3.BitVecVal(37657, 32), P4Cast("sGPTcR_4", z3.BitVecSort(32)))),
                    AssignmentStatement("hasReturned_6", z3.BoolVal(True)),
                    AssignmentStatement("retval_8", "LRpMbf_4"),
                    AssignmentStatement("IArlRL_tmp_0", "retval_8"),]
                ),
                AssignmentStatement("IArlRL_tmp_1", P4add("IArlRL_tmp", "IArlRL_tmp_0")),
                AssignmentStatement("IArlRL_tmp_2", P4subsat("IArlRL_tmp_1", z3.BitVecVal(2827375294, 32))),
                AssignmentStatement("IArlRL_xQNzSP", "IArlRL_tmp_2"),
                BlockStatement([
                    AssignmentStatement("hasReturned_7", z3.BoolVal(False)),
                    AssignmentStatement("sGPTcR_5", z3.BitVecVal(8331771506825847071, 64)),
                    AssignmentStatement("sGPTcR_5", "sGPTcR_5"),
                    AssignmentStatement("LRpMbf_5", P4subsat(z3.BitVecVal(37657, 32), P4Cast("sGPTcR_5", z3.BitVecSort(32)))),
                    AssignmentStatement("hasReturned_7", z3.BoolVal(True)),
                    AssignmentStatement("retval_9", "LRpMbf_5"),]
                ),
                AssignmentStatement("IArlRL_SYsGZI", "IArlRL_SYsGZI"),
                BlockStatement([
                    AssignmentStatement("hasReturned_8", z3.BoolVal(False)),
                    AssignmentStatement("kXmlrB_1", P4Slice(P4addsat(P4Cast(z3.BitVecVal(9569382937354443357, 64), z3.BitVecSort(43)), z3.BitVecVal(1462566353592, 43)), 16, 9)),
                    AssignmentStatement("kXmlrB_1", "kXmlrB_1"),
                    BlockStatement([
                        AssignmentStatement("hasReturned_9", z3.BoolVal(False)),
                        AssignmentStatement("sGPTcR_6", z3.BitVecVal(8331771506825847071, 64)),
                        AssignmentStatement("sGPTcR_6", "sGPTcR_6"),
                        AssignmentStatement("LRpMbf_6", P4subsat(z3.BitVecVal(37657, 32), P4Cast("sGPTcR_6", z3.BitVecSort(32)))),
                        AssignmentStatement("hasReturned_9", z3.BoolVal(True)),
                        AssignmentStatement("retval_11", "LRpMbf_6"),]
                    ),
                    AssignmentStatement("tmp_31", z3.BoolVal(False)),
                    AssignmentStatement("tmp_32", P4Cast(z3.BitVecVal(9569382937354443357, 64), z3.BitVecSort(32))),
                    AssignmentStatement("tmp_33", z3.BitVecVal(14442, 16)),
                    BlockStatement([
                        AssignmentStatement("hasReturned_10", z3.BoolVal(False)),
                        AssignmentStatement("sGPTcR_7", z3.BitVecVal(8331771506825847071, 64)),
                        AssignmentStatement("sGPTcR_7", "sGPTcR_7"),
                        AssignmentStatement("LRpMbf_7", P4subsat(z3.BitVecVal(37657, 32), P4Cast("sGPTcR_7", z3.BitVecSort(32)))),
                        AssignmentStatement("hasReturned_10", z3.BoolVal(True)),
                        AssignmentStatement("retval_12", "LRpMbf_7"),
                        AssignmentStatement("tmp_36", "retval_12"),]
                    ),
                    AssignmentStatement("tmp_37", P4bor(P4Cast("tmp_36", z3.BitVecSort(9)), z3.BitVecVal(260, 9))),
                    AssignmentStatement("tmp_35", "tmp_37"),
                    BlockStatement([
                        AssignmentStatement("hasReturned_11", z3.BoolVal(False)),
                        AssignmentStatement("sGPTcR_8", z3.BitVecVal(8331771506825847071, 64)),
                        AssignmentStatement("sGPTcR_8", "sGPTcR_8"),
                        AssignmentStatement("LRpMbf_8", P4subsat(z3.BitVecVal(37657, 32), P4Cast("sGPTcR_8", z3.BitVecSort(32)))),
                        AssignmentStatement("hasReturned_11", z3.BoolVal(True)),
                        AssignmentStatement("retval_13", "LRpMbf_8"),
                        AssignmentStatement("tmp_38", "retval_13"),]
                    ),
                    AssignmentStatement("tmp_39", P4ne("tmp_35", P4Cast("tmp_38", z3.BitVecSort(9)))),
                    IfStatement(P4not("tmp_39"), BlockStatement([
                        AssignmentStatement("tmp_40", z3.BoolVal(False)),]
                    ), BlockStatement([
                        AssignmentStatement("tmp_40", P4eq(z3.BitVecVal(1444364813109517, 51), P4Cast(z3.BitVecVal(0, 16), z3.BitVecSort(51)))),]
                    )),
                    AssignmentStatement("tmp_34", "tmp_40"),
                    AssignmentStatement("tmp_41", z3.BitVecVal(127537729978999984111170865926198740152, 128)),
                    AssignmentStatement("hasReturned_8", z3.BoolVal(True)),
                    AssignmentStatement("retval_10", P4Cast(P4Initializer(["tmp_31", "tmp_32", "tmp_33", "tmp_34", "tmp_41", ], ), "Vnytmj")),]
                ),
                BlockStatement([
                    AssignmentStatement("hasReturned_12", z3.BoolVal(False)),
                    AssignmentStatement("kXmlrB_2", P4Slice(P4addsat(P4Cast(z3.BitVecVal(16257984866694305357, 64), z3.BitVecSort(43)), z3.BitVecVal(1462566353592, 43)), 16, 9)),
                    AssignmentStatement("kXmlrB_2", "kXmlrB_2"),
                    BlockStatement([
                        AssignmentStatement("hasReturned_13", z3.BoolVal(False)),
                        AssignmentStatement("sGPTcR_9", z3.BitVecVal(8331771506825847071, 64)),
                        AssignmentStatement("sGPTcR_9", "sGPTcR_9"),
                        AssignmentStatement("LRpMbf_9", P4subsat(z3.BitVecVal(37657, 32), P4Cast("sGPTcR_9", z3.BitVecSort(32)))),
                        AssignmentStatement("hasReturned_13", z3.BoolVal(True)),
                        AssignmentStatement("retval_15", "LRpMbf_9"),]
                    ),
                    AssignmentStatement("tmp_42", z3.BoolVal(False)),
                    AssignmentStatement("tmp_43", P4Cast(z3.BitVecVal(16257984866694305357, 64), z3.BitVecSort(32))),
                    AssignmentStatement("tmp_44", z3.BitVecVal(14442, 16)),
                    BlockStatement([
                        AssignmentStatement("hasReturned_14", z3.BoolVal(False)),
                        AssignmentStatement("sGPTcR_10", z3.BitVecVal(8331771506825847071, 64)),
                        AssignmentStatement("sGPTcR_10", "sGPTcR_10"),
                        AssignmentStatement("LRpMbf_10", P4subsat(z3.BitVecVal(37657, 32), P4Cast("sGPTcR_10", z3.BitVecSort(32)))),
                        AssignmentStatement("hasReturned_14", z3.BoolVal(True)),
                        AssignmentStatement("retval_16", "LRpMbf_10"),
                        AssignmentStatement("tmp_47", "retval_16"),]
                    ),
                    AssignmentStatement("tmp_48", P4bor(P4Cast("tmp_47", z3.BitVecSort(9)), z3.BitVecVal(260, 9))),
                    AssignmentStatement("tmp_46", "tmp_48"),
                    BlockStatement([
                        AssignmentStatement("hasReturned_15", z3.BoolVal(False)),
                        AssignmentStatement("sGPTcR_11", z3.BitVecVal(8331771506825847071, 64)),
                        AssignmentStatement("sGPTcR_11", "sGPTcR_11"),
                        AssignmentStatement("LRpMbf_11", P4subsat(z3.BitVecVal(37657, 32), P4Cast("sGPTcR_11", z3.BitVecSort(32)))),
                        AssignmentStatement("hasReturned_15", z3.BoolVal(True)),
                        AssignmentStatement("retval_17", "LRpMbf_11"),
                        AssignmentStatement("tmp_49", "retval_17"),]
                    ),
                    AssignmentStatement("tmp_50", P4ne("tmp_46", P4Cast("tmp_49", z3.BitVecSort(9)))),
                    IfStatement(P4not("tmp_50"), BlockStatement([
                        AssignmentStatement("tmp_51", z3.BoolVal(False)),]
                    ), BlockStatement([
                        AssignmentStatement("tmp_51", P4eq(z3.BitVecVal(1444364813109517, 51), P4Cast(z3.BitVecVal(65535, 16), z3.BitVecSort(51)))),]
                    )),
                    AssignmentStatement("tmp_45", "tmp_51"),
                    AssignmentStatement("tmp_52", z3.BitVecVal(127537729978999984111170865926198740152, 128)),
                    AssignmentStatement("hasReturned_12", z3.BoolVal(True)),
                    AssignmentStatement("retval_14", P4Cast(P4Initializer(["tmp_42", "tmp_43", "tmp_44", "tmp_45", "tmp_52", ], ), "Vnytmj")),]
                ),
                AssignmentStatement(P4Member(P4Member("h", "BqNk"), "iUNX"), P4Member(P4Member("h", "zkbz"), "mjHD")),
                BlockStatement([
                    AssignmentStatement("hasReturned_16", z3.BoolVal(False)),
                    AssignmentStatement("sGPTcR_12", z3.BitVecVal(8331771506825847071, 64)),
                    AssignmentStatement("sGPTcR_12", "sGPTcR_12"),
                    AssignmentStatement("LRpMbf_12", P4subsat(z3.BitVecVal(37657, 32), P4Cast("sGPTcR_12", z3.BitVecSort(32)))),
                    AssignmentStatement("hasReturned_16", z3.BoolVal(True)),
                    AssignmentStatement("retval_18", "LRpMbf_12"),]
                ),
                AssignmentStatement(P4Member(P4Member("h", "BqNk"), "YwAD"), z3.BitVecVal(4314245641897930119, 64)),
                AssignmentStatement(P4Member(P4Member("h", "BqNk"), "YwAD"), P4Member(P4Member("h", "BqNk"), "YwAD")),]
            ),
            local_decls=[
ValueDeclaration("tmp", None, z3_type=z3.BitVecSort(16)), 
ValueDeclaration("tmp_0", None, z3_type=z3.BitVecSort(32)), 
ValueDeclaration("tmp_1", None, z3_type=z3.BitVecSort(16)), 
ValueDeclaration("tmp_2", None, z3_type=z3.BitVecSort(16)), 
ValueDeclaration("tmp_3", None, z3_type=z3.BitVecSort(16)), 
ValueDeclaration("IArlRL_xQNzSP", None, z3_type=z3.BitVecSort(32)), 
ValueDeclaration("IArlRL_SYsGZI", None, z3_type=z3.BitVecSort(128)), 
ValueDeclaration("IArlRL_tmp", None, z3_type=z3.BitVecSort(32)), 
ValueDeclaration("IArlRL_tmp_0", None, z3_type=z3.BitVecSort(32)), 
ValueDeclaration("IArlRL_tmp_1", None, z3_type=z3.BitVecSort(32)), 
ValueDeclaration("IArlRL_tmp_2", None, z3_type=z3.BitVecSort(32)), 
ValueDeclaration("hasReturned", None, z3_type=z3.BoolSort()), 
ValueDeclaration("retval", None, z3_type=z3.BitVecSort(32)), 
ValueDeclaration("sGPTcR_0", None, z3_type=z3.BitVecSort(64)), 
ValueDeclaration("LRpMbf_0", None, z3_type=z3.BitVecSort(32)), 
ValueDeclaration("hasReturned_0", None, z3_type=z3.BoolSort()), 
ValueDeclaration("retval_0", None, z3_type="Vnytmj"), 
ValueDeclaration("tmp_4", None, z3_type=z3.BoolSort()), 
ValueDeclaration("tmp_5", None, z3_type=z3.BitVecSort(32)), 
ValueDeclaration("tmp_6", None, z3_type=z3.BitVecSort(16)), 
ValueDeclaration("tmp_7", None, z3_type=z3.BoolSort()), 
ValueDeclaration("tmp_8", None, z3_type=z3.BitVecSort(9)), 
ValueDeclaration("tmp_9", None, z3_type=z3.BitVecSort(32)), 
ValueDeclaration("tmp_14", None, z3_type=z3.BitVecSort(9)), 
ValueDeclaration("tmp_15", None, z3_type=z3.BitVecSort(32)), 
ValueDeclaration("tmp_16", None, z3_type=z3.BoolSort()), 
ValueDeclaration("tmp_17", None, z3_type=z3.BoolSort()), 
ValueDeclaration("tmp_18", None, z3_type=z3.BitVecSort(128)), 
ValueDeclaration("kXmlrB_0", None, z3_type=z3.BitVecSort(8)), 
ValueDeclaration("hasReturned_3", None, z3_type=z3.BoolSort()), 
ValueDeclaration("retval_5", None, z3_type=z3.BitVecSort(32)), 
ValueDeclaration("sGPTcR_1", None, z3_type=z3.BitVecSort(64)), 
ValueDeclaration("LRpMbf_1", None, z3_type=z3.BitVecSort(32)), 
ValueDeclaration("hasReturned_4", None, z3_type=z3.BoolSort()), 
ValueDeclaration("retval_6", None, z3_type=z3.BitVecSort(32)), 
ValueDeclaration("sGPTcR_2", None, z3_type=z3.BitVecSort(64)), 
ValueDeclaration("LRpMbf_2", None, z3_type=z3.BitVecSort(32)), 
ValueDeclaration("hasReturned_5", None, z3_type=z3.BoolSort()), 
ValueDeclaration("retval_7", None, z3_type=z3.BitVecSort(32)), 
ValueDeclaration("sGPTcR_3", None, z3_type=z3.BitVecSort(64)), 
ValueDeclaration("LRpMbf_3", None, z3_type=z3.BitVecSort(32)), 
ValueDeclaration("hasReturned_6", None, z3_type=z3.BoolSort()), 
ValueDeclaration("retval_8", None, z3_type=z3.BitVecSort(32)), 
ValueDeclaration("sGPTcR_4", None, z3_type=z3.BitVecSort(64)), 
ValueDeclaration("LRpMbf_4", None, z3_type=z3.BitVecSort(32)), 
ValueDeclaration("hasReturned_7", None, z3_type=z3.BoolSort()), 
ValueDeclaration("retval_9", None, z3_type=z3.BitVecSort(32)), 
ValueDeclaration("sGPTcR_5", None, z3_type=z3.BitVecSort(64)), 
ValueDeclaration("LRpMbf_5", None, z3_type=z3.BitVecSort(32)), 
ValueDeclaration("hasReturned_8", None, z3_type=z3.BoolSort()), 
ValueDeclaration("retval_10", None, z3_type="Vnytmj"), 
ValueDeclaration("tmp_31", None, z3_type=z3.BoolSort()), 
ValueDeclaration("tmp_32", None, z3_type=z3.BitVecSort(32)), 
ValueDeclaration("tmp_33", None, z3_type=z3.BitVecSort(16)), 
ValueDeclaration("tmp_34", None, z3_type=z3.BoolSort()), 
ValueDeclaration("tmp_35", None, z3_type=z3.BitVecSort(9)), 
ValueDeclaration("tmp_36", None, z3_type=z3.BitVecSort(32)), 
ValueDeclaration("tmp_37", None, z3_type=z3.BitVecSort(9)), 
ValueDeclaration("tmp_38", None, z3_type=z3.BitVecSort(32)), 
ValueDeclaration("tmp_39", None, z3_type=z3.BoolSort()), 
ValueDeclaration("tmp_40", None, z3_type=z3.BoolSort()), 
ValueDeclaration("tmp_41", None, z3_type=z3.BitVecSort(128)), 
ValueDeclaration("kXmlrB_1", None, z3_type=z3.BitVecSort(8)), 
ValueDeclaration("hasReturned_9", None, z3_type=z3.BoolSort()), 
ValueDeclaration("retval_11", None, z3_type=z3.BitVecSort(32)), 
ValueDeclaration("sGPTcR_6", None, z3_type=z3.BitVecSort(64)), 
ValueDeclaration("LRpMbf_6", None, z3_type=z3.BitVecSort(32)), 
ValueDeclaration("hasReturned_10", None, z3_type=z3.BoolSort()), 
ValueDeclaration("retval_12", None, z3_type=z3.BitVecSort(32)), 
ValueDeclaration("sGPTcR_7", None, z3_type=z3.BitVecSort(64)), 
ValueDeclaration("LRpMbf_7", None, z3_type=z3.BitVecSort(32)), 
ValueDeclaration("hasReturned_11", None, z3_type=z3.BoolSort()), 
ValueDeclaration("retval_13", None, z3_type=z3.BitVecSort(32)), 
ValueDeclaration("sGPTcR_8", None, z3_type=z3.BitVecSort(64)), 
ValueDeclaration("LRpMbf_8", None, z3_type=z3.BitVecSort(32)), 
ValueDeclaration("hasReturned_12", None, z3_type=z3.BoolSort()), 
ValueDeclaration("retval_14", None, z3_type="Vnytmj"), 
ValueDeclaration("tmp_42", None, z3_type=z3.BoolSort()), 
ValueDeclaration("tmp_43", None, z3_type=z3.BitVecSort(32)), 
ValueDeclaration("tmp_44", None, z3_type=z3.BitVecSort(16)), 
ValueDeclaration("tmp_45", None, z3_type=z3.BoolSort()), 
ValueDeclaration("tmp_46", None, z3_type=z3.BitVecSort(9)), 
ValueDeclaration("tmp_47", None, z3_type=z3.BitVecSort(32)), 
ValueDeclaration("tmp_48", None, z3_type=z3.BitVecSort(9)), 
ValueDeclaration("tmp_49", None, z3_type=z3.BitVecSort(32)), 
ValueDeclaration("tmp_50", None, z3_type=z3.BoolSort()), 
ValueDeclaration("tmp_51", None, z3_type=z3.BoolSort()), 
ValueDeclaration("tmp_52", None, z3_type=z3.BitVecSort(128)), 
ValueDeclaration("kXmlrB_2", None, z3_type=z3.BitVecSort(8)), 
ValueDeclaration("hasReturned_13", None, z3_type=z3.BoolSort()), 
ValueDeclaration("retval_15", None, z3_type=z3.BitVecSort(32)), 
ValueDeclaration("sGPTcR_9", None, z3_type=z3.BitVecSort(64)), 
ValueDeclaration("LRpMbf_9", None, z3_type=z3.BitVecSort(32)), 
ValueDeclaration("hasReturned_14", None, z3_type=z3.BoolSort()), 
ValueDeclaration("retval_16", None, z3_type=z3.BitVecSort(32)), 
ValueDeclaration("sGPTcR_10", None, z3_type=z3.BitVecSort(64)), 
ValueDeclaration("LRpMbf_10", None, z3_type=z3.BitVecSort(32)), 
ValueDeclaration("hasReturned_15", None, z3_type=z3.BoolSort()), 
ValueDeclaration("retval_17", None, z3_type=z3.BitVecSort(32)), 
ValueDeclaration("sGPTcR_11", None, z3_type=z3.BitVecSort(64)), 
ValueDeclaration("LRpMbf_11", None, z3_type=z3.BitVecSort(32)), 
ValueDeclaration("hasReturned_16", None, z3_type=z3.BoolSort()), 
ValueDeclaration("retval_18", None, z3_type=z3.BitVecSort(32)), 
ValueDeclaration("sGPTcR_12", None, z3_type=z3.BitVecSort(64)), 
ValueDeclaration("LRpMbf_12", None, z3_type=z3.BitVecSort(32)), ]
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
