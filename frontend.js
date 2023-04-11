function start_new_form() {
    const uri = "http://localhost:8080/form";
    const config = "";            // new tab
    const win = window.open(uri, "", config);
}

function view_form_input() {
    const uri = "http://localhost:8080/view/input";
    const config = "";
    const win = window.open(uri, "", config);
}

function view_profile() {
    const uri = "http://localhost:8080/view/profile";
    const config = "";
    const win = window.open(uri, "", config);
}

function main_page() {
    const uri = "http://localhost:8080";
    const config = "";
    const win = window.open(uri, "", config);
}

function get_input_data() {
    let xmlhttp = new XMLHttpRequest();
    xmlhttp.onload = function () {
        let data = JSON.parse(xmlhttp.responseText)

        for (const key in data) {
            document.getElementById('data').innerHTML +=
                `<b> ${key}:</b> ${data[key]}\n\r`
        }

    }
    xmlhttp.open("GET", "../user_data/user_data.json", true);
    xmlhttp.send();
}


function get_profile_data() {
    let xmlhttp = new XMLHttpRequest();
    xmlhttp.onload = function () {
        let data = JSON.parse(xmlhttp.responseText)
        let animals = ["Dog", "Cat", "Duck"]
        for (const key in data) {
            if (animals.includes(key)) {
                document.getElementById('Pet').innerHTML = `<h2>Pets:</h2>`

                get_image(key, data[key])
            } else if (key === 'Movies') {
                format_movie(data[key])

            } else {
                document.getElementById('data').innerHTML += `<b>${key}:</b> ${data[key]}\n\r`
            }
        }

    }


    xmlhttp.open("GET", "../user_data/analysed_data.json", true);
    xmlhttp.send();
}


function get_image(key, value) {

    const canv = document.getElementById(key);
    const ctx = canv.getContext("2d");
    const image = new Image();
    console.log(value)
    image.src = "../" + value

    image.addEventListener("load", () => {
        let scaleFactor = 400 / Math.max(image.width, image.height);
        let newWidth = image.width * scaleFactor;
        let newHeight = image.height * scaleFactor;
        canv.width = newWidth
        canv.height = newHeight
        ctx.drawImage(image, 0, 0, image.width, image.height, 0, 0, newWidth, newHeight);

    });
}

function format_movie(movies) {

    for (let i = 0; i < movies.length; i++) {
        console.log(typeof `Movie ${i + 1}`)
        document.getElementById(`Movie ${i + 1}`).innerHTML =
            `<b>Title: </b> ${movies[i][0]} \n\r` +
            `<b>Director: </b> ${movies[i][1]} \n\r` +
            `<b>Date Released: </b> ${movies[i][2]} \n\r` +
            `<b>Genre: </b> ${movies[i][3]} \n\r` + `\n\r`
    }


}