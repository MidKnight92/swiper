console.log('Running');

document.addEventListener('DOMContentLoaded', () => {
    
    // Listen for when the icon is clicked
    document.querySelectorAll('i').forEach(i => {
        i.onclick = () => {         
            addOrRemoveItem(i);
        }
    })
})

const addOrRemoveItem = (icon) => {
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
            fetch(url, {
                method: 'Post',
                body: JSON.stringify({
                    "item": item,
                    "price": price,
                    "action": 'add'
                })
            }).then( response => {
                console.log(response);
            })
        } catch (error) {
            console.log(error);
        }

        

    // Item has been added, item is to be removed 
    } else {
        // Change action and sign
        icon.dataset.action = 'add';
        icon.innerHTML = 'add';

        try {
            fetch(url, {
                method: 'Put',
                body: JSON.stringify({
                    "item": item,
                    "price": price,
                    "action": 'remove'
                })
            }).then( response => {
                console.log(response);
            })
        } catch (error) {
            console.log(error);
        }
    }
}

