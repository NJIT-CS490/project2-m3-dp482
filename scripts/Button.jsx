import * as React from 'react';
import { Socket } from './Socket';

function handleSubmit(event) {
    let newMessage = document.getElementById("message_input");
    Socket.emit('new address input', {
       'address': newMessage.value,
    });
    newMessage.value
    
    console.log('Sending the address ' + newMessage.value + ' to server!');
    newMessage.value = ''
    
    event.preventDefault();
}

export function Button() {
    return (
        <form onSubmit={handleSubmit}>
            <input id="message_input" placeholder="Enter a message"></input>
            <button> Send! </button>
        </form>
    );
}
