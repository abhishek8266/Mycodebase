def find_runner_up_score(scores):
    
    unique_scores = sorted(set(scores), reverse=True)
    
    
    if len(unique_scores) > 1:
        return unique_scores[1]  
    else:
        return None  


if __name__ == "__main__":
    scores = [2, 3, 6, 6, 5]  
    runner_up_score = find_runner_up_score(scores)
    
    if runner_up_score is not None:
        print(f"The runner-up score is: {runner_up_score}")
    else:
        print("There's no runner-up score.")
