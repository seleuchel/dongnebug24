import React, { Component } from 'react';
import { Platform, Text, View, StyleSheet,WebView } from 'react-native';
import ReactDOM from 'react-dom'
import Constants from 'expo-constants';
import * as Location from 'expo-location';
import * as Permissions from 'expo-permissions';
import MapView from 'react-native-maps'
import { RequestHttp, SendData } from './RequestHttp.js'  //함수 모듈화(여러군데서 쓸지도 모르니깐..)

export default class App extends Component<Props>{
  constructor(props){
    super(props)
  this.state = {
    location: null,
    errorMessage: null,
    is_location_on : null,
    itRoaded: false,
    data: 'test',
  };
}

  componentDidMount(){
    setInterval(function(){SendData(this.state.location)}, 1000)
    this.setState({data : RequestHttp()}) //처음 마운트 했을때 리퀘스트 보냄
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


    if (this.state.errorMessage) {
      text = this.state.errorMessage;
      is_loc = "no, sir..";
    } else if (this.state.location) {
      text = JSON.stringify(this.state.location);
      is_loc = String(this.state.is_location_on);
      street = JSON.stringify(this.state.way);
    }
    if(this.state.data._55!=undefined)
      console.log(this.state.data._55.description) //리스폰스가 오기전까지 언디파인드임 언디파인드이면 오류발생하니까 언디파인드인지 먼저 확인
    return (
      <View style={styles.container}>
      <WebView style={styles.web}
        source = {{ uri : 'https://naver.com'}}
      />
      <Text></Text>

      <MapView
        style={styles.map}
        initialRegion={{
          latitude:35,
          longitude:127,
          latitudeDelta: 0.0,
          longitudeDelta:0.0201,
        }}/>
      </View>
    );
  }
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    top: 60,
    backgroundColor: 'blue',
  },
  paragraph: {
    margin: 24,
    fontSize: 18,
    textAlign: 'center',
  },
  web:{
    height: "50%",
    top : 0
  },
  map:{
    height: "50%",
    left: 0,
    right: 0,
    bottom: 0,
  },
});
