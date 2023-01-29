

def get_qual_risk(sharpe_denom):
    if sharpe_denom < .0260:
        return "low risk"
    if sharpe_denom > .0335:
        return "high risk"

    return "medium risk"


def get_qual_performance_risk(sharpe_value):
    if sharpe_value> 3:
        return "excellent"
    if sharpe_value > 2:
        return "very good"
    if sharpe_value > .9:
        return "good"
    if sharpe_value > 0:
        return "mediocre"

    return "bad"

