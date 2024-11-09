import 'package:flutter/material.dart';

class ModelsProvider with ChangeNotifier {
  String currentModel = "gpt-4o-mini";

  String get getCurrentModel {
    return currentModel;
  }

  void setCurrentModel(String newModel) {
    currentModel = newModel;
    notifyListeners();
  }
}
