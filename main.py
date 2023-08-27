class Inspector:
    def __init__(self):
        self.arstotzka_documents = []
        self.foreigners_documents = []
        self.vaccination = []
        self.workers_documents = []
        self.criminal = []
        self.whitelist = []

    def receive_bulletin(self, day_bulletin):
        day_bulletin = day_bulletin.split('\n')
        for i in day_bulletin:
            if 'Allow citizens of' in i:
                self.whitelist.extend(i[18:].split(', '))
            elif 'Deny citizens of' in i:
                temp = i[17:].split(', ')
                for j in temp:
                    while j in self.whitelist:
                        self.whitelist.remove(j)
            elif 'Wanted by the State:' in i:
                self.criminal.extend(i[21:].split(', '))
            elif 'Foreigners require' in i:
                self.foreigners_documents.extend(i[19:].split(', '))
            elif 'Citizens of Arstotzka require' in i:
                self.arstotzka_documents.extend(i[30:].split(', '))

            elif 'Workers require':
                self.workers_documents.extend(i[17:].split(', '))

    
