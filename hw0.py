import numpy as np
import matplotlib.pyplot as plt


def simulate_prizedoor(nsim, ndoor):
    return np.random.randint(0, ndoor, (nsim))


def simulate_guess(nsim):
    return np.zeros(nsim, dtype=np.int)


def goat_door(nsim, prizedoors, guesses, ndoor):
    result = []
    for i in range(nsim):
        if prizedoors[i] == guesses[i]:
            result.append(np.random.choice([x for x in range(ndoor) if x != prizedoors[i]], ndoor - 2, replace=False))
        else:
            result.append(np.random.choice([x for x in range(ndoor) if x !=prizedoors[i] and x != guesses[i]], ndoor - 2, replace=False))
    return result


def switch_guess(nsim, ndoor, guesses, goatdoors):
    result = []
    for t in range(nsim):
        result.append(*list(set(range(ndoor)) - set([guesses[t]]) - set(goatdoors[t])))
    return np.array(result)


def win_percentage(guesses, prizedoors):
    return 100 * (guesses == prizedoors).mean()


nsim = 5000
door_min = 3
door_max = 50
wr_l = []
wr_s_l = []
for ndoor in range(door_min, door_max + 1):
    prize = simulate_prizedoor(nsim, ndoor)
    guess = simulate_guess(nsim)
    goats = goat_door(nsim, prize, guess, ndoor)
    guess2 = switch_guess(nsim, ndoor, guess, goats)
    wr_l.append(win_percentage(prize, simulate_guess(nsim)))
    wr_s_l.append(win_percentage(prize, guess2).mean())

plt.plot(range(door_min, door_max + 1), wr_l, label='Win rate with origin choice')
plt.plot(range(door_min, door_max + 1), wr_s_l, label='Win rate with switched choice')
plt.title('N-door winning rate')
plt.xlabel('ndoor')
plt.legend(loc='mid right')
plt.ylabel('Wining rate')
plt.show()


