import { Login, Profile } from "./components";
import { StatusBar } from "expo-status-bar";
import { NavigationContainer } from "@react-navigation/native";
import { createNativeStackNavigator } from "@react-navigation/native-stack";
import { screens } from "./utils";
import AppProvider from "./context";

type RootStackParamList = {
  Login: undefined;
  Profile: undefined;
};

const { Navigator, Screen } = createNativeStackNavigator<RootStackParamList>();

export default () => {
  return (
    <AppProvider>
      <StatusBar style="dark" />
      <NavigationContainer>
        <Login />
        <Navigator initialRouteName={screens.PROFILE}>
          <Screen name={screens.PROFILE} component={Profile} />
        </Navigator>
      </NavigationContainer>
    </AppProvider>
  );
};
