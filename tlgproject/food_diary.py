#!/usr/bin/env python3

"""TLG Project | Shalese Childress
        Food Diary"""
        
def introduction(Greeting): 
   content = TextField()
   timestamp = DateTimeField(default=datetime.datetime.now)

def initialize(passphrase):
   db.init('diary.db', passphrase=passphrase, kdf_iter=64000)
   Entry.create_table()

def menu_loop():
  choice = None
  while choice != 'q':
     for key, value in menu.items():
         print('%s) %s' % (key, value.__doc__))
        choice = raw_input('Action: ').lower().strip()
     if choice in menu:
         menu[choice]()

def add_entry():
    """Add entry"""

def view_entries(search_query=None):
    """View previous entries"""

def search_entries():
    """Search entries"""

menu = OrderedDict([
    ('a', add_entry),
    ('v', view_entries),
    ('s', search_entries),
])

if __name__ == '__main__':

def add_entry():
    """Add entry"""
    print('Enter your entry. Press ctrl+d when finished.')
    data = sys.stdin.read().strip()
    if data and raw_input('Save entry? [Yn] ') != 'n':
        Entry.create(content=data)
        print('Saved successfully.')

def view_entries(search_query=None):
    """View previous entries"""
    query = Entry.select().order_by(Entry.timestamp.desc())
    if search_query:
        query = query.where(Entry.content.contains(search_query))

    for entry in query:
        timestamp = entry.timestamp.strftime('%A %B %d, %Y %I:%M%p')
        print(timestamp)
        print('=' * len(timestamp))
        print(entry.content)
        print('n) next entry')
        print('q) return to main menu')
        if raw_input('Choice? (Nq) ') == 'q':
            break
