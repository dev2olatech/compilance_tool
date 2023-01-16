// var ip = document.getElementById("photo_file");
// ip.addEventListener("change", pri)
// function pri() {
//     var path = URL.createObjectURL(ip.files[0]);
//     console.log(path);
//     document.getElementById("photo").src = path;
// }

// For Image Preview
document.getElementById("photo_file").onchange = function() {
    var path = URL.createObjectURL(document.getElementById("photo_file").files[0]);
    console.log(path);
    document.getElementById("photo").src = path;
}

// For Select option value
var svalue;
let select = document.getElementById('sid')
select.addEventListener('change', function() {
    var idno = document.getElementById("idno");
    idno.value = "";
    svalue = select.value;
    if (svalue == "PAN") {
        document.getElementById("idno").placeholder = "Enter your PAN";
    } else if (svalue == "Adhar") {
        document.getElementById("idno").placeholder = "Enter your Adhar No";
    }

})

// For ID check
document.getElementById("idno").onkeyup = function() {
    regex1 = /^([A-Z]){5}([0-9]){4}([A-Z]){1}$/;
    regex2 = /^[2-9]{1}[0-9]{11}$/;

    var idno = document.getElementById("idno");
    var testTxt = idno.value;

    if (regex1.test(testTxt)) {
        idno.style.color = "green";
    } else if (regex2.test(testTxt)) {
        idno.style.color = "green";
    } else {
        idno.style.color = "red";
    }

}


//For Mobile no check
document.getElementById("mob").onkeyup = function() {
    regex1 = /^[6-9]{1}[0-9]{9}$/;

    var mob = document.getElementById("mob");
    var testTxt = mob.value;

    if (regex1.test(testTxt)) {
        mob.style.color = "green";
    } else {
        mob.style.color = "red";
    }

}


//For Add row in Qualification table
document.getElementById("btn_add1").onclick = function() {
    var row = document.getElementById("tbody").lastElementChild;
    var newrowrow = row.cloneNode(true);
    document.getElementById("tbody").appendChild(newrowrow);
}


//For delet row in Qualification table
function delfirst() {
    var tbl = document.getElementById("Qualification");

    if (tbl.rows.length > 2) {
        tbl.deleteRow(tbl.rows.length - 1);
    } else {
        window.alert("can't delete last row");
    }
}

//For delet row in Experience table
function delsecond() {
    var tbl = document.getElementById("Experience");

    if (tbl.rows.length > 2) {
        tbl.deleteRow(tbl.rows.length - 1);
    } else {
        window.alert("can't delete last row");
    }
}


//For Add row in Experience table
document.getElementById("btn_add2").onclick = function() {
    var row = document.getElementById("addr2");
    var newrowrow = row.cloneNode(true);
    document.getElementById("Experience").appendChild(newrowrow);
}