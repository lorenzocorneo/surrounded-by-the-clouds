LINES = ["-", "--", "-."]
# COLORS = ["#66c2a5", "#fc8d62", "#8da0cb", "#e78ac3", "#a6d854", "#ffd92f", "#e5c494"]
# COLORS = ["#728ea4", "#abe2fa", "#97c324", "#b6120f", "#faaab0", "#894fc8", "#485052"]
COLORS = ["#7598b6", "#914c09", "#ce9c7f", "#c1d5e2", "#663979", "#6a7465", "#fbe17b"]
COLORS_MAP = [
    "#c1d5e2",
    "#ce9c7f",
    "#7598b6",
    "#6a7465",
    "#914c09",
    "#663979",
    "#fbe17b",
]
PROVIDERS = ["AMZN", "BABA", "DO", "GOOG", "IBM", "LIN", "MSFT", "ORCL", "VLTR"]
HATCHES = ["-", "+", "x", "\\", "*", "o", "O", "."]
WIDTH_IN = 3.37


def short_cloud(name: str) -> str:
    name = name.lower()
    if "amazon" in name:
        return "AMZN"
    if "google" in name:
        return "GOOG"
    if "microsoft" in name:
        return "MSFT"
    if "oracle" in name:
        return "ORCL"
    if "ocean" in name:
        return "DO"
    if "baba" in name:
        return "BABA"
    if "linode" in name:
        return "LIN"
    if "vultr" in name:
        return "VLTR"
    if "ibm" in name:
        return "IBM"
    else:
        return ""
