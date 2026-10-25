def check_threat_severity(score):
    if score >= 80:
        return "Critical"
    elif score >= 50:
        return "High"
    else:
        return "Low"


if __name__ == "__main__":
    print("Cyber Security Threat Management System")
    print("Threat Severity:", check_threat_severity(90))
