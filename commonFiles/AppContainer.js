import React, {Component} from 'react';
import {
  SafeAreaView,
  StatusBar,
  View,
  Dimensions,
  StyleSheet,
  UIManager,
  Platform
} from 'react-native';
import Navigation from './navigations';
import {Colors, Typography} from './styles';
import {connect} from 'react-redux';
import Spinner from 'react-native-spinkit';
import DropdownAlert from 'react-native-dropdownalert';
import DropDownService from './DropDownService'

const {BLACK, TRANSLUCENT_WHITE, ORANGE, RED, GREEN} = Colors;
const {FONT_SEMIBOLD, FONT_MEDIUM} = Typography
const {width, height} = Dimensions.get('window');

class App extends Component {

  componentDidMount() {
    if (Platform.OS === 'android') {
      if (UIManager.setLayoutAnimationEnabledExperimental) {
        UIManager.setLayoutAnimationEnabledExperimental(true);
      }
    }
  }

  showSpinner = () => {
    const {spinnerContainerStyle} = styles
    return (
      <View style={spinnerContainerStyle}>
        <Spinner isVisible={true} type={'Wave'} color={ORANGE} size={50} />
      </View>
    );
  };
  

  render() {
    console.disableYellowBox = true;
    const {loadingStatus, statusColor} = this.props.state;

    return (
      <SafeAreaView style={{flex: 1, backgroundColor: BLACK}}>
        <StatusBar backgroundColor={statusColor} barStyle="light-content" />
        <DropdownAlert 
          ref={ref => DropDownService.setDropDownAlert(ref)} 
          successColor={GREEN}
          errorColor={RED}
          infoColor={BLACK}
          tapToCloseEnabled
          titleStyle={FONT_SEMIBOLD}
          messageStyle={FONT_MEDIUM}
          inactiveStatusBarBackgroundColor={BLACK}
        />
        <Navigation />
        {loadingStatus ? this.showSpinner() : false}
      </SafeAreaView>
    );
  }
}

const styles = StyleSheet.create({
  spinnerContainerStyle: {
    position: 'absolute',
    width,
    height,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: TRANSLUCENT_WHITE,
  },
});

const mapStateToProps = state => {
  return {state: state.reducer};
};

export default connect(mapStateToProps)(App);
