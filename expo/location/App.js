import React, { Component } from 'react';
import { Platform, Text, View, Button, StyleSheet,WebView, BackHandler, Alert, TouchableOpacity, Image,Clipboard } from 'react-native';
import Constants from 'expo-constants';
import * as Location from 'expo-location';
import * as Permissions from 'expo-permissions';
import SlidingUpPanel from 'rn-sliding-up-panel';
import * as TaskManager from 'expo-task-manager';

//user component
import {handleBackButton} from './component/Backbutton';
import { CreateLocation, CreatePushToken, UpdateLocation, ReadLocation } from './RequestHttp';
import { registerForPushNotificationsAsync } from './push_token';

const LOCATION_TASK_NAME = 'background-my-location-get';

var vi = {
  "locations" : [
    {
      "coords" : {
        "latitude" : 0,
        "longitude" : 0,
      },
        "timestamp" : 0,
    }
  ]
};

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
      latitude: null,
      longitude: null,
      timestamp: null,
      //back
       canGoBack : false,
       token : '불러오는 중이에요~',
    };
}


//생성자가 처음 만들어 질 때 실행
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

//render 이후에 실행
 componentDidMount(){
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
  }, 5000);
 }

 componentWillUnmount() {
//BackHandler : detach to hardwareBackPress
  BackHandler.removeEventListener('hardwareBackPress');
 }

_getLocationAsync = async () => {
  //get Token
      var tmp_token = await registerForPushNotificationsAsync();
      var token =tmp_token;
      this.setState({
        token : token
      });
      console.log('[DEBUG] get token : ', this.state.token);

  //init Create Location #이거는 그냥 DB에 장고가 생성하게 할 수도 있음
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

//Clipboard token
  onBack() {
      this.refs[WEBVIEW_REF].goBack();
  }


  copyOk(){
    if(this.state.token === '불러오는 중이에요~'){
      alert('잠시만 기다려주세요!');
    }else{
      alert('토큰이 복사되었어요!');
      Clipboard.setString(this.state.token);
    }
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
      CreateLocation(this.state.token,lat,lon);
      //#UPDATE
      //UpdateLocation(this.state.token,lat,lon);
      //#READ
      //console.log('readLocation',ReadLocation());

    }else{//여기
      console.log('\n<< LOCATION is NULL !  \n');
      }
    }

    return (
      <View style={styles.container}>
        <WebView
        ref = {WEBVIEW_REF}
        style={styles.web}
        onNavigationStateChange=
        {this.onNavigationStateChange.bind(this)}
        source = {{uri: 'http://168.131.151.162:8000/complain/1/'}}/>

        <TouchableOpacity  style={styles.tokenbuttonOff} onPress={() => this._panel.show()}>
          <Image
            style = {styles.image}
            source={require('./assets/drum.png')}
          />
        </TouchableOpacity>
        <SlidingUpPanel ref={c => this._panel = c}>
          <View style={{top:600}}>
            <TouchableOpacity style={styles.tokenbuttonOn} onPress={() => this._panel.show()}>
              <Text style={{fontSize:20,color:'black', textAlign:'center', marginBottom:5}} >내 토큰</Text>
              <TouchableOpacity style={styles.tokenbox} onPress={() => this.copyOk()} color="black">
               <Text style={{fontSize:16,color:'black', textAlign:'center', top:13}} >{this.state.token}</Text>
            </TouchableOpacity>
               </TouchableOpacity>
          </View>
        </SlidingUpPanel>
                </View>
    );
  }
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#D9EDFD',
  },
  web:{
    flex: 0.97,
    top : 25,
    backgroundColor : "white"
  },
  image:{
    width : 40,
    height: 40,
  },
  tokenbuttonOff:{
    position:'absolute',
    bottom:60,
    borderRadius:15,
    marginRight:5,
    marginLeft:5,
    backgroundColor:'#D9EDFD',
    padding:10,
  },
  tokenbuttonOn:{
    borderRadius:15,
    marginRight:5,
    marginLeft:5,
    backgroundColor:'#D9EDFD',
    padding:10,
    height:200
  },
  tokenbox:{
    marginRight:0,
    marginLeft:0,
    borderRadius:15,
    backgroundColor:'white',
    padding:2,
    height:120
  },
  dragHandler: {
  alignSelf: 'stretch',
  height: 64,
  alignItems: 'center',
  justifyContent: 'center',
  backgroundColor: '#ccc'
}
});
