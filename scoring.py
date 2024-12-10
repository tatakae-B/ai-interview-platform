def calculate_score(technical_score, behavioral_score, aptitude_score, weights=(0.5, 0.3, 0.2)):
    total_score = (technical_score * weights[0] + 
                   behavioral_score * weights[1] + 
                   aptitude_score * weights[2])
    return total_score
