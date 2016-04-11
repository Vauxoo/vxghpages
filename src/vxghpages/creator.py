'''
Create gh-pages for an existent repository.

https://help.github.com/articles/creating-project-pages-manually/

And then precofigure if a doc folder exists the autodeployment.
'''

from subprocess import call
from os.path import isdir
from os.path import join


class Creator(object):
    def __init__(self):
        pass
        
    def checks(self):
        assert isdir(join('.', 'docs')), '''
        You need to have an sphinx docs folder properly configured on docs 
        folder to help you to prepare this see sphinx-quickstart --help and 
        install sphinx to help you.'''

    def git_create_orphan(self):
        call(['git', 'checkout', '--orphan', 'gh-pages'])

    def git_clean_orphan(self):
        call(['git', 'rm', '-rf', '.'])

    def git_first_commit(self):
        with open('index.html', 'w') as ind:
            ind.write("My Page")
        call(['git', 'add', 'index.html'])
        call(['git', 'commit', '-a', '-m', '"First pages commit"'])
        call(['git', 'push', 'origin', 'gh-pages'])
        call(['git', 'checkout', '@{-1}'])

    def first_commit(self):
        pass
    
    def run(self):
        self.git_create_orphan()
        self.git_clean_orphan()
        self.git_first_commit()
