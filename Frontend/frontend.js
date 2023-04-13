/*
* Lydia Price, 20004521
* The below functions provide client side usability
*/
function start_new_form() {
    // Opens new psych form in a new tab
    let current_port = window.location.port; // Added to work in a docker container
    const uri = `http://localhost:${current_port}/form`;
    const config = "";
    const win = window.open(uri, "", config);
}

function view_form_input() {
    // Opens view/input in a new tab
    let current_port = window.location.port;// Added to work in a docker container
    const uri = `http://localhost:${current_port}/input`;
    const config = "";
    const win = window.open(uri, "", config);
}

function view_profile() {
    //Open view/profile in new tab
    let current_port = window.location.port;// Added to work in a docker container
    const uri = `http://localhost:${current_port}/view/profile`;
    const config = "";
    const win = window.open(uri, "", config);
}

function main_page() {
    //Return to the main page after analysis
    let current_port = window.location.port; // Added to work in a docker container
    const uri = `http://localhost:${current_port}`;
    const config = "";
    const win = window.open(uri, "", config);
}

function get_input_data() {
    // Get the input data, parse the JSON data, and format the data
    let xmlhttp = new XMLHttpRequest();
    xmlhttp.onload = function () {
        let data = JSON.parse(xmlhttp.responseText)
        let count = 0
        for (const key in data) {
            if (key.startsWith('question')) {
                if (count < 10) {
                    document.getElementById('question_data_1').innerHTML +=
                        `<b> ${key}:</b> ${data[key]}\n\r`
                } else {
                    document.getElementById('question_data_2').innerHTML +=
                        `<b> ${key}:</b> ${data[key]}\n\r`
                }
                count++
            } else if (key.startsWith('pet')) {
                document.getElementById('pet_data').innerHTML +=
                    `${data[key]}\n\r`
            } else {
                document.getElementById('personal_data').innerHTML +=
                    `<b> ${key}:</b> ${data[key]}\n\r`
            }
        }

    }
    xmlhttp.open("GET", "../user_data/user_data.json", true);
    xmlhttp.send();
}


function get_profile_data() {
    // Get the profile data, parse the JSON data, and format the data
    let xmlhttp = new XMLHttpRequest();
    xmlhttp.onload = function () {
        let data = JSON.parse(xmlhttp.responseText)
        let animals = ["Dog", "Cat", "Duck"]
        for (const key in data) { // If the user has selected a pet, then get relevant image
            if (animals.includes(key)) {
                document.getElementById('Pet').innerHTML = `<h2>Pets:</h2>`
                get_image(key, data[key])
            } else if (key === 'Movies') { //For the Movie recommendations, we want to format this separately
                format_movie(data[key])
            } else {
                document.getElementById('profile_details').innerHTML += `<b>${key}:</b> ${data[key]}\n\r`
            }
        }

    }
    xmlhttp.open("GET", "../user_data/analysed_data.json", true);
    xmlhttp.send();
}


function get_image(key, value) {
    // Get the image and draw to a canvas
    const canv = document.getElementById(key);
    const ctx = canv.getContext("2d");
    const image = new Image();
    console.log(value)
    image.src = "../" + value

    image.addEventListener("load", () => {
        // Scale the image to fit within a 400x400 space
        let scaleFactor = 400 / Math.max(image.width, image.height);
        let newWidth = image.width * scaleFactor;
        let newHeight = image.height * scaleFactor;
        canv.width = newWidth
        canv.height = newHeight
        ctx.drawImage(image, 0, 0, image.width, image.height, 0, 0, newWidth, newHeight);
    });
}

function format_movie(movies) {
    // Format each of the movie recommendations
    for (let i = 0; i < movies.length; i++) {
        document.getElementById(`Movie_${i + 1}`).innerHTML =
            `<b>Title: </b> ${movies[i][0]} \n\r` +
            `<b>Director: </b> ${movies[i][1]} \n\r` +
            `<b>Date Released: </b> ${movies[i][2]} \n\r` +
            `<b>Genre: </b> ${movies[i][3]} \n\r` + `\n\r`
    }
}