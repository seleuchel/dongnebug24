import React, { Component } from 'react';
import { Platform, Text, View, Button, StyleSheet,WebView, BackHandler, Alert, TouchableOpacity } from 'react-native';
import Constants from 'expo-constants';
import * as Location from 'expo-location';
import * as Permissions from 'expo-permissions';
import MapView, {Marker} from 'react-native-maps';
import SlidingUpPanel from 'rn-sliding-up-panel';
import * as TaskManager from 'expo-task-manager';
import { BackgroundFetch } from 'expo';


const LOCATION_TASK_NAME = 'background-my-location-get';

TaskManager.defineTask(LOCATION_TASK_NAME, ({ data, error }) => {
  if (error) {
    return;
  }
  if (data) {
    console.log('hello~');
  }
});

//location get coords data

export default class App extends Component<Props>{


  constructor(props){
    super(props);
  }

  render() {
return(
  <View>
  </View>
    );
  }
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: 'white',
  },
  paragraph: {

    fontSize: 18,
    textAlign: 'center',
  },
  web:{
    height: "50%",
    top : 0,
    backgroundColor : "white"
  },
  map:{
    height: "80%",
    left: 0,
    right: 0,
    bottom: 0,
  },
});
