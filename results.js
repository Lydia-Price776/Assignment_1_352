function get_results(path) {
            let xmlhttp = new XMLHttpRequest();
            xmlhttp.onload = function () {
                document.getElementById("data").innerHTML = xmlhttp.responseText;
            }
            xmlhttp.open("GET", path, true);
            xmlhttp.send();
        }