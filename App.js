import 'react-native-gesture-handler';
import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View } from 'react-native';
import React, {useState} from 'react';
import HomePage from './screens/Home/home';
import { createStackNavigator } from 'node_modules/@react-navigation/stack'; //Insert screens into a stack
import { NavigationContainer } from '@react-navigation/native'; //contains navigator and screen



export default function App() {
  return (
    <View style={styles.container}>
      <Text style={styles.titleText}> HELLO THERE</Text>
    <Text style={styles.baseText}>this is our super cool awesome app</Text>
      <StatusBar style="auto"> THIS IS THE STAT BAR</StatusBar>
     </View>

   // <HomePage/>

  );
}

const styles = StyleSheet.create({
  titleText: {
    color: 'red',
    fontSize: 30,
  },
  baseText: {
    color: 'grey',
    fontSize: 15,
  },
  container: {
    flex: 1,
    backgroundColor: 'white',
    alignItems: 'center',
    justifyContent: 'center',
  },
});
