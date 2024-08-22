import configparser
import sys

config = configparser.ConfigParser()
config.read('game.ini')
# get
money = int( config['swit']['money'] )
budget = int( config['swit']['budget'] )
year = int( config['swit']['year'] )

def set_year():
    config.set('swit', 'money', str( money + budget + 172000000 ))
    config.set('swit', 'budget', str( 25000000 - 22025000 ))
    config.set('swit', 'year', str( year + 1 ))

def decrease_budget(dmoney):
    dmoney = int(dmoney)

    config.set('swit', 'money', str( money ))
    config.set('swit', 'budget', str( budget - dmoney ))

def increase_budget(imoney):
    imoney = int(imoney)

    config.set('swit', 'money', str( money ))
    config.set('swit', 'budget', str( budget + imoney ))

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