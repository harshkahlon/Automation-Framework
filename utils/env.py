#CONSTANTS
import inspect

#ref1URL = "https://testwebportal.wellpartner.com/Security/Authentication/LoginForm"
#prodURL = "https://webportal.wellpartner.com"
#dev3 = "http://devwebportal.wellpartner.com:3/Security/Authentication/LoginForm"
#DrServer = "https://10.201.250.60/Security/Authentication/LoginForm"
#UAT2 Server = "https://10.200.250.22/Clarity/Dashboard"



baseURL = "https://testwebportal.wellpartner.com/Security/Authentication/LoginForm"


wrongUSERNAME = "entityauto"
wrongPASSWORD = "123456"


entityUSERNAME = "entityauto"
entityPASSWORD = "Aug@2020"

# entityUSERNAME = "hkahlon"
# entityPASSWORD = "Test@2021"

adminUSERNAME = "hkahlon"
adminPASSWORD = "Aug@2020"


def whoami():
    return inspect.stack()[1][3]



