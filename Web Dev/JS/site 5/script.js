
function myFunction() {

    const nodeMap = document.getElementById("content").attributes;
    const nodeMap2 = document.getElementById("content2").attributes;
    let name = nodeMap[0].value;
    let name2 = nodeMap2[0].value;
    console.log (name);
    console.log (name2)
    nodeMap[0].value = name2;
    nodeMap2[0].value = name;
    document.getElementById("content").innerHTML = nodeMap[0].value;
    document.getElementById("content2").innerHTML = nodeMap2[0].value;
}

function ChangeText() {
    document.getElementsByClassName("everything")[0].innerHTML = "I Changed";
    document.getElementsByClassName("everything")[0].style.color = "purple";
    document.getElementsByClassName("everything")[1].innerHTML = "Everything!";
    document.getElementsByClassName("everything")[1].style.color = "green";
}