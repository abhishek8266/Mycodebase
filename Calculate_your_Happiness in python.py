def calculate_happiness():
    
    job_satisfaction = 8
    health = 9
    relationships = 7
    hobbies = 6
    
   
    job_weight = 0.4
    health_weight = 0.3
    relationships_weight = 0.2
    hobbies_weight = 0.1
    
    
    happiness = (job_satisfaction * job_weight +
                 health * health_weight +
                 relationships * relationships_weight +
                 hobbies * hobbies_weight)
    
    return happiness


happiness_score = calculate_happiness()
print(f"My happiness score is: {happiness_score}")