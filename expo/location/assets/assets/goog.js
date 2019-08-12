import React from 'react';
import {StyleSheet} from 'react-native';
import MapView from 'react-native-maps';

export default class App extends React.Component {
  render() {
    return (
      <MapView
        style={{flex: 1}}} />
    );
  }
}
