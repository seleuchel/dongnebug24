import React, { Component } from 'react';
import { Platform, Text, View, Button, StyleSheet,WebView,BackHandler, Alert, TouchableOpacity } from 'react-native';
import Constants from 'expo-constants';
import * as Location from 'expo-location';
import * as Permissions from 'expo-permissions';
import MapView, {Marker} from 'react-native-maps';
import SlidingUpPanel from 'rn-sliding-up-panel';
import * as TaskManager from 'expo-task-manager';
import { CreateLocation, UpdateLocation, ReadLocation } from './RequestHttp';

const LOCATION_TASK_NAME = 'background-location-task';
var vi = null;

TaskManager.defineTask(LOCATION_TASK_NAME, ({ data, error }) => {
  if (error) {
    return;
  }
  if (data) {
    vi = data;
  }
});

class MarkerComponent extends Component<props>{
  constructor(props){
    super(props)
    this.state={
      location: 'test',
    };
  }

  componentDidMount(){
    this.setState(async function() {location : ReadLocation()})
  };


  render(){
    console.log(this.state.location)
    return(<View><Text>test</Text></View>);
  }
}

export default class App extends Component<Props>{
  constructor(props){
    super(props);
    this.handleBackButtonClick = this.handleBackButtonClick.bind(this);
    this.state = {
      errorMessage: null,
      region: null,
      //new
      latitude:null,
      longitude: null,
      timestamp: null,
      data: '',
    };
}

  componentDidMount(){
    //setInterval(function(){SendData()}, 1000)
    this.setState({data : ReadLocation()}) //처음 마운트 했을때 리퀘스트 보냄
  /*setInterval(async () => {
    await Location.startLocationUpdatesAsync(LOCATION_TASK_NAME,);
    //console.log('--------------------------- DEBUG : GET vi --------------------------- \n', vi);
    this.setState({location:vi.locations[0]});  //delete please
    this.setState({
      latitude : vi.locations[0].coords.latitude,
      longitude : vi.locations[0].coords.longitude,
      timestamp : vi.locations[0].timestamp,
    })

    //here - sendPacket 1

    console.log('\n--------------------------- DEBUG : get state : lant, lon, timestamp --------------------------- \n',
      'latitude : ', this.state.latitude,
      'longitude : ', this.state.longitude,
      'timestamp : ', this.state.timestamp);
  }, 5000)*/
  };
  componentWillUnmount() {
    BackHandler.removeEventListener('hardwareBackPress', this.handleBackButtonClick);
}

handleBackButtonClick() {
    this.props.navigation.goBack(null);
    return true;
}

//is this android?
componentWillMount() {
    BackHandler.addEventListener('hardwareBackPress', this.handleBackButtonClick);


    //is this android?
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

    if(vi!=undefined)
    this.setState({
      latitude : vi.latitude,
      longitude : vi.longitude,
    });

    let location = Location.getCurrentPositionAsync({});
    this.setState({ location });
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
      console.log(this.state.data) //리스폰스가 오기전까지 언디파인드임 언디파인드이면 오류발생하니까 언디파인드인지 먼저 확인
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
