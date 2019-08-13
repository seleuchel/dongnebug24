import React, {Component,} from 'react';
import {
  View,
  Text,
  BackHandler,
  Alert
} from 'react-native';

class BackButton extends Component<Props>{
  componentDidMount(){
    BackHandler.addEventListener('hardwareBackPress',this.handleBackButton);
  }

  componentWillUnmount(){
    BackHandler.removeEventListener('hardwareBackPress',this.handleBackButton);
  }

  handleBackButton(){
    Alert.alert(
      '정말 끌거예요?',
      '진짜루????',
      [
        {text:'취소', onPress: ()=> console.log('Cancle App'), style:'cancle'},
        {text:'확인', onPress: ()=> BackHandler.exitApp()},
      ],
      {canaelable: false}
    )
    return true;
  }

  render(){
    return{
      <View>

      </View>
    }
  }
}
