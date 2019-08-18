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
