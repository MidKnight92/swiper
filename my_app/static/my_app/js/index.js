console.log('Running');

document.addEventListener('DOMContentLoaded', () => {
    
    // Listen for when the icon is clicked
    document.querySelectorAll('i').forEach(i => {
        i.onclick = () => {         
            addOrRemoveItem(i);
        }
    })
})

const addOrRemoveItem = async (icon) => {
    url = window.location.href;
    
    // Get item and price values 
    const item = icon.dataset.item_name;
    const price =  icon.dataset.item_price;

    // Item has not been added, item is to be added
    if (icon.dataset.action == 'add'){
        // Change action and sign 
        icon.dataset.action = 'remove';
        icon.innerHTML = 'check';


        try {
           const data = await fetch(url, {
                method: 'POST',
                body: JSON.stringify({
                    "item": item,
                    "price": price,
                    "action": 'add'
                })
            })
            console.log(data.json());
        } catch (error) {
            console.log(error);
        }

        

    // Item has been added, item is to be removed 
    } else {
        // Change action and sign
        icon.dataset.action = 'add';
        icon.innerHTML = 'add';

        try {
            const data = await fetch(url, {
                method: 'PUT',
                body: JSON.stringify({
                    "item": item,
                    "price": price,
                    "action": 'remove'
                })
            })
            console.log(data.json());
        } catch (error) {
            console.log(error);
        }
    }
}

async function sendRequest(url, method="GET", payload=null){
    const options = { method };
    if (payload){
        options.headers = {"Content-Type": "application/json"};
        options.body = JSON.stringify(payload);
        const data = fetch(url, options)
    }
}