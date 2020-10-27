import * as React from 'react';
import { GoogleButton } from './GoogleButton';
import { Socket } from './Socket';

export function Content_Auth() {
    const [accounts, setAccounts] = React.useState([]);
    
    function getAllAccounts() {
        React.useEffect(() => {
            Socket.on('addresses received', (data) => {
                 let allAccounts = data['allAccounts'];
                 console.log("Received message from server: " + allAccounts);
                 setAccounts(allAccounts);
            })
        });
    }
    getAllAccounts();
    
    return (
        <div>
          <h1> Log in to Explore!</h1>
          <GoogleButton />
        </div>
    );
}