from ..requests.trust import AddressRequest

class AddressFactory:
    def make(self):
        address = AddressRequest()
        address.street1='1600 Pennsylvania Avenue NW'
        address.street2= ''
        address.postal_code='20500'
        address.city='Washington'
        address.state='DC'
        address.country='US'
       return address