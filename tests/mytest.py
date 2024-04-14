from matchmatrix import (
    MatchManager
    , standardise_company_name
    , strip_company_name
    , strip_domain_suffix
    )

standardise_company_name("my company l.t.d.")
strip_company_name("my company limited")
strip_domain_suffix("mydomain.uk.com")

MyMatch = MatchManager()
MyMatch.strip_company_name("my company limited")