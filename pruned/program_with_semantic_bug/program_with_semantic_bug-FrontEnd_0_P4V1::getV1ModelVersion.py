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
                ValueDeclaration("sGPTcR", P4Initializer(P4Slice(z3.BitVecVal(53557031161070797374, 68), 64, 1), z3.BitVecSort(64)), z3_type=z3.BitVecSort(64)),
                BlockStatement([
                    ValueDeclaration("oZMmrS", z3.BitVecVal(37657, 16), z3_type=z3.BitVecSort(16)),
                    AssignmentStatement("sGPTcR", "sGPTcR"),
                    ValueDeclaration("LRpMbf", P4Initializer(P4Cast(P4subsat(P4Cast("oZMmrS", z3.BitVecSort(32)), P4Cast("sGPTcR", z3.BitVecSort(32))), z3.BitVecSort(32)), z3.BitVecSort(32)), z3_type=z3.BitVecSort(32)),
                    AssignmentStatement("sGPTcR", P4mod(z3.BitVecVal(16398916870993737006, 64), z3.BitVecVal(427530368926876134, 64))),
                    P4Return("LRpMbf"),]
                ),
                AssignmentStatement("sGPTcR", "sGPTcR"),
                ValueDeclaration("noVnDj", P4Initializer(z3.BitVecVal(1172448623121743915, 64), z3.BitVecSort(64)), z3_type=z3.BitVecSort(64)),
                AssignmentStatement("noVnDj", P4neg(z3.BitVecVal(9291219075994716466, 64))),
                AssignmentStatement("noVnDj", 859692371),
                AssignmentStatement("sGPTcR", P4lshift(P4Cast(z3.BitVecVal(2898692507126017355, 64), z3.BitVecSort(64)), P4Cast(z3.BitVecVal(11981686051562272611, 64), z3.BitVecSort(8)))),
                AssignmentStatement("sGPTcR", P4add(P4lshift(P4sub("sGPTcR", z3.BitVecVal(11817574793371717234, 64)), P4Cast(P4Concat(z3.BitVecVal(13079922245, 34), z3.BitVecVal(269591351, 30)), z3.BitVecSort(8))), "noVnDj")),
                ValueDeclaration("yZIceN", 838390161, z3_type=z3.IntSort()),
                P4Return(z3.BitVecVal(2806012093, 32)),]
            ),
            ValueDeclaration("AfXLZG", P4Initializer(2144402680, z3.BitVecSort(128)), z3_type=z3.BitVecSort(128)),
            AssignmentStatement("AfXLZG", P4band(z3.BitVecVal(290201655608422881013301261221431492354, 128), P4Mux(P4not(P4lor(P4not(P4lor(z3.BoolVal(False), P4lor(P4not(P4not(P4lor(z3.BoolVal(True), P4not(P4not(z3.BoolVal(False)))))), P4not(z3.BoolVal(True))))), z3.BoolVal(True))), P4subsat(P4Cast(z3.BitVecVal(898317342468254849257934916010057547, 128), z3.BitVecSort(128)), z3.BitVecVal(7095990583075605562491329095786241671, 128)), P4Concat(z3.BitVecVal(26593309204912329688403, 78), z3.BitVecVal(796590729582915, 50))))),
            AssignmentStatement("AfXLZG", "AfXLZG"),
            AssignmentStatement("AfXLZG", P4Mux(P4not(P4not(P4lor(z3.BoolVal(False), P4land(z3.BoolVal(True), P4eq(z3.BitVecVal(126521560808615075284510202349, 99), z3.BitVecVal(93554252872241793680402658917, 99)))))), z3.BitVecVal(265277269598615858768621607659578766285, 128), "AfXLZG")),
            AssignmentStatement("AfXLZG", z3.BitVecVal(306288353508935945900133283398710167980, 128)),
            AssignmentStatement("AfXLZG", "AfXLZG"),
            BlockStatement([
                AssignmentStatement("AfXLZG", z3.BitVecVal(203190633050105623488232349361061266317, 128)),
                AssignmentStatement("AfXLZG", z3.BitVecVal(119851796932508784808775619006417521460, 128)),
                AssignmentStatement("AfXLZG", z3.BitVecVal(89063546262527641425054991023365647631, 128)),
                AssignmentStatement("AfXLZG", "AfXLZG"),
                ValueDeclaration("pQiUqJ", z3.BitVecVal(15318551338288664749, 64), z3_type=z3.BitVecSort(64)),
                ValueDeclaration("rPqZzN", P4Mux(P4not(z3.BoolVal(False)), P4Cast(P4neg(1784394285), z3.BitVecSort(8)), P4mod(z3.BitVecVal(143, 8), z3.BitVecVal(170, 8))), z3_type=z3.BitVecSort(8)),
                AssignmentStatement("AfXLZG", P4Slice(z3.BitVecVal(1767574341728031404715666999839022448308662552235129012715307495487784, 235), 229, 102)),
                AssignmentStatement("AfXLZG", P4add(P4lshift(P4Cast(P4sub(P4neg(2108222292), P4neg(2028710138)), z3.BitVecSort(128)), P4Cast(z3.BitVecVal(65220779906866385009446598857967736806, 128), z3.BitVecSort(8))), z3.BitVecVal(232550981149043971176658599253778146419, 128))),
                AssignmentStatement("AfXLZG", "AfXLZG"),
                P4Return(P4add(P4Cast("rPqZzN", z3.BitVecSort(32)), z3.BitVecVal(1938567588, 32))),]
            ),
            P4Return(P4Mux(P4not(P4not(z3.BoolVal(False))), P4Cast("AfXLZG", z3.BitVecSort(32)), P4Cast(P4bor(839498710, P4Cast("AfXLZG", z3.BitVecSort(32))), z3.BitVecSort(32)))),]
        )        )        )
    )
    z3_reg.declare_global(
        P4Declaration("IBaXWsK", P4Function("IBaXWsK", return_type="Vnytmj", params=[
            P4Parameter("none", "yQJV", z3.BitVecSort(64), None),
            P4Parameter("none", "gOEI", z3.BitVecSort(16), None),],         body=BlockStatement([
            ValueDeclaration("kXmlrB", P4Initializer(P4Slice(P4Mux(P4not(P4not(z3.BoolVal(True))), P4addsat(P4bor(P4Cast("yQJV", z3.BitVecSort(43)), P4Cast("yQJV", z3.BitVecSort(43))), z3.BitVecVal(1462566353592, 43)), z3.BitVecVal(984356912767, 43)), 16, 9), z3.BitVecSort(8)), z3_type=z3.BitVecSort(8)),
            BlockStatement([
                IfStatement(P4land(P4not(P4land(z3.BoolVal(False), z3.BoolVal(True))), P4not(z3.BoolVal(False))), BlockStatement([
                    AssignmentStatement("kXmlrB", P4Mux(z3.BoolVal(True), "kXmlrB", P4Slice(P4Cast("yQJV", z3.BitVecSort(30)), 26, 19))),]
                ), BlockStatement([
                    AssignmentStatement("kXmlrB", "kXmlrB"),]
                )),
                AssignmentStatement("kXmlrB", "kXmlrB"),
                ValueDeclaration("YXRheT", 77175706, z3_type=z3.IntSort()),
                MethodCallStmt(MethodCallExpr("ZqTDGWH", [], )),
                AssignmentStatement("kXmlrB", z3.BitVecVal(174, 8)),
                P4Return([P4not(P4not(P4lor(z3.BoolVal(False), P4not(z3.BoolVal(True))))), P4Cast("yQJV", z3.BitVecSort(32)), z3.BitVecVal(14442, 16), P4not(P4not(P4land(P4ne(P4bor(P4Cast(MethodCallExpr("ZqTDGWH", [], ), z3.BitVecSort(9)), z3.BitVecVal(260, 9)), P4Cast(MethodCallExpr("ZqTDGWH", [], ), z3.BitVecSort(9))), P4not(P4not(P4not(P4not(P4eq(z3.BitVecVal(1444364813109517, 51), P4Mux(z3.BoolVal(False), P4Cast("gOEI", z3.BitVecSort(51)), P4Cast("gOEI", z3.BitVecSort(51))))))))))), z3.BitVecVal(127537729978999984111170865926198740152, 128), ]),]
            ),
            ValueDeclaration("wUxkGX", [z3.BitVecVal(11, 4), z3.BitVecVal(16737022111367307944, 64), z3.BitVecVal(2836164008, 32), ], z3_type="jCFTwO"),
            AssignmentStatement("kXmlrB", P4band(P4xor(P4neg(1656398165), P4band(1119644396, P4neg(1299329753))), z3.BitVecVal(14, 8))),
            AssignmentStatement("kXmlrB", "kXmlrB"),
            MethodCallStmt(MethodCallExpr("ZqTDGWH", [], )),
            P4Return([z3.BoolVal(True), z3.BitVecVal(1354969928, 32), "gOEI", z3.BoolVal(True), P4band(P4Cast(P4Member("wUxkGX", "iUNX"), z3.BitVecSort(128)), P4Cast(P4Member("wUxkGX", "PamX"), z3.BitVecSort(128))), ]),]
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
                AssignmentStatement("xQNzSP", P4subsat(P4add("xQNzSP", P4Cast(MethodCallExpr("ZqTDGWH", [], ), z3.BitVecSort(32))), z3.BitVecVal(2827375294, 32))),
                MethodCallStmt(MethodCallExpr("ZqTDGWH", [], )),
                AssignmentStatement("SYsGZI", "SYsGZI"),
                AssignmentStatement("xQNzSP", "xQNzSP"),
                MethodCallStmt(MethodCallExpr("IBaXWsK", [], z3.BitVecVal(9569382937354443357, 64), P4div(z3.BitVecVal(47370, 16), z3.BitVecVal(52726, 16)), )),
                AssignmentStatement("SYsGZI", P4bor(P4sub("SYsGZI", z3.BitVecVal(174843887977112616899567535517197106864, 128)), "SZxu")),]
            ),
            local_decls=[
ValueDeclaration("oHvtbH", P4Initializer(P4lor(z3.BoolVal(False), P4not(P4lor(P4not(P4eq(P4bor(P4subsat(P4Mux(z3.BoolVal(True), P4Slice(P4Cast(P4Cast("SZxu", z3.BitVecSort(79)), z3.BitVecSort(79)), 78, 22), z3.BitVecVal(27316355257469953, 57)), z3.BitVecVal(128961855891103457, 57)), z3.BitVecVal(83480883236889332, 57)), P4Cast("lcNR", z3.BitVecSort(57)))), P4not(P4not(P4lor(P4not(z3.BoolVal(False)), z3.BoolVal(True))))))), z3.BoolSort()), z3_type=z3.BoolSort()), 
ValueDeclaration("nYJwrn", P4Initializer(z3.BitVecVal(12914525900351020762, 64), z3.BitVecSort(64)), z3_type=z3.BitVecSort(64)), 
ValueDeclaration("htHGwZ", P4Initializer(P4not(P4not("oHvtbH")), z3.BoolSort()), z3_type=z3.BoolSort()), 
ValueDeclaration("xQNzSP", P4Initializer(z3.BitVecVal(1305108261, 32), z3.BitVecSort(32)), z3_type=z3.BitVecSort(32)), 
ValueDeclaration("SYsGZI", P4Initializer(P4xor(P4neg(69135971), P4neg(84018189)), z3.BitVecSort(128)), z3_type=z3.BitVecSort(128)), 
ValueDeclaration("NdjDFo", P4Initializer(P4lor(P4ne(P4Slice(P4addsat(P4Cast(P4Cast("nYJwrn", z3.BitVecSort(113)), z3.BitVecSort(113)), P4Cast("lcNR", z3.BitVecSort(113))), 62, 9), P4add(z3.BitVecVal(5833293339867020, 54), z3.BitVecVal(14324310626544480, 54))), P4ne(P4band(z3.BitVecVal(1972002707832674242128141845115307680, 124), P4neg(1808553676)), z3.BitVecVal(10100509633410923453791864725814817281, 124))), z3.BoolSort()), z3_type=z3.BoolSort()), 
P4Declaration("woqMg", P4Action("woqMg", params=[
                    P4Parameter("inout", "OcIW", z3.BitVecSort(4), None),
                    P4Parameter("out", "ILUP", "Vnytmj", None),
                    P4Parameter("none", "YFnT", z3.BitVecSort(128), None),],                 body=BlockStatement([
                    AssignmentStatement("OcIW", z3.BitVecVal(15, 4)),
                    BlockStatement([
                        AssignmentStatement("OcIW", z3.BitVecVal(1, 4)),
                        AssignmentStatement("nYJwrn", P4neg(P4neg(440494971))),
                        AssignmentStatement(P4Member("ILUP", "GXQs"), "SZxu"),
                        AssignmentStatement("nYJwrn", "nYJwrn"),
                        AssignmentStatement("xQNzSP", P4Concat(P4Cast(z3.BitVecVal(3072515, 22), z3.BitVecSort(22)), z3.BitVecVal(235, 10))),
                        AssignmentStatement(P4Slice(P4Member("ILUP", "GXQs"), 56, 41), P4Member("ILUP", "pBFG")),
                        AssignmentStatement("lcNR", P4xor(P4add(P4band(P4neg(2139035674), 756808726), P4neg(1830690600)), 1514111508)),
                        ValueDeclaration("xtBTEG", P4Initializer(z3.BitVecVal(4137147051, 32), z3.BitVecSort(32)), z3_type=z3.BitVecSort(32)),
                        AssignmentStatement(P4Member("ILUP", "pBFG"), z3.BitVecVal(23124, 16)),
                        AssignmentStatement(P4Slice(P4Member("ILUP", "xjKr"), 8, 5), "OcIW"),]
                    ),
                    AssignmentStatement("OcIW", P4addsat(P4Cast(P4neg("OcIW"), z3.BitVecSort(4)), P4Slice(P4Cast(MethodCallExpr("ZqTDGWH", [], ), z3.BitVecSort(78)), 73, 70))),
                    AssignmentStatement(P4Slice(P4Member("ILUP", "GXQs"), 36, 5), z3.BitVecVal(1728758457, 32)),
                    MethodCallStmt(MethodCallExpr("IBaXWsK", [], z3.BitVecVal(10928050462811547131, 64), z3.BitVecVal(55614, 16), )),
                    AssignmentStatement(P4Slice("nYJwrn", 6, 3), P4Cast(MethodCallExpr("ZqTDGWH", [], ), z3.BitVecSort(4))),
                    P4Return(None),
                    MethodCallStmt(MethodCallExpr("IBaXWsK", [], z3.BitVecVal(6235384825236171976, 64), z3.BitVecVal(36291, 16), )),]
                )                )), 
P4Declaration("CBiEr", P4Action("CBiEr", params=[
                    P4Parameter("in", "DgGZ", z3.BitVecSort(8), None),
                    P4Parameter("none", "MevJ", "KGAUpM", None),
                    P4Parameter("none", "PHeC", z3.BitVecSort(8), None),],                 body=BlockStatement([
                    ValueDeclaration("UitBTw", P4Initializer([z3.BitVecVal(1531371326, 32), "xQNzSP", P4inv(P4xor("PHeC", z3.BitVecVal(221, 8))), z3.BitVecVal(3628752390428671448, 64), ], "pQcOkh"), z3_type="pQcOkh"),
                    AssignmentStatement("SYsGZI", z3.BitVecVal(216323781136148277345578055083500959293, 128)),
                    AssignmentStatement(P4Member("UitBTw", "wBCb"), z3.BitVecVal(2554680596, 32)),
                    AssignmentStatement(P4Member("UitBTw", "XbXc"), z3.BitVecVal(10, 8)),
                    MethodCallStmt(MethodCallExpr("ZqTDGWH", [], )),
                    AssignmentStatement("SYsGZI", "SZxu"),
                    AssignmentStatement("SYsGZI", P4neg(P4Slice(P4Cast("lcNR", z3.BitVecSort(182)), 131, 4))),
                    AssignmentStatement("SYsGZI", P4neg(P4rshift(P4subsat("SYsGZI", P4xor(z3.BitVecVal(243328255867979410922387748647889646280, 128), z3.BitVecVal(142069344174629607110478862563052744580, 128))), P4Cast(z3.BitVecVal(97451597401805586974158020750006213781, 128), z3.BitVecSort(8))))),
                    ValueDeclaration("GSuYjJ", P4Initializer(P4inv(P4Member("UitBTw", "wBCb")), z3.BitVecSort(32)), z3_type=z3.BitVecSort(32)),
                    AssignmentStatement(P4Member("UitBTw", "XbXc"), P4Slice(P4Cast("DgGZ", z3.BitVecSort(130)), 109, 102)),
                    MethodCallStmt(MethodCallExpr("ZqTDGWH", [], )),]
                )                )), 
P4Declaration("TNAYJq", P4Table("TNAYJq", key=[("SYsGZI", "exact"), ], actions=[], immutable=False)), 
P4Declaration("VtgSNW", P4Table("VtgSNW", key=[(P4Mux(P4not(P4not(z3.BoolVal(False))), P4Slice(P4Cast("xQNzSP", z3.BitVecSort(185)), 162, 35), z3.BitVecVal(50421981630794248132575380387204031162, 128)), "exact"), (P4Mux("oHvtbH", P4neg(z3.BitVecVal(952818420, 32)), z3.BitVecVal(3429918406, 32)), "exact"), (z3.BitVecVal(17488452717387411170, 64), "exact"), ], actions=[], immutable=False)), 
P4Declaration("YSvMfd", P4Table("YSvMfd", key=[(P4Slice(P4Cast("xQNzSP", z3.BitVecSort(213)), 157, 30), "exact"), ], actions=[], immutable=False)), ]
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
                AssignmentStatement(P4Member(P4Member("h", "zkbz"), "WNfX"), P4add(P4bor(P4bor(P4Member(P4Member("h", "eth_hdr"), "eth_type"), P4Cast(MethodCallExpr("ZqTDGWH", [], ), z3.BitVecSort(16))), z3.BitVecVal(58652, 16)), z3.BitVecVal(30345, 16))),
                MethodCallStmt(MethodCallExpr("IBaXWsK", [], z3.BitVecVal(11378255015260334646, 64), z3.BitVecVal(59162, 16), )),
                MethodCallStmt(MethodCallExpr(P4Member("IArlRL", "apply"), [], P4Member(P4Member("h", "zkbz"), "WNfX"), 1017011646, )),
                IfStatement(P4not(z3.BoolVal(False)), BlockStatement([
                    MethodCallStmt(MethodCallExpr("IBaXWsK", [], z3.BitVecVal(16257984866694305357, 64), P4addsat(P4Cast(z3.BitVecVal(23685, 16), z3.BitVecSort(16)), P4inv(P4Mux(P4not(z3.BoolVal(False)), z3.BitVecVal(16709, 16), z3.BitVecVal(22268, 16)))), )),]
                ), BlockStatement([
                    SwitchStatement(P4Member(MethodCallExpr(P4Member("QyKFXD", "apply"), [], ), "action_run"),cases=[("dpTJp", BlockStatement([
                        AssignmentStatement(P4Member(P4Member("h", "zkbz"), "WNfX"), P4Slice(z3.BitVecVal(1842415444230137893288072292211188200133399, 141), 87, 72)),
                        AssignmentStatement(P4Member(P4Member("h", "BqNk"), "YwAD"), z3.BitVecVal(5755209842779639858, 64)),
                        AssignmentStatement(P4Member(P4Member("h", "BqNk"), "YwAD"), z3.BitVecVal(11024526164810448119, 64)),
                        IfStatement(z3.BoolVal(False), BlockStatement([
                            AssignmentStatement("TCVSkL", P4Cast(MethodCallExpr("ZqTDGWH", [], ), z3.BitVecSort(8))),]
                        ), BlockStatement([
                            AssignmentStatement(P4Member(P4Member("h", "zkbz"), "mjHD"), P4Member(P4Member("h", "BqNk"), "iUNX")),]
                        )),
                        AssignmentStatement(P4Member(P4Member("h", "BqNk"), "PamX"), z3.BitVecVal(4169415496, 32)),
                        MethodCallStmt(MethodCallExpr("ZqTDGWH", [], )),
                        MethodCallStmt(MethodCallExpr("IBaXWsK", [], z3.BitVecVal(12301071070313056270, 64), P4mul(z3.BitVecVal(34838, 16), z3.BitVecVal(47871, 16)), )),
                        MethodCallStmt(MethodCallExpr("IBaXWsK", [], z3.BitVecVal(7199869912651391625, 64), z3.BitVecVal(11619, 16), )),]
                    )), ]),]
                )),
                AssignmentStatement(P4Member(P4Member("h", "BqNk"), "iUNX"), P4Member(P4Member("h", "zkbz"), "mjHD")),
                MethodCallStmt(MethodCallExpr("ZqTDGWH", [], )),
                AssignmentStatement(P4Member(P4Member("h", "BqNk"), "YwAD"), z3.BitVecVal(4314245641897930119, 64)),
                AssignmentStatement(P4Member(P4Member("h", "BqNk"), "YwAD"), P4Member(P4Member("h", "BqNk"), "YwAD")),
                ValueDeclaration("oOqmbD", z3.BitVecVal(34931, 16), z3_type=z3.BitVecSort(16)),]
            ),
            local_decls=[
ValueDeclaration("TCVSkL", P4Initializer(z3.BitVecVal(41, 8), z3.BitVecSort(8)), z3_type=z3.BitVecSort(8)), 
InstanceDeclaration("IArlRL", "PFizfTj", ), 
P4Declaration("dpTJp", P4Action("dpTJp", params=[],                 body=BlockStatement([
                    MethodCallStmt(MethodCallExpr("IBaXWsK", [], P4sub(z3.BitVecVal(11781722781536468735, 64), P4neg(z3.BitVecVal(13608868080722905925, 64))), P4inv(z3.BitVecVal(51927, 16)), )),
                    MethodCallStmt(MethodCallExpr(P4Member("IArlRL", "apply"), [], P4Member(P4Member("h", "eth_hdr"), "eth_type"), z3.BitVecVal(30865149178727196209754798400394629432, 128), )),
                    P4Return(None),
                    AssignmentStatement(P4Member(P4Member("h", "eth_hdr"), "src_addr"), P4neg(78715458)),
                    ValueDeclaration("QlaOEA", P4Cast(z3.BitVecVal(2475038456, 32), z3.BitVecSort(32)), z3_type=z3.BitVecSort(32)),]
                )                )), 
P4Declaration("QyKFXD", P4Table("QyKFXD", key=[], actions=[MethodCallExpr("dpTJp", [], ), ], immutable=False)), ]
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
