class Speaker(object):

    def __init__(self, name):
        self.__name = name

    def say(self, something):
        """
        say something as a Speaker named with name
        """
        print('{} says: {}'.format(self.__name, something))

if __name__ == '__main__':
    rachel = Speaker(name='Rachel')
    rachel.say('hello')
    rachel.say('coucou')