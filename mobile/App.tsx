import { Login, Profile } from "./components";
import { StatusBar } from "expo-status-bar";
import { NavigationContainer } from "@react-navigation/native";
import { createNativeStackNavigator } from "@react-navigation/native-stack";
import { screens } from "./utils";
import AppProvider from "./context";
import { QueryClient, QueryClientProvider } from "react-query";
import { ModalContainer } from "./components/ModalContainer";

type RootStackParamList = {
  Login: undefined;
  Profile: undefined;
};

const { Navigator, Screen } = createNativeStackNavigator<RootStackParamList>();

const client = new QueryClient();

export default () => {
  return (
    <QueryClientProvider client={client}>
      <AppProvider>
        <StatusBar style="dark" />
        <NavigationContainer>
          <ModalContainer />
          <Navigator initialRouteName={screens.PROFILE}>
            <Screen name={screens.PROFILE} component={Profile} />
          </Navigator>
        </NavigationContainer>
      </AppProvider>
    </QueryClientProvider>
  );
};
