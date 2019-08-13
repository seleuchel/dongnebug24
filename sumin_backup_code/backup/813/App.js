import React, { Component } from 'react';
import { Platform, Text, View, Button, StyleSheet,WebView, BackHandler, Alert, TouchableOpacity,BackAndroid } from 'react-native';
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

//location get coords data
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
    };
}

//vi는 통째로 받고
componentDidMount(){
  setInterval(async () => {
    await Location.startLocationUpdatesAsync(LOCATION_TASK_NAME,);
    console.log('--------------------------- DEBUG : GET vi --------------------------- \n', vi);
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
  }, 5000);

  console.log('readLocation',ReadLocation());
}

componentWillUnmount() {
    BackHandler.removeEventListener('hardwareBackPress', this.handleBackButtonClick);
}

handleBackButtonClick() {
    this.props.navigation.goBack(null);
    return true;
}

//컴포넌트가 화면에 나가기 직전에 호출되는 api
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

  _getLocationAsync = async () => {

    let { status } = await Permissions.askAsync(Permissions.LOCATION);
    if (status !== 'granted') {
      this.setState({
        errorMessage: 'Permission to access location was denied',
      });
    }

    this.setState({
      latitude : vi.locations[0].coords.latitude,
      longitude : vi.locations[0].coords.longitude,
      timestamp : vi.locations[0].timestamp,
    });


  };


//안움직일때 render가 대기 타야 되는데
  render() {
    let text = 'Waiting..';
    let lat = "";
    let lon = "";

    console.log('\n--------------------------- DEBUG : get this.state.location in render() --------------------------- \n',this.state.location);

    if (this.state.errorMessage) {
      text = this.state.errorMessage;
      console.log(text);
    } else if (this.state.latitude) {

      if( (this.state.latitude !=='undefined') && (this.state.latitude !== null))//// 여기
      {
        console.log('\n>> GET LOCATION!  \n');
        lat = this.state.latitude;
        lon = this.state.longitude;

      //here - sendPacket
      //#CREATE
      //CreateLocation(lat,lon);
      //#UPDATE
      //UpdateLocation(lat,lon);
      //#READ
      console.log('readLocation',ReadLocation());

    }else{//여기
      console.log('\n<< LOCATION is NULL !  \n');
      }
    }
    console.log('hello lat',lat);
//http://168.131.151.165/p2p/812/content.html
//mizoo : http://168.131.151.165/p2p/812/content.html


//source = {{ uri : 'http://168.131.151.165/maps/linktoread.html'}}
    return (
      <View style={styles.container}>
      <WebView style={styles.web}
          source = {{ uri : 'http://168.131.151.165/maps/viv.html'}}
        />
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
//예쁘게 안됨. coordinate
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
    height: "100%",
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
