import React, { Component } from 'react';
import { Platform, Text, View, Button, StyleSheet,WebView, BackHandler, Alert, TouchableOpacity } from 'react-native';
import Constants from 'expo-constants';
import * as Location from 'expo-location';
import * as Permissions from 'expo-permissions';
import MapView, {Marker} from 'react-native-maps';
import SlidingUpPanel from 'rn-sliding-up-panel';
import * as TaskManager from 'expo-task-manager';

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
      location: null,
      errorMessage: null,
      region: null,
      coordinate : null,
      lati:null,
      longi: null,
    };
}

componentDidMount(){
  setInterval(async () => {
    await Location.startLocationUpdatesAsync(LOCATION_TASK_NAME,);
    console.log('--------------------------- DEBUG : GET vi --------------------------- \n', vi.locations[0]);
    this.setState({location:vi.locations[0]});
    console.log('\n--------------------------- DEBUG : this.state.location by vi --------------------------- \n',this.state.location);
  }, 5000)
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

    let location = await Location.getCurrentPositionAsync({});
    let way = await Location.reverseGeocodeAsync(location.coords);

    this.setState({ location });
    this.setState({ way });
    this.setState({location: vi});

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
    } else if (this.state.location) {

      if( this.state.location !=='undefined')//// 여기
      {
        console.log('\n>> GET LOCATION!  \n');
      lat = parseFloat(this.state.location.coords.latitude);
      lon = parseFloat(this.state.location.coords.longitude);
      //
    }else{//여기
      console.log('\n<< LOCATION is NULL !  \n');
      this.setState({
        location: this.state.location
      });
    }
    }
    console.log('hello lat',lat);

    return (
      <View style={styles.container}>
      <WebView style={styles.web}
          source = {{ uri : 'https://google.com'}}
        />
        <TouchableOpacity style={{backgroundColor:'black',padding:10}} onPress={() => this._panel.show()}>
          <Text style={{fontSize:20,color:'white', textAlign:'center'}}>'내 위치'</Text>
        </TouchableOpacity>
                <SlidingUpPanel ref={c => this._panel = c} >
                  <View style={{flex:0.7, top:300}}>
                    <Button title='내 현재 위치' color="black" />

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
    backgroundColor : "pink"
  },
  map:{
    height: "80%",
    left: 0,
    right: 0,
    bottom: 0,
  },
});
