import { Notifications } from 'expo';
import * as Permissions from 'expo-permissions';
import React, { Component } from 'react';
import {Text} from 'react-native';
import CryptoJS from "react-native-crypto-js";
import key from "./key/key.json";

//http://168.131.153.40:8000/api/pushtoken/
function encrypt_su(data){
  let ciphertext = CryptoJS.AES.encrypt(data,key["key"]).toString();
  console.log('[DEBUG] ciphertext : ',ciphertext);

  //DEBUG : decrypt
  let bytes  = CryptoJS.AES.decrypt(ciphertext, key["key"]);
  let originalText = bytes.toString(CryptoJS.enc.Utf8);
  console.log('[DEBUG] originalText : ',originalText);

  return ciphertext;
}


async function registerForPushNotificationsAsync() {

  const { status: existingStatus } = await Permissions.getAsync(
    Permissions.NOTIFICATIONS
  );
  let finalStatus = existingStatus;

  // only ask if permissions have not already been determined, because
  // iOS won't necessarily prompt the user a second time.
  if (existingStatus !== 'granted') {
    // Android remote notification permissions are granted during the app
    // install, so this will only ask on iOS
    const { status } = await Permissions.askAsync(Permissions.NOTIFICATIONS);
    finalStatus = status;
  }

  // Stop here if the user did not grant permissions
  if (finalStatus !== 'granted') {
    return;
  }

  // Get the token that uniquely identifies this device
  let token = await Notifications.getExpoPushTokenAsync();
  let v = encrypt_su(token);
  console.log('Encrypt >>>>>>',v);

  // POST the token to your backend server from where you can retrieve it to send push notifications.
  return v;
}

export {encrypt_su, registerForPushNotificationsAsync };
