import configparser

config = configparser.ConfigParser()
config.read('example.ini')
print('Sections:', config.sections())
print('\n-- ALL DATA --')
for section in config.sections():
    print('[' + str(section) + ']')
    for key in config[section]:
        print('\t' + str(key) + ': ' + str(config[section][key]))
    print('\n')
