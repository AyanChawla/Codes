#!/bin/python3


# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):
    scores.append(0)
    rnk = sorted(set(scores), reverse = True)
    l = len(rnk)
    #print(alice,rnk)
    for i in alice:
        while (l > 0) and (i >= rnk[l-1]):
            l -= 1
        print(l+1)


                

            
                    






if __name__ == '__main__':


    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    climbingLeaderboard(scores, alice)


