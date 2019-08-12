import React, { Component } from 'react';
import { Platform, Text, View, StyleSheet,WebView,TouchableOpacity } from 'react-native';
import Constants from 'expo-constants';
import * as Location from 'expo-location';
import * as Permissions from 'expo-permissions';
import MapView from 'react-native-maps'


export default class MyWeb extends Component<Props>{
  render(){
    return(
      <View style={styles.container}>
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
      </View>
    );
  }
}


const styles = StyleSheet.create({
  container :{
    flex:1,

  },
  web:{
    height: "50%",
    backgroundColor:'blue',
  },
  map:{
    height: "50%",
    left: 0,
    right: 0,
    bottom: 0,
  },
}
);
