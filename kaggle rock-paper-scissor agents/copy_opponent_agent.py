# agent that copies whatever the opponent did last
def copy_opponent(obs, config):
    if obs.step > 0:
        return obs.lastOpponentAction
    else:
        random.randint(0,2)
       
    