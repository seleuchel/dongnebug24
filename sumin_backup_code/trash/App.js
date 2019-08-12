import React, { Component } from 'react';
import { Platform, Text, View, StyleSheet,WebView } from 'react-native';
import Constants from 'expo-constants';
import * as Location from 'expo-location';
import * as Permissions from 'expo-permissions';
import MapView from 'react-native-maps'


class MyWeb extends Component{
  render(){
    return(
      <WebView
      source={{ uri: 'https://github.com/facebook/react-native' }}
      style={{ marginTop: 20 }}
    />
    );
  }
}
export default class App extends Component {
  state = {
    location: null,
    errorMessage: null,
    is_location_on : null,

  };
//is this android?
  componentWillMount() {
    if (Platform.OS === 'android' && !Constants.isDevice) {
      this.setState({
        errorMessage: 'Oops, this will not work on Sketch in an Android emulator. Try it on your device!',
      });
    } else {
      this._getLocationAsync();
    }
  }
  //is permissions ok?
  _getLocationAsync = async () => {
    let { status } = await Permissions.askAsync(Permissions.LOCATION);
    if (status !== 'granted') {
      this.setState({
        errorMessage: 'Permission to access location was denied',
      });
    }

    let location = await Location.getCurrentPositionAsync({});
    let is_location_on = await Location.hasServicesEnabledAsync({});
    let t_1 = await Location.getCurrentPositionAsync();
    let way = await Location.reverseGeocodeAsync(location.coords);


    this.setState({ location });
    this.setState({ is_location_on});
    this.setState({ way });
  };

  render() {
    let text = 'Waiting..';

    if (this.state.errorMessage) {
      text = this.state.errorMessage;
    } else if (this.state.location) {
      text = this.state.location.latitudeDelta;
    }

    return (
      <View style={styles.container}>

        <MapView
          style={styles.map}
          initialRegion={{
            latitude:35,
            longitude:127,
            latitudeDelta: 0.0,
            longitudeDelta:0.0201,
          }}/>
          <WebView
            source={{ uri: 'https://naver.com'}}
            style={styles.map}
          />

      </View>
    );
  }
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
    paddingTop: Constants.statusBarHeight,
    backgroundColor: '#ecf0f1',
  },
  paragraph: {
    height: 600,
    fontSize: 10,
    textAlign: 'center',
  },
  map:{
    flex: 45,
    position: 'absolute',
    top: 0,
    left: 0,
    right: 0,
    bottom: 0,
  },
});
