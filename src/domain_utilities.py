import dns
import dns.resolver
def get_dns_record_form_domain(domain_name):
    text_records=[]
    answers=dns.resolver.resolve(domain_name,dns.rdatatype.RdataType.TXT)
    for answer in answers:
        text_record=str(answer).strip("\"")
        text_records.append(text_record) 
    return text_records   

def search_for_text_record_in_domain(domain_name,text_record):
    text_records_of_domain=get_dns_record_form_domain(domain_name)
    if text_record in text_records_of_domain:
        return text_record
        