import { Login, Profile } from "./components";
import { StatusBar } from "expo-status-bar";
import { NavigationContainer } from "@react-navigation/native";
import { createNativeStackNavigator } from "@react-navigation/native-stack";
import { screens } from "./utils";
import { useState } from "react";

type RootStackParamList = {
  Login: undefined;
  Profile: undefined;
};

const { Navigator, Screen } = createNativeStackNavigator<RootStackParamList>();

export default function App() {
  const [showModal] = useState(true);

  return (
    <>
      <StatusBar style="dark" />
      <NavigationContainer>
        {showModal && <Login />}
        <Navigator initialRouteName={screens.PROFILE}>
          {/* <Screen name={screens.LOGIN} component={Login} /> */}
          <Screen name={screens.PROFILE} component={Profile} />
        </Navigator>
      </NavigationContainer>
    </>
  );
}
