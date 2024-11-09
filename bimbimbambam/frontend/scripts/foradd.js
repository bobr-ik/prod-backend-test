// var debtors = Array();

function get_info(value) {
    switch (value) {
        case 1:
            const name = document.getElementById('name').value
            console.log(name);
            break;
        case 2:
            const general_summ = document.getElementById('summ').value
            console.log(general_summ);
            break;
        case 3:
            const name_who_pay = document.getElementById('input_person_who_pay').value
            console.log(name_who_pay);
            break;
        case 4:
            const person_name = document.getElementById('new_person_name').value
            console.log(person_name);
            document.getElementById('new_person_name').id = "new_person_name_done";
            break;
        case 5:
            const person_summ = document.getElementById('new_person_summ').value
            console.log(person_summ);
            document.getElementById('new_person_summ').id = "new_person_summ_done";
            break;
    }
}

function add_payment() {
    document.getElementById("button_who_pay").remove();

    const person_pay = document.createElement('input');
    person_pay.id = "input_person_who_pay";
    person_pay.classList.add("input_class");
    person_pay.setAttribute("value", "@");
    person_pay.onchange = () => get_info(3);
    document.getElementById("who_pay").appendChild(person_pay);

    const cansel_add = document.createElement('button');
    cansel_add.classList.add("cancel_button");
    cansel_add.id = "cancel_add";
    cansel_add.onclick = () => remove_changes("input_person_who_pay", "replace_button", "button_who_pay", "who_pay", "Добавить оплатившего", "add_payment()");
    document.getElementById("who_pay").appendChild(cansel_add);
}

function remove_changes(remove_id, return_elem, elem_id, parent_id, text, func) {
    document.getElementById(remove_id).remove();
    document.getElementById("cancel_add").remove();
    
    const was_elem = document.createElement("button");
    was_elem.classList.add(return_elem);
    was_elem.innerHTML = text;
    was_elem.id = elem_id;
    was_elem.setAttribute("onclick", func);
    document.getElementById(parent_id).appendChild(was_elem);
}

function add_person() {
    const person_block = document.createElement('div');
    person_block.classList.add("style_person_block");
    document.getElementById("add_person").appendChild(person_block);

    const person_name = document.createElement('input');
    person_name.classList.add("style_person_name");
    person_name.id = "new_person_name";
    person_name.onchange = () => get_info(4);
    person_name.setAttribute('value', '@');
    person_block.appendChild(person_name);

    const person_summ = document.createElement('input');
    person_summ.classList.add("style_person_summ");
    person_summ.id = "new_person_summ";
    person_summ.onchange = () => get_info(5);
    person_summ.setAttribute("placeholder", "Сумма");
    person_block.appendChild(person_summ);

    if (document.getElementById("send_list_button") == null) {
        const send_list = document.createElement('button');
        send_list.classList.add("send_button");
        send_list.innerHTML = "Отправить";
        send_list.id = "send_list_button";
        document.body.appendChild(send_list);
    }
}