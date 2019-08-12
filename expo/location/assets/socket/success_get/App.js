import React, { Component } from 'react';
import { Platform, Text, View, StyleSheet,WebView } from 'react-native';
import Constants from 'expo-constants';
import * as Location from 'expo-location';
import * as Permissions from 'expo-permissions';
import MapView from 'react-native-maps'
import HttpExample from './http_example.js'

export default class App extends Component<Props>{
  render(){
    return (
     <HttpExample />
  );
  }
}
