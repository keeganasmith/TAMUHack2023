

def get_qual_risk(sharpe_denom):
    if sharpe_denom < .0260:
        return "Low"
    if sharpe_denom > .0335:
        return "High"

    return "Medium"


def get_qual_performance_risk(sharpe_value):
    if sharpe_value> 3:
        return "Excellent"
    if sharpe_value > 2:
        return "Very good"
    if sharpe_value > .9:
        return "Good"
    if sharpe_value > 0:
        return "Mediocre"

    return "Bad"

