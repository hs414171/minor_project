import whois 
def whois_target(host):
    w = whois.whois(host)

    return w
sit = "jiit.ac.in"
print(whois_target(sit))
