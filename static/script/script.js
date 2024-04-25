function handle() {
    alert('Registration completed')
    let inputs = document.querySelectorAll("input");
    let input_values = [];
    for (let i = 0; i < inputs.length; i++) {
        input_values.push(inputs[i].value);
    }
    console.log(input_values);
};


let btn = document.querySelector('.sub');
btn.addEventListener('click', handle);
