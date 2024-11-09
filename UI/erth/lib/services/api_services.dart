import 'dart:convert';
import 'package:http/http.dart' as http;
import 'package:erth/models/chat_model.dart';
import 'package:erth/constants/api_consts.dart';

class ApiService {
  static Future<List<ChatModel>> sendMessage({required String message}) async {
    try {
      var response = await http.post(
        Uri.parse(BASE_URL),
        headers: {
          "Content-Type": "application/json",
        },
        body: jsonEncode({"query": message}),
      );

      if (response.statusCode != 200) {
        throw Exception("Failed to get response: ${response.statusCode}");
      }

      Map<String, dynamic> jsonResponse =
          jsonDecode(utf8.decode(response.bodyBytes));
      if (!jsonResponse.containsKey("response")) {
        throw Exception("Invalid response format");
      }
      String fullResponse = jsonResponse["response"];
      String trimmedResponse = fullResponse.split("user").first;

      return [ChatModel(msg: trimmedResponse, chatIndex: 0)];
    } catch (error) {
      print("Error in ApiService.sendMessage: $error");
      rethrow;
    }
  }
}
