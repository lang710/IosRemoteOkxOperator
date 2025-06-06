import argparse


def ParserOkx():
    parser = argparse.ArgumentParser(description="get api arguments")
    parser.add_argument("--account", type=str, default="mock", required=True, help="account[mock|chilang|juyou]")
    parser.add_argument("--action", type=str, required=True, help="action[order|cancel|list]")
    parser.add_argument("--ordId", type=str, help="ordId(int)")
    parser.add_argument("--side", type=str, help="side[buy|sell]")
    parser.add_argument("--posSide", type=str, help="posSide[long|short]")
    parser.add_argument("--ordType", type=str, help="ordType[market|limit]")
    parser.add_argument("--sz", type=str, help="sz(float)")
    parser.add_argument("--px", type=str, help="px(float)")
    args = parser.parse_args()

    return args
