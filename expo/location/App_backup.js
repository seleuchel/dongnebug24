import React, { Component } from 'react';
import { Platform, Text, View, Button, StyleSheet,WebView, BackHandler, Alert, TouchableOpacity } from 'react-native';
import Constants from 'expo-constants';
import * as Location from 'expo-location';
import * as Permissions from 'expo-permissions';
import MapView, {Marker} from 'react-native-maps';
import SlidingUpPanel from 'rn-sliding-up-panel';
import * as TaskManager from 'expo-task-manager';
import { BackgroundFetch } from 'expo';
import { Notifications } from 'expo';


//user component
import {handleBackButton} from './component/Backbutton';
import { CreateLocation, CreatePushToken, UpdateLocation, ReadLocation } from './RequestHttp';
//import { registerForPushNotificationsAsync } from './push_token';

const LOCATION_TASK_NAME = 'background-my-location-get';

var vi = {};
var uri = "http://naver.com";

  const PUSH_ENDPOINT = 'http://168.131.153.40:8000/api/pushtoken/';

TaskManager.defineTask(LOCATION_TASK_NAME, async ({ data, error }) => {
  if (error) {
    return;
  }
  if (data) {
    vi = data;
  }
});

//location get coords data
  let WEBVIEW_REF = 'webview';

export default class App extends Component<Props>{
  constructor(props){
    super(props);
    this.state = {
      errorMessage: null,
      region: null,
      //new
      latitude:null,
      longitude: null,
      timestamp: null,
      //back
       canGoBack : false,
    };
}

 componentDidMount(){
//backgrond
  //BackgroundFetch.registerTaskAsync(LOCATION_TASK_NAME);
//BackHandler : listens to hardwareBackPress
  BackHandler.addEventListener('hardwareBackPress',async function(){
      if(this.state.canGoBack){
        this.onBack();
        return false;
      }else{
        handleBackButton();
      }
  }.bind(this));



  //get location
  setInterval(async () => {
    await Location.startLocationUpdatesAsync(LOCATION_TASK_NAME,);

      console.log('--------------------------- DEBUG : GET vi --------------------------- \n', vi);
     this.setState({
        latitude : vi.locations[0].coords.latitude,
        longitude : vi.locations[0].coords.longitude,
        timestamp : vi.locations[0].timestamp,
      });

    // console.log('\n--------------------------- DEBUG : get state : lant, lon, timestamp --------------------------- \n',
    //   'latitude : ', this.state.latitude,
    //   'longitude : ', this.state.longitude,
    //   'timestamp : ', this.state.timestamp);
  }, 5000);

 }

//componentWillMount : api called just before the component print the screen
componentWillMount() {
    //is this android?
    if (Platform.OS === 'android' && !Constants.isDevice) {
      this.setState({
        errorMessage: 'Oops, this will not work on Sketch in an Android emulator. Try it on your device!',
      });
    } else {
      this._getLocationAsync();
    }

}
 componentWillUnmount() {
//BackHandler : detach to hardwareBackPress
  BackHandler.removeEventListener('hardwareBackPress');
 }

  _getLocationAsync = async () => {

    let { status } = await Permissions.askAsync(Permissions.LOCATION);
    if (status !== 'granted') {
      this.setState({
        errorMessage: 'Permission to access location was denied',
      });
    }
  };




//BackHandler
  webView_with_back = () =>{
    if(this.state.canGoBack){
      this.props.navigation.goBack(null);
      console.log('no');
      return false;
    }else{
      return handleBackButton();
    }
  }
// show the site in the browser (navigate.canGoBack)
onNavigationStateChange(navState){
  this.setState({
    canGoBack: navState.canGoBack
  });
}

  onBack() {
      this.refs[WEBVIEW_REF].goBack();
  }

  //귀주 : readLocation
  ReadLocation(){
      return fetch('http://168.131.153.40:8000/location/7/', {
      method: 'GET'
      })
      .then((response) => response.json())
      .catch((error) => {
         console.error(error);
      });
  }

  render() {

    let text = 'Waiting..';
    let lat = "";
    let lon = "";


    if (this.state.errorMessage) {
      text = this.state.errorMessage;
    } else if (this.state.latitude) {

      if( (this.state.latitude !=='undefined') && (this.state.latitude !== null))//// 여기
      {
        console.log('\n>> GET LOCATION!  \n');
        lat = this.state.latitude;
        lon = this.state.longitude;

      //SEND : here - sendPacket
      //#CREATE
      //CreateLocation(lat,lon);
      //#UPDATE
      //UpdateLocation(lat,lon);
      //#READ
      //console.log('readLocation',ReadLocation());
      //#reginster PUSH token to rest api server
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
        console.log('>>>>>>>',token);

        // POST the token to your backend server from where you can retrieve it to send push notifications.
        return fetch(PUSH_ENDPOINT, {
          method: 'POST',
          headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
              'user' : 1,
              'token' : token,
          }),
        });
      }

      registerForPushNotificationsAsync();


    }else{//여기
      console.log('\n<< LOCATION is NULL !  \n');
      }
    }
//http://168.131.151.165/p2p/812/content.html
//mizoo : http://168.131.151.165/p2p/812/content.html


    return (
      <View style={styles.container}>
        <WebView
        ref = {WEBVIEW_REF}
        style={styles.web}
        onNavigationStateChange=
        {this.onNavigationStateChange.bind(this)}
        source = {{uri: 'https://google.com'}}/>

        <TouchableOpacity style={{backgroundColor:'#D9EDFD',padding:10}} onPress={() => this._panel.show()}>
          <Text style={{fontSize:20,color:'black', textAlign:'center'}}>'내 위치'</Text>
        </TouchableOpacity>
                <SlidingUpPanel ref={c => this._panel = c} >
                  <View style={{flex:0.7, top:300}}>
                    <TouchableOpacity style={{backgroundColor:'#D9EDFD',padding:3}} onPress={() => this._panel.hide()}>
                      <Text style={{fontSize:20,color:'black', textAlign:'center'}}>'내 현재 위치'</Text>
                    </TouchableOpacity>

                      <MapView
                        style={styles.map}
                        initialRegion = {{
                          latitude : Number(lat),
                          longitude : Number(lon),
                          latitudeDelta : 0.005,
                          longitudeDelta : 0.005,
                        }}
                        region={{
                          latitude : Number(lat),
                          longitude : Number(lon),
                          latitudeDelta : 0.005,
                          longitudeDelta : 0.005,
                        }}>
                      <Marker title="box" pinColor = "blue"
                      coordinate = {{
                        latitude: Number(lat),
                        longitude: Number(lon)
                      }}/>
                      </MapView>
                  </View>
                </SlidingUpPanel>
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
