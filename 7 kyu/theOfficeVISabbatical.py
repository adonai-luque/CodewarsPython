def sabb(s, value, happiness):
    return 'Sabbatical! Boom!' if (value + happiness + sum(c in 'sabbatical' for c in s.lower()) > 22) else 'Back to your desk, boy.'
    