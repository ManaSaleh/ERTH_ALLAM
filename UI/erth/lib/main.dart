import 'package:flutter/material.dart';
import 'package:erth/constants/constants.dart';
import 'package:erth/providers/models_provider.dart';
import 'package:erth/screens/chat_screen.dart';
import 'package:provider/provider.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MultiProvider(
      providers: [
        ChangeNotifierProvider(
          create: (_)=>ModelsProvider()
          )
      ],
      child: MaterialApp(
        title: 'ALLAM Project',
        debugShowCheckedModeBanner: false,
        theme: ThemeData(
          scaffoldBackgroundColor: scaffoldBackgroundColor,
          appBarTheme: AppBarTheme(color: cardColor),
        ),
        home: const ChatScreen(),
      ),
    );
  }
}
