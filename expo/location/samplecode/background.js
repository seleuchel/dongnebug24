import BackgroundFetch from "react-native-background-fetch";

export default class App extends Component {
  componentDidMount() {
    // Configure it.
    BackgroundFetch.configure({
      minimumFetchInterval: 15,     // <-- minutes (15 is minimum allowed)
      // Android options
      stopOnTerminate: false,
      startOnBoot: true,
      requiredNetworkType: BackgroundFetch.NETWORK_TYPE_NONE, // Default
      requiresCharging: false,      // Default
      requiresDeviceIdle: false,    // Default
      requiresBatteryNotLow: false, // Default
      requiresStorageNotLow: false  // Default
    }, () => {
      console.log("[js] Received background-fetch event");
      // Required: Signal completion of your task to native code
      // If you fail to do this, the OS can terminate your app
      // or assign battery-blame for consuming too much background-time
      BackgroundFetch.finish(BackgroundFetch.FETCH_RESULT_NEW_DATA);
    }, (error) => {
      console.log("[js] RNBackgroundFetch failed to start");
    });

    // Optional: Query the authorization status.
    BackgroundFetch.status((status) => {
      switch(status) {
        case BackgroundFetch.STATUS_RESTRICTED:
          console.log("BackgroundFetch restricted");
          break;
        case BackgroundFetch.STATUS_DENIED:
          console.log("BackgroundFetch denied");
          break;
        case BackgroundFetch.STATUS_AVAILABLE:
          console.log("BackgroundFetch is enabled");
          break;
      }
    });
  }
};
