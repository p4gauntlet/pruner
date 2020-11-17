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
            ValueDeclaration("sGPTcR_0", None, z3_type=z3.BitVecSort(64)),
            ValueDeclaration("LRpMbf_0", None, z3_type=z3.BitVecSort(32)),
            ValueDeclaration("AfXLZG_0", None, z3_type=z3.BitVecSort(128)),
            AssignmentStatement("sGPTcR_0", z3.BitVecVal(8331771506825847071, 64)),
            AssignmentStatement("sGPTcR_0", "sGPTcR_0"),
            AssignmentStatement("LRpMbf_0", P4subsat(z3.BitVecVal(37657, 32), P4Cast("sGPTcR_0", z3.BitVecSort(32)))),
            P4Return("LRpMbf_0"),
            P4Return(z3.BitVecVal(2806012093, 32)),
            P4Return(z3.BitVecVal(1938567799, 32)),
            P4Return(P4bor(z3.BitVecVal(839498710, 32), P4Cast("AfXLZG_0", z3.BitVecSort(32)))),]
        )        )        )
    )
    z3_reg.declare_global(
        P4Declaration("IBaXWsK", P4Function("IBaXWsK", return_type="Vnytmj", params=[
            P4Parameter("none", "yQJV", z3.BitVecSort(64), None),
            P4Parameter("none", "gOEI", z3.BitVecSort(16), None),],         body=BlockStatement([
            ValueDeclaration("tmp", None, z3_type=z3.BoolSort()),
            ValueDeclaration("tmp_0", None, z3_type=z3.BitVecSort(32)),
            ValueDeclaration("tmp_1", None, z3_type=z3.BitVecSort(16)),
            ValueDeclaration("tmp_2", None, z3_type=z3.BoolSort()),
            ValueDeclaration("tmp_3", None, z3_type=z3.BitVecSort(9)),
            ValueDeclaration("tmp_4", None, z3_type=z3.BitVecSort(32)),
            ValueDeclaration("tmp_5", None, z3_type=z3.BitVecSort(9)),
            ValueDeclaration("tmp_6", None, z3_type=z3.BitVecSort(32)),
            ValueDeclaration("tmp_7", None, z3_type=z3.BoolSort()),
            ValueDeclaration("tmp_8", None, z3_type=z3.BoolSort()),
            ValueDeclaration("tmp_9", None, z3_type=z3.BitVecSort(128)),
            ValueDeclaration("kXmlrB_0", None, z3_type=z3.BitVecSort(8)),
            AssignmentStatement("kXmlrB_0", P4Slice(P4addsat(P4Cast("yQJV", z3.BitVecSort(43)), z3.BitVecVal(1462566353592, 43)), 16, 9)),
            AssignmentStatement("kXmlrB_0", "kXmlrB_0"),
            MethodCallStmt(MethodCallExpr("ZqTDGWH", [], )),
            AssignmentStatement("tmp", z3.BoolVal(False)),
            AssignmentStatement("tmp_0", P4Cast("yQJV", z3.BitVecSort(32))),
            AssignmentStatement("tmp_1", z3.BitVecVal(14442, 16)),
            AssignmentStatement("tmp_4", MethodCallExpr("ZqTDGWH", [], )),
            AssignmentStatement("tmp_5", P4bor(P4Cast("tmp_4", z3.BitVecSort(9)), z3.BitVecVal(260, 9))),
            AssignmentStatement("tmp_3", "tmp_5"),
            AssignmentStatement("tmp_6", MethodCallExpr("ZqTDGWH", [], )),
            AssignmentStatement("tmp_7", P4ne("tmp_3", P4Cast("tmp_6", z3.BitVecSort(9)))),
            IfStatement(P4not("tmp_7"), BlockStatement([
                AssignmentStatement("tmp_8", z3.BoolVal(False)),]
            ), BlockStatement([
                AssignmentStatement("tmp_8", P4eq(z3.BitVecVal(1444364813109517, 51), P4Cast("gOEI", z3.BitVecSort(51)))),]
            )),
            AssignmentStatement("tmp_2", "tmp_8"),
            AssignmentStatement("tmp_9", z3.BitVecVal(127537729978999984111170865926198740152, 128)),
            P4Return(P4Cast(P4Initializer(["tmp", "tmp_0", "tmp_1", "tmp_2", "tmp_9", ], ), "Vnytmj")),
            MethodCallStmt(MethodCallExpr("ZqTDGWH", [], )),
            P4Return(P4Cast(P4Initializer([z3.BoolVal(True), z3.BitVecVal(1354969928, 32), "gOEI", z3.BoolVal(True), z3.BitVecVal(8, 128), ], ), "Vnytmj")),]
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
                AssignmentStatement("xQNzSP_0", z3.BitVecVal(1305108261, 32)),
                AssignmentStatement("SYsGZI_0", z3.BitVecVal(18672238, 128)),
                AssignmentStatement("tmp_10", "xQNzSP_0"),
                AssignmentStatement("tmp_11", MethodCallExpr("ZqTDGWH", [], )),
                AssignmentStatement("tmp_12", P4add("tmp_10", "tmp_11")),
                AssignmentStatement("tmp_13", P4subsat("tmp_12", z3.BitVecVal(2827375294, 32))),
                AssignmentStatement("xQNzSP_0", "tmp_13"),
                MethodCallStmt(MethodCallExpr("ZqTDGWH", [], )),
                AssignmentStatement("SYsGZI_0", "SYsGZI_0"),
                MethodCallStmt(MethodCallExpr("IBaXWsK", [], z3.BitVecVal(9569382937354443357, 64), z3.BitVecVal(0, 16), )),]
            ),
            local_decls=[
ValueDeclaration("xQNzSP_0", None, z3_type=z3.BitVecSort(32)), 
ValueDeclaration("SYsGZI_0", None, z3_type=z3.BitVecSort(128)), 
ValueDeclaration("tmp_10", None, z3_type=z3.BitVecSort(32)), 
ValueDeclaration("tmp_11", None, z3_type=z3.BitVecSort(32)), 
ValueDeclaration("tmp_12", None, z3_type=z3.BitVecSort(32)), 
ValueDeclaration("tmp_13", None, z3_type=z3.BitVecSort(32)), ]
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
                AssignmentStatement("tmp_14", P4Member(P4Member("h", "eth_hdr"), "eth_type")),
                AssignmentStatement("tmp_15", MethodCallExpr("ZqTDGWH", [], )),
                AssignmentStatement("tmp_16", P4bor("tmp_14", P4Cast("tmp_15", z3.BitVecSort(16)))),
                AssignmentStatement("tmp_17", P4bor("tmp_16", z3.BitVecVal(58652, 16))),
                AssignmentStatement("tmp_18", P4add("tmp_17", z3.BitVecVal(30345, 16))),
                MethodCallStmt(MethodCallExpr("IBaXWsK", [], z3.BitVecVal(11378255015260334646, 64), z3.BitVecVal(59162, 16), )),
                MethodCallStmt(MethodCallExpr(P4Member("IArlRL_0", "apply"), [], P4Member(P4Member("h", "zkbz"), "WNfX"), z3.BitVecVal(1017011646, 128), )),
                MethodCallStmt(MethodCallExpr("IBaXWsK", [], z3.BitVecVal(16257984866694305357, 64), z3.BitVecVal(65535, 16), )),
                AssignmentStatement(P4Member(P4Member("h", "BqNk"), "iUNX"), P4Member(P4Member("h", "zkbz"), "mjHD")),
                MethodCallStmt(MethodCallExpr("ZqTDGWH", [], )),
                AssignmentStatement(P4Member(P4Member("h", "BqNk"), "YwAD"), z3.BitVecVal(4314245641897930119, 64)),
                AssignmentStatement(P4Member(P4Member("h", "BqNk"), "YwAD"), P4Member(P4Member("h", "BqNk"), "YwAD")),]
            ),
            local_decls=[
ValueDeclaration("tmp_14", None, z3_type=z3.BitVecSort(16)), 
ValueDeclaration("tmp_15", None, z3_type=z3.BitVecSort(32)), 
ValueDeclaration("tmp_16", None, z3_type=z3.BitVecSort(16)), 
ValueDeclaration("tmp_17", None, z3_type=z3.BitVecSort(16)), 
ValueDeclaration("tmp_18", None, z3_type=z3.BitVecSort(16)), 
InstanceDeclaration("IArlRL_0", "PFizfTj", ), ]
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
