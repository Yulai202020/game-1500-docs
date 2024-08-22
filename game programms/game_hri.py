import configparser
import sys

config = configparser.ConfigParser()
config.read('game.ini')
# get
money = int( config['hri']['money'] )
budget = int( config['hri']['budget'] )

def set_year():
    config.set('hri','money',str( money + budget + 600000000 ))
    config.set('hri','budget',str( 100000000 - 94450000  ))

def decrease_budget(dmoney):
    dmoney = int(dmoney)

    config.set('hri','money',str(money))
    config.set('hri','budget',str(budget - dmoney))

def increase_budget(imoney):
    imoney = int(imoney)

    config.set('hri','money',str(money))
    config.set('hri','budget',str(budget + imoney))

def final():
    with open('game.ini','w') as confpath:
        config.write(confpath)

if __name__ == "__main__":
    if sys.argv[1] == 'dm':
        decrease_budget( sys.argv[2] )
   
    elif sys.argv[1] == 'im':
        increase_budget( sys.argv[2] )
   
    elif sys.argv[1] == 'sy':
        set_year()
   
    elif sys.argv[1] == 'show':
        print( f"Money : {money}" )
        print( f"Budget : {budget}" )
   
    final()