fetch = Entrez.efetch(db='pmc',
                     resetmode='xml',
                     id='15718680',
                     rettype='full')
article =  fetch.read()
