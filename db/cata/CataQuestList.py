from db.QuestList import QuestList

import os.path
import pickle

from db.cata.readMangosQuestList import read_mangos_quest_list
from db.cata.readTrinityQuestList import read_trinity_quest_list


class CataQuestList(QuestList):

    def __init__(self, version):
        super().__init__(version)

    def run(self, cursor, dictCursor, db_flavor, recache=False):
        if not os.path.isfile(f'data/cata/quests.pkl') or recache:
            dicts = load_quests(cursor, dictCursor, db_flavor)
            print('Caching quests...')
            self.cacheQuests(dicts)
        else:
            try:
                with open(f'data/cata/quests.pkl', 'rb') as f:
                    self.qList = pickle.load(f)
                print('Using cached quests.')
            except:
                print('ERROR: Something went wrong while loading cached quests. Re-caching.')
                dicts = load_quests(cursor, dictCursor, db_flavor)
                self.cacheQuests(dicts)

def load_quests(cursor, dictCursor, db_flavor):
    if db_flavor == 'trinity':
        return read_trinity_quest_list(cursor, dictCursor)
    else:
        return read_mangos_quest_list(cursor, dictCursor)
