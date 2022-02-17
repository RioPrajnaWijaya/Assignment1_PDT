function square() {
    var numberClient = document.getElementById("number").value;

    var url = "/squareRoot";

    axios({
        method: "post",
        url: url,
        data: {
            number: numberClient,
        },
        headers: {
            "Content-Type": "application/json",
        }
    }).then(
        (response) => {
            var result = response.data;
            console.log(response);
            document.getElementById("result").innerHTML = result["result"];
        },
        (error) => {
            console.log(error);
        }
    );
}

function convert() {
    var numberClient = document.getElementById("number").value;

    var url = "/convertLetter";

    axios({
        method: "post",
        url: url,
        data: {
            number: numberClient,
        },
        headers: {
            "Content-Type": "application/json",
        }
    }).then(
        (response) => {
            var result = response.data;
            console.log(response);
            document.getElementById("result").innerHTML = result["result"];
        },
        (error) => {
            console.log(error);
        }
    );
}

function hypotenuse() {
    var numberClient1 = document.getElementById("number1").value;
    var numberClient2 = document.getElementById("number2").value;

    var url = "/calculateHypotenuse";

    axios({
        method: "post",
        url: url,
        data: {
            number1: numberClient1,
            number2: numberClient2,
        },
        headers: {
            "Content-Type": "application/json",
        }
    }).then(
        (response) => {
            var result = response.data;
            console.log(response);
            document.getElementById("result").innerHTML = result["result"];
        },
        (error) => {
            console.log(error);
        }
    );
}
