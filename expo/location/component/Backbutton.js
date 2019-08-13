import { Alert, BackHandler } from 'react-native';

//all back handler
function  handleBackButton(){
    Alert.alert(
      '정말 끌거야??',
      '진짜,진짜,진짜루????',
      [
        {text:'취소', onPress: ()=> console.log('Cancle App'), style:'cancle'},
        {text:'확인', onPress: ()=> BackHandler.exitApp()},
      ],
      {canaelable: false}
    )
    return true;
}


export {handleBackButton};
