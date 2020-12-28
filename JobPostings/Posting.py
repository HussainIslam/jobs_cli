from abc import ABC, abstractproperty

class Posting(ABC):
    
    @abstractproperty
    def company_name(self):
        pass

    @abstractproperty
    def position(self):
        pass

    @abstractproperty
    def posting_number(self):
        pass

    @abstractproperty
    def contact_email(self):
        pass

    @abstractproperty
    def contact_phone(self):
        pass

    @abstractproperty
    def city(self):
        pass

    @abstractproperty
    def province(self):
        pass

    @abstractproperty
    def posting_site(self):
        pass

    @abstractproperty
    def job_url(self):
        pass

    @abstractproperty
    def posting_date(self):
        pass

    

