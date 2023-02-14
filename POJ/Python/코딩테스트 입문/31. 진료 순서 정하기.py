def solution(emergency):
    emergency_c = sorted(emergency, reverse=True)
    return [emergency_c.index(i)+1 for i in emergency]