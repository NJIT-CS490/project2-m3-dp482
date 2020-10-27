import * as React from 'react';
import { Socket } from './Socket';
import ReactDOM from 'react-dom';
import GoogleLogin from 'react-google-login';
import { Content } from './Content';


function handleSubmit(response) {
  console.log(response)
  let username = response.profileObj.name;
  Socket.emit('new username', {
    'address': username,
  });
    
    console.log('Sent the name ' + username + ' to server!');
    ReactDOM.render(<Content />, document.getElementById('content'));
}

export function GoogleButton() {
  return <GoogleLogin
    clientId="791154624378-g41rhk0tetto6ueot7mcjffts9g294e7.apps.googleusercontent.com"
    buttonText="Login"
    onSuccess={handleSubmit}
    onFailure={handleSubmit}
    fields="name"
    cookiePolicy={'single_host_origin'}/>;
}