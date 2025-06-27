from zxcvbn import zxcvbn

def analyze_password(password):
    result = zxcvbn(password)
    return {
        "score": result['score'],
        "feedback": result['feedback'],
        "crack_times_display": result['crack_times_display']
    }
