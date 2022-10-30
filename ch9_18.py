players = {'Stephen Curry':'Golden State Warriors',
           'Kevin Durant':'Golden State Warriors',
           'Leborn James':'Cleveland Cavaliers',
           'James Harden':'Houston SRockets',
           'Paul Gasol':'San antonio Spurs'
          }
for name in sorted(players.keys(),reverse=True):
    print(name)
    print("Hi! %s 我喜歡看你在 %s 的表現" % (name, players[name]))