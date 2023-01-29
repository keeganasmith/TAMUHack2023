
import risk
import risk_evaluation
import interest_rates

def get_qual_risk(sharpe_denom):
    unemployment = risk_evaluation.unemployment_risk()
    interest = interest_rates.interest_rate_risk_factor()
    total = sharpe_denom * unemployment * interest
    reasons = "";
    if(sharpe_denom > .035):
        reasons += "High volatility, "
    if(risk_evaluation.unemployment_rate > .07):
        reasons += f"High unemployment ({risk_evaluation.unemployment * 100}%), ";
    if(interest_rates.interest_rate > 4.0):
        reasons += f"High Fed interest rates ({interest_rates.interest_rate}), ";
    if total < .03:
        return "Low"
    if total > .039:
        return "High, Reasons: " + reasons

    return "Medium, Reasons: " + reasons 


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

get_qual_risk(.02)