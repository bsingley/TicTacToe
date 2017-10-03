import requests
import datetime

PP_API_BASE_URL = 'https://pp.engineering.redhat.com/pp/api/latest'

def _get_json(url):
    response = requests.get(url,
                            headers=dict(Accept='application/json'),
                            verify=False)
#    except urllib3.exceptions.SSLError as e:
#        print e
    return response.json()


class Release(object):
    """defining what are we gonna get from releases jsons"""
    def __init__(self, rel):
        """list of parameters getting from json"""
        self.bu = rel['bu_name']
        self.name = rel['name']
        self.rel_id = rel['id']
        self.date = rel['ga_date']
        self._peeps = None
        self._nname = None
        self._docs = None
        self._docsurl = None


def get_releases():
    today = datetime.datetime.today().date()
    all_rels = _get_json(
            '%s/releases/?active&ga_date__gte=%s' %(PP_API_BASE_URL, today))

    releases = []
    for rel in all_rels:
        # filter out "internal" releases
        if rel['bu_name'] in ('PnT Operations','Certifications'):
            continue

        # filter out Fedora releases
        if 'Fedora' in rel['name']:
            continue

        # Add this release to our list
        releases.append( Release(rel) )

        # see if there are any Beta's for this release
        betas =_get_json( '%s/releases/%s/schedule-tasks/?name=Public%%20Beta'\
                %(PP_API_BASE_URL, rel['id']))
        for beta in betas:
            releases.append( Release(rel,beta) )

        print releases

def main():
    get_releases()


if __name__== "__main__":
    main()
