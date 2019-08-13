import { Alert, BackHandler } from 'react-native';

function  handleBackButton(){
    Alert.alert(
      '정말 끌거예요?',
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
