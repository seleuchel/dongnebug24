import React, { Component } from 'react';
import { Platform, Text, View, Button, StyleSheet,WebView, BackHandler, Alert, TouchableOpacity } from 'react-native';
import Constants from 'expo-constants';
import * as Location from 'expo-location';
import * as Permissions from 'expo-permissions';
import MapView, {Marker} from 'react-native-maps';
import SlidingUpPanel from 'rn-sliding-up-panel';
import { BackgroundFetch } from 'expo';
import * as TaskManager from 'expo-task-manager';

const LOCATION_TASK_NAME = 'background-location-task';

export default class App extends Component<Props>{
  onPress = async () => {
    await Location.startLocationUpdatesAsync(LOCATION_TASK_NAME, {
      accuracy: Location.Accuracy.Balanced,
    });
  };

  render() {
    return (
      <TouchableOpacity onPress={this.onPress}>
        <Text>Enable background location</Text>
      </TouchableOpacity>
    );
  }
}

TaskManager.defineTask(LOCATION_TASK_NAME, ({ data, error }) => {
  if (error) {
    // Error occurred - check `error.message` for more details.
    return;
  }
  if (data) {
    const { locations } = data;
    console.log(locations);
    // do something with the locations captured in the background
  }
});
