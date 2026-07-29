def clamp(value): return max(0,min(100,round(value)))
def average(values): return clamp(sum(values)/len(values)) if values else 0
