import React, { Component } from 'react'
import { View, Text } from 'react-native'


export default class HttpExample extends Component {
   state = {
      data: ''
   }
   componentDidMount = () => {
      fetch('http://168.131.153.40:8000/persons/', {
         method: 'POST',
         headers: {
           'Accept': 'application/json',
           'Content-Type' : 'application/json'
         },
         body: JSON.stringify({
           "first_name" : "sumin",
           "last_name" : "deamon"

         })
      })
      .then((response) => response.json())
      .then((responseJson) => {
         console.log(responseJson);
         this.setState({
            data: responseJson
         })
      })
      .catch((error) => {
         console.error(error);
      });
   }
   render() {
      return (
         <View>
            <Text>
               {this.state.data.body}
            </Text>
         </View>
      )
   }
}
