let add = document.getElementById('AddItem');
let inputField = document.getElementById('NewItem');
let listContainer = document.getElementById('container');
let clear = document.getElementById('clear');
add.addEventListener('click', (e) => {
    e.preventDefault();

    const task = inputField.value;

    if (!task) {
        alert("alarm")
    } else {
        console.log("Success")
    }

    const task_el = document.createElement("div");
    task_el.classList.add("item");

    const task_checkbox_el = document.createElement("input");
    task_checkbox_el.type = "checkbox"
    task_checkbox_el.classList.add("checkbox")

    const task_content_el = document.createElement("label");
    task_content_el.innerText = task;

    task_el.appendChild(task_checkbox_el)
    task_el.appendChild(task_content_el);
    listContainer.appendChild(task_el);
})


clear.addEventListener('click', () =>{
    let child = listContainer.lastElementChild;
    while (child){
        listContainer.removeChild(child);
        child = listContainer.lastElementChild;
    }
})

