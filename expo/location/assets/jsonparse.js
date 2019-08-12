import React, { Component } from 'react';
import { Platform, Text, View, StyleSheet,WebView } from 'react-native';
import Constants from 'expo-constants';
import * as Location from 'expo-location';
import * as Permissions from 'expo-permissions';
import MapView from 'react-native-maps'

export default class App extends Component<Props>{
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
    let is_loc = "is location oK?";
    let street = "";

    let box  = "";

    if (this.state.errorMessage) {
      text = this.state.errorMessage;
      is_loc = "no, sir..";
    } else if (this.state.location) {
      //json을 문자열로 변환한다.


      text = JSON.stringify(this.state.location);
      is_loc = String(this.state.is_location_on);
      street = JSON.stringify(this.state.way);

      let k = this.state.location
      box = this.state.location

    }

    return (


      <View style={styles.container}>

        <Text style={styles.paragraph}>{text}</Text>
        <Text style={styles.paragraph}> {is_loc} </Text>
        <Text> {street} </Text>
{/*
      <WebView style={styles.web}
        source = {{ uri : 'https://naver.com'}}
      />
      <MapView
        style={styles.map}
        initialRegion={{
          latitude:35,
          longitude:127,
          latitudeDelta: 0.0,
          longitudeDelta:0.0201,
        }}/>

        <Text style={{fontSize:15}}>{is_loc}</Text>
*/}
      </View>

    );
  }
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    top: 20,
    backgroundColor: 'white',
  },
  paragraph: {
    margin: 24,
    fontSize: 18,
    textAlign: 'center',
  },
  web:{
    height: "50%",
    top : 0,
    backgroundColor : "pink"
  },
  map:{
    height: "50%",
    left: 0,
    right: 0,
    bottom: 0,
  },
});
