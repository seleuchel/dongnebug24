import React from 'react';
import {WebView,BackHandler} from 'react-native';

class WebViewWithBack extends React.Component{
  var uri = 'https://naver.com';

  constructor(props){
    super(props);
    this.state={
      canGoBack : true,
    }

    this.onnavigationStateChange = this.onnavigationStateChange.bind(this); //?
  }

  backHandlerEvent
onnavigationStateChange(navState){
  this.setState({
    canGoBack : navState.canGoBack
  });
}

  render(){
    return (
      <WebView
      source={uri};
      domStorageEnabled={true}
      onnavigationStateChange = {this.onnavigationStateChange.bind(this)}
      />

    );
  }
}

export {WebViewWithBack};
