import React, { Component } from 'react';
import { Platform, Text, View, StyleSheet,WebView } from 'react-native';
import Constants from 'expo-constants';
import * as Location from 'expo-location';
import * as Permissions from 'expo-permissions';
import MapView, {Marker} from 'react-native-maps';
import SwipeUpDown from 'react-native-swipe-up-down';

export default class App extends Component<Props>{
  state = {
    location: null,
    errorMessage: null,
    is_location_on : null,
    slideViewVisible : false
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
//    this.setState({region});
  };


  render() {
    let text = 'Waiting..';
    let is_loc = "is location oK?";
    let street = "";

    var box  = "";
    let lat = "";
    let lon = "";

    if (this.state.errorMessage) {
      text = this.state.errorMessage;
      is_loc = "no, sir..";
    } else if (this.state.location) {
      //json을 문자열로 변환한다.


      text = JSON.stringify(this.state.location);
      is_loc = String(this.state.is_location_on);
      street = JSON.stringify(this.state.way);


      box = this.state.location.coords;
      lat = parseFloat(box.latitude);
      lon = parseFloat(box.longitude);

    }

    return (
      <View style={styles.container}>




      <WebView style={styles.web}
          source = {{ uri : 'https://naver.com'}}
        />
<SwipeUpDown
	itemMini={<Text>hello</Text>} // Pass props component when collapsed
	itemFull={
    <View>
        <MapView
          style={styles.map}
          initialRegion ={{
              latitude: lat,
              longitude: lon,
              latitudeDelta : 0.0009,
              longitudeDelta : 0.0009,
          }}>

        <Marker title="box" pinColor = "pink"
        coordinate = {{
          latitude: Number(lat),
          longitude: Number(lon)
        }}/>
        </MapView>
      </View>
    } // Pass props component when show full
	onShowMini={() => console.log('mini')}
	onShowFull={() => console.log('full')}
	onMoveDown={() => console.log('down')}
	onMoveUp={() => console.log('up')}
	disablePressToShow={false} // Press item mini to show full
	style={{ backgroundColor: 'pink' }} // style for swipe
  animation = "easeInEaseOut"
  swipeHeight={50}
/>

      </View>

    );
  }
}

//필수 Number



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
    height: "100%",
    top : 0,
    backgroundColor : "pink"
  },
  map:{
    height: "100%",
    left: 0,
    right: 0,
    bottom: 0,
  },
});
